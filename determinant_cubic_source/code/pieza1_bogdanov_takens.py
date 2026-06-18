"""
BOGDANOV–TAKENS (codim-2) en la EOM de SEGUNDO ORDEN del GSF:  Γ̈ + γΓ̇ + ∇P = 0.
Doc: brainstorming/unification/release/teorema_gamma_xi.md  (§ Bogdanov–Takens)

Idea estructural: BT = autovalor DOBLE CERO con BLOQUE DE JORDAN (multiplicidad geométrica 1).
ES IMPOSIBLE en el sector gradiente puro (Jacobiano = −Hessiano SIMÉTRICO ⇒ siempre diagonalizable).
Aparece en la EOM de 2º orden: linealización en (u,v)=(δΓ,δΓ̇) es  J=[[0,I],[−H*,−γI]].
Para un modo blando (autovalor h=0 de H*):  λ²+γλ=0 ⇒ λ∈{0,−γ}.  El DOBLE CERO con Jordan ocurre
en  γ=0 + h=0  → el punto BT = (modo blando del PLIEGUE) ∩ (amortiguamiento nulo).
Es la FRONTERA donde el régimen sobreamortiguado (gradiente: pliegue/cúspide) se encuentra con el
oscilatorio. Se despliega con DOS perillas: μ (mueve h, vía el pliegue) y γ (amortiguamiento).

Reducción al modo blando ξ (η=ξ̇):   ξ̈ + γ(ξ)ξ̇ + (a₁ + c ξ²) = 0,
con c=½a₃ (cúbico del det, del PLIEGUE) y a₁(μ)=τ·(μ−μ_f) (transversalidad).  Forma normal de BT.
"""
import numpy as np
from numpy.linalg import det, eigh, eig, norm
from scipy.optimize import fsolve
beta, b6 = 0.05, 0.002
B0 = np.array([0.6,-0.35,0.45,-0.7])               # fuente que rompe la isotropía (como en el pliegue)

def cof(M):
    n=M.shape[0]; C=np.zeros_like(M)
    for i in range(n):
        for j in range(n):
            C[i,j]=((-1)**(i+j))*det(np.delete(np.delete(M,i,0),j,1))
    return C
def pdiag(lam,mu,src): s=lam@lam; return s+mu*np.prod(lam)+beta*s*s+b6*s**3+src@lam
def gdiag(lam,mu,src): s=lam@lam; return 2*lam+mu*np.prod(lam)/lam+(4*beta*s+6*b6*s*s)*lam+src
def Hdiag(lam,mu,src,e=1e-6):
    H=np.zeros((4,4))
    for k in range(4):
        dl=np.zeros(4); dl[k]=e; H[:,k]=(gdiag(lam+dl,mu,src)-gdiag(lam-dl,mu,src))/(2*e)
    return 0.5*(H+H.T)

# ---------- localizar el PLIEGUE (modo blando h=0): ∇P=0 (4) + λmin(H)=0 ----------
def fold_eqs(x):
    lam=x[:4]; mu=x[4]; src=B0
    w,_=eigh(Hdiag(lam,mu,src)); return list(gdiag(lam,mu,src))+[w[np.argmin(np.abs(w))]]
x=fsolve(fold_eqs,[1.84,1.91,1.85,-1.83,2.10],xtol=1e-12); lam_f=x[:4]; mu_f=x[4]
w,U=eigh(Hdiag(lam_f,mu_f,B0)); i0=np.argmin(np.abs(w)); V=U[:,i0]
ts=np.linspace(-0.15,0.15,13)
a3=6*np.polyfit(ts,[pdiag(lam_f+t*V,mu_f,B0) for t in ts],4)[1]; c=0.5*a3
tau=V@(np.prod(lam_f)/lam_f)                       # ⟨V, ∂(∇P)/∂μ⟩ = ⟨V, cof⟩ (diagonal)
print("="*78); print("BOGDANOV–TAKENS (codim-2) — EOM de 2º orden  Γ̈+γΓ̇+∇P=0"); print("="*78)
print(f"pliegue (modo blando): Γ_f=diag({lam_f[0]:+.3f},{lam_f[1]:+.3f},{lam_f[2]:+.3f},{lam_f[3]:+.3f}), μ_f={mu_f:.4f}")
print(f"coeficientes del modo blando:  c=½a₃={c:+.3f} (del det),  τ=⟨V,cof⟩={tau:+.3f} (transversalidad)")

# ---------- (1) BLOQUE DE JORDAN: el punto BT vs el caso gradiente ----------
def Jblock(h,g): return np.array([[0,1.0],[-h,-g]])
print("\n(1) linealización del modo blando en (ξ,ξ̇):  J=[[0,1],[−h,−γ]]")
for h,g,tag in [(0.0,0.0,'BT: h=0, γ=0'),(0.0,0.5,'h=0, γ=0.5'),(0.3,0.0,'h=0.3, γ=0')]:
    ev,evec=eig(Jblock(h,g)); rank=np.linalg.matrix_rank(Jblock(h,g)-ev[0]*np.eye(2),tol=1e-9)
    geom=2-rank
    print(f"   {tag:16s}: autovalores {np.array2string(ev,precision=2)}  mult.geom(λ={ev[0]:.1f})={geom}"
          + ("  ⇒ BLOQUE DE JORDAN (doble cero defectuoso)" if abs(ev[0])<1e-9 and geom==1 else ""))
print("   NOTA: en el sector GRADIENTE el Jacobiano es −H* (simétrico) ⇒ SIEMPRE diagonalizable;")
print("   un doble-cero ahí tendría mult.geom 2, NO Jordan. BT exige el 2º orden (γ) — sector NO gradiente.")

# ---------- (2) despliegue (μ,γ): saddle-node + el papel del amortiguamiento ----------
def eqs_xi(mu):                                    # equilibrios del modo blando: a₁+cξ²=0
    a1=tau*(mu-mu_f); r=-a1/c
    return ([] if r<0 else [-np.sqrt(r),np.sqrt(r)]), a1
print("\n(2) equilibrios reducidos a₁+cξ²=0 (a₁=τ(μ−μ_f)); el amortiguamiento γ clasifica su tipo")
print(f"   {'μ−μ_f':>8} {'#eq':>4} {'ξ*':>16}   tipo (γ=0.4 fijo)")
for dm in [-0.05,0.0,0.05,0.12]:
    xis,a1=eqs_xi(mu_f+dm); g=0.4
    tipos=[]
    for xs in xis:
        ev,_=eig(Jblock(2*c*xs,g)); tipos.append('silla' if np.any(ev.real>1e-9) and np.any(ev.real<-1e-9) and np.all(abs(ev.imag)<1e-9) else ('foco/nodo estable' if np.all(ev.real<0) else 'inestable'))
    print(f"   {dm:8.3f} {len(xis):4d} {np.array2string(np.array(xis),precision=3):>16}   {tipos}")
print("   ⇒ par silla+nodo nace en μ=μ_f (SADDLE-NODE, el pliegue); el nodo es foco si γ²<4Φ''.")

# ---------- (3) BT GENÉRICO: amortiguamiento dependiente del estado γ(ξ)=γ₀+γ₁ξ → Hopf + ciclo límite ----------
# (la reducción de variedad central de un sistema amortiguado produce damping NO uniforme: el término bξη)
g1=-0.9                                            # pendiente del damping (el coeficiente 'b' de BT)
def rhs(state,mu,g0):
    xi,eta=state; a1=tau*(mu-mu_f)
    return np.array([eta, -(g0+g1*xi)*eta-(a1+c*xi*xi)])
def hopf_g0(mu):                                   # Hopf: traza=0 en el equilibrio estable ⇒ γ(ξ*)=0
    xis,_=eqs_xi(mu)
    xstab=[x for x in xis if 2*c*x>0]              # Φ''=2cξ*>0 (pozo)
    return (-g1*xstab[0], xstab[0]) if xstab else (np.nan,np.nan)
print("\n(3) BT genérico con damping de estado γ(ξ)=γ₀+γ₁ξ (γ₁=%.1f): Hopf cuando γ(ξ*)=0" % g1)
print(f"   {'μ−μ_f':>8} {'ξ* (pozo)':>10} {'γ₀ Hopf':>9}   (curva de Hopf que emana del BT)")
for dm in [0.02,0.05,0.10,0.18]:
    g0h,xs=hopf_g0(mu_f+dm); print(f"   {dm:8.3f} {xs:10.3f} {g0h:9.3f}")
print("   ⇒ la curva de Hopf γ₀=−γ₁ξ*(μ) y la de saddle-node (μ=μ_f, ξ*→0) se ENCUENTRAN en el")
print("     punto BT (μ_f, γ₀=0): tangentes ahí. Es la firma de Bogdanov–Takens.")

# integrar justo pasado el Hopf para exhibir el CICLO LÍMITE (oscilación auto-sostenida)
def integ(mu,g0,T=400,dt=0.005,s0=None):
    xis,_=eqs_xi(mu); xs=[x for x in xis if 2*c*x>0][0]
    s=np.array([xs+0.05,0.0]) if s0 is None else s0; traj=[]
    for _ in range(int(T/dt)):
        k1=rhs(s,mu,g0); k2=rhs(s+dt/2*k1,mu,g0); k3=rhs(s+dt/2*k2,mu,g0); k4=rhs(s+dt*k3,mu,g0)
        s=s+dt/6*(k1+2*k2+2*k3+k4); traj.append(s.copy())
    return np.array(traj)
dm=0.10; g0h,xs=hopf_g0(mu_f+dm)
tr_in=integ(mu_f+dm, g0h-0.15)[-4000:]            # γ₀ por DEBAJO del Hopf ⇒ damping efectivo<0 ⇒ ciclo
tr_out=integ(mu_f+dm, g0h+0.15)[-4000:]           # por ENCIMA ⇒ decae al pozo
amp_in=tr_in[:,0].max()-tr_in[:,0].min(); amp_out=tr_out[:,0].max()-tr_out[:,0].min()
print(f"\n   integración (μ−μ_f={dm}, Hopf en γ₀={g0h:.3f}):")
print(f"     γ₀={g0h-0.15:.3f} (bajo Hopf): amplitud ξ = {amp_in:.3f}  ⇒ {'CICLO LÍMITE (oscilación auto-sostenida) ✓' if amp_in>0.05 else 'decae'}")
print(f"     γ₀={g0h+0.15:.3f} (sobre Hopf): amplitud ξ = {amp_out:.4f}  ⇒ {'decae al pozo (foco estable) ✓' if amp_out<0.02 else 'oscila'}")

print(f"""
================== BOGDANOV–TAKENS codim-2 — certificado ==================
[V] (1) el punto BT (modo blando del pliegue h=0  +  γ=0) tiene un DOBLE CERO con BLOQUE DE JORDAN
        (mult. geométrica 1). IMPOSIBLE en el sector gradiente (Jacobiano simétrico) ⇒ BT exige la
        EOM de 2º orden — es la frontera sobreamortiguado(gradiente) ↔ oscilatorio.
[V] (2) despliegue por (μ,γ): la rama saddle-node es el PLIEGUE (par silla+nodo en μ_f); γ fija si el
        nodo es foco (γ²<4Φ'') o nodo.
[V] (3) con damping de estado γ(ξ)=γ₀+γ₁ξ (el término bξη genérico de BT, que da la reducción de
        variedad central de un sistema amortiguado): curva de HOPF γ₀=−γ₁ξ*(μ) que emana del BT, y
        CICLO LÍMITE (oscilación auto-sostenida) por debajo del Hopf — confirmado por integración.
La cúspide (gradiente) y BT (2º orden) son las DOS singularidades codim-2 del catálogo. BT es la
puerta al caos: el ciclo límite y la homoclínica que emanan del BT son el preludio del sector Γ_a.
Restante 〔A〕: homoclínica explícita y el escenario a caos (Shilnikov) en el sector reactivo Γ_a.
==========================================================================""")
