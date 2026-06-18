"""
English figures for the autonomous manuscript (paper_DS_normal_forms_en.md).
Outputs 4 figures (vector PDF + PNG) to brainstorming/unification/release/figs_en/.
Same content as pieza1_figuras_paper.py; labels in English.
"""
import numpy as np, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"axes.grid":True,"grid.alpha":0.25,"figure.dpi":140})
OUT=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","figs_en"))
os.makedirs(OUT,exist_ok=True)
def save(fig,name):
    for ext in ("pdf","png"): fig.savefig(os.path.join(OUT,f"{name}.{ext}"),bbox_inches="tight")
    plt.close(fig); print("  ",os.path.join(OUT,name+".pdf"))
BLU,RED="#1f5fa8","#c0392b"

# ---------- Fig 1: codim-1 ----------
fig,(a1,a2)=plt.subplots(1,2,figsize=(9,3.6))
al=np.linspace(0,1.2,400); xp=np.sqrt(al)
a1.plot(al,xp,color=BLU,lw=2.2,label="stable"); a1.plot(al,-xp,color=RED,lw=2.0,ls="--",label="unstable")
a1.scatter([0],[0],color="k",zorder=5,s=25); a1.annotate("fold",(0,0),(0.18,0.25),arrowprops=dict(arrowstyle="->"))
a1.set_title("(a) Fold (saddle-node)  $\\dot\\xi=\\alpha-\\xi^2$")
a1.set_xlabel("$\\alpha\\;(\\propto\\mu-\\mu_*)$"); a1.set_ylabel("equilibria $\\xi^*$"); a1.legend(frameon=False,fontsize=9)
lam=np.linspace(-1,1.2,500); zero=np.zeros_like(lam)
a2.plot(lam[lam<=0],zero[lam<=0],color=BLU,lw=2.2); a2.plot(lam[lam>0],zero[lam>0],color=RED,lw=2.0,ls="--")
lp=lam[lam>0]; a2.plot(lp,np.sqrt(lp),color=BLU,lw=2.2); a2.plot(lp,-np.sqrt(lp),color=BLU,lw=2.2)
a2.scatter([0],[0],color="k",zorder=5,s=25)
a2.set_title("(b) Pitchfork  $\\dot\\xi=\\lambda\\xi-\\xi^3$")
a2.set_xlabel("$\\lambda$  (AM-GM threshold $\\mu=16\\beta$)"); a2.set_ylabel("equilibria $\\xi^*$")
fig.suptitle("Codimension-1 bifurcations: the cubic comes from $\\det\\Gamma$",y=1.02,fontsize=12)
save(fig,"fig1_codim1")

# ---------- Fig 2: cusp ----------
fig,ax=plt.subplots(figsize=(5.4,4.6))
t=np.linspace(0,1.25,400); a2c=-3*(t**2); a1c=2*t**3
ax.plot(a1c,a2c,color="k",lw=2); ax.plot(-a1c,a2c,color="k",lw=2)
ax.fill_betweenx(a2c,-a1c,a1c,color=BLU,alpha=0.15)
ax.text(0,-2.6,"3 equilibria",ha="center",color=BLU,fontsize=11)
ax.text(2.0,-0.5,"1 equilibrium",ha="center",color="0.3",fontsize=11)
ax.scatter([0],[0],color=RED,zorder=5,s=40); ax.annotate("cusp $(a_1,a_2)=(0,0)$",(0,0),(1.2,0.55),
            color=RED,arrowprops=dict(arrowstyle="->",color=RED))
ax.set_xlabel("$a_1$  (imperfection $\\propto$ source $s$)"); ax.set_ylabel("$a_2$  (eigenvalue $\\propto\\mu$)")
ax.set_title("Cusp ($A_3$): universal unfolding of the pitchfork")
ax.set_xlim(-3.5,3.5); ax.set_ylim(-3.2,0.6)
ai=ax.inset_axes([0.60,0.10,0.36,0.34])
na2=np.array([0.02,0.05,0.1,0.2,0.4]); width=2*2*(na2/3)**1.5*np.sqrt(3)
ai.loglog(na2,width,"o-",color=BLU,ms=4); ai.set_title("width $\\propto(-a_2)^{3/2}$",fontsize=8)
ai.tick_params(labelsize=7); ai.set_xlabel("$-a_2$",fontsize=7)
save(fig,"fig2_cusp")

# ---------- Fig 3: Bogdanov–Takens ----------
fig,ax=plt.subplots(figsize=(5.4,4.4))
dm=np.linspace(0,0.25,300); xs=np.sqrt(dm*12.842/2.551); g1=0.9
hopf=g1*xs; hom=0.46/0.639*hopf
ax.axvline(0,color="k",lw=2); ax.text(0.002,0.95,"saddle-node\n(= fold)",rotation=90,va="top",fontsize=8)
ax.plot(dm,hopf,color=BLU,lw=2,label="Hopf  $\\gamma_0=-\\gamma_1\\xi_*$")
ax.plot(dm,hom,color=RED,lw=2,ls="--",label="homoclinic")
ax.fill_between(dm,hom,hopf,color="#f0c000",alpha=0.25)
ax.text(0.16,0.30,"limit cycle",color="#9a7d00",fontsize=10)
ax.text(0.16,0.85,"stable focus",color="0.35",fontsize=10)
ax.text(0.13,0.02,"saddle / escape",color=RED,fontsize=9)
ax.scatter([0],[0],color="k",zorder=6,s=45); ax.annotate("BT",(0,0),(0.03,0.12),fontsize=11,arrowprops=dict(arrowstyle="->"))
ax.set_xlabel("$\\mu-\\mu_f$"); ax.set_ylabel("$\\gamma_0$  (damping)")
ax.set_title("Bogdanov–Takens: three curves emanate from BT"); ax.legend(frameon=False,fontsize=9,loc="upper left")
ax.set_xlim(-0.01,0.25); ax.set_ylim(-0.02,1.0)
save(fig,"fig3_bogdanov_takens")

# ---------- Fig 4: Shilnikov chaos ----------
def rk4(f,s,dt): k1=f(s);k2=f(s+dt/2*k1);k3=f(s+dt/2*k2);k4=f(s+dt*k3); return s+dt/6*(k1+2*k2+2*k3+k4)
def jerk(s,a=2.017): x,y,z=s; return np.array([y,z,-a*z+y*y-x])
s=np.array([0.05,0,0]); dt=0.01
for _ in range(5000): s=rk4(jerk,s,dt)
T=np.array([ (s:=rk4(jerk,s,dt)).copy() for _ in range(30000)])
fig=plt.figure(figsize=(8.2,3.8))
ax=fig.add_subplot(1,2,1,projection="3d")
ax.plot(T[:,0],T[:,1],T[:,2],lw=0.35,color=BLU); ax.set_title("(a) Chaotic attractor (saddle-focus)")
ax.set_xlabel("$\\xi$"); ax.set_ylabel("$\\dot\\xi$"); ax.set_zlabel("$\\ddot\\xi$"); ax.tick_params(labelsize=7)
a3=fig.add_subplot(1,2,2)
s1=np.array([0.05,0,0])
for _ in range(5000): s1=rk4(jerk,s1,dt)
s2=s1+np.array([1e-9,0,0]); sep=[]
for _ in range(9000): s1=rk4(jerk,s1,dt); s2=rk4(jerk,s2,dt); sep.append(np.linalg.norm(s2-s1))
tt=np.arange(len(sep))*dt
a3.semilogy(tt,sep,color=RED,lw=1.2)
a3.plot(tt,1e-9*np.exp(0.0553*tt),"k--",lw=1,label="$e^{\\lambda t},\\ \\lambda=0.055$")
a3.set_title("(b) Sensitive dependence"); a3.set_xlabel("$t$"); a3.set_ylabel("separation")
a3.legend(frameon=False,fontsize=9)
fig.suptitle("Reactive-sector chaos: quadratic jerk, $\\lambda_{\\max}\\approx0.055$",y=1.02,fontsize=12)
save(fig,"fig4_chaos")
print("English figures in:",OUT)
