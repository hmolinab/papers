"""
einstein_completo_tensor_energia_momento.py

Primera pieza de "Einstein completo" (jul-07 2026), vía la ruta
termodinámica de Jacobson (1995) -- NO la ruta de acción cuadrática, que
ya mostró tener un ghost de Boulware-Deser sin cancelación limpia
(einstein_cancelacion_masa_verificacion.py). Jacobson deriva las
ecuaciones de Einstein COMPLETAS (no linealizadas) desde la relación de
Clausius dQ=TdS sobre horizontes de Rindler locales, usando:
  (a) S = A/4G (entropía de Bekenstein-Hawking) -- GSF YA TIENE esto
      como S_BH=k_B*rho, verificado a 12 dígitos (Ch36).
  (b) dQ = integral(T_ab*chi^a dSigma^b) -- el FLUJO DE CALOR, que
      requiere el tensor T_ab de la MATERIA/CAMPO cruzando el horizonte.
  (c) la ecuación de Raychaudhuri (geométrica, exacta, no linealizada)
      relacionando el cambio de área con R_ab k^a k^b.

Este script ataca el ingrediente (b) que falta: construir T_mu_nu desde
el Lagrangiano de campo de GSF vía el teorema de Noether (tensor
canónico), y verificar dos propiedades necesarias para que el argumento
de Jacobson funcione:
  1. CONSERVACIÓN: d_mu T^mu_nu = 0 sobre soluciones de la EOM (esto es
     un teorema general de Noether para Lagrangianos invariantes bajo
     traslación -- se verifica aquí explícitamente para el Lagrangiano
     de GSF, no se cita el teorema general sin más)
  2. SIMETRÍA: el tensor canónico de Noether NO es automáticamente
     simétrico en general -- se verifica si el de GSF lo es, o si
     necesita la mejora de Belinfante-Rosenfeld (relevante porque
     Jacobson necesita acoplar T_mu_nu a un tensor de Einstein
     simétrico)

LAGRANGIANO DE GSF (gsf_field_extension_nabla2.md), Minkowski,
Gamma = Gamma(t,x) escalar-matricial (se usa 1+1D para tratabilidad
simbólica -- el argumento de conservación/simetría es local y no depende
de cuántas dimensiones espaciales haya):

  L = eta^{mu nu} Tr(d_mu Gamma^T d_nu Gamma) - Tr(Gamma^T Gamma) - mu*det(Gamma)
"""

import sympy as sp

t, x = sp.symbols('t x', real=True)
coords = [t, x]
eta_diag = [1, -1]  # (1+1)D Minkowski, mismo argumento se generaliza a 3+1D
n_dim = 2

# Gamma como matriz 2x2 general (no simétrica) de campos, para conservar
# generalidad del Tr(Gamma^T Gamma) y det(Gamma) de GSF
G = sp.Matrix(2, 2, lambda i, j: sp.Function(f'G{i}{j}')(t, x))
mu_sym = sp.symbols('mu', real=True)


def d(expr, idx):
    return sp.diff(expr, coords[idx])


def eta(i, j):
    return eta_diag[i] if i == j else 0


# ============================================================================
print("=" * 78)
print("PASO 1 -- Lagrangiano de campo de GSF y ecuaciones de Euler-Lagrange")
print("=" * 78)

kinetic = sum(eta(a, a) * sum(d(G[i, j], a) * d(G[i, j], a) for i in range(2) for j in range(2))
              for a in range(n_dim))
potential = sum(G[i, j] * G[i, j] for i in range(2) for j in range(2)) + mu_sym * G.det()
L = kinetic - potential
print(f"L = {sp.expand(L)}")


def euler_lagrange(Lagr, i, j):
    Gij = G[i, j]
    dL_dG = sp.diff(Lagr, Gij)
    total = -dL_dG
    for a in range(n_dim):
        dGij_a = sp.diff(Gij, coords[a])
        dL_ddG = sp.diff(Lagr, dGij_a)
        total += d(dL_ddG, a)
    return sp.expand(total)


EL = sp.Matrix(2, 2, lambda i, j: euler_lagrange(L, i, j))
print("\nEcuación de Euler-Lagrange, componente (0,0):")
print(f"  {EL[0,0]} = 0")

# ============================================================================
print()
print("=" * 78)
print("PASO 2 -- tensor energía-momento canónico (Noether, traslaciones espaciotemporales)")
print("=" * 78)
print("""
T^mu_nu = sum_ij [ dL/d(d_mu G_ij) * d_nu G_ij ] - delta^mu_nu * L
(índice mu subido con eta, índice nu queda como en la definición canónica)
""")


def T_canonical(mu_idx, nu_idx):
    """Corriente canónica de Noether Theta^mu_nu = sum_i dL/d(d_mu phi_i) * d_nu phi_i
    - delta^mu_nu * L. Es una identidad puramente algebraica (regla de la
    cadena) que d_mu Theta^mu_nu = sum_i (d_nu phi_i)*EL_i -- NO requiere
    subir índices con la métrica; ese paso (que causaba un residuo no nulo
    en un primer intento) era un error, no parte de la construcción de Noether."""
    term = 0
    for i in range(2):
        for j in range(2):
            dGij_mu = sp.diff(G[i, j], coords[mu_idx])
            dL_ddGmu = sp.diff(L, dGij_mu)
            dGij_nu = sp.diff(G[i, j], coords[nu_idx])
            term += dL_ddGmu * dGij_nu
    delta = 1 if mu_idx == nu_idx else 0
    return sp.expand(term - delta * L)


T = sp.Matrix(n_dim, n_dim, lambda mu_idx, nu_idx: T_canonical(mu_idx, nu_idx))
print("T^0_0 (densidad de energía):")
print(f"  {T[0,0]}")
print("T^0_1:")
print(f"  {T[0,1]}")
print("T^1_0:")
print(f"  {T[1,0]}")
print("T^1_1:")
print(f"  {T[1,1]}")

# ============================================================================
print()
print("=" * 78)
print("PASO 3 -- ¿es T simétrico? (comparar T^0_1 con T^1_0 bajando/subiendo índices)")
print("=" * 78)

# T_mu_nu (ambos índices abajo) = eta_mu_mu * T^mu_nu
T_lower = sp.Matrix(n_dim, n_dim, lambda i, j: eta(i, i) * T[i, j])
print("T_mu_nu (ambos índices abajo):")
sp.pprint(T_lower)

diff_symmetry_raw = sp.expand(T_lower[0, 1] - T_lower[1, 0])
print(f"\nT_01 - T_10 (sin usar la EOM): {diff_symmetry_raw}")

# sustituir la EOM (EL[i,j]=0) para ver si la antisimetría se anula ON-SHELL
# se resuelve una de las derivadas segundas desde EL=0 y se sustituye
if diff_symmetry_raw == 0:
    is_onshell_symmetric = True
    print("  T_01-T_10 = 0 EXACTAMENTE, sin siquiera usar la EOM -- simétrico OFF-shell,")
    print("  más fuerte de lo estrictamente necesario para Jacobson (que solo pide on-shell).")
else:
    print("\nProbando si T_01=T_10 se cumple usando la ecuación de movimiento (on-shell)...")
    is_onshell_symmetric = None
    for candidate_combo in [1, -1]:
        test_expr = sp.expand(diff_symmetry_raw + candidate_combo * EL[0, 1] - candidate_combo * EL[1, 0])
        if test_expr == 0:
            is_onshell_symmetric = True
            print(f"  T_01-T_10 = -({candidate_combo})*(EL_01-EL_10) -- se anula ON-SHELL (usando EOM=0)")
            break
    if is_onshell_symmetric is None:
        print("  No se encontró una combinación simple de EL=0 que anule T_01-T_10 --")
        print("  el tensor canónico de Noether de GSF NO es simétrico ni siquiera on-shell;")
        print("  necesitaría la mejora de Belinfante-Rosenfeld (no construida aquí).")

# ============================================================================
print()
print("=" * 78)
print("PASO 4 -- conservación: d_mu T^mu_nu = 0 usando la EOM")
print("=" * 78)

for nu_idx in range(n_dim):
    div = sum(d(T[mu_idx, nu_idx], mu_idx) for mu_idx in range(n_dim))
    div = sp.expand(div)
    print(f"d_mu T^mu_{nu_idx} (sin usar EOM) = {div}")

    # verificar si esta divergencia es una combinación lineal de las EL=0
    # (si T viene de Noether con L invariante bajo traslaciones, debe serlo)
    residual = div
    for i in range(2):
        for j in range(2):
            dGij_nu = sp.diff(G[i, j], coords[nu_idx])
            residual = sp.expand(residual - dGij_nu * EL[i, j])
    print(f"  Residuo tras restar sum(d_nu G_ij * EL_ij): {residual}  (debe ser 0 si Noether es exacto aquí)")
    assert residual == 0, f"la identidad de Noether no cierra exactamente para nu={nu_idx}"

print("\nOK -- para las dos componentes nu=0,1: d_mu T^mu_nu = sum_ij (d_nu G_ij)*EL_ij EXACTAMENTE.")
print("Esto confirma el teorema de Noether de forma explícita (no citado): la conservación")
print("d_mu T^mu_nu=0 se sigue automáticamente de la ecuación de movimiento EL_ij=0, sin excepción.")

# ============================================================================
print()
print("=" * 78)
print("CONCLUSIÓN")
print("=" * 78)
print(f"""
RESULTADO 1 -- CONSERVACIÓN: CONFIRMADA, de forma general y exacta (no
aproximada). d_mu T^mu_nu = sum_ij (d_nu G_ij)*[EL_ij], una identidad
algebraica exacta independiente de la forma específica de mu(rho) o del
potencial -- se cumple para CUALQUIER Lagrangiano de la forma
cinético-menos-potencial de GSF. Sobre soluciones de la EOM (source-free,
EL_ij=0), T^mu_nu de GSF se conserva automáticamente. Este es el primer
ingrediente que Jacobson necesita para su argumento (T_ab conservado) --
CERRADO para el Lagrangiano de campo de GSF tal como está.

RESULTADO 2 -- SIMETRÍA: CONFIRMADA, y más fuerte de lo necesario: T_mu_nu
es simétrico EXACTAMENTE (T_01=T_10 se cumple sin siquiera usar la EOM,
off-shell), no solo sobre soluciones. Esto es MEJOR que el caso genérico
de un tensor canónico de Noether (que en general no es simétrico y
requiere la mejora de Belinfante-Rosenfeld) -- para el Lagrangiano
cinético-menos-potencial de GSF (sin términos con más de una derivada por
campo, sin acoplamiento a espín), el tensor canónico ya sale simétrico,
sin mejora adicional necesaria.

AMBOS ingredientes que Jacobson necesita de T_mu_nu (conservación +
simetría) están CONFIRMADOS para el Lagrangiano de campo de GSF, de forma
exacta y sin aproximar -- un resultado limpio, en contraste con el
resultado negativo de la cancelación +Γ/adj(Γ).

PENDIENTE HONESTO para completar el ingrediente (b) de Jacobson:
1. Este cálculo se hizo en 1+1D por tratabilidad simbólica -- la
   identidad de Noether (conservación) y la simetría son ambas
   consecuencias algebraicas locales de la FORMA del Lagrangiano
   (cinético cuadrático diagonal en eta menos potencial sin derivadas),
   que no cambia en 3+1D -- pero no se re-verificó explícitamente ahí.
2. Falta el ingrediente (c): repetir el argumento de Raychaudhuri+Clausius
   con este T_mu_nu específico y la identificación rho=entropía LOCAL
   (no solo la de Sitter global de Ch36) -- no atacado en este script.
3. Falta verificar que T_mu_nu tiene el SIGNO/interpretación física
   correcta (energía positiva, condiciones de energía estándar) para
   una configuración concreta de materia -- no se probó ningún caso de
   materia real aquí, solo la estructura algebraica general.
""")
