"""
Cálculo 2 — Relaciones de dispersión ω(k) por sector

Linealizamos la EOM alrededor de Γ₀ en cada sector:
  Γ(t,x) = Γ₀ + δΓ · e^{i(kx - ωt)}

Sustituyendo: (-ω² - iγω + c²k² + m_eff²) δΓ = 0
donde m_eff² = eigenvalue del Hessiano de P evaluado en Γ₀.

Los tres sectores producen tres relaciones de dispersión:
  det>0 (Γ_s): ω² = c²k² + m_eff²    (partícula masiva — Newton/KG)
  det=0 (borde): ω = ck               (fotón — Maxwell)
  det<0 (Γ_a): ω² = c²k² - |m_eff²|  (boost/oscilatorio)

Guarda: fig_calc2_dispersion.pdf
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

OUT_DIR = os.path.dirname(__file__)
c = 1.0  # velocidad estructural (unidades naturales)

# ─── Masas efectivas por sector ────────────────────────────────────────────────
# P = ||Γ||² + μ det Γ + β||Γ||⁴
# ∂²P/∂Γ² en cada Γ₀:
#
# Para Γ₀ diagonal con eigenvalues (λ₁, λ₂, ...), el hessiano es diagonal
# con entradas 2 + μ·(∂det/∂λᵢ²) + 4β||Γ||²  (en el modo longitudinal)
# y el modo de menor masa corresponde al eigenvalue más cercano a cero.

def m_eff_sq(Gamma0, mu, beta):
    """Masa efectiva cuadrada = eigenvalue mínimo del Hessiano de P en Γ₀."""
    lams = np.linalg.eigvalsh(Gamma0)
    norm2 = np.sum(lams**2)
    det = np.prod(lams)
    # Hessiano en modo longitudinal para Γ diagonal:
    # ∂²P/∂λᵢ² = 2 + μ·det/λᵢ² + 4β·(2λᵢ² + norm2·... )
    # En la dirección del modo blando (λ_min):
    lam_min = lams[np.argmin(np.abs(lams))]
    if abs(lam_min) < 1e-10:
        return 0.0  # det=0: sin masa
    h = 2 + 4*beta*norm2 + 8*beta*lam_min**2
    if abs(lam_min) > 1e-10:
        h += mu * det / lam_min**2
    return h

# ─── Γ₀ representativos por sector ────────────────────────────────────────────
mu = 0.0
beta = 0.1
gamma_dissip = 0.1  # disipación pequeña

sectors = [
    dict(name='det>0\n(masivo, Newton/KG)',
         Gamma0=np.diag([1.0, 0.8, 0.6, 0.4]),
         color='#2166ac', ls='-',
         label=r'$\det>0$: $\omega^2=c^2k^2+m_{\rm eff}^2$ (masivo)'),
    dict(name='det=0\n(sin masa, fotón)',
         Gamma0=np.diag([1.0, 0.5, 0.2, 0.0]),
         color='#fd8d3c', ls='--',
         label=r'$\det=0$: $\omega=ck$ (fotón)'),
    dict(name='det<0\n(boost, QM/GR)',
         Gamma0=np.diag([1.0, 0.5, -0.2, -0.4]),
         color='#d73027', ls='-.',
         label=r'$\det<0$: $\omega^2=c^2k^2-|m^2|$ (taquiónico/boost)'),
]

k = np.linspace(0, 4, 300)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# ─── Panel A: ω(k) en cada sector ────────────────────────────────────────────
ax = axes[0]
for sec in sectors:
    m2 = m_eff_sq(sec['Gamma0'], mu, beta)
    print(f"Sector {sec['name'].split(chr(10))[0]}: m_eff² = {m2:.4f}")

    if m2 > 0:
        omega_real = np.sqrt(np.maximum(c**2 * k**2 + m2, 0))
        ax.plot(k, omega_real, color=sec['color'], ls=sec['ls'],
                lw=2.5, label=sec['label'])
        # Marcar la brecha de masa
        ax.axhline(np.sqrt(m2), color=sec['color'], alpha=0.3, lw=1, ls=':')
        ax.annotate(rf'$m_{{\rm eff}}={np.sqrt(m2):.2f}$',
                    xy=(0, np.sqrt(m2)), xytext=(0.3, np.sqrt(m2)+0.05),
                    fontsize=8, color=sec['color'])
    elif abs(m2) < 1e-6:
        omega_real = c * k
        ax.plot(k, omega_real, color=sec['color'], ls=sec['ls'],
                lw=2.5, label=sec['label'])
    else:
        omega_sq = c**2 * k**2 + m2
        omega_real = np.sqrt(np.maximum(omega_sq, 0))
        omega_imag_region = k[omega_sq < 0]
        ax.plot(k, omega_real, color=sec['color'], ls=sec['ls'],
                lw=2.5, label=sec['label'])
        if len(omega_imag_region) > 0:
            ax.axvspan(0, omega_imag_region[-1], alpha=0.08,
                       color=sec['color'], label='_nolegend_')
            ax.text(omega_imag_region[-1]/2, 0.1, 'inestable\n(Im ω>0)',
                    fontsize=7, ha='center', color=sec['color'])

ax.set_xlabel(r'Número de onda $k$', fontsize=12)
ax.set_ylabel(r'Frecuencia $\omega(k)$', fontsize=12)
ax.set_title(r'\textbf{A.} Relaciones de dispersión por sector', fontsize=12)
ax.legend(fontsize=9, loc='upper left')
ax.set_xlim(0, 4)
ax.set_ylim(0, 5)
ax.grid(alpha=0.3)

# Línea de luz ck como referencia
ax.plot(k, c*k, 'k--', lw=1, alpha=0.4, label='_nolegend_')
ax.text(3.2, 3.4, r'$\omega=ck$', fontsize=9, color='gray', rotation=37)

# ─── Panel B: Mapa de sectores en espacio (k, det) ───────────────────────────
ax = axes[1]

# Mostrar mapa ω(k, det_sign)
k_vals = np.linspace(0.1, 4, 100)
det_vals = np.linspace(-1.5, 1.5, 100)
K, D = np.meshgrid(k_vals, det_vals)

# m_eff² ~ lineal en det (primer orden)
M2 = 0.5 + 2.0 * D  # m_eff² = m₀² + α·det
Omega = np.sqrt(np.abs(c**2 * K**2 + M2)) * np.sign(c**2 * K**2 + M2)

# Velocidad de grupo ∂ω/∂k
v_group = np.where(M2 >= 0,
                   c**2 * K / np.maximum(np.sqrt(c**2*K**2 + M2), 0.01),
                   c**2 * K / np.maximum(np.sqrt(c**2*K**2 + M2), 0.01))
v_group = np.clip(v_group, 0, 1.0)  # ≤ c

im = ax.pcolormesh(K, D, v_group, cmap='RdYlBu_r', vmin=0, vmax=1)
plt.colorbar(im, ax=ax, label=r'Velocidad de grupo $v_g/c$')

ax.axhline(0, color='orange', lw=2.5, label=r'$\det=0$ (fotón)')
ax.text(0.3, 0.05, r'$\det=0$: $\omega=ck$', color='orange', fontsize=9)
ax.text(0.3, 0.8, r'$\det>0$: masivo', color='white', fontsize=9, fontweight='bold')
ax.text(0.3, -1.1, r'$\det<0$: boost/QM', color='white', fontsize=9, fontweight='bold')

ax.set_xlabel(r'Número de onda $k$', fontsize=12)
ax.set_ylabel(r'$\mathrm{sign}(\det\,\Gamma_0)$ → sector', fontsize=12)
ax.set_title(r'\textbf{B.} Atlas de dispersión (mapa $k$–det)', fontsize=12)
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'fig_calc2_dispersion.pdf'),
            bbox_inches='tight', dpi=150)
plt.savefig(os.path.join(OUT_DIR, 'fig_calc2_dispersion.png'),
            bbox_inches='tight', dpi=150)
plt.close()
print("fig_calc2_dispersion guardada.")

# ─── Tabla analítica de dispersión ────────────────────────────────────────────
print("\n=== Cálculo 2: relaciones de dispersión por sector ===")
print(f"{'Sector':<15} {'m_eff²':>8} {'ω(k=1)':>10} {'v_g(k=1)':>10} {'Física':>20}")
print("-"*70)
k0 = 1.0
for sec in sectors:
    m2 = m_eff_sq(sec['Gamma0'], mu, beta)
    om2 = c**2 * k0**2 + m2
    om = np.sqrt(abs(om2)) * (1 if om2 >= 0 else 1j)
    vg = c**2 * k0 / abs(om) if abs(om) > 0 else float('inf')
    sector_name = sec['name'].split('\n')[0]
    fisica = sec['label'].split(':')[1].strip()[:20]
    print(f"{sector_name:<15} {m2:>8.4f} {abs(om):>10.4f} {vg:>10.4f}   {fisica}")
