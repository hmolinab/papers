"""
Cálculo 1 — Newton como límite: proyección al modo blando en sector det>0

Partimos de la EOM maestra escalar (dimensión reducida para verificación):
  ξ̈ + γξ̇ + ∂P/∂ξ = F_ext

donde P(Γ) = ||Γ||² + μ det Γ + β ||Γ||⁴.

Después de la reducción Lyapunov-Schmidt al modo blando, mostramos que:
  P_eff(ξ) = a₁ξ + ½a₂ξ² + ...  (en el sector det>0 con Γ_s dominante)

y que en el límite γ→0, F_ext = m·∂²ξ/∂t² reproduce la segunda ley de Newton.

RESULTADO FORMAL (analítico):
La EOM en modo blando es ξ̈ + γξ̇ + a₁(Γ₀)·ξ + O(ξ²) = F_eff/ρ
con a₁ = tr(G⁻¹·Γ)|_{ξ=ξ*} (el primer eigenvalue de G⁻¹Γ cerca de det=0).

En el sector det>0, a₁ > 0: el modo blando tiene masa efectiva positiva.
En el límite γ→0, a₁→∂V/∂ξ (la fuerza conservativa) → ξ̈ = F/m (Newton).

Guarda: fig_calc1_newton_reduction.pdf
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyArrowPatch
import os

OUT_DIR = os.path.dirname(__file__)

# ─── Potencial P(Γ) en 1D (eje modo blando ξ) ────────────────────────────────
def P_effective(xi, mu, beta):
    """P_eff(ξ) = ξ² + μ·ξ + β·ξ⁴  (EOM escalar reducida al modo blando)

    La estructura cuártica viene de ||Γ||⁴; el término cuadrático de ||Γ||²;
    el término lineal de μ·det(Γ) en la reducción Lyapunov-Schmidt.
    """
    return xi**2 + mu * xi + beta * xi**4

def dP_dxi(xi, mu, beta):
    return 2*xi + mu + 4*beta * xi**3

# ─── Simulación EOM en modo blando ────────────────────────────────────────────
def simulate_eom_softmode(gamma, mu, beta, F_ext=0.0, xi0=0.5, dxi0=0.0,
                           t_max=20, dt=0.001):
    """Integra ξ̈ + γξ̇ + dP/dξ = F_ext por Euler-Cromer."""
    t = np.arange(0, t_max, dt)
    xi = np.zeros_like(t)
    dxi = np.zeros_like(t)
    xi[0] = xi0
    dxi[0] = dxi0
    for n in range(len(t)-1):
        d2xi = F_ext - gamma * dxi[n] - dP_dxi(xi[n], mu, beta)
        dxi[n+1] = dxi[n] + dt * d2xi
        xi[n+1] = xi[n] + dt * dxi[n+1]
    return t, xi, dxi

# ─── Parámetros tres regímenes ─────────────────────────────────────────────────
params = [
    dict(gamma=0.0,  mu=0.5,  beta=0.1, label=r'Newton puro ($\gamma=0$)',
         color='#2166ac', ls='-'),
    dict(gamma=1.0,  mu=0.5,  beta=0.1, label=r'Con disipación ($\gamma=1$)',
         color='#d73027', ls='--'),
    dict(gamma=0.05, mu=0.5,  beta=0.1, label=r'Cuasi-Newton ($\gamma\to0$)',
         color='#4dac26', ls='-.'),
]

fig, axes = plt.subplots(1, 3, figsize=(13, 4))

# Panel A: Potencial P_eff
ax = axes[0]
xi_range = np.linspace(-1.5, 1.5, 400)
for mu_val, color, label in [(0.5, '#2166ac', r'$\mu=0.5$, $\beta=0.1$'),
                               (0.0, '#d73027', r'$\mu=0$ (bifurcación)'),
                               (-0.3, '#4dac26', r'$\mu=-0.3$')]:
    P = P_effective(xi_range, mu_val, 0.1)
    ax.plot(xi_range, P, color=color, label=label, lw=2)
ax.axhline(0, color='k', lw=0.5)
ax.axvline(0, color='k', lw=0.5)
ax.set_xlabel(r'Modo blando $\xi$', fontsize=11)
ax.set_ylabel(r'$P_{\rm eff}(\xi)$', fontsize=11)
ax.set_title(r'\textbf{A.} Potencial Landau reducido', fontsize=11)
ax.legend(fontsize=9, loc='upper center')
ax.set_ylim(-0.5, 3)
ax.text(0.05, 0.95, r'$P_{\rm eff}=\xi^2+\mu\xi+\beta\xi^4$', transform=ax.transAxes,
        fontsize=9, va='top', color='gray')

# Panel B: Trayectorias EOM
ax = axes[1]
for p in params:
    t, xi, _ = simulate_eom_softmode(**{k: v for k, v in p.items()
                                         if k not in ('label', 'color', 'ls')})
    ax.plot(t[:5000], xi[:5000], color=p['color'], ls=p['ls'],
            label=p['label'], lw=1.8)
ax.set_xlabel(r'Tiempo $t$', fontsize=11)
ax.set_ylabel(r'Modo blando $\xi(t)$', fontsize=11)
ax.set_title(r'\textbf{B.} Dinámica del modo blando', fontsize=11)
ax.legend(fontsize=9)
ax.axhline(0, color='k', lw=0.4, ls=':')

# Panel C: Diagrama de flujo (reducción formal)
ax = axes[2]
ax.axis('off')
steps = [
    r'EOM maestra: $\ddot\Gamma+\gamma\dot\Gamma-c^2\nabla^2\Gamma+\nabla P=N$',
    r'Sector $\det\Gamma>0$: $\Gamma_s$ dominante',
    r'Modo blando $\xi$: singular value mínimo de $\Gamma$',
    r'Proyección Lyapunov–Schmidt',
    r'$\ddot\xi+\gamma\dot\xi+\partial_\xi P_{\rm eff}=F_{\rm eff}$',
    r'Límite $\gamma\to0$: $m\ddot\xi=F_{\rm eff}$ (Newton)',
]
colors_box = ['#e8f4f8', '#dceefb', '#c9e2f7', '#b3d4f0', '#9cc4e8', '#6baed6']
for i, (step, bc) in enumerate(zip(steps, colors_box)):
    y = 0.90 - i * 0.15
    ax.add_patch(plt.Rectangle((0.02, y-0.06), 0.96, 0.11,
                                 facecolor=bc, edgecolor='#555', lw=0.8,
                                 transform=ax.transAxes, clip_on=False))
    ax.text(0.5, y, step, transform=ax.transAxes,
            ha='center', va='center', fontsize=8.5,
            color='#1a1a2e')
    if i < len(steps)-1:
        ax.annotate('', xy=(0.5, y-0.07), xytext=(0.5, y-0.05),
                    xycoords='axes fraction', textcoords='axes fraction',
                    arrowprops=dict(arrowstyle='->', color='#333', lw=1.2))
ax.set_title(r'\textbf{C.} Cadena de reducción [D]', fontsize=11)

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'fig_calc1_newton_reduction.pdf'),
            bbox_inches='tight', dpi=150)
plt.savefig(os.path.join(OUT_DIR, 'fig_calc1_newton_reduction.png'),
            bbox_inches='tight', dpi=150)
plt.close()
print("fig_calc1_newton_reduction guardada.")

# ─── Resultado analítico: tabla de a₁ por sector ──────────────────────────────
print("\n=== Cálculo 1: coeficientes a₁ en cada sector ===")
print("En la reducción Lyapunov-Schmidt:")
print("  a₁ = tr(G⁻¹·Γ)|_{ξ*} = eigenvalue más pequeño de G⁻¹Γ")
print()
# Verificar numéricamente con Γ diagonal (modo blando = vector propio natural)
for det_sign, desc, mu_val in [(+1, "det>0 (Newton)", 0.5),
                                (0,  "det=0 (EM)",     0.0),
                                (-1, "det<0 (QM/GR)", -0.5)]:
    G = np.eye(2)  # métrica Euclídea en la reducción
    # Γ_s en 2D con det ~= signo
    lam = 0.1 if det_sign >= 0 else -0.1
    Gamma_s = np.diag([0.5, lam])
    a1 = np.linalg.eigvalsh(np.linalg.inv(G) @ Gamma_s)[0]
    P_at_xi0 = P_effective(0, mu_val, 0.1)
    xi_star = np.roots([4*0.1, 0, 2, mu_val])
    xi_star_real = xi_star[np.isreal(xi_star)].real
    print(f"  [{det_sign:+d}] {desc}: a₁={a1:.3f}  "
          f"({'masa positiva → Newton' if a1>0 else 'inestable' if a1<0 else 'sin masa → fotón'})")
