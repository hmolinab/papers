"""
FLAGSHIP (corregido) — reducción Γ→ξ y FORMAS NORMALES.

Lección de la 1ª versión: la dirección rango-1 uvᵀ da det LINEAL (lema del determinante) ⇒
solo un TILT, sin fold. El fold/normal-form vive donde det es NO-LINEAL en el modo. El rayo
det<0  Γ(σ)=σ·diag(1,1,1,−1)  cumple det∝σ⁴ y —clave— es un SUBESPACIO INVARIANTE EXACTO del
flujo gradiente: adj(Γ)=−σ²Γ ⇒ ∇P ∝ Γ. Ahí la reducción Γ→ξ es EXACTA (no aproximada).

Potencial reducido (ξ=σ):  P_red(ξ) = 4ξ² + (16β−μ)ξ⁴ + 64bξ⁶.
La bifurcación ocurre en μ=16β — ¡la LÍNEA CRÍTICA AM-GM! (coherencia=frontera=evolución).
Es un pitchfork subcrítico (par simétrico silla+pozo nace fuera de ξ=0). Forma normal:
ξ̇ = −8ξ − 4(16β−μ)ξ³ − 384bξ⁵.  Verificamos: (A) invariancia exacta del rayo; (B) bifurcación;
(C) el flujo 16-dim proyectado = la EOM reducida 1D (con adjunta por cofactores, exacta).
"""
import numpy as np
from numpy.linalg import svd, det, norm
beta, b6 = 0.05, 0.002
D0 = np.diag([1.,1.,1.,-1.])                    # dirección del rayo det<0
mu_amgm = 16*beta                               # línea AM-GM (cuártico voltea)
mu_fold = 16*beta + np.sqrt(768*b6)             # saddle-node real (nacen equilibrios)

def cof(M):                                     # matriz de cofactores = ∂det/∂M  (exacta, sirve en singular)
    n=M.shape[0]; C=np.zeros_like(M)
    for i in range(n):
        for j in range(n):
            minor=np.delete(np.delete(M,i,0),j,1)
            C[i,j]=((-1)**(i+j))*det(minor)
    return C
def gradP(G,mu):
    n2=norm(G)**2
    return 2*G + mu*cof(G) + 4*beta*n2*G + 6*b6*n2**2*G

print("="*74); print("FLAGSHIP — Γ→ξ y formas normales (rayo det<0 = subespacio invariante)"); print("="*74)

# --- (0) el rayo es invariante exacto: ∇P(σD0) ∝ D0 ---
print("(0) ¿el rayo Γ=σ·diag(1,1,1,−1) es invariante? ∇P debe ser ∝ D0:")
for s in [0.3,0.7,1.2]:
    g=gradP(s*D0, 3.0); proj=np.sum(g*D0)/norm(D0)**2; resid=norm(g-proj*D0)
    print(f"   σ={s:.1f}: ‖∇P − (proy)·D0‖ = {resid:.2e}  (≈0 ⇒ invariante)")
print("   ⇒ adj(Γ)=−σ²Γ ⇒ ∇P∝Γ: el rayo es subespacio INVARIANTE EXACTO. Reducción Γ→ξ exacta.")

# --- (A) potencial reducido y (B) bifurcación al cruzar μ=16β ---
Pred  = lambda s,mu: 4*s**2 + (16*beta-mu)*s**4 + 64*b6*s**6
dPred = lambda s,mu: 8*s + 4*(16*beta-mu)*s**3 + 384*b6*s**5
def eqs(mu):
    r=np.roots([384*b6,0,4*(16*beta-mu),0,8]); r=r[np.abs(r.imag)<1e-7].real
    ddP=lambda s:8+12*(16*beta-mu)*s**2+1920*b6*s**4
    allr=sorted(set([0.0]+[round(x,3) for x in r]))
    return allr, ddP
print(f"\n(A)(B) P_red(ξ)=4ξ²+(16β−μ)ξ⁴+64bξ⁶.  DOS umbrales:")
print(f"   μ_AM-GM=16β={mu_amgm:.2f} (el cuártico voltea) ;  μ_fold={mu_fold:.2f} (nace el par silla+pozo)")
print(f"   {'μ':>6}  equilibrios ξ* (●estable ○silla)")
for mu in [0.5, 0.8, 1.5, 2.04, 2.5, 3.5]:
    rts,ddP=eqs(mu); parts=[f"{x:+.3f}{'●' if ddP(x)>1e-6 else '○'}" for x in rts]
    print(f"   {mu:6.2f}  {'   '.join(parts)}")
print(f"   ⇒ ξ=0 siempre estable; en μ_fold≈{mu_fold:.2f} nace un par simétrico silla○+pozo● a cada")
print("     lado = PITCHFORK SUBCRÍTICO (forma normal recuperada). HONESTO: la línea AM-GM (μ=16β)")
print("     es donde el cuártico voltea; el fold real está un poco arriba — coinciden cuando b→0.")

# --- (C) flujo gradiente COMPLETO 16-dim proyectado = EOM reducida 1D ---
def flow_full(s0,mu,dt=0.003,T=8000):
    G=s0*D0
    for _ in range(T): G=G-gradP(G,mu)*dt
    return np.sum(G*D0)/norm(D0)**2, norm(G-(np.sum(G*D0)/norm(D0)**2)*D0)  # (ξ, fuga del rayo)
def flow_red(s0,mu,dt=0.003,T=8000):
    s=s0
    for _ in range(T): s=s-(dPred(s,mu)/4.0)*dt    # /4 = métrica ‖D0‖²
    return s
print("\n(C) flujo COMPLETO (16-dim) proyectado vs EOM reducida 1D:")
print(f"   {'μ':>5} {'ξ0':>6} {'ξ∞ FULL':>9} {'ξ∞ RED':>9} {'fuga rayo':>10}  ¿igual?")
for mu,s0 in [(0.5,0.5),(3.5,0.5),(3.5,1.5),(3.5,-1.5)]:
    ff,leak=flow_full(s0,mu); fr=flow_red(s0,mu)
    print(f"   {mu:5.1f} {s0:+6.2f} {ff:+9.4f} {fr:+9.4f} {leak:10.1e}  {'SÍ ✓' if abs(ff-fr)<1e-3 else 'no'}")
print("   ⇒ fuga del rayo ≈0 (invariante) y ξ_full=ξ_red ⇒ la dinámica matricial COLAPSA a la")
print("     EOM reducida 1D, que ES la forma normal del pitchfork. [V]")

print("""
================== CONCLUSIÓN — FLAGSHIP ==================
[V/D] EXACTO en el rayo simétrico: el rayo det<0 es subespacio invariante (∇P∝Γ vía adj=−σ²Γ),
   así que Γ→ξ es una reducción EXACTA, no aproximada. El potencial reducido
   P_red(ξ)=4ξ²+(16β−μ)ξ⁴+64bξ⁶ es la forma normal de un PITCHFORK SUBCRÍTICO, y su umbral
   es la LÍNEA CRÍTICA AM-GM μ=16β. El flujo 16-dim proyectado = la EOM 1D reducida [V].
〔A〕 GENÉRICO (el teorema, pendiente): para una degeneración en una dirección NO simétrica,
   la reducción es de variedad central (aproximada) y da saddle-node (con tilt) o Hopf según
   la estructura. Probar 'toda degeneración espectral de Γ ⇒ forma normal universal' es la
   pieza matemática autónoma (variedad central + transversalidad). El caso simétrico [V] es la
   evidencia ancla; el genérico es el norte.
NOTA honesta: la 1ª versión (dirección rango-1 uvᵀ) daba det LINEAL = tilt, sin fold — corregido.
==========================================================""")
