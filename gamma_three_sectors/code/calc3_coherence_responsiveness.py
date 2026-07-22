"""
Cálculo 3 — C y R como observables de la película Γ(t)

FÓRMULAS EXACTAS en términos de invariantes de Γ:

  ||Γ||²_F = tr(Γᵀ Γ)                 (norma de Frobenius)
  ||Γ_s||²  = (tr(Γ²) + ||Γ||²_F) / 2  (parte simétrica)
  ||Γ_a||²  = (||Γ||²_F - tr(Γ²)) / 2  (parte antisimétrica)

  C(Γ) = ||Γ_a||² / ||Γ||²_F = (||Γ||²_F - tr(Γ²)) / (2·||Γ||²_F)

En términos de invariantes primarios:
  I₁ = tr(Γ²)        (traza del cuadrado)
  I₂ = tr(ΓᵀΓ)       (norma al cuadrado)

  C = (I₂ - I₁) / (2·I₂) = ½(1 - I₁/I₂)

  R = Ċ/γ (tasa de cambio de C normalizada por disipación)

VERIFICACIÓN NUMÉRICA:
Simular Γ(t) en los tres sectores y graficar C(t), R(t), mostrar que
son distinguibles entre sectores.

Guarda: fig_calc3_coherence_observables.pdf
"""

import numpy as np
import matplotlib.pyplot as plt
import os

OUT_DIR = os.path.dirname(__file__)

# ─── Fórmulas de C y R ────────────────────────────────────────────────────────
def C_coherence(Gamma):
    """C(Γ) = (||Γ||²_F - tr(Γ²)) / (2||Γ||²_F).

    Equivalente: C = ||Γ_a||²_F / ||Γ||²_F.
    Rango: [0, 1]. C=0 → Γ simétrico puro. C=1 → Γ antisimétrico puro.
    """
    I2 = np.sum(Gamma * Gamma)           # tr(Γᵀ Γ)
    I1 = np.trace(Gamma @ Gamma)          # tr(Γ²)
    if I2 < 1e-12:
        return 0.0
    return (I2 - I1) / (2 * I2)

def C_from_parts(Gamma):
    """C directa desde las partes."""
    Gs = (Gamma + Gamma.T) / 2
    Ga = (Gamma - Gamma.T) / 2
    norm_Gs = np.sum(Gs * Gs)
    norm_Ga = np.sum(Ga * Ga)
    total = norm_Gs + norm_Ga
    if total < 1e-12:
        return 0.0
    return norm_Ga / total

def responsiveness(C_traj, gamma_val, dt):
    """R(t) = Ċ(t) / γ."""
    dC = np.gradient(C_traj, dt)
    return dC / gamma_val

# ─── EOM de Γ simplificada ────────────────────────────────────────────────────
def eom_Gamma_step(Gamma, dGamma, dt, gamma, mu, beta, c2=1.0):
    """Un paso Euler-Cromer de la EOM 4×4 reducida (sin gradiente espacial).

    Γ̈ + γΓ̇ + ∂P/∂Γ = 0
    P = ||Γ||² + μ det Γ + β||Γ||⁴

    ∂P/∂Γ = 2Γ + μ·adj(Γ)ᵀ + 4β||Γ||²·Γ
    """
    norm2 = np.sum(Gamma * Gamma)
    det = np.linalg.det(Gamma)
    adj = det * np.linalg.inv(Gamma) if abs(det) > 1e-10 else np.zeros_like(Gamma)
    dP = 2 * Gamma + mu * adj.T + 4 * beta * norm2 * Gamma
    d2Gamma = -gamma * dGamma - dP
    dGamma_new = dGamma + dt * d2Gamma
    Gamma_new = Gamma + dt * dGamma_new
    return Gamma_new, dGamma_new

def simulate_sector(Gamma0, dGamma0, gamma, mu, beta, t_max=15, dt=0.01):
    t_arr = np.arange(0, t_max, dt)
    Gamma = Gamma0.copy()
    dGamma = dGamma0.copy()
    C_arr = np.zeros(len(t_arr))
    det_arr = np.zeros(len(t_arr))
    norm_arr = np.zeros(len(t_arr))
    for i, t in enumerate(t_arr):
        C_arr[i] = C_coherence(Gamma)
        det_arr[i] = np.linalg.det(Gamma)
        norm_arr[i] = np.sqrt(np.sum(Gamma * Gamma))
        Gamma, dGamma = eom_Gamma_step(Gamma, dGamma, dt, gamma, mu, beta)
    return t_arr, C_arr, det_arr, norm_arr

# ─── Configuraciones iniciales por sector ────────────────────────────────────
gamma_val = 0.5
beta = 0.1

# Una perturbación antisimétrica inicial (activa Γ_a)
dGamma_pert = np.array([[0, 0.3, 0, 0],
                          [-0.3, 0, 0.2, 0],
                          [0, -0.2, 0, 0.1],
                          [0, 0, -0.1, 0]], dtype=float) * 0.5

sector_configs = [
    dict(label=r'det>0 (Newton/masivo)',
         Gamma0=np.diag([1.0, 0.8, 0.5, 0.3]),
         mu=0.1, color='#2166ac', ls='-'),
    dict(label=r'det=0 (borde, fotón)',
         Gamma0=np.diag([1.0, 0.7, 0.4, 0.001]),
         mu=0.0, color='#fd8d3c', ls='--'),
    dict(label=r'det<0 (QM/boost)',
         Gamma0=np.diag([1.0, 0.5, -0.2, -0.4]),
         mu=-0.1, color='#d73027', ls='-.'),
]

# ─── Verificación de la fórmula C en Γ de prueba ─────────────────────────────
print("=== Verificación fórmula C(Γ) ===")
test_cases = [
    ("Simétrica pura", np.diag([1.0, 2.0, 0.5, 0.3])),
    ("Antisimétrica pura", np.array([[0, 1, 0, 0], [-1, 0, 1, 0],
                                      [0, -1, 0, 1], [0, 0, -1, 0]], dtype=float)),
    ("Mixta (50/50)", np.array([[1, 0.5, 0, 0], [-0.5, 1, 0.5, 0],
                                 [0, -0.5, 1, 0.5], [0, 0, -0.5, 1]], dtype=float)),
]
for name, G in test_cases:
    c1 = C_coherence(G)
    c2 = C_from_parts(G)
    print(f"  {name:<25}: C_formula={c1:.4f}, C_direct={c2:.4f}  "
          f"{'✓' if abs(c1-c2)<1e-8 else '✗ DISCREPANCIA'}")

# ─── Simulación ───────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(13, 8))

for col, sc in enumerate(sector_configs):
    t, C, det, norm = simulate_sector(
        sc['Gamma0'], dGamma_pert, gamma_val, sc['mu'], beta)
    R = responsiveness(C, gamma_val, t[1]-t[0])

    # C(t)
    ax = axes[0, col]
    ax.plot(t, C, color=sc['color'], lw=2)
    ax.fill_between(t, C, alpha=0.15, color=sc['color'])
    ax.set_ylim(-0.05, 1.05)
    ax.axhline(0, color='k', lw=0.5, ls=':')
    ax.axhline(1, color='k', lw=0.5, ls=':')
    ax.set_title(sc['label'], fontsize=10, color=sc['color'])
    ax.set_ylabel(r'Coherencia $\mathcal{C}(t)$', fontsize=10)
    ax.set_xlabel(r'Tiempo $t$', fontsize=10)
    ax.grid(alpha=0.3)

    # Anotación del valor inicial y final
    ax.text(0.05, 0.85, f'$\\mathcal{{C}}_0={C[0]:.2f}$', transform=ax.transAxes,
            fontsize=9, color=sc['color'])
    ax.text(0.05, 0.75, f'$\\mathcal{{C}}_\\infty={C[-1]:.2f}$', transform=ax.transAxes,
            fontsize=9, color='gray')

    # R(t)
    ax = axes[1, col]
    R_clipped = np.clip(R, -3, 3)
    ax.plot(t, R_clipped, color=sc['color'], lw=2, ls='--')
    ax.fill_between(t, R_clipped, alpha=0.1, color=sc['color'])
    ax.axhline(0, color='k', lw=0.8)
    ax.set_ylabel(r'Responsividad $\mathcal{R}(t)=\dot{\mathcal{C}}/\gamma$', fontsize=10)
    ax.set_xlabel(r'Tiempo $t$', fontsize=10)
    ax.set_ylim(-3, 3)
    ax.grid(alpha=0.3)
    ax.text(0.05, 0.9, r'$\mathcal{R}=\dot{\mathcal{C}}/\gamma$', transform=ax.transAxes,
            fontsize=9, color='gray')

    # Marcar R_max (pico de responsividad)
    R_max = np.max(np.abs(R_clipped))
    ax.text(0.5, 0.85, f'$|\\mathcal{{R}}|_{{\\rm max}}={R_max:.2f}$',
            transform=ax.transAxes, fontsize=9, color=sc['color'], ha='center')

axes[0, 0].set_title(r'\textbf{det>0} (Newton/masivo)', fontsize=10, color='#2166ac')
axes[0, 1].set_title(r'\textbf{det=0} (borde, fotón)', fontsize=10, color='#fd8d3c')
axes[0, 2].set_title(r'\textbf{det<0} (QM/boost)', fontsize=10, color='#d73027')

fig.suptitle(r'$\mathcal{C}(t)$ y $\mathcal{R}(t)$ como observables de la película $\Gamma(t)$ — tres sectores',
             fontsize=12, y=1.01)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'fig_calc3_coherence_observables.pdf'),
            bbox_inches='tight', dpi=150)
plt.savefig(os.path.join(OUT_DIR, 'fig_calc3_coherence_observables.png'),
            bbox_inches='tight', dpi=150)
plt.close()
print("\nfig_calc3_coherence_observables guardada.")

# ─── Fórmulas finales para el paper ──────────────────────────────────────────
print("\n=== Fórmulas para Paper 4 ===")
print("C(Γ) = (I₂ - I₁) / (2·I₂)")
print("     donde I₁ = tr(Γ²), I₂ = tr(ΓᵀΓ) = ||Γ||²_F")
print()
print("Propiedades:")
print("  Γ = Γᵀ  (simétrico puro) → I₁ = I₂  →  C = 0   (no campo)")
print("  Γ = -Γᵀ (antisimétrico)  → I₁ = -I₂ →  C = 1   (campo puro)")
print("  Γ general                → C ∈ (0,1)  (mixto)")
print()
print("R(t) = Ċ(t) / γ  [tasa de cambio de C normalizada]")
print("     = d/dt [(I₂ - I₁)/(2I₂)] / γ")
print()
print("Par observable (C, R):")
print("  (alto C, alto R) → sistema vivo en transición")
print("  (alto C, bajo R) → sistema vivo estacionario (esclerosis)")
print("  (bajo C, alto R) → sistema en colapso hacia Γ_s")
print("  (bajo C, bajo R) → sistema disipado (atractor alcanzado)")
