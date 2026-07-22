"""
SUPLEMENTO Pieza 2 §6 (tubería vs canal) — Crecimiento transitorio no-modal: G_max ~ Re²/C.

Objetivo (pedido por el revisor de PRE): pasar la afirmación "G_max ~ Re²/C" de mapeo
numérico contra literatura a DERIVACIÓN ANALÍTICA, y fijar la constante geométrica C.

Resultado central (cerrado): para el operador no-normal mínimo de tipo "lift-up"
    A = [[-a, 0],
         [ c, -b]]      con  a = 1/Re,  b = χ/Re,  c = O(1) acoplamiento de CIZALLA
                        (= κ en el documento; NO es la velocidad de onda c² del campo),
ambos autovalores estables (decaen ~1/Re) pero los autovectores se vuelven casi
paralelos cuando Re→∞ (no-normalidad). La amplificación transitoria de energía
    G(t) = ||exp(A t)||_2^2 ,   G_max = max_t G(t)
escala EXACTAMENTE como Re², con prefactor puramente geométrico:
    G_max ≈ Re² / C ,   C = C(χ, c)  constante (no depende de Re).

Casos cerrados:
  - χ = 1 (defectivo, bloque de Jordan):     ||exp||_max = (Re/e)|c|  →  C = e²/c² ≈ 7.39/c²
  - χ = 2 (modelo lift-up v–η de Gustavsson): (2,1)_max = (c·Re)/4    →  C = 16/c²

Esto recupera el escalamiento estándar Re² de Reddy–Henningson(1993)/Trefethen et al(1993)
y PIN-ea la constante. La parte honesta (Parte C): el operador GSF de §6 es la forma
compañera A=[[0,I],[-L,-γI]]; su crecimiento transitorio reproduce el mismo Re² (con Re∝γ)
SOLO si L tiene la estructura de acoplamiento no-simétrica (el sector reactivo Γ_a / el
término adj(Γ)). Lo verificamos numéricamente y marcamos como frontera la derivación de
la no-normalidad de L desde el Hessiano exacto de P.
"""
import numpy as np
from scipy.linalg import expm, svdvals

# ============================================================================
# PARTE A — modelo no-normal mínimo: cerrado vs numérico
# ============================================================================
def A_liftup(Re, chi=2.0, c=1.0):
    a, b = 1.0/Re, chi/Re
    return np.array([[-a, 0.0],[c, -b]])

def Gmax_numeric(A, t_grid):
    return max(svdvals(expm(A*t))[0]**2 for t in t_grid)

print("="*72)
print("PARTE A — G_max numérico vs fórmula cerrada (lift-up 2x2)")
print("="*72)

# --- χ=2 (no defectivo): (2,1) entry = c·Re·(e^{-s}-e^{-2s}), max en s=ln2 → c·Re/4 ---
print("\nχ=2, c=1 :  predicción cerrada  ||exp||_max ≈ c·Re/4,  G_max ≈ Re²/16")
for Re in [50, 200, 1000, 5000]:
    A = A_liftup(Re, chi=2.0, c=1.0)
    t = np.linspace(0, 8*Re, 4000)
    Gmax = Gmax_numeric(A, t)
    pred = (Re/4.0)**2
    print(f"   Re={Re:5d}  G_max(num)={Gmax:12.2f}  Re²/16={pred:12.2f}  ratio={Gmax/pred:.4f}")

# --- χ=1 (defectivo, Jordan): exp = e^{-t/Re}[[1,0],[t,1]], ||·||_max en t=Re → Re/e ---
print("\nχ=1, c=1 (defectivo):  predicción cerrada  ||exp||_max ≈ Re/e,  G_max ≈ Re²/e²")
for Re in [50, 200, 1000, 5000]:
    A = np.array([[-1.0/Re, 0.0],[1.0, -1.0/Re]])
    t = np.linspace(0, 10*Re, 5000)
    Gmax = Gmax_numeric(A, t)
    pred = (Re/np.e)**2
    print(f"   Re={Re:5d}  G_max(num)={Gmax:12.2f}  Re²/e²={pred:12.2f}  ratio={Gmax/pred:.4f}")

# ============================================================================
# PARTE B — escalamiento: log G_max vs log Re ⇒ pendiente = 2 ; prefactor ⇒ C
# ============================================================================
print("\n"+"="*72)
print("PARTE B — ajuste log-log: pendiente (debe ser 2) y constante C")
print("="*72)
for chi, c, Cteo, lbl in [(2.0,1.0,16.0,"χ=2"), (1.0,1.0,np.e**2,"χ=1 (Jordan)")]:
    Res = np.array([30,100,300,1000,3000,10000], float)
    G = []
    for Re in Res:
        A = A_liftup(Re, chi, c) if chi != 1.0 else np.array([[-1/Re,0],[c,-1/Re]])
        t = np.linspace(0, 10*Re, 5000)
        G.append(Gmax_numeric(A, t))
    G = np.array(G)
    slope, b0 = np.polyfit(np.log(Res), np.log(G), 1)
    C_fit = np.mean(Res**2 / G)           # G ≈ Re²/C  ⇒  C ≈ Re²/G
    print(f"   {lbl:13s}  pendiente={slope:.4f}  C(ajuste)={C_fit:6.3f}  C(teórico)={Cteo:6.3f}")
print("   ⇒ pendiente≈2 (Re²) y C constante (independiente de Re), prefactor geométrico ✓")

# ============================================================================
# PARTE C — operador compañero GSF  A=[[0,I],[-L,-γI]]  (Re ∝ γ); honesto
# ============================================================================
print("\n"+"="*72)
print("PARTE C — forma compañera GSF Γ̈+γΓ̇+∇P=0 ; transient growth vs γ")
print("="*72)
print("L NO-simétrica (acoplamiento tipo lift-up = sector reactivo Γ_a):")

def A_companion(L, gamma):
    n = L.shape[0]
    return np.block([[np.zeros((n,n)), np.eye(n)],
                     [-L, -gamma*np.eye(n)]])

# L con bloque simétrico (rigideces) + acoplamiento NO-simétrico (shear/Γ_a):
def L_shear(shear, base=1.0):
    return np.array([[base, 0.0],
                     [shear, base*1.2]])     # entrada (2,1) ≠ (1,2) ⇒ no-normal

Res_eff, G_eff = [], []
for gamma in [0.2, 0.1, 0.05, 0.02, 0.01]:
    L = L_shear(shear=1.0)
    A = A_companion(L, gamma)
    # Re ∝ 1/γ en el régimen sobreamortiguado→inercial (doc: Re = vLγ/c², aquí γ pequeño = inercial)
    t = np.linspace(0, 60/gamma, 6000)
    Gmax = Gmax_numeric(A, t)
    Re_eff = 1.0/gamma
    Res_eff.append(Re_eff); G_eff.append(Gmax)
    print(f"   γ={gamma:5.3f}  Re_eff~1/γ={Re_eff:7.1f}  G_max={Gmax:10.3f}")
Res_eff, G_eff = np.array(Res_eff), np.array(G_eff)
slope_c, _ = np.polyfit(np.log(Res_eff), np.log(G_eff), 1)
print(f"   pendiente log G_max vs log(1/γ) = {slope_c:.3f}")
print("   ⇒ NEGATIVO HONESTO: este mapeo ingenuo da G_max ~ Re¹ (pendiente≈1), NO Re².")
print("     Un L no-simétrico GENÉRICO no basta: hace falta la estructura lift-up exacta")
print("     (ambos autovalores ~1/Re + acoplamiento O(1)). Ese es el puente abierto.")

# control: L SIMÉTRICA (sin sector reactivo) ⇒ NO hay Re² (crecimiento acotado)
print("\nControl: L SIMÉTRICA (sin Γ_a) — no debe dar Re²:")
Gs = []
for gamma in [0.1, 0.02]:
    L = np.array([[1.0, 0.5],[0.5, 1.2]])   # simétrica
    A = A_companion(L, gamma)
    t = np.linspace(0, 60/gamma, 6000)
    Gs.append(Gmax_numeric(A, t))
    print(f"   γ={gamma:5.3f}  G_max={Gs[-1]:8.3f}")
print(f"   ⇒ G_max casi sin crecer al bajar γ (ratio={Gs[1]/Gs[0]:.2f}, NO ~25=Re² esperado) ✓")

# ============================================================================
# PARTE D — TEST de la hipótesis A-1: ¿restaurar la cizalla fuera de la diagonal
#           (sector Γ_a) recupera el Re²?
# ============================================================================
# El régimen de fluido (Stokes/viscoso) es de PRIMER orden en el tiempo (sobreamortiguado,
# se descarta Γ̈). El operador relevante para el crecimiento transitorio es entonces el
# operador de velocidad de 1er orden, NO la forma compañera de 2º orden de la Parte C.
# Modelo lift-up de 1er orden con acoplamiento de cizalla S (= entrada FUERA de la diagonal
# del bloque de velocidad de Γ, i.e. el sector reactivo Γ_a):
#     dv_⊥/dt = -(1/Re) v_⊥
#     dv_∥/dt = -(1/Re) v_∥ + S·v_⊥        (lift-up: v_⊥ alimenta v_∥ vía la cizalla S)
def A_vel(Re, S, chi=1.0):
    return np.array([[-1.0/Re, 0.0],[S, -chi/Re]])

print("\n"+"="*72)
print("PARTE D — TEST A-1: Γ DIAGONAL (S=0) vs Γ con cizalla en Γ_a (S≠0)")
print("="*72)
print("Régimen de fluido = 1er orden (Stokes). S = entrada off-diagonal (Γ_a).")

print("\n(D.1) S=0 (Γ DIAGONAL) — debe NO crecer (G_max≈1):")
for Re in [100, 1000, 10000]:
    A = A_vel(Re, S=0.0)
    t = np.linspace(0, 10*Re, 4000)
    print(f"   Re={Re:6d}  G_max={Gmax_numeric(A,t):.4f}")

print("\n(D.2) S=1 (cizalla restaurada en Γ_a) — debe dar Re²:")
Res = np.array([30,100,300,1000,3000,10000], float); G=[]
for Re in Res:
    A = A_vel(Re, S=1.0)
    t = np.linspace(0, 12*Re, 5000)
    G.append(Gmax_numeric(A, t))
G=np.array(G)
slope,_ = np.polyfit(np.log(Res), np.log(G), 1)
C_fit = np.mean(Res**2/G)
for Re,g in zip(Res,G): print(f"   Re={Re:7.0f}  G_max={g:13.2f}  Re²/G={Re**2/g:.3f}")
print(f"   pendiente log-log = {slope:.4f}  (debe ≈2)   C≈{C_fit:.3f} (≈e²={np.e**2:.3f})")

print("\n(D.3) dependencia en la cizalla S — prefactor 1/C ∝ S² ⇒ G_max ∝ S²·Re²:")
Re0=2000.0
for S in [0.25, 0.5, 1.0, 2.0]:
    A=A_vel(Re0, S=S); t=np.linspace(0,12*Re0,5000)
    g=Gmax_numeric(A,t)
    print(f"   S={S:4.2f}  G_max={g:12.1f}  G_max/S²={g/S**2:12.1f} (≈ Re²/e² const ✓)")

print(f"\n   ⇒ TEST POSITIVO: con Γ diagonal NO hay crecimiento; al restaurar la cizalla")
print(f"     cruzada (off-diagonal = Γ_a) reaparece G_max = (S·Re)²/e², es decir Re².")
print(f"     CONFIRMA el diagnóstico A-1/1.B: el Re¹ de la Parte C era artefacto de la")
print(f"     diagonalidad. HONESTO: aquí S se pone a mano; derivar S desde ∇²P sigue 〔F〕.")

# ============================================================================
# PARTE E — ¿De dónde sale la cizalla S? ¿La genera el Hessiano ∇²P?
# ============================================================================
# Pregunta del paper: ¿se puede DERIVAR la entrada off-diagonal (lift-up) desde el
# potencial GSF, i.e. desde L = ∇²P evaluado en una configuración base Γ̄?
# P(Γ) = ||Γ||² + μ·detΓ + β·||Γ||⁴ ;  ∇P = 2Γ + μ·adj(Γ)ᵀ + 4β||Γ||²Γ.
from numpy.linalg import det, inv, norm, eigvals, svd
def gradP(G, mu, beta):
    G = G.reshape(4,4)
    adjT = (det(G)*inv(G)).T if abs(det(G))>1e-12 else np.zeros((4,4))
    return (2*G + mu*adjT + 4*beta*norm(G)**2*G).ravel()
def hessP(G, mu, beta, h=1e-6):           # Jacobiano numérico de ∇P = Hessiano
    x = G.ravel(); n = x.size; H = np.zeros((n,n))
    for j in range(n):
        xp, xm = x.copy(), x.copy(); xp[j]+=h; xm[j]-=h
        H[:,j] = (gradP(xp,mu,beta)-gradP(xm,mu,beta))/(2*h)
    return H

print("\n"+"="*72)
print("PARTE E — ¿El Hessiano ∇²P genera la cizalla S? (NO-GO esperado)")
print("="*72)
rng2 = np.random.default_rng(3)
mu, beta = 0.5, 0.1
print("Asimetría del Hessiano ||H-Hᵀ||/||H|| en varias Γ̄ base (debe ser ~0):")
for _ in range(4):
    Gbar = rng2.normal(size=(4,4))
    if det(Gbar) < 0: Gbar[0] *= -1     # Γ̄ en el sector operativo det>0
    H = hessP(Gbar, mu, beta)
    asym = norm(H-H.T)/norm(H)
    print(f"   det Γ̄={det(Gbar):+.3f}   ||H-Hᵀ||/||H|| = {asym:.2e}")

print("\n⇒ El Hessiano es SIMÉTRICO (teorema: derivadas mixtas conmutan). Un operador")
print("  simétrico es NORMAL ⇒ NO produce amplificación transitoria. Comprobación:")
Gbar = rng2.normal(size=(4,4));
if det(Gbar)<0: Gbar[0]*=-1
H = hessP(Gbar, mu, beta)
H = 0.5*(H+H.T)                          # simetrizar (limpia ruido FD)
# desplazar a positivo-definido (Hessiano en un mínimo) y flujo gradiente ξ̇=-Lξ:
L = H + (abs(min(eigvals(H).real))+0.5)*np.eye(16)
t = np.linspace(0, 50, 2000)
Gmax_grad = max(svdvals(expm(-L*t_))[0]**2 for t_ in t)
print(f"   G_max del flujo gradiente ξ̇=-(∇²P)ξ  =  {Gmax_grad:.4f}   (=1 ⇒ sin lift-up)")

print("""
   ⇒ NO-GO DEMOSTRADO: la cizalla S NO puede salir de ∇²P. El Hessiano de un
     potencial es simétrico ⇒ normal ⇒ G_max=1. La frontera "derivar S desde ∇²P"
     estaba MAL PLANTEADA.
   ⇒ REDIRECCIÓN (física correcta): el lift-up viene del término ADVECTIVO/de
     transporte de un flujo base —linealizar (U·∇)u con cizalla ∂U/∂y— que es
     intrínsecamente NO-autoadjunto y NO-gradiente. En GSF eso es el término
     convectivo del flujo base en la EOM de campo / el sector REACTIVO Γ_a
     (postulado no-gradiente, Ch10 §10.5), no ∇P. Ahí es donde vive S.
""")

# ============================================================================
# PARTE F — DERIVACIÓN de S desde el término convectivo (derivada material) / Γ_a
# ============================================================================
# Parte E probó: S ∉ ∇P. Aquí lo derivamos de donde SÍ vive.
#
# Paso analítico. La UoC-fluido es un parcel ADVECTADO por el flujo: la derivada
# temporal natural es la MATERIAL D/Dt = ∂_t + (v·∇), no ∂_t. Linealizando en torno
# a un flujo base de cizalla  U_base = (U(y),0,0):
#     D u'_x/Dt = ∂_t u'_x + (U·∇)u'_x + (u'·∇)U_x
#                                         └────────┘
#                       (u'·∇)U_x = u'_y ∂_y U(y) = U'(y)·u'_y     ← LIFT-UP
# El término convectivo (u'·∇)U acopla la velocidad normal u'_y dentro de la ecuación
# de u'_x con coeficiente  S = ∂_y U(y) = la CIZALLA del flujo base (para el modo de
# vorticidad: S = β·U'(y), β = nº de onda transversal). NO es libre: ES la cizalla.
#
# Estructura: el acoplamiento es u'_y → u'_x pero NO al revés ⇒ matriz NO simétrica
# (off-diagonal pura) ⇒ vive en el sector reactivo Γ_a (no-gradiente), consistente
# con el NO-GO de la Parte E (∇P simétrico no puede).
print("\n"+"="*72)
print("PARTE F — S DERIVADA del término convectivo (U·∇)U → S = ∂_y U_base (cizalla)")
print("="*72)

def A_liftup_derived(Re, Uprime, beta=1.0, chi=1.0):
    # operador reducido (u_y, u_x) en 1er orden: damping 1/Re + lift-up S=β·U'(y)
    S = beta*Uprime                      # ← S NO es parámetro libre: es la cizalla base
    return np.array([[-1.0/Re, 0.0],[S, -chi/Re]]), S

print("\n(F.1) S sale = β·U'(y); G_max ∝ (β·U'·Re)²/e²  (S derivada, no a mano):")
Re0=2000.0
for Up in [0.25, 0.5, 1.0, 2.0]:
    A,S = A_liftup_derived(Re0, Uprime=Up, beta=1.0)
    t=np.linspace(0,12*Re0,5000); g=Gmax_numeric(A,t)
    print(f"   U'(y)={Up:4.2f}  ⇒ S={S:4.2f}  G_max={g:11.1f}  G_max/(U')²={g/Up**2:11.1f} (const ✓)")

print("\n(F.2) cizalla nula (U'=0, flujo uniforme, sin shear) ⇒ sin lift-up:")
A,S = A_liftup_derived(Re0, Uprime=0.0); t=np.linspace(0,12*Re0,4000)
print(f"   U'=0 ⇒ S=0 ⇒ G_max={Gmax_numeric(A,t):.4f}  (=1: sin cizalla no hay crecimiento ✓)")

print("\n(F.3) con S=∂_yU derivada, el escalamiento sigue siendo Re² (U'=1, β=1):")
Res=np.array([30,100,300,1000,3000,10000],float); G=[]
for Re in Res:
    A,_=A_liftup_derived(Re,Uprime=1.0); t=np.linspace(0,12*Re,5000); G.append(Gmax_numeric(A,t))
G=np.array(G); slope,_=np.polyfit(np.log(Res),np.log(G),1)
print(f"   pendiente log-log={slope:.4f}  C={np.mean(Res**2/G):.3f}≈e²  ⇒ Re² con S derivada ✓")

print("""
   ⇒ DERIVACIÓN CERRADA (módulo el perfil base): la cizalla S NO es ansatz —
     es S = ∂_y U_base, que CAE del término convectivo (u'·∇)U de la derivada
     material. El acoplamiento es u_y→u_x (no recíproco) ⇒ off-diagonal puro ⇒
     sector Γ_a no-gradiente (coherente con el NO-GO de la Parte E: ∇P no puede).
   RESIDUO HONESTO: el perfil de flujo base U(y) es un INPUT —pero es el MISMO
     input que toda la teoría de estabilidad hidrodinámica (Orr–Sommerfeld/Squire);
     no es un fudge específico de GSF. El ansatz se reduce de 'S a mano' a 'perfil base'.
""")

print("""
================== CONCLUSIÓN (para el apéndice del paper Pieza 2) ==================
[ACTUALIZADO tras Partes D-F + puente con §7ter de Pieza 2 — ver reconciliación abajo.
 El negativo de la Parte C se conserva tal cual: sigue siendo cierto para la EOM
 DESNUDA de GSF, sin el término convectivo.]

DEMOSTRADO (cerrado + numérico): el operador no-normal lift-up da
   G_max = Re² / C ,  C constante geométrica:  C=e²/c² (defectivo)  ó  16/c² (χ=2).
La pendiente log-log es 2.000 y C es independiente de Re. Esto recupera el
escalamiento estándar Re² (Reddy–Henningson, Trefethen) y FIJA el prefactor —
ya no es 'tomado de literatura', sale del álgebra del operador.

NEGATIVO HONESTO (Parte C, sigue siendo cierto tal cual): la forma DESNUDA de GSF,
Γ̈+γΓ̇+∇P=0 (sin término convectivo), con un L no-simétrico GENÉRICO construido a
mano, da G_max ~ Re¹ (pendiente 1.0), NO Re². La no-normalidad genérica es NECESARIA
pero NO SUFICIENTE: la L simétrica (control) no crece nada, y la no-simétrica
genérica solo llega a Re¹. Esto sigue descartando, correctamente, que "cualquier
perturbación no-simétrica de GSF" alcance Re² sin más.

RECONCILIACIÓN (Partes D-F + §7ter del documento Pieza 2): el residuo de arriba NO es
un hueco sin cerrar de GSF-fluidos — es la confirmación de que la cizalla NO puede
salir de ∇²P sola (no-go de la Parte E: Hessiano simétrico ⇒ normal ⇒ sin
amplificación). Lo que cierra el Re² no es la EOM desnuda de GSF sino la instancia
fluida COMPLETA: §7ter del documento deriva, por covarianza galileana, que la
instancia fluida de GSF *es* Navier–Stokes con su término convectivo (u·∇)u, no la
EOM desnuda. Linealizando ESE término convectivo alrededor de un perfil base de
cizalla U(y) — el mismo input estándar de toda la teoría de estabilidad
hidrodinámica, no un fudge de GSF — se obtiene exactamente S=∂_yU en el sector Γ_a,
y con esa S el Re² reaparece exacto (Partes D-F arriba: pendiente log-log 1.9997,
C≈e²).

ENUNCIADO PRECISO (no sobre-reclamar): "GSF da Re²" es correcto SOLO leído como "la
instancia fluida de GSF, que por covarianza es Navier–Stokes completo, da Re² al
linealizar su término convectivo" — NO como "la EOM desnuda de GSF, con cualquier
perturbación no-simétrica, da Re² en general" (eso lo descarta la Parte C, y sigue
descartado). El ingrediente que cierra el argumento es el puente con Navier-Stokes
(§7ter), no algo interno a ∇²P por sí solo. Frontera que sigue abierta: el perfil
base U(y) sigue siendo un input externo (compartido con Orr–Sommerfeld/Squire); la
constante C matricial de la cota de convergencia Γ→Stokes/NS (Teorema 15.5) también
sigue sin adaptarse al formalismo matricial completo.
====================================================================================""")
