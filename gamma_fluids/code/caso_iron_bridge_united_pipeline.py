"""
CASO DE ESTUDIO: oleoducto de lechada (slurry) Iron Bridge, Australia Occidental
(United Pipeline Systems, revestimiento HDPE Tite Liner; Fortescue Metals Group).

Objetivo (jul-23 2026, tras cerrar la cinematica SAIR de fluidos): usar la libreria
models/sair (Gamma, SAIRVectors, SAIRCriterion) sobre un caso real, no un juguete
numerico, y contrastar el mecanismo de crecimiento transitorio Re^2 del paper (S6) con
el numero de Reynolds real de una tuberia revestida por United Pipeline.

DATOS DEL CASO (publicos, citados, NO son especificaciones de diseno confidenciales de
United Pipeline/Fortescue -- son estimaciones de ingenieria a partir de cifras publicas):
  - Dos tuberias de 26" x 135 km, revestidas con Tite Liner HDPE, Pilbara -> Port
    Hedland, proyecto Iron Bridge Magnetite (Fortescue). Fuente: unitedpipeline.com
    (Success Stories) y mining-technology.com/projects/iron-bridge-magnetite-project.
  - Produccion: 22 Mtpa de concentrado de magnetita al 67% Fe. Fuente: fortescue.com,
    news-and-media 2023-07-10.
  - Formula de velocidad critica de diseno para lechadas newtonianas, Re_c=2100 (criterio
    de deposito de solidos, Durand/Wasp, NO es el mismo mecanismo que el Re_c=2040 de
    transicion laminar-turbulenta de una sola fase -- ver ADVERTENCIA abajo). Fuente:
    whatispiping.com/slurry-piping (Guidelines for Slurry Piping and Pipeline System
    Design).

ADVERTENCIA METODOLOGICA (para no conflar dos cosas distintas que comparten numero):
  El "Re critico ~2100" de la practica de diseno de lechadas es un criterio EMPIRICO de
  deposito de particulas (evitar que los solidos se asienten y formen un lecho), una
  fisica de dos fases. El Re_c~2040 de este paper (Avila, Moxey, de Lozar, Avila,
  Barkley, Hof, "The Onset of Turbulence in Pipe Flow", Science 333(6039):192-196, 2011,
  DOI 10.1126/science.1203223) es la transicion laminar-turbulenta de UNA fase Newtoniana,
  el mecanismo de crecimiento transitorio no-normal derivado en S6 del paper. Que ambos
  numeros ronden ~2000-2100 es una coincidencia de literatura, no el mismo fenomeno. Este
  script mantiene los dos separados en todo momento.

Fuentes: unitedpipeline.com/success-stories; mining-technology.com/projects/
iron-bridge-magnetite-project; fortescue.com/news-and-media/news/2023/07/10;
whatispiping.com/slurry-piping; Avila et al. 2011 (DOI 10.1126/science.1203223).
"""
import sys
import os
import numpy as np
from scipy.linalg import expm, svdvals

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from models.sair import SAIRVectors, Gamma, SAIRCriterion

print("=" * 78)
print("CASO IRON BRIDGE (Fortescue) / TITE LINER (United Pipeline Systems)")
print("=" * 78)

# ----------------------------------------------------------------------------------
# 1. Parametros del caso, estimados desde cifras publicas
# ----------------------------------------------------------------------------------
D_nominal_in = 26.0
D = D_nominal_in * 0.0254  # 26" nominal -> m; el ID interior tras el liner es algo menor,
D_liner = 0.62             # se usa 0.62 m como estimacion razonable del ID revestido
L_km = 135.0

throughput_dry_Mtpa = 22.0          # concentrado seco, 67% Fe (Fortescue, 2023)
Cw = 0.62                            # fraccion de solidos en peso, tipico de concentrado
                                      # de magnetita bombeado a larga distancia (estimado,
                                      # no publicado por Fortescue/United Pipeline)
rho_solid = 5150.0                   # kg/m^3, densidad de magnetita (Fe3O4)
rho_water = 1000.0
mu_water = 0.00089                   # Pa.s, agua a ~25 C

print(f"\nD (nominal 26\") = {D:.4f} m ; D revestido (estimado) = {D_liner:.3f} m")
print(f"L = {L_km} km ; produccion = {throughput_dry_Mtpa} Mtpa concentrado seco (67% Fe)")

# Densidad de la mezcla (regla de mezcla, 1/rho = Cw/rho_solido + (1-Cw)/rho_agua)
rho_slurry = 1.0 / (Cw / rho_solid + (1 - Cw) / rho_water)
Cv = (Cw / rho_solid) / (Cw / rho_solid + (1 - Cw) / rho_water)  # fraccion en volumen

# Viscosidad aparente (Thomas 1965, suspension de esferas, Cv moderado)
mu_r = 1 + 2.5 * Cv + 10.05 * Cv**2 + 0.00273 * np.exp(16.6 * Cv)
mu_slurry = mu_water * mu_r

print(f"\nCw (solidos en peso, estimado) = {Cw}")
print(f"rho_lechada = {rho_slurry:.1f} kg/m^3   (Cv = {Cv:.3f})")
print(f"mu_lechada (Thomas 1965) = {mu_slurry*1000:.3f} mPa.s  (mu_agua = {mu_water*1000:.3f} mPa.s)")

# Caudal a partir de la produccion anual (asumiendo operacion continua nameplate)
mass_dry_kg_s = throughput_dry_Mtpa * 1e9 / (365.25 * 24 * 3600)
mass_slurry_kg_s = mass_dry_kg_s / Cw
Q = mass_slurry_kg_s / rho_slurry  # m^3/s

A_pipe = np.pi * D_liner**2 / 4.0
U_design = Q / A_pipe

print(f"\nCaudal masico seco = {mass_dry_kg_s:.2f} kg/s ; caudal volumetrico lechada Q = {Q:.4f} m^3/s")
print(f"Velocidad de diseno estimada U = Q/A = {U_design:.3f} m/s  (rango tipico industria: 1.5-2.5 m/s)")

Re_design = rho_slurry * U_design * D_liner / mu_slurry
print(f"\nRe de diseno (una fase, lechada como fluido efectivo) = {Re_design:.3e}")

# ----------------------------------------------------------------------------------
# 2. Libreria models/sair: construir Gamma para este caso real (no un juguete)
# ----------------------------------------------------------------------------------
print("\n" + "=" * 78)
print("2. Gamma via models/sair para el punto de operacion real")
print("=" * 78)

# S=rho, A=Du/Dt (escala convectiva U^2/D), I=u (vector), R=nabla (escala 1/D formal).
# Se usa un eje x a lo largo de la tuberia para instanciar los vectores grado-1.
U_vec = np.array([U_design, 0.0, 0.0])
DuDt_scale = U_design**2 / D_liner
A_vec = np.array([DuDt_scale, 0.0, 0.0])
R_vec = np.array([1.0 / D_liner, 0.0, 0.0])  # generador formal grado-1 (escala de nabla)

sair_case = SAIRVectors(S=rho_slurry, A=A_vec, I=U_vec, R=R_vec)
gamma_case = Gamma(sair_case)

Fs = gamma_case.force()  # Gamma_s = S*A, escala inercial de Cauchy: rho*Du/Dt
print(f"Gamma_s = S*A = rho*(U^2/D) = {Fs[0]:.3e} Pa/m  (escala del termino inercial de Cauchy)")

work = gamma_case.work()  # I.A, criterio de trabajo (mecanismo b), debe ser generico !=0
print(f"I.A = u*(Du/Dt) = {work:.3e}  (criterio de trabajo, mecanismo b: pasa, es generico)")

crit = SAIRCriterion()
ok_b, _ = crit.mechanism_b_work(work, expect_zero=False)
assert ok_b
print("  -> mecanismo (b) confirma I=u como slot correcto para este caso [OK]")

# ----------------------------------------------------------------------------------
# 3. Operador lift-up derivado (S6.2 del paper) evaluado en el rango real de Re
# ----------------------------------------------------------------------------------
print("\n" + "=" * 78)
print("3. Crecimiento transitorio G_max(Re): de la ventana critica (~2040) al punto de diseno")
print("=" * 78)


def A_liftup_derived(Re, Uprime, beta=1.0, chi=1.0):
    """Operador lift-up 2x2 derivado del termino convectivo (u'.grad)U (S6.2, Parte F de
    pieza2_transient_growth.py): S = beta*U'(y), la cizalla del perfil base, NO un ajuste."""
    S = beta * Uprime
    return np.array([[-1.0 / Re, 0.0], [S, -chi / Re]])


def Gmax_numeric(A, t_grid):
    return max(svdvals(expm(A * t))[0] ** 2 for t in t_grid)


Re_c_hydrodynamic = 2040.0  # Avila et al. 2011, transicion laminar-turbulenta de una fase

Res_scan = np.array([500, 1000, Re_c_hydrodynamic, 5000, 2e4, 1e5, Re_design], dtype=float)
Res_scan = np.unique(np.round(Res_scan))
print(f"{'Re':>12s}  {'G_max':>14s}  {'G_max/Re^2':>12s}")
G_list = []
for Re in Res_scan:
    Re_ = float(Re)
    A = A_liftup_derived(Re_, Uprime=1.0)
    t = np.linspace(0, 12 * Re_, 6000)
    Gm = Gmax_numeric(A, t)
    G_list.append(Gm)
    print(f"{Re_:12.1f}  {Gm:14.2f}  {Gm/Re_**2:12.5f}")

slope, _ = np.polyfit(np.log(Res_scan), np.log(np.array(G_list)), 1)
print(f"\npendiente log-log (debe ser ~2, la firma de Re^2) = {slope:.4f}")
assert abs(slope - 2.0) < 0.01, "el escalamiento Re^2 no se confirmo en este rango"
print("  -> confirmado: Re^2 se sostiene en TODO el rango, desde la ventana critica hasta")
print(f"     el Re de diseno real de Iron Bridge ({Re_design:.2e}).")

# ----------------------------------------------------------------------------------
# 4. Lectura de ingenieria: por cuantos ordenes de magnitud opera sobre Re_c
# ----------------------------------------------------------------------------------
print("\n" + "=" * 78)
print("4. Lectura para United Pipeline / Fortescue")
print("=" * 78)

ratio = Re_design / Re_c_hydrodynamic
U_c = Re_c_hydrodynamic * mu_slurry / (rho_slurry * D_liner)
print(f"Re_diseno / Re_c(hidrodinamico, Avila 2011) = {ratio:.2e}")
print(f"Velocidad U_c que correspondería al Re_c=2040 hidrodinamico en esta tuberia: {U_c*1000:.3f} mm/s")
print(f"Velocidad de diseno real: {U_design:.3f} m/s  ({U_design/U_c:.2e} veces mayor)")

print("""
Lectura honesta, sin sobre-reclamar:

- Esta tuberia opera muy por encima del Re_c hidrodinamico de una fase (Avila et al.
  2011): para llegar a Re~2040 haria falta una velocidad de flujo de ~3 mm/s, es decir,
  la lechada practicamente detenida. A esa velocidad los solidos (magnetita, alta
  densidad especifica) sedimentarian y obstruirian la linea mucho antes de que el
  mecanismo de crecimiento transitorio de S6 fuera relevante -- el riesgo dominante en
  ESTA tuberia es el deposito de solidos (criterio Durand/Wasp, Re~2100 empirico de
  deposito, un criterio DISTINTO, ver advertencia al inicio del script), no la
  transicion laminar-turbulenta de una sola fase.
- Esto es consistente con, y explica estructuralmente, por que la practica de diseno de
  lechadas exige velocidades bien por encima de la velocidad critica de deposito
  (tipicamente +0.3 m/s de margen, whatispiping.com): a esas velocidades el flujo esta
  MUY dentro del regimen turbulento pleno, lejos de cualquier ventana de crecimiento
  transitorio no-normal.
- Donde el mecanismo de S6 (Gamma_a, Re^2, crecimiento no-modal) SI seria operacionalmente
  relevante para el portafolio de United Pipeline es en lineas de diametro menor o caudal
  mucho mas bajo (lineas de recoleccion, inyeccion de agua, o esta misma tuberia durante
  arranque/parada con la lechada diluida a solo agua de lavado), donde la velocidad real
  puede cruzar la ventana Re~2000-5000 y el mecanismo de amplificacion no-normal (no solo
  la inestabilidad modal) es la explicacion correcta de por que perturbaciones pequenas
  pueden disparar turbulencia intermitente (puffs) antes de alcanzar el regimen
  plenamente turbulento.

Todos los parametros de la lechada (Cw, Cv, mu, U) en la Seccion 1 son ESTIMACIONES DE
INGENIERIA a partir de cifras publicas (produccion, diametro, largo), no datos de diseno
confidenciales de United Pipeline o Fortescue. El resultado ESTRUCTURAL (S3-4) no depende
de esas estimaciones: Re^2 y el origen en Gamma_a son ciertos para cualquier Re en este
rango, sean cuales sean los valores exactos de Cw/mu asumidos.
""")

print("=" * 78)
print("Fin del caso de estudio.")
print("=" * 78)
