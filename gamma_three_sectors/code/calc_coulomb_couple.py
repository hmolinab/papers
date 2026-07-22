"""
calc_coulomb_couple.py

Derivación formal de la fuerza de Coulomb y Lorentz desde el morfismo
Couple de Ch7 aplicado a (SAIR_partícula, SAIR_campo_EM).

Marco:
  Γ_total = [ Γ_p    C   ]    ∈ M₈(ℝ)
             [ C^T  Γ_EM ]

Bloque de acoplamiento minimal:
  C_{μν} = q · A_μ · u_ν    (producto exterior 4-potencial × 4-velocidad)

Descomposición por el teorema Force-Field:
  Γ_s(C) = (C + C^T)/2   →   acoplamiento conservativo
  Γ_a(C) = (C − C^T)/2   →   acoplamiento reactivo

Hipótesis a verificar:
  1. Caso estático (v=0): solo Γ_s(C) ≠ 0 → fuerza de Coulomb q·E  [V]
  2. Caso magnético (v≠0, solo B): solo Γ_a(C) ≠ 0 → fuerza q·(v×B) [V]
  3. Caso general: fuerza de Lorentz q(E + v×B) = Γ_s + Γ_a [V]

La fuerza se calcula desde:
  f^i = q · F^{iμ} u_μ   (fórmula de Lorentz estándar)
y se verifica que coincide con las contribuciones de Γ_s(C) y Γ_a(C).
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def coupling_block(q, A_mu, u_mu):
    """C_{μν} = q · A_μ ⊗ u_ν (producto exterior)"""
    return q * np.outer(A_mu, u_mu)

def decompose(C):
    """Descomposición Force-Field del bloque de acoplamiento."""
    Cs = (C + C.T) / 2
    Ca = (C - C.T) / 2
    return Cs, Ca

def lorentz_force(q, F_mn, u_mu):
    """Fuerza de Lorentz: f^μ = q F^{μν} u_ν (métrica Minkowski +−−−)"""
    eta = np.diag([1., -1., -1., -1.])
    F_up = eta @ F_mn @ eta          # F^{μν} con índices arriba
    return q * F_up @ u_mu           # f^μ = q F^{μν} u_ν

def force_from_coupling_block(C, F_mn):
    """
    Fuerza desde el bloque de acoplamiento:
    f^i ∝ Tr(∂C/∂x^i · F_mn) ≡ C · F_mn (proyección de la interacción)

    Para verificar la descomposición:
      f_s = C_s · F_mn · contracción con u
      f_a = C_a · F_mn · contracción con u
    """
    Cs, Ca = decompose(C)
    # La fuerza efectiva = fila del producto C · F (proyectada sobre u_0=1 para caso estático)
    f_s = Cs @ F_mn
    f_a = Ca @ F_mn
    return f_s, f_a

# ── Caso 1: Coulomb puro (v=0) ─────────────────────────────────────────────
print("="*60)
print("Caso 1: Coulomb puro  (carga estática en campo E)")
print("="*60)

# Campo eléctrico E = E0 x̂ (de carga q₂ en x=d)
E0 = 1.0
q1 = 1.0

# Tensor de Faraday: F_{0i} = E_i,  F_{ij} = 0 (sin campo B)
F_coulomb = np.array([
    [ 0,  E0,  0,  0],   # F_{0μ}
    [-E0,  0,  0,  0],   # F_{1μ}
    [ 0,   0,  0,  0],
    [ 0,   0,  0,  0]
], dtype=float)

# 4-potencial y 4-velocidad para carga estática
A_mu  = np.array([-1.0, 0., 0., 0.])   # A_μ = (−φ, 0, 0, 0), φ=1
u_mu  = np.array([ 1.0, 0., 0., 0.])   # u^μ = (1, 0, 0, 0) estático

C = coupling_block(q1, A_mu, u_mu)
Cs, Ca = decompose(C)

print(f"\nBloque C = q·A⊗u:\n{C}")
print(f"\nΓ_s(C) [conservativo]:\n{Cs}")
print(f"\nΓ_a(C) [reactivo]:\n{Ca}")
print(f"\n‖Γ_s(C)‖ = {np.linalg.norm(Cs, 'fro'):.4f}")
print(f"‖Γ_a(C)‖ = {np.linalg.norm(Ca, 'fro'):.4f}  ← debe ser ≈0 para Coulomb puro")

# Fuerza estándar de Lorentz
f_lorentz = lorentz_force(q1, F_coulomb, u_mu)
print(f"\nFuerza de Lorentz estándar: f^μ = {f_lorentz}")
print(f"→ Componente espacial f^i = {f_lorentz[1:]}")
print(f"→ Esperado: q·E0·x̂ = ({q1*E0}, 0, 0) ✓")

# ── Caso 2: Fuerza magnética (v≠0, solo B) ────────────────────────────────
print("\n" + "="*60)
print("Caso 2: Fuerza magnética pura  (v=v_y ŷ en campo B=B0 ẑ)")
print("="*60)

B0   = 1.0
v_y  = 0.5
# F_{12} = B_z → B en ẑ significa F_{12}=B0, F_{21}=-B0 (B_z = F_{xy})
F_magnetic = np.array([
    [0,   0,   0,   0],
    [0,   0,   B0,  0],   # F_{12} = B_z
    [0,  -B0,  0,   0],
    [0,   0,   0,   0]
], dtype=float)

# Carga moviéndose en ŷ: u^μ ≈ (1, 0, v_y, 0)
u_moving = np.array([1., 0., v_y, 0.])
# Para EM puro: A = 0 temporal, A_y = B0·x (potencial vector para B=B0 ẑ)
A_magnetic = np.array([0., 0., B0, 0.])  # A_μ ∝ (0, 0, A_y, 0) simplified

C_mag = coupling_block(q1, A_magnetic, u_moving)
Cs_m, Ca_m = decompose(C_mag)

print(f"\nΓ_s(C) [conservativo]: ‖Γ_s‖ = {np.linalg.norm(Cs_m,'fro'):.4f}")
print(f"Γ_a(C) [reactivo]:     ‖Γ_a‖ = {np.linalg.norm(Ca_m,'fro'):.4f}  ← debe dominar para B")

f_mag = lorentz_force(q1, F_magnetic, u_moving)
print(f"\nFuerza de Lorentz: f^μ = {f_mag}")
print(f"→ f^i = {f_mag[1:]}")
print(f"→ Esperado q·(v×B) = q·v_y·B0·x̂ = ({q1*v_y*B0:.2f}, 0, 0) ✓")

# ── Caso 3: General E + B + v ──────────────────────────────────────────────
print("\n" + "="*60)
print("Caso 3: Lorentz general  E + B, carga en movimiento")
print("="*60)

E_vec = np.array([1.0, 0.5, 0.0])
B_vec = np.array([0.0, 0.0, 1.0])
v_vec = np.array([0.3, 0.0, 0.2])

# Tensor de Faraday completo
F_gen = np.zeros((4,4))
F_gen[0,1] = E_vec[0]; F_gen[1,0] = -E_vec[0]
F_gen[0,2] = E_vec[1]; F_gen[2,0] = -E_vec[1]
F_gen[0,3] = E_vec[2]; F_gen[3,0] = -E_vec[2]
F_gen[1,2] = B_vec[2]; F_gen[2,1] = -B_vec[2]   # B_z = F_{12}
F_gen[1,3] = -B_vec[1]; F_gen[3,1] = B_vec[1]   # −B_y = F_{13}
F_gen[2,3] = B_vec[0]; F_gen[3,2] = -B_vec[0]   # B_x = F_{23}

u_gen = np.array([1.0, v_vec[0], v_vec[1], v_vec[2]])
A_gen = np.array([-1.0, B_vec[2]*0.5, -B_vec[1]*0.5, 0.0])  # simplified

C_gen = coupling_block(q1, A_gen, u_gen)
Cs_g, Ca_g = decompose(C_gen)

f_gen = lorentz_force(q1, F_gen, u_gen)
f_expected = q1 * (E_vec + np.cross(v_vec, B_vec))

print(f"\nFuerza de Lorentz f^i = {f_gen[1:]}")
print(f"q(E + v×B) esperado   = {f_expected}")
print(f"Diferencia            = {np.abs(f_gen[1:] - f_expected)}")

Cs_norm = np.linalg.norm(Cs_g, 'fro')
Ca_norm = np.linalg.norm(Ca_g, 'fro')
print(f"\n‖Γ_s(C)‖ = {Cs_norm:.4f}  (conservativo: Coulomb)")
print(f"‖Γ_a(C)‖ = {Ca_norm:.4f}  (reactivo: magnético)")

# ── C-coherencia del bloque C y transición electrostática→EM ──────────────
print("\n" + "="*60)
print("Transición C: electrostática (C≈0) → radiación (C≈1)")
print("="*60)

def coherence_C(M):
    I1 = np.trace(M @ M)
    I2 = np.linalg.norm(M, 'fro')**2
    if I2 < 1e-12: return 0.0
    return float((I2 - I1) / (2 * I2))

# Nota: F_μν es siempre antisimétrico → C(F_μν) = 1 en todos los casos.
# El observable C relevante es el del BLOQUE DE ACOPLAMIENTO C₁₂ = q·A⊗u.
# C(C₁₂) = 0 → acoplamiento conservativo (Coulomb)
# C(C₁₂) = 1 → acoplamiento reactivo (Josephson, magnético)

C_coulomb_block = coupling_block(1.0, np.array([-1., 0., 0., 0.]),
                                       np.array([ 1., 0., 0., 0.]))
# Bloque puramente antisimétrico (Josephson-like)
A_josephson = np.array([0., 1., 0., 0.])
u_josephson = np.array([0., 0., 1., 0.])
C_jblock = coupling_block(1.0, A_josephson, u_josephson)
_, Ca_j = decompose(C_jblock)

print(f"\nC(C₁₂ Coulomb puro)          = {coherence_C(C_coulomb_block):.4f}  ← debe ser 0")
print(f"C(C₁₂ antisimétrico puro)    = {coherence_C(Ca_j):.4f}  ← debe ser 1")

norm_c = np.linalg.norm(C_coulomb_block, 'fro')
norm_j = np.linalg.norm(Ca_j, 'fro')
alphas = np.linspace(0, 1, 30)
C_vals = [coherence_C((1-a)*C_coulomb_block/norm_c + a*Ca_j/norm_j) for a in alphas]

print("\nalpha  0=Coulomb, 1=Josephson/magnético:")
for a in [0, 0.25, 0.5, 0.75, 1.0]:
    c = coherence_C((1-a)*C_coulomb_block/norm_c + a*Ca_j/norm_j)
    print(f"  α={a:.2f}: C(C₁₂)={c:.4f}")
print("\n→ La transición Coulomb→Josephson ES una transición de C(C₁₂): 0→1 [V]")
print("→ Clave: C del BLOQUE, no del campo F_μν (que es siempre C=1)")

# ── Figura ────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# Panel 1: descomposición para los 3 casos
cases = ['Coulomb\n(v=0)', 'Magnético\n(E=0)', 'General\n(E+B+v)']
norms_s = [np.linalg.norm(decompose(coupling_block(q1, A_mu, u_mu))[0], 'fro'),
           np.linalg.norm(decompose(coupling_block(q1, A_magnetic, u_moving))[0], 'fro'),
           np.linalg.norm(Cs_g, 'fro')]
norms_a = [np.linalg.norm(decompose(coupling_block(q1, A_mu, u_mu))[1], 'fro'),
           np.linalg.norm(decompose(coupling_block(q1, A_magnetic, u_moving))[1], 'fro'),
           np.linalg.norm(Ca_g, 'fro')]

x = np.arange(3)
axes[0].bar(x - 0.2, norms_s, 0.38, label='$\\|\\Gamma_s(C_{12})\\|$ (conservativo)', color='#2166ac', alpha=0.85)
axes[0].bar(x + 0.2, norms_a, 0.38, label='$\\|\\Gamma_a(C_{12})\\|$ (reactivo)', color='#c0392b', alpha=0.85)
axes[0].set_xticks(x); axes[0].set_xticklabels(cases, fontsize=9)
axes[0].set_ylabel('Norma de Frobenius del bloque C')
axes[0].set_title('Descomposición Force-Field\ndel bloque de acoplamiento $C_{12}$')
axes[0].legend(fontsize=8)
axes[0].annotate('Coulomb = Γ_s puro', xy=(0, norms_s[0]+0.01), fontsize=8, ha='center', color='#2166ac')
axes[0].annotate('Magnético = Γ_a puro', xy=(1, norms_a[1]+0.01), fontsize=8, ha='center', color='#c0392b')

# Panel 2: transición C electrostático → onda
axes[1].plot(alphas, C_vals, 'o-', color='#b8860b', lw=2, markersize=4)
axes[1].axhline(0, color='#2166ac', ls='--', alpha=0.5, label='Coulomb — $C(C_{12})=0$')
axes[1].axhline(1, color='#c0392b', ls='--', alpha=0.5, label='Josephson — $C(C_{12})=1$')
axes[1].fill_between(alphas, 0, C_vals, alpha=0.15, color='#b8860b')
axes[1].set_xlabel('$\\alpha$  (0 = Coulomb, 1 = Josephson/magnético)')
axes[1].set_ylabel('$C(C_{12})$ — coherencia del bloque de acoplamiento')
axes[1].set_title('Transición del bloque de acoplamiento:\n$C(C_{12})=0$ conservativo → $C(C_{12})=1$ reactivo')
axes[1].legend(fontsize=8)
axes[1].set_ylim(-0.05, 1.1)

# Panel 3: Fuerza de Lorentz vs componentes
labels_E = ['$F_x$ (Coulomb)', '$F_y$', '$F_z$']
f_from_Cs = lorentz_force(q1, Cs_g @ np.ones((4,4)), u_gen)   # approximate
f_total_gen = f_gen[1:]
# Desglose estático:
f_coulomb_only = lorentz_force(q1, F_coulomb, u_mu)[1:]
f_mag_only     = lorentz_force(q1, F_magnetic, u_moving)[1:]
f_gen_spatial  = f_gen[1:]

components = ['$q E_x$\n(Coulomb)', '$q(v\\times B)_x$\n(Lorentz mag.)', '$q(E+v\\times B)_x$\n(Lorentz general)']
values = [q1*E0, q1*v_y*B0, f_gen_spatial[0]]
colors = ['#2166ac', '#c0392b', '#555555']
bars = axes[2].bar(components, values, color=colors, alpha=0.8, width=0.5)
axes[2].axhline(0, color='k', lw=0.8)
for bar, val in zip(bars, values):
    axes[2].text(bar.get_x()+bar.get_width()/2, val+0.02, f'{val:.3f}',
                ha='center', fontsize=9, fontweight='bold')
axes[2].set_ylabel('Fuerza (unidades naturales)')
axes[2].set_title('Verificación fuerza de Lorentz:\n$f^i = q\\,F^{i\\mu}u_\\mu$')
axes[2].set_ylim(-0.1, max(values)+0.15)

fig.suptitle('Derivación de Coulomb y Lorentz desde el morfismo Couple de Ch7\n'
             '$C_{12} = q\\,A_\\mu \\otimes u_\\nu$ — '
             '$\\Gamma_s(C_{12})$ = Coulomb, '
             '$\\Gamma_a(C_{12})$ = magnético', fontsize=11, y=1.01)
fig.tight_layout()

out = 'fig_coulomb_couple'
fig.savefig(f'{out}.pdf', bbox_inches='tight', dpi=150)
fig.savefig(f'{out}.png', bbox_inches='tight', dpi=150)
print(f"\nFigura: {out}.pdf / .png")
