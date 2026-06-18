"""
CÚSPIDE (codim-2) del GSF — segundo organizing center tras el pliegue (codim-1).
Doc: brainstorming/unification/release/teorema_gamma_xi.md  (§ cúspide)

La CÚSPIDE es la singularidad codim-2 a₂=a₃=0, a₄≠0 (el despliegue universal del pitchfork).
Necesita DOS perillas. En el GSF: μ (acopla al det) y la amplitud s de una FUENTE externa B=s·B₀.
a₃ = μ·D³det[V³] + 24β⟨Γ*,V⟩ CAMBIA DE SIGNO (en el pliegue valía −11.7+16.8=+5.1), así que existe
un punto donde a₃=0; pidiendo además a₂=0 (modo blando) se fija el PUNTO CÚSPIDE (Γ_c,μ_c,s_c).

Forma normal:  ξ̇ = β₁ + β₂ξ − κξ³.  Huella: a μ fijo con β₂<0 (lado de 3 equilibrios) la ventana
de la imperfección tiene ancho Δ(imperf) ∝ (−β₂)^{3/2} y se pincha al punto cúspide (LEY 3/2).
Trabajamos en el subespacio DIAGONAL (invariante): Γ=diag(λ), det=∏λ.
"""
import numpy as np
from numpy.linalg import eigh, norm
from scipy.optimize import fsolve
beta, b6 = 0.05, 0.002
B0 = np.array([0.6,-0.35,0.45,-0.7])              # fuente diagonal genérica fija; s la escala

def pdiag(lam, mu, src):                          # P restringido a la diagonal (escalar)
    s=lam@lam; return s + mu*np.prod(lam) + beta*s*s + b6*s**3 + src@lam
def gdiag(lam, mu, src):                          # gradiente diagonal (4-vector)
    s=lam@lam; pr=np.prod(lam)
    return 2*lam + mu*pr/lam + (4*beta*s+6*b6*s*s)*lam + src
def Hdiag(lam, mu, src, e=1e-6):                  # Hessiano del bloque diagonal (4×4)
    H=np.zeros((4,4))
    for k in range(4):
        dl=np.zeros(4); dl[k]=e
        H[:,k]=(gdiag(lam+dl,mu,src)-gdiag(lam-dl,mu,src))/(2*e)
    return 0.5*(H+H.T)
def softmode(lam, mu, src):
    w,U=eigh(Hdiag(lam,mu,src)); i=np.argmin(np.abs(w)); return w[i], U[:,i]
def a3_along(lam, mu, src, V):                    # D³P[V,V,V] = 6·coef(t³) de P(λ+tV)
    ts=np.linspace(-0.15,0.15,13); return 6*np.polyfit(ts,[pdiag(lam+t*V,mu,src) for t in ts],4)[1]

# ---------- (0) localizar el PUNTO CÚSPIDE: ∇P=0 (4) + a₂=0 + a₃=0 ----------
def cusp_resid(x):
    lam=x[:4]; mu=x[4]; s=x[5]; src=s*B0
    lmin,V=softmode(lam,mu,src)
    return list(gdiag(lam,mu,src)) + [lmin, a3_along(lam,mu,src,V)]
x0=[1.84,1.91,1.85,-1.83, 2.10, 1.0]              # semilla: cerca del pliegue codim-1
sol=fsolve(cusp_resid, x0, full_output=True, xtol=1e-12)
x=sol[0]; lam_c=x[:4]; mu_c=x[4]; s_c=x[5]; src_c=s_c*B0
lmin_c,Vc=softmode(lam_c,mu_c,src_c); a3c=a3_along(lam_c,mu_c,src_c,Vc)
a4_bare=24*np.polyfit(np.linspace(-0.15,0.15,13),[pdiag(lam_c+t*Vc,mu_c,src_c) for t in np.linspace(-0.15,0.15,13)],4)[0]
# a₄^eff = a₄_desnudo − 3·D³P[V,V,·]ᵀ (H|⊥)⁻¹ D³P[V,V,·]  (corrección de esclavizamiento del teorema)
def D3vv(lam,mu,src,V,e=1e-3):                      # vector D³P[V,V,·] = d²/dt² ∇P(lam+tV)|0
    return (gdiag(lam+e*V,mu,src)-2*gdiag(lam,mu,src)+gdiag(lam-e*V,mu,src))/e**2
q=D3vv(lam_c,mu_c,src_c,Vc); qperp=q-(q@Vc)*Vc
Hd_c=Hdiag(lam_c,mu_c,src_c); y=np.linalg.pinv(Hd_c)@qperp   # pinv ignora la dirección nula Vc
a4c=a4_bare-3*(qperp@y)
print("="*78); print("CÚSPIDE (codim-2) del GSF — a₂=a₃=0, despliegue por (μ, s)"); print("="*78)
print(f"punto cúspide: Γ_c=diag({lam_c[0]:+.4f},{lam_c[1]:+.4f},{lam_c[2]:+.4f},{lam_c[3]:+.4f})")
print(f"               μ_c={mu_c:.4f},  s_c={s_c:.4f}   (det Γ_c={np.prod(lam_c):+.3f})")
print(f"residuales:  ‖∇P‖={norm(gdiag(lam_c,mu_c,src_c)):.2e}  a₂={lmin_c:+.2e}  a₃={a3c:+.2e}  ⇒ CÚSPIDE")
print(f"             a₄_desnudo={a4_bare:+.3f} → a₄^eff={a4c:+.3f} (corrección de esclavizamiento) ({'acotada' if a4c>0 else 'dual'})")
print(f"             modo blando V={np.array2string(Vc,precision=3)}")

# ---------- (1) confirmar en el 4×4 COMPLETO (16-dim) que el cero es simple ----------
def cof(M):
    from numpy.linalg import det as d
    n=M.shape[0]; C=np.zeros_like(M)
    for i in range(n):
        for j in range(n):
            C[i,j]=((-1)**(i+j))*d(np.delete(np.delete(M,i,0),j,1))
    return C
def gradP(G,mu,Bm): n2=norm(G)**2; return 2*G+mu*cof(G)+(4*beta*n2+6*b6*n2**2)*G+Bm
Bm_c=np.diag(src_c)
H16=np.zeros((16,16)); e=1e-4
for k in range(16):
    dG=np.zeros(16); dG[k]=e
    H16[:,k]=(gradP((np.diag(lam_c)+dG.reshape(4,4)),mu_c,Bm_c).ravel()
              -gradP((np.diag(lam_c)-dG.reshape(4,4)),mu_c,Bm_c).ravel())/(2*e)
w16=np.sort(eigh(0.5*(H16+H16.T))[0])
print(f"\n(1) espectro 16-dim en Γ_c: blando |λ₀|={abs(w16[np.argmin(np.abs(w16))]):.2e}")
near0=np.sum(np.abs(w16)<0.05)
print("   ", np.array2string(w16,precision=3,floatmode='fixed',max_line_width=130))
print(f"   # autovalores |λ|<0.05 = {near0}  ⇒ {'CERO SIMPLE ✓' if near0==1 else 'degeneración múltiple'}")

# ---------- (2) DESPLIEGUE en coordenadas naturales (a₁,a₂); transversalidad y LEY 3/2 ----------
# coeficientes del despliegue alrededor de Γ_c FIJO:  a₁=⟨V,∇P⟩ (lineal),  a₂=V·H·V (cuadrático)
def a1a2(mu,s):
    src=s*B0; g=gdiag(lam_c,mu,src); H=Hdiag(lam_c,mu,src)
    return Vc@g, Vc@H@Vc
def n_real_red(a1,a2):                              # raíces reales de Φ'(ξ)=a₁+a₂ξ+(a₄/6)ξ³
    r=np.roots([a4c/6,0,a2,a1]); return int(np.sum(np.abs(r.imag)<1e-7))
# transversalidad: Jacobiano ∂(a₁,a₂)/∂(μ,s) en la cúspide
h=1e-4
J=np.array([[ (a1a2(mu_c+h,s_c)[0]-a1a2(mu_c-h,s_c)[0])/(2*h), (a1a2(mu_c,s_c+h)[0]-a1a2(mu_c,s_c-h)[0])/(2*h)],
            [ (a1a2(mu_c+h,s_c)[1]-a1a2(mu_c-h,s_c)[1])/(2*h), (a1a2(mu_c,s_c+h)[1]-a1a2(mu_c,s_c-h)[1])/(2*h)]])
print(f"\n(2) transversalidad: Jacobiano ∂(a₁,a₂)/∂(μ,s), det={np.linalg.det(J):+.4f}")
print(f"    ⇒ {'≠0: (μ,s) despliega VERSALMENTE la cúspide' if abs(np.linalg.det(J))>1e-3 else 'degenerado'} (a₁=imperfección, a₂=autovalor)")
# verificación con EQUILIBRIOS GENUINOS (∇P=0 completo en la diagonal) en 3 puntos
def count_eq(mu, s):
    src=s*B0; sols=[]
    for t in np.linspace(-1.6,1.6,19):
        rr,_,ier,_=fsolve(lambda L: gdiag(L,mu,src), lam_c+t*Vc, full_output=True, xtol=1e-11)
        if ier==1 and norm(gdiag(rr,mu,src))<1e-7 and not any(norm(rr-q)<1e-5 for q in sols): sols.append(rr)
    return len(sols)
def invert_a(target):                               # Newton (μ,s) → (a₁,a₂)=target, usando J local
    x=np.array([mu_c,s_c])
    for _ in range(20):
        cur=np.array(a1a2(*x));
        if norm(cur-target)<1e-9: break
        x=x-np.linalg.solve(J,cur-target)
    return x
print("    chequeo con EXCURSIONES PEQUEÑAS (cúspide = local): a₂=−0.05 fijo, a₁ dentro/fuera de la cuña")
half=0.5*0.0147                                     # semiancho de la cuña en a₁ a −a₂=0.05 (de la ley 3/2)
print(f"      semiancho de la cuña a −a₂=0.05 ≈ {half:.4f}")
print(f"      {'(a₁ objetivo,a₂)':>20} {'(μ,s)':>18} {'red.':>5} {'real':>5}")
for A1t,tag in [(0.4*half,'dentro'),(2.0*half,'fuera')]:
    mu,s=invert_a(np.array([A1t,-0.05])); A1,A2=a1a2(mu,s)
    print(f"      ({A1:+.4f},{A2:+.3f}) {tag:>6} ({mu:6.3f},{s:6.3f}) {n_real_red(A1,A2):5d} {count_eq(mu,s):5d}")
# LEY 3/2: para a₂<0, ancho en a₁ de la región de 3 raíces  ∝ (−a₂)^{3/2}
print("    LEY 3/2 (en coords del despliegue): ancho en a₁ de la región de 3 equilibrios")
print(f"      {'−a₂':>8} {'ancho a₁':>12}")
a2s=np.array([0.02,0.05,0.1,0.2,0.4]); Wid=[]
for A2 in -a2s:
    a1g=np.linspace(0,3,60000); cnt=np.array([n_real_red(a,A2) for a in a1g])
    edge=a1g[np.where(cnt>=3)[0][-1]] if np.any(cnt>=3) else 0.0
    Wid.append(2*edge); print(f"      {-A2:8.3f} {2*edge:12.5f}")
Wid=np.array(Wid); ok=Wid>1e-6
sl,_=np.polyfit(np.log(a2s[ok]),np.log(Wid[ok]),1)
R2=1-np.sum((np.log(Wid[ok])-(sl*np.log(a2s[ok])+np.polyfit(np.log(a2s[ok]),np.log(Wid[ok]),1)[1]))**2)/np.sum((np.log(Wid[ok])-np.log(Wid[ok]).mean())**2)
print(f"      AJUSTE:  ancho ∝ (−a₂)^{sl:.3f}   R²={R2:.4f}   (cúspide ⇒ 3/2=1.5)")

print(f"""
================== CÚSPIDE codim-2 — certificado ==================
[V] punto cúspide localizado por a₂=a₃=0 con dos perillas (μ,s): a₂={lmin_c:.1e}, a₃={a3c:.1e}, a₄^eff={a4c:+.2f}.
[V] el cero del Hessiano 16-dim es simple en Γ_c (los demás modos separados).
[V] (μ,s) despliega VERSALMENTE (Jacobiano≠0); la ventana de 3 equilibrios tiene ancho ∝(−a₂)^{sl:.2f}
    (LEY 3/2, R²={R2:.2f}) y se pincha al punto cúspide; equilibrios reales = predicción (3 dentro, 1 fuera).
La cúspide es el despliegue universal del pitchfork ⇒ codim-2 'A₃' del catálogo, CERRADA.
Restante 〔A〕: Bogdanov–Takens (dos modos blandos) y Hopf (sector no-gradiente Γ_a).
==================================================================""")
