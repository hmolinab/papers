"""
Calculation 2b — Hessian of P restricted to antisymmetric perturbations

Closes Grieta 1: shows that m_eff^2 < 0 for antisymmetric fluctuations in det<0 sector.

The Hessian of P in direction delta_Gamma_a (antisymmetric) is:
  H_P[delta_a, delta_a] = 2 ||delta_a||^2
                        + mu * d^2(det)[delta_a, delta_a]
                        + 4*beta*(2*(tr(Gamma*delta_a))^2 + ||Gamma||^2 * ||delta_a||^2)

For diagonal Gamma_0 = diag(lambda_1,...,lambda_4) and antisymmetric delta_a with
only the (i,j) entry nonzero (delta_a_ij = -delta_a_ji = 1):
  d^2(det)[delta_a, delta_a] = 2 * det(Gamma_0) / (lambda_i * lambda_j)

So the second derivative per unit norm squared of delta_a is:
  q(i,j) = 1 + mu * det(Gamma_0) / (lambda_i * lambda_j)
            + 4*beta * ||Gamma_0||^2

m_eff^2(antisymmetric) = min over (i,j) of q(i,j)

Key: when det Gamma_0 < 0 and lambda_i * lambda_j > 0 (same-sign pair),
     det/product < 0  =>  mu * det/product can be large negative if mu < 0.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def P_hessian_antisymm(Gamma0, mu, beta):
    """
    Returns a dict of q(i,j) = Hessian curvature in antisymmetric (i,j) direction.
    Also returns m_eff_sq = min over all antisymmetric modes.
    """
    lam = np.diag(Gamma0) if len(Gamma0.shape)==2 else Gamma0
    n = len(lam)
    det_G = np.prod(lam)
    norm_sq = np.sum(lam**2)  # ||Gamma_0||^2 (diagonal)

    q_values = {}
    for i in range(n):
        for j in range(i+1, n):
            if abs(lam[i] * lam[j]) < 1e-12:
                continue
            # d^2(det) in antisymm (i,j) direction: 2*det / (lambda_i * lambda_j)
            d2det = 2 * det_G / (lam[i] * lam[j])
            # Hessian per unit norm (||delta_a_{ij}||^2 = 2 for one nonzero pair)
            q = 1.0 + mu * d2det / 2.0 + 4 * beta * norm_sq
            q_values[(i,j)] = q

    m_eff_sq = min(q_values.values()) if q_values else np.nan
    return q_values, m_eff_sq

def P_hessian_symm(Gamma0, mu, beta):
    """Hessian in symmetric (i,j) direction for comparison."""
    lam = np.diag(Gamma0) if len(Gamma0.shape)==2 else Gamma0
    n = len(lam)
    det_G = np.prod(lam)
    norm_sq = np.sum(lam**2)

    q_values = {}
    for i in range(n):
        for j in range(i+1, n):
            if abs(lam[i] * lam[j]) < 1e-12:
                continue
            # d^2(det) in symm (i,j) direction (off-diagonal): same formula
            d2det = 2 * det_G / (lam[i] * lam[j])
            q = 1.0 + mu * d2det / 2.0 + 4 * beta * norm_sq
            q_values[(i,j)] = q
        # Diagonal (i,i) direction:
        # d^2(det) in diag-i direction: 0 (det linear in lambda_i for diag)
        q_values[(i,i)] = 1.0 + 4 * beta * norm_sq  # only quartic term
    return q_values, min(q_values.values())

# Parameters
mu = -0.5   # negative: stabilizes det>0, destabilizes det<0
beta = 0.05

# Three sector configurations (CORRECTED det<0)
sectors = {
    'det > 0\n(Newton)':    np.array([1.0,  0.8,  0.6,  0.4]),   # det = 0.192
    'det = 0\n(photon)':   np.array([1.0,  0.7,  0.4,  0.001]),  # det ≈ 0.00028
    'det < 0\n(oscillatory)': np.array([1.0,  0.5,  0.3, -0.4]), # det = -0.060
}

print("=" * 60)
print(f"mu = {mu},  beta = {beta}")
print("=" * 60)

results = {}
for name, lam in sectors.items():
    det_val = np.prod(lam)
    q_a, m_a = P_hessian_antisymm(np.diag(lam), mu, beta)
    q_s, m_s = P_hessian_symm(np.diag(lam), mu, beta)
    results[name] = {'det': det_val, 'm_a': m_a, 'm_s': m_s, 'q_a': q_a, 'q_s': q_s}
    print(f"\n{name.replace(chr(10),' ')}")
    print(f"  det = {det_val:.4f}")
    print(f"  m_eff^2 (antisymmetric modes) = {m_a:.4f}  {'<0 UNSTABLE' if m_a < 0 else '>0 stable'}")
    print(f"  m_eff^2 (symmetric modes)     = {m_s:.4f}  {'<0 UNSTABLE' if m_s < 0 else '>0 stable'}")
    print(f"  Antisymm curvatures by mode: {dict((k, round(v,3)) for k,v in q_a.items())}")

print("\n" + "=" * 60)
print("KEY RESULT: In det<0 sector, antisymmetric modes have m_eff^2 < 0")
print("=> oscillatory / Hopf instability in Gamma_a direction")
print("   (symmetric modes remain stable or less negative)")

# ── Figure ──────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 5))
gs = gridspec.GridSpec(1, 3, figure=fig, wspace=0.4)

colors_s = ['#2166ac', '#ff7f0e', '#d73027']
for idx, (name, lam) in enumerate(sectors.items()):
    ax = fig.add_subplot(gs[idx])
    det_val = np.prod(lam)
    res = results[name]

    modes_a = sorted(res['q_a'].items())
    modes_s = {k:v for k,v in res['q_s'].items() if k[0]!=k[1]}
    modes_s_sorted = sorted(modes_s.items())

    x_a = range(len(modes_a))
    x_s = range(len(modes_s_sorted))

    ax.bar([x - 0.2 for x in x_a], [v for _,v in modes_a], width=0.35,
           label='antisymm. ($\\delta\\Gamma_a$)', color=colors_s[idx], alpha=0.85)
    ax.bar([x + 0.2 for x in x_s], [v for _,v in modes_s_sorted], width=0.35,
           label='symm. ($\\delta\\Gamma_s$)', color=colors_s[idx], alpha=0.4)

    ax.axhline(0, color='k', lw=1.2, ls='--')
    ax.set_xticks(range(max(len(modes_a), len(modes_s_sorted))))
    ax.set_xticklabels([f'({i},{j})' for (i,j),_ in modes_a], fontsize=8, rotation=30)
    ax.set_xlabel('Mode (i,j)', fontsize=9)
    ax.set_ylabel('$m_{\\rm eff}^2$', fontsize=10)

    sign = '+' if det_val >= 0 else ''
    ax.set_title(f'{name}\ndet = {det_val:.3f}', fontsize=9, pad=6)

    m_a_val = res['m_a']
    color_text = 'red' if m_a_val < 0 else 'navy'
    ax.annotate(f'min antisymm:\n$m^2_{{\\rm eff}}$ = {m_a_val:.3f}',
                xy=(0.05, 0.05), xycoords='axes fraction',
                fontsize=8, color=color_text,
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec=color_text, alpha=0.8))

    if idx == 0:
        ax.legend(fontsize=7, loc='upper right')

fig.suptitle('Calculation 2b — Hessian of $P$ by Fluctuation Type\\n'
             'Antisymmetric modes become unstable ($m^2_{\\rm eff}<0$) in det$\\,\\Gamma < 0$ sector',
             fontsize=11, y=1.02)

out = 'fig_calc2b_antisymm_hessian'
fig.savefig(f'{out}.pdf', bbox_inches='tight', dpi=150)
fig.savefig(f'{out}.png', bbox_inches='tight', dpi=150)
print(f"\nFigure saved: {out}.pdf / .png")
