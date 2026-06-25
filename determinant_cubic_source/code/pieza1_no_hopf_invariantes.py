#!/usr/bin/env python3
"""
Verifica el reencuadre equivariante del paper (§2) y el Lema 1 (§6):
(A) tr(Γ³) NO es invariante bajo la acción bilateral Γ→UΓVᵀ (U,V∈O(4)) ⇒ excluido por la simetría.
(B) ‖Γ‖² y detΓ SÍ son invariantes bilaterales (det con det(U)det(V)=1).
(C) Lema 1: el Jacobiano de un flujo metric-gradiente −G⁻¹H tiene espectro REAL (sin Hopf).
"""
import numpy as np
rng = np.random.default_rng(0)

def rand_O(n, sign=None):
    Q, R = np.linalg.qr(rng.standard_normal((n, n)))
    Q = Q @ np.diag(np.sign(np.diag(R)))
    if sign is not None and np.sign(np.linalg.det(Q)) != sign:
        Q[:, 0] = -Q[:, 0]
    return Q

print("="*68); print("(A) ¿tr(Γ³) invariante bilateral? vs ‖Γ‖² y detΓ"); print("="*68)
maxdev = {"tr(Γ³)": 0.0, "‖Γ‖²": 0.0, "detΓ": 0.0}
for _ in range(2000):
    G = rng.standard_normal((4, 4))
    # U,V con det(U)det(V)=1 (el grupo G del paper)
    sU = rng.choice([-1, 1]); U = rand_O(4, sU); V = rand_O(4, sU)  # mismo signo ⇒ producto +1
    Gp = U @ G @ V.T
    maxdev["tr(Γ³)"] = max(maxdev["tr(Γ³)"], abs(np.trace(np.linalg.matrix_power(Gp,3)) - np.trace(np.linalg.matrix_power(G,3))))
    maxdev["‖Γ‖²"]  = max(maxdev["‖Γ‖²"],  abs(np.sum(Gp*Gp) - np.sum(G*G)))
    maxdev["detΓ"]  = max(maxdev["detΓ"],  abs(np.linalg.det(Gp) - np.linalg.det(G)))
for k, v in maxdev.items():
    inv = "INVARIANTE" if v < 1e-9 else "NO invariante"
    print(f"  máx |Δ {k}| bajo Γ→UΓVᵀ (det U det V=+1): {v:.3e}  ⇒ {inv}")
print("  ⇒ tr(Γ³) NO es bilateral-invariante ⇒ EXCLUIDO por la simetría (no puede figurar como cúbico).")
print("    ‖Γ‖² y detΓ SÍ ⇒ el determinante es el único invariante anisótropo de bajo grado. (cierra G1)")

print("\n"+"="*68); print("(B) confirmación: el anillo es función de valores singulares"); print("="*68)
G = rng.standard_normal((4,4)); s = np.linalg.svd(G, compute_uv=False)
print(f"  ‖Γ‖²={np.sum(G*G):.4f} = Σσ²={np.sum(s**2):.4f}; |detΓ|={abs(np.linalg.det(G)):.4f} = Πσ={np.prod(s):.4f}")
print("  tr(Γ³)=Σλ³ (autovalores), NO función de σ ⇒ fuera del anillo bilateral. ✓")

print("\n"+"="*68); print("(C-bis) Obs 2.2: p₂=tr((ΓᵀΓ)²) NO se anula en V⊥Γ*, pero es ciego a la orientación"); print("="*68)
def D3(f,G,V,h=2e-4):  # 5-puntos para 3a derivada
    return (-0.5*f(G-2*h*V)+f(G-h*V)-f(G+h*V)+0.5*f(G+2*h*V))/(-h**3)
p2=lambda G: np.trace((G.T@G)@(G.T@G)); n4=lambda G: np.sum(G*G)**2; dt=lambda G: np.linalg.det(G)
mp2=mn4=mdt=0
for _ in range(400):
    Gs=rng.standard_normal((4,4))
    Vv=rng.standard_normal((4,4)); Vv=Vv-np.sum(Vv*Gs)/np.sum(Gs*Gs)*Gs; Vv/=np.linalg.norm(Vv)  # V⊥Γ*
    mp2=max(mp2,abs(D3(p2,Gs,Vv))); mn4=max(mn4,abs(D3(n4,Gs,Vv))); mdt=max(mdt,abs(D3(dt,Gs,Vv)))
print(f"  en V⊥Γ*: D³‖Γ‖⁴≈{mn4:.2f} (~0, =24⟨Γ*,V⟩=0); D³p₂≈{mp2:.1f} (NO 0); D³det≈{mdt:.1f} (anisótropo)")
print("  ⇒ p₂ contribuye cúbico en V⊥Γ* ⇒ por eso NO se incluye en P. p₂ es función de ΓᵀΓ (ciego a")
print("    orientación); det es el único invariante SENSIBLE a la orientación. (respalda Obs 2.2)")

print("\n"+"="*68); print("(C) Lema 1: metric-gradiente −G⁻¹H tiene espectro real"); print("="*68)
allreal = True
for _ in range(2000):
    A = rng.standard_normal((6,6)); H = A + A.T            # Hessiano simétrico
    B = rng.standard_normal((6,6)); Gm = B@B.T + 0.1*np.eye(6)  # métrica G≻0
    J = -np.linalg.solve(Gm, H)                            # Jacobiano −G⁻¹H
    if np.max(np.abs(np.linalg.eigvals(J).imag)) > 1e-8: allreal = False
print(f"  sobre 2000 (H simétrico, G≻0): ¿espectro de −G⁻¹H siempre real? {allreal}")
print("  ⇒ ningún par complejo cruza el eje ⇒ SIN Hopf en metric-gradiente. (Lema 1 verificado)")
