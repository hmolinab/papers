"""
Cálculo 4 — Película espectral: trayectorias de eigenvalues en ℂ

La "foto" de Γ es su espectro {λᵢ} ∈ ℂ.
La "película" es {λᵢ(t)} mientras Γ evoluciona.

Para cada sector mostramos:
  - Las trayectorias {λᵢ(t)} en el plano complejo
  - El mapa (det Γ, ||Γ_a||) en el tiempo
  - El atlas completo: dónde vive cada sector en el espacio (Re λ, Im λ)

Guarda: fig_calc4_spectral_film.pdf
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import os

OUT_DIR = os.path.dirname(__file__)

def eom_Gamma_step(Gamma, dGamma, dt, gamma, mu, beta):
    norm2 = np.sum(Gamma * Gamma)
    det = np.linalg.det(Gamma)
    try:
        adj = det * np.linalg.inv(Gamma)
    except:
        adj = np.zeros_like(Gamma)
    dP = 2 * Gamma + mu * adj.T + 4 * beta * norm2 * Gamma
    d2Gamma = -gamma * dGamma - dP
    dGamma_new = dGamma + dt * d2Gamma
    Gamma_new = Gamma + dt * dGamma_new
    return Gamma_new, dGamma_new

def simulate_spectrum(Gamma0, dGamma0, gamma, mu, beta, t_max=12, dt=0.02):
    t_arr = np.arange(0, t_max, dt)
    Gamma = Gamma0.copy()
    dGamma = dGamma0.copy()
    lambdas = []
    dets = []
    norms = []
    for t in t_arr:
        eigs = np.linalg.eigvals(Gamma)
        eigs_sorted = sorted(eigs, key=lambda z: (z.real, z.imag))
        lambdas.append(eigs_sorted)
        dets.append(np.linalg.det(Gamma))
        norms.append(np.sqrt(np.sum(Gamma * Gamma)))
        Gamma, dGamma = eom_Gamma_step(Gamma, dGamma, dt, gamma, mu, beta)
    return t_arr, np.array(lambdas, dtype=complex), np.array(dets), np.array(norms)

gamma_val = 0.4
beta = 0.1
dGamma_pert = np.array([[0, 0.3, 0.1, 0],
                          [-0.3, 0, 0.2, 0.1],
                          [-0.1, -0.2, 0, 0.15],
                          [0, -0.1, -0.15, 0]], dtype=float) * 0.3

sector_configs = [
    dict(label=r'det>0 (Newton/masivo)',
         Gamma0=np.diag([1.0, 0.8, 0.5, 0.3]),
         mu=0.1, color='#2166ac'),
    dict(label=r'det=0 (borde, fotón)',
         Gamma0=np.diag([1.0, 0.7, 0.3, 0.001]),
         mu=0.0, color='#fd8d3c'),
    dict(label=r'det<0 (QM/boost)',
         Gamma0=np.diag([1.0, 0.5, -0.2, -0.4]),
         mu=-0.1, color='#d73027'),
]

fig = plt.figure(figsize=(14, 10))

# ─── Fila superior: trayectorias en plano complejo ─────────────────────────────
for col, sc in enumerate(sector_configs):
    ax = fig.add_subplot(2, 3, col+1)

    t, lambdas, dets, norms = simulate_spectrum(
        sc['Gamma0'], dGamma_pert, gamma_val, sc['mu'], beta)

    n_eigs = lambdas.shape[1]
    alphas = np.linspace(0.2, 1.0, len(t))

    for ie in range(n_eigs):
        traj_r = lambdas[:, ie].real
        traj_i = lambdas[:, ie].imag
        # Colorear la trayectoria por tiempo (más oscuro = más tarde)
        for j in range(0, len(t)-1, 2):
            ax.plot(traj_r[j:j+2], traj_i[j:j+2],
                    color=sc['color'], alpha=alphas[j], lw=1.2)
        # Marcar inicio y fin
        ax.plot(traj_r[0], traj_i[0], 'o', color=sc['color'],
                ms=6, alpha=0.5, zorder=5)
        ax.plot(traj_r[-1], traj_i[-1], 's', color=sc['color'],
                ms=6, zorder=6)

    # Ejes
    ax.axhline(0, color='k', lw=0.8)
    ax.axvline(0, color='k', lw=0.8, ls='--', alpha=0.5)
    ax.set_xlabel(r'$\mathrm{Re}(\lambda_i)$', fontsize=10)
    ax.set_ylabel(r'$\mathrm{Im}(\lambda_i)$', fontsize=10)
    ax.set_title(sc['label'], fontsize=10, color=sc['color'], fontweight='bold')
    ax.grid(alpha=0.25)

    # Regiones
    ax.axvspan(ax.get_xlim()[0] if ax.get_xlim()[0] < 0 else -0.01,
               0, alpha=0.05, color='red')
    ax.text(0.02, 0.95, r'$\circ=t_0$, $■=t_f$', transform=ax.transAxes,
            fontsize=7, color='gray')

    det_sign = '+' if dets[0] > 0 else ('=0' if abs(dets[0]) < 0.01 else '-')
    ax.text(0.98, 0.95, rf'$\det_0{det_sign}$', transform=ax.transAxes,
            fontsize=9, ha='right', color=sc['color'])

# ─── Fila inferior: atlas y evolución del det ────────────────────────────────
# Panel 4: Atlas espectral (foto del sector)
ax4 = fig.add_subplot(2, 3, 4)
# Mostrar eigenvalues iniciales para cada sector en el plano complejo
for sc in sector_configs:
    eigs = np.linalg.eigvals(sc['Gamma0'])
    for ie, ev in enumerate(eigs):
        ax4.scatter(ev.real, ev.imag, color=sc['color'], s=80,
                    zorder=5, edgecolors='white', lw=0.5)
    # Leyenda
    ax4.scatter([], [], color=sc['color'], s=60,
                label=sc['label'].split('(')[0].strip())
ax4.axhline(0, color='k', lw=0.8)
ax4.axvline(0, color='k', lw=0.8, ls='--', alpha=0.5)
ax4.set_xlabel(r'$\mathrm{Re}(\lambda)$', fontsize=10)
ax4.set_ylabel(r'$\mathrm{Im}(\lambda)$', fontsize=10)
ax4.set_title(r'\textbf{Atlas espectral: foto $t_0$ por sector}', fontsize=10)
ax4.legend(fontsize=8, loc='upper right')
ax4.grid(alpha=0.25)
# Zonas del plano complejo
ax4.axvspan(-0.1, 0, alpha=0.08, color='red')
ax4.text(0.02, 0.05, r'inestable\n(Re<0)', transform=ax4.transAxes,
         fontsize=7, color='red')
ax4.text(0.55, 0.05, r'estable\n(Re>0)', transform=ax4.transAxes,
         fontsize=7, color='green')

# Panel 5: Evolución de det(Γ(t))
ax5 = fig.add_subplot(2, 3, 5)
for sc in sector_configs:
    t, lambdas, dets, norms = simulate_spectrum(
        sc['Gamma0'], dGamma_pert, gamma_val, sc['mu'], beta)
    ax5.plot(t, dets, color=sc['color'], lw=2,
             label=sc['label'].split('(')[0].strip())
ax5.axhline(0, color='orange', lw=2, ls='--', label=r'$\det=0$ (borde)')
ax5.set_xlabel(r'Tiempo $t$', fontsize=10)
ax5.set_ylabel(r'$\det\,\Gamma(t)$', fontsize=10)
ax5.set_title(r'\textbf{Cruce de sector: } $\det\,\Gamma(t)$', fontsize=10)
ax5.legend(fontsize=8)
ax5.grid(alpha=0.25)
ax5.set_ylim(-0.5, 0.5)
ax5.text(0.5, 0.95, r'Bisagra: $\det=0$', transform=ax5.transAxes,
         ha='center', fontsize=9, color='orange')

# Panel 6: Mapa (det, C) — el atlas de dos variables
ax6 = fig.add_subplot(2, 3, 6)
def C_coherence(G):
    I2 = np.sum(G * G)
    I1 = np.trace(G @ G)
    return (I2 - I1) / (2 * I2) if I2 > 1e-12 else 0.0

for sc in sector_configs:
    t, lambdas, dets, norms = simulate_spectrum(
        sc['Gamma0'], dGamma_pert, gamma_val, sc['mu'], beta)
    # Reconstruir C a lo largo de la trayectoria
    Gamma = sc['Gamma0'].copy()
    dGamma = dGamma_pert.copy()
    C_traj = []
    det_traj = []
    for _ in t:
        C_traj.append(C_coherence(Gamma))
        det_traj.append(np.linalg.det(Gamma))
        Gamma, dGamma = eom_Gamma_step(Gamma, dGamma, 0.02, gamma_val, sc['mu'], beta)
    C_traj = np.array(C_traj)
    det_traj = np.array(det_traj)
    alphas = np.linspace(0.2, 1.0, len(t))
    for j in range(0, len(t)-2, 3):
        ax6.plot(det_traj[j:j+4], C_traj[j:j+4],
                 color=sc['color'], alpha=alphas[j], lw=1.5)
    ax6.scatter(det_traj[0], C_traj[0], color=sc['color'], s=60,
                marker='o', zorder=5, edgecolors='white', lw=0.5)
    ax6.scatter(det_traj[-1], C_traj[-1], color=sc['color'], s=60,
                marker='s', zorder=6, edgecolors='white', lw=0.5,
                label=sc['label'].split('(')[0].strip())

ax6.axvline(0, color='orange', lw=2, ls='--', alpha=0.8)
ax6.set_xlabel(r'$\det\,\Gamma$', fontsize=10)
ax6.set_ylabel(r'Coherencia $\mathcal{C}$', fontsize=10)
ax6.set_title(r'\textbf{Atlas dinámico: trayectorias en }$(\det\Gamma,\,\mathcal{C})$', fontsize=10)
ax6.legend(fontsize=8)
ax6.set_xlim(-0.5, 0.5)
ax6.set_ylim(-0.05, 1.05)
ax6.grid(alpha=0.25)
# Etiquetas de zonas
ax6.text(0.1, 0.85, 'Newton', fontsize=8, color='#2166ac', alpha=0.7)
ax6.text(-0.45, 0.85, 'QM/boost', fontsize=8, color='#d73027', alpha=0.7)
ax6.text(-0.05, 0.05, r'$\det\!=\!0$', fontsize=8, color='orange', rotation=90)

fig.suptitle(r'Película espectral $\{\lambda_i(t)\}$ — el atlas de la física como espectro de $\Gamma(t)$',
             fontsize=12, y=1.01)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'fig_calc4_spectral_film.pdf'),
            bbox_inches='tight', dpi=150)
plt.savefig(os.path.join(OUT_DIR, 'fig_calc4_spectral_film.png'),
            bbox_inches='tight', dpi=150)
plt.close()
print("fig_calc4_spectral_film guardada.")
