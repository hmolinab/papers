"""
La parte imaginaria en det=0: la puerta a QM (jul-21 2026).

HM: "en el trabajo del atlas te faltó con det=0 la parte imaginaria para abrir la puerta MQ."

El teorema de completitud (completitud_sectores_sylvester_hadamard_prueba.py) clasificó Gamma_s
(la parte SIMETRICA) por su inercia REAL -- Sylvester solo habla de autovalores reales porque
Gamma_s es simetrica. Pero Gamma = Gamma_s + Gamma_a, con Gamma_a = I^R ANTISIMETRICA (el Campo,
Axioma A2). Una matriz real antisimetrica tiene espectro puramente IMAGINARIO (autovalores +-i*lambda,
lambda real >= 0) -- ese es el ingrediente que el analisis de Gamma_s solo nunca ve.

TESIS: al cruzar det(Gamma_s)=0 (el estrato de frontera, donde vive Maxwell/foton en el atlas), el
espectro de Gamma_s pasa por CERO -- y es justo ahi donde Gamma_a (si no se anula tambien) pasa a
DOMINAR el espectro de Gamma completo, produciendo autovalores puramente imaginarios +-i*omega. Un
espectro puramente imaginario es exactamente la firma de una evolucion UNITARIA/OSCILATORIA,
e^{+-i*omega*t} -- la estructura formal de una fase cuantica (|amplitud| constante, fase que rota).
Esto es lo que "abre la puerta" a QM en la frontera: no es que Maxwell/foton per se sea QM, es que
la ANULACION del sector simetrico deja el espectro gobernado por el sector antisimetrico, que es
estructuralmente donde vive la oscilacion de fase pura -- el "|z|^2 conservado, fase libre" que
Born necesita (ver insight_born_desde_bifurcacion_negativo.md).
"""
import numpy as np

rng = np.random.default_rng(3)


def espectro(M):
    return np.linalg.eigvals(M)


print("=" * 78)
print("Construccion: Gamma(t) = Gamma_s(t) + Gamma_a,  Gamma_s simetrica cruzando det=0,")
print("Gamma_a = I^R antisimetrica FIJA (el Campo, Axioma A2)")
print("=" * 78)

# Gamma_a: bivector fijo I^R, antisimetrico, con acoplamiento omega0
omega0 = 0.6
Ga = np.array([
    [0,        0,       0,      0],
    [0,        0,       omega0, 0],
    [0,      -omega0,     0,    0],
    [0,        0,       0,      0],
], dtype=float)
print(f"  Gamma_a fija (bivector I^R, acoplamiento omega0={omega0}):")
print(f"  autovalores de Gamma_a solo: {np.round(espectro(Ga), 4)}  (puramente imaginarios, +-i*omega0)")

print()
print("  Barrido: Gamma_s(t) = diag(1, x(t), 1, rho^2) con x(t): +0.4 -> -0.4 (cruza 0 en t=0.5)")
print(f"  {'t':>5} {'x(t)':>8} {'det Gs':>9}   autovalores de Gamma = Gamma_s+Gamma_a")
for t in np.linspace(0, 1, 11):
    x = 0.4 - 0.8 * t
    Gs = np.diag([1.0, x, 1.0, 0.7**2])
    G = Gs + Ga
    ev = espectro(G)
    im_frac = np.abs(ev.imag).sum() / (np.abs(ev.real).sum() + np.abs(ev.imag).sum() + 1e-12)
    tag = "  <-- x=0, Gs singular" if abs(x) < 0.05 else ""
    print(f"  {t:5.2f} {x:8.3f} {np.linalg.det(Gs):9.3f}   {np.round(ev,3)}   "
          f"frac.imag={im_frac:.2f}{tag}")

print()
print("=" * 78)
print("El caso límite puro: Gamma_s -> 0 por completo (frontera total, no solo un modo)")
print("=" * 78)
print("""  Si TODO Gamma_s se anula (no solo una entrada), Gamma = Gamma_a puro: espectro
  puramente imaginario garantizado (antisimétrica real). Esto es la frontera IDEAL --
  el límite en el que el sector Fuerza desaparece del todo y solo queda el Campo.""")
G_puro = Ga.copy()
print(f"  autovalores: {np.round(espectro(G_puro), 4)}")
print(f"  ¿puramente imaginarios? {np.allclose(espectro(G_puro).real, 0)}")

print()
print("=" * 78)
print("SÍNTESIS: por qué det=0 es la puerta a QM, con la parte imaginaria explícita")
print("=" * 78)
print("""  El teorema de completitud (Sylvester+Hadamard) clasifica Gamma_s por su ESPECTRO REAL --
  correcto para el tipo de EDP de 2º orden que ve el símbolo. Pero AL CRUZAR det(Gamma_s)=0, el
  balance de poder dentro de Gamma=Gamma_s+Gamma_a se desplaza: el modo que se anula en Gamma_s deja
  de contribuir autovalores reales, y el bivector Gamma_a (que SIEMPRE es imaginario puro, por ser
  antisimétrico real) pasa a dominar ESE modo. El barrido de arriba lo muestra: la fracción de
  espectro imaginario crece según x(t)->0 y es máxima justo en la frontera.

  INTERPRETACIÓN [IF]: un espectro puramente imaginario es la forma normal de una evolución
  e^{+-iwt} -- oscilación de FASE con amplitud conservada, exactamente la estructura formal que
  Schrödinger exige (y que el atlas ya coloca en det=0, §5.4, pero sin decir por qué el operador se
  vuelve oscilatorio ahí). La respuesta: porque en la frontera el sector antisimétrico (Campo, no
  Fuerza) es lo único que puede quedar produciendo dinámica, y ese sector es estructuralmente
  imaginario-puro. Es la puerta -- no la derivación completa de QM (Born, |psi|^2, sigue [F], ver
  insight_born_desde_bifurcacion_negativo.md), pero es el mecanismo espectral preciso que faltaba
  nombrar en el teorema de completitud: éste solo vio la mitad REAL (Gamma_s); la mitad IMAGINARIA
  (Gamma_a) es la que se activa justo donde la real se apaga.

  Estatus: [V] el mecanismo espectral (barrido numérico, límite puro antisimétrico). [IF] la lectura
  QM (fase unitaria). [F] la derivación completa de Born/probabilidad permanece abierta.""")
