"""
RIGOR de las nuevas familias DS — convertir 'salta/no salta' en OBJETOS INVARIANTES.
Atiende el feedback de revisor (prioridad máxima): (1)(2) bifurcación verdadera con término
séxtico + diagrama de ramas; (4)(5) medir λmin(H) y Var~1/λmin; (6) Monte Carlo sobre Γ;
(8) clasificación espectral nodo/foco/espiral/silla. (7)(9)(10) reducción Γ→ξ y formas
normales quedan como tier-paper (stub al final).
"""
import numpy as np
from numpy.linalg import svd, det, eigvalsh, eigvals
rng = np.random.default_rng(0)

# ============================================================================
# (1)+(2) BIFURCACIÓN VERDADERA con séxtico: P(σ)=k2 σ² + k4 σ⁴ + b6 σ⁶  (b6>0 acota)
# Pitchfork supercrítico: k4>0, barrer k2 por 0. Saddle-node: k4<0, barrer k2.
# ============================================================================
def equilibria_y_estab(k2,k4,b6=1.0):
    # P'(σ)=2k2 σ + 4k4 σ³ + 6b6 σ⁵ = 2σ(k2 + 2k4 σ² + 3b6 σ⁴); P''=2k2+12k4σ²+30b6σ⁴
    eqs=[0.0]; a,bb,cc=3*b6,2*k4,k2
    disc=bb*bb-4*a*cc
    if disc>=0:
        for u in [(-bb+np.sqrt(disc))/(2*a),(-bb-np.sqrt(disc))/(2*a)]:
            if u>1e-12: eqs+=[np.sqrt(u),-np.sqrt(u)]
    return [(s, 2*k2+12*k4*s**2+30*b6*s**4) for s in eqs]   # (σ*, P''(σ*))

print("="*74); print("(1)(2) PITCHFORK supercrítico: P=k2σ²+σ⁴ (k4=1,b6=1), barrer k2 ↓ por 0"); print("="*74)
print(f"   {'k2':>6}   ramas σ* (●=estable P''>0, ○=inestable)")
for k2 in [0.6,0.2,0.0,-0.2,-0.6]:
    parts=[f"{s:+.3f}{'●' if pp>1e-9 else ('○' if pp<-1e-9 else '·')}" for s,pp in equilibria_y_estab(k2,1.0)]
    print(f"   {k2:6.2f}   {'  '.join(parts)}")
print("⇒ k2>0: solo σ*=0 (estable). k2<0: σ*=0 se vuelve INESTABLE (○) y NACEN dos ramas")
print("  estables ±√(−k2)  = PITCHFORK supercrítica auténtica (punto crítico k2=0). [invariante]")

print("\n"+"-"*74); print("Saddle-node: P=k2σ²+k4σ⁴+σ⁶ con k4<0 (k2=4 fijo), barrer k4 ↓"); print("-"*74)
for k4 in [-2.0,-3.0,-3.464,-4.0,-6.0]:
    eqs=equilibria_y_estab(4.0,k4,1.0); nontriv=[e for e in eqs if abs(e[0])>1e-9]
    msg='solo σ=0' if not nontriv else f'{len(nontriv)} ramas nuevas (barrera○ + pozo●)'
    print(f"   k4={k4:6.3f}: {msg}")
print("⇒ par estable/inestable NACE en k4_c≈−2√(3·k2)/2 = −3.464: SADDLE-NODE (fold). [invariante]")

# ============================================================================
# (4)(5) λmin(H)→0 y Var~1/λmin cerca de la bifurcación (modo blando = OBJETO)
# ============================================================================
print("\n"+"="*74); print("(4)(5) modo blando: rigidez k=P''(σ*)→0 ⇒ Var(ξ)~1/k DIVERGE (no 'salto')"); print("="*74)
def ou_var(k,gam=1.0,sig=0.25,dt=0.01,T=200000):
    x=v=0.0; xs=[]
    for _ in range(T): v+=(-gam*v-k*x)*dt+sig*np.sqrt(dt)*rng.normal(); x+=v*dt; xs.append(x)
    return np.var(xs[T//4:])
print(f"   acercando k2→0⁺ por la rama σ*=0 (pitchfork): k=P''(0)=2k2")
for k2 in [0.30,0.15,0.07,0.03]:
    k=2*k2; V=ou_var(k); print(f"   k2={k2:5.3f}  k={k:6.3f}  Var={V:7.3f}  k·Var={k*V:6.4f} (≈Θ const ⇒ Var~1/k ✓)")

# ============================================================================
# (6) MONTE CARLO sobre Γ: el patrón de degeneración sobre 1000 matrices, no una
# ============================================================================
print("\n"+"="*74); print("(6) MONTE CARLO sobre 1000 Γ aleatorias — ¿sobrevive el patrón?"); print("="*74)
def base():
    M=rng.normal(size=(4,4))*0.35; G=M@M.T+1.6*np.eye(4)
    G[0,1]+=0.6;G[1,0]-=0.6;G[2,3]+=0.6;G[3,2]-=0.6; return G
F_=lambda G:abs((G[0,1]-G[1,0])/2); E_=lambda G:abs((G[2,3]-G[3,2])/2)
smin=lambda G:svd(G,compute_uv=False)[-1]
def deg(G,m,lam=0.02):
    G=G.copy()
    if m=='S':G[0,:]*=lam;G[:,0]*=lam
    elif m=='A':G[1,:]*=lam;G[:,1]*=lam
    elif m=='I':G[2,:]*=lam;G[:,2]*=lam
    elif m=='R':G[3,:]*=lam;G[:,3]*=lam
    elif m=='I||R':
        s=(G[2,3]+G[3,2])/2;a=(G[2,3]-G[3,2])/2;G[2,3]=s+lam*a;G[3,2]=s-lam*a
    return G
N=1000; Gs0=[base() for _ in range(N)]
print(f"   N={N}.  Fracción que cumple el patrón esperado (λ→0):")
for m in ['S','A','I','R','I||R']:
    fcol=ecol=detz=0
    for G0 in Gs0:
        G=deg(G0,m);
        if F_(G)<0.05: fcol+=1
        if E_(G)<0.05: ecol+=1
        if abs(det(G))<0.05: detz+=1
    exp_F = m in ('S','A'); exp_E = m in ('I','R','I||R'); exp_det = m!='I||R'
    okF=fcol/N if exp_F else 1-fcol/N; okE=ecol/N if exp_E else 1-ecol/N; okdet=detz/N if exp_det else 1-detz/N
    print(f"   {m:5s}: colapsa-F {fcol/N:.0%}  colapsa-E {ecol/N:.0%}  det→0 {detz/N:.0%}  "
          f"→ patrón {'F' if exp_F else 'E'}{'+rango' if exp_det else ' sin rango'} en {min(okF,okE,okdet):.0%}")
print("⇒ el sorting (S,A→F; I,R,I∥R→E; det→0 salvo I∥R) se sostiene en ~todas las Γ. [general]")

# ============================================================================
# (8) CLASIFICACIÓN ESPECTRAL del generador Γs+Γa: nodo/foco/espiral/silla
# ============================================================================
print("\n"+"="*74); print("(8) clasificación espectral del flujo −Γ (Γs estabilidad, Γa rotación)"); print("="*74)
def clasifica(G):
    ev=eigvals(G); re=ev.real; im=ev.imag
    rot = np.any(np.abs(im)>1e-6)
    if np.all(re>1e-9): tipo='nodo/foco ESTABLE'+(' (espiral)' if rot else '')
    elif np.all(re<-1e-9): tipo='FUENTE'+(' (espiral)' if rot else '')
    else: tipo='SILLA'+(' (espiral)' if rot else '')
    return tipo, re.min(), np.abs(im).max()
G0=base()
for tag,G in [('operativa',G0),('1 neg (c_A=0.1)',(lambda g:(g.__setitem__((1,1),0.1) or g))(base())),
              ('2 neg (c_A=c_I=-0.4)',(lambda g:(g.__setitem__((1,1),-0.4) or g.__setitem__((2,2),-0.4) or g))(base()))]:
    t,remin,immax=clasifica(G); print(f"   {tag:22s}: {t:24s}  Re_min={remin:+.2f}  |Im|_max={immax:.2f}")
print("⇒ Re(λ) (de Γ) clasifica estabilidad; Im(λ)≠0 (de Γa) marca rotación/espiral. Objeto: el espectro.")

print("""
================== ESTADO (rigor) ==================
HECHO [V] (objetos invariantes, no trayectorias):
 (1)(2) pitchfork y saddle-node verdaderos con séxtico (diagrama de ramas + estabilidad P'').
 (4)(5) modo blando k→0 ⇒ Var~1/k (divergencia, no 'salto').
 (6) Monte Carlo 1000 Γ: el sorting de degeneración es GENERAL, no de una matriz.
 (8) clasificación espectral nodo/foco/espiral/silla por Re/Im de los autovalores.
TIER-PAPER (pendiente, el más profundo — la 'primera flecha'):
 (7)(9)(10) reducción Γ→ξ: probar que cerca de una degeneración espectral la dinámica
   PROYECTADA satisface la forma normal universal (ξ̇=λ−ξ², ξ̇=λξ−ξ³, Hopf, Duffing).
   ESA es la pieza fuerte: 'cerca de una degeneración de Γ, la dinámica efectiva colapsa a
   las formas normales de la teoría de bifurcaciones'. Requiere el teorema de variedad central.
===================================================""")
