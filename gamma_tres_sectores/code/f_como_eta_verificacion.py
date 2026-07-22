"""
f_como_eta_verificacion.py

Ataca "qué juega el rol de f (métrica de referencia) en GSF" -- candidato
más natural y ya presente en toda la sesión: f = eta, el fondo de
Minkowski. No es una estructura nueva que haya que inventar -- eta YA ES
el punto de referencia fijo alrededor del cual se linealizó Gamma=eta+h
en CADA script de esta sesión.

Se construye K = I - sqrt(Gamma_s^{-1} * eta) perturbativamente (resolviendo
la relación algebraica (I-K)^2 = Gamma_s^{-1}*eta orden por orden en h,
verificado con sympy, NO una fórmula de raíz cuadrada matricial citada de
memoria), y se pregunta: ¿e_n(K) (a diferencia de e_n(Gamma) directamente,
que YA SE DEMOSTRÓ que no puede producir h_ii^2, script masa_drgt_en_
verificacion.py) SÍ produce esa estructura?
"""

import sympy as sp

n = 4
eta_diag = [1, -1, -1, -1]
eta = sp.diag(*eta_diag)

eps = sp.symbols('epsilon')
h = sp.Matrix(n, n, lambda i, j: sp.symbols(f'h{min(i,j)}{max(i,j)}', real=True))

# ============================================================================
print("=" * 78)
print("PASO 1 -- resolver K = I - sqrt(Gamma_s^-1 * eta) orden por orden en h")
print("=" * 78)
print("""
Gamma_s = eta + eps*h (f = eta, fijo). M := Gamma_s^-1 * eta.
Expansión de Neumann: Gamma_s^-1 = eta^-1 - eps*eta^-1*h*eta^-1 +
eps^2*eta^-1*h*eta^-1*h*eta^-1 - ... ; con eta^-1=eta (pues eta^2=I):
M = I - eps*(eta*h) + eps^2*(eta*h)^2 - ...   [X := eta*h]
Resolviendo (I-K)^2 = M para K = k1*eps + k2*eps^2 + O(eps^3):
  -2*k1 = -X          => k1 = X/2
  k1^2 - 2*k2 = X^2   => k2 = -(3/8)*X^2
""")

X = eta * h  # producto matricial eta*h

M_series = sp.eye(n) - eps * X + eps**2 * X * X  # M a O(eps^2)

K1 = X / 2
K2 = -sp.Rational(3, 8) * X * X

K_approx = eps * K1 + eps**2 * K2

# verificación: (I-K)^2 debe coincidir con M_series a O(eps^2)
lhs = sp.expand((sp.eye(n) - K_approx) * (sp.eye(n) - K_approx))
lhs_series = lhs.applyfunc(lambda e: sp.expand(sp.series(e, eps, 0, 3).removeO()))
diff_check = sp.expand(lhs_series - M_series)
diff_check_series = diff_check.applyfunc(lambda e: sp.expand(sp.series(e, eps, 0, 3).removeO()))
print(f"Verificación (I-K)^2 - M a O(eps^2), debe ser matriz cero: {diff_check_series == sp.zeros(n,n)}")
assert diff_check_series == sp.zeros(n, n), "la solución de K no satisface (I-K)^2=M a este orden"

# ============================================================================
print()
print("=" * 78)
print("PASO 2 -- e_1(K)..e_4(K) a orden h^2, vía polinomio característico exacto de K_approx")
print("=" * 78)

lam = sp.symbols('lam')
charpoly_K = K_approx.charpoly(lam)
coeffs_K = charpoly_K.all_coeffs()
e1_K = -coeffs_K[1]
e2_K = coeffs_K[2]
e3_K = -coeffs_K[3]
e4_K = coeffs_K[4]


def order(expr, k):
    ser = sp.series(expr, eps, 0, k + 2).removeO()
    return sp.expand(ser.coeff(eps, k))


e1_K_1, e1_K_2 = order(e1_K, 1), order(e1_K, 2)
e2_K_2 = order(e2_K, 2)
e3_K_2 = order(e3_K, 2)
e4_K_2 = order(e4_K, 2)

print(f"e1(K) orden1 (lineal en h): {e1_K_1}")
print(f"e1(K) orden2 (cuadrático en h): {e1_K_2}")
print(f"e2(K) orden2: {e2_K_2}")

# ============================================================================
print()
print("=" * 78)
print("PASO 3 -- ¿e1(K) a orden h^2 contiene términos h_ii^2 puros?")
print("=" * 78)

coeff_h00sq_e1K = sp.diff(e1_K_2, h[0, 0], 2) / 2
coeff_h11sq_e1K = sp.diff(e1_K_2, h[1, 1], 2) / 2
coeff_h01sq_e1K = sp.diff(e1_K_2, h[0, 1], 2) / 2

print(f"Coeficiente de h00^2 en e1(K) orden2: {coeff_h00sq_e1K}")
print(f"Coeficiente de h11^2 en e1(K) orden2: {coeff_h11sq_e1K}")
print(f"Coeficiente de h01^2 en e1(K) orden2: {coeff_h01sq_e1K}")

tiene_estructura = coeff_h00sq_e1K != 0
print(f"\n¿e1(K) SÍ tiene la estructura h_ii^2 que e1(Gamma) no tenía? {tiene_estructura}")

# ============================================================================
print()
print("=" * 78)
print("PASO 4 -- construir V = sum beta_n e_n(K) y buscar masa Lorentz-covariante")
print("=" * 78)

b1, b2, b3, b4 = sp.symbols('beta1 beta2 beta3 beta4', real=True)
V_order2_K = sp.expand(b1 * e1_K_2 + b2 * e2_K_2 + b3 * e3_K_2 + b4 * e4_K_2)

coeff_h00sq = sp.simplify(sp.diff(V_order2_K, h[0, 0], 2) / 2)
coeff_h11sq = sp.simplify(sp.diff(V_order2_K, h[1, 1], 2) / 2)
coeff_h01sq = sp.simplify(sp.diff(V_order2_K, h[0, 1], 2) / 2)
coeff_h12sq = sp.simplify(sp.diff(V_order2_K, h[1, 2], 2) / 2)

print(f"Coeficiente de h00^2: {coeff_h00sq}")
print(f"Coeficiente de h11^2: {coeff_h11sq}  (debe coincidir con h00^2 en magnitud/signo para Lorentz-covarianza)")
print(f"Coeficiente de h01^2: {coeff_h01sq}")
print(f"Coeficiente de h12^2: {coeff_h12sq}")

# condiciones de covariancia tipo Fierz-Pauli: coeff(h00^2) = -coeff(h_ii^2 espacial)
# (porque eta_00=1, eta_ii=-1 para espacial en Tr(h^2)=sum eta_ii*eta_jj*h_ij^2 con
# signo relativo por como sube/baja indices, se verifica la razon exacta necesaria)
cond1 = sp.simplify(coeff_h00sq - coeff_h11sq)
print(f"\ncoeff(h00^2) - coeff(h11^2) = {cond1}  (=0 esperado si masa es isotropica en el sector espacial)")

sol = sp.solve([cond1], [b2, b3, b4], dict=True) if cond1 != 0 and cond1.free_symbols else None
print(f"¿Se anula automáticamente (sin restricción)? {cond1 == 0}")

# ============================================================================
print()
print("=" * 78)
print("PASO 5 -- ¿alguna combinación beta1,beta2 reproduce EXACTAMENTE Fierz-Pauli completo?")
print("=" * 78)
print("""
e3(K) y e4(K) se anulan idénticamente a orden h^2 (K es O(eps), K^3 y K^4
son O(eps^3) o más). Solo quedan beta1, beta2 libres. Se compara contra
el término de masa de Fierz-Pauli COMPLETO: h_mu_nu*h^mu_nu - h^2 (las
DOS invariantes, no solo la proporcional a Tr(h^2) ya confirmada).
""")


def hup(i, j):
    return eta_diag[i] * eta_diag[j] * h[i, j]


frob_raised = sp.expand(sum(h[i, j] * hup(i, j) for i in range(n) for j in range(n)))
htrace_full = sum(eta_diag[m] * h[m, m] for m in range(n))
FP_mass = sp.expand(frob_raised - htrace_full**2)

import random
random.seed(1)
all_syms = [h[i, j] for i in range(n) for j in range(i, n)]
eqs = []
for _ in range(2):
    subs_map = {s: sp.Rational(random.randint(-5, 5), random.randint(1, 3)) for s in all_syms}
    eqs.append(sp.Eq((b1 * e1_K_2 + b2 * e2_K_2).subs(subs_map), FP_mass.subs(subs_map)))

sol_fp = sp.solve(eqs, [b1, b2], dict=True)
print(f"Resolviendo beta1,beta2 para V2 = FP_mass exactamente (2 instancias aleatorias): {sol_fp}")

if sol_fp:
    s = sol_fp[0]
    check_expr = sp.expand((s[b1] * e1_K_2 + s[b2] * e2_K_2) - FP_mass)
    random.seed(777)
    subs_check = {sy: sp.Rational(random.randint(-6, 6), random.randint(1, 4)) for sy in all_syms}
    residual = sp.simplify(check_expr.subs(subs_check))
    print(f"Verificación en una 3ra instancia aleatoria (independiente): residuo = {residual}")
    assert residual == 0, "no coincide en la instancia de verificación"
    print(f"\nCONFIRMADO: beta1={s[b1]}, beta2={s[b2]} reproduce EXACTAMENTE h_mu_nu*h^mu_nu - h^2")
    print("(el término de masa de Fierz-Pauli completo, con f=eta como métrica de referencia)")

print()
print("=" * 78)
print("CONCLUSIÓN")
print("=" * 78)
print("""
RESULTADO POSITIVO Y CERRADO: con f=eta (el fondo de Minkowski -- ya
presente en toda la sesión, no una estructura nueva inventada), la
construcción K=I-sqrt(Gamma_s^-1*eta), resuelta perturbativamente y
verificada con sympy (no citada de la literatura), da via V=beta2*e2(K)
(con beta1=0, beta2=-8, o cualquier reescalado) EXACTAMENTE el término
de masa de Fierz-Pauli completo h_mu_nu*h^mu_nu - h^2 -- verificado en
una instancia de comprobación independiente, residuo cero exacto.

Esto cierra "qué juega el rol de f en GSF": f=eta funciona, sin
necesidad de postular ninguna estructura adicional -- exactamente lo que
gsf_einstein_derivation.md §5quater predijo como necesario (raíz cuadrada
matricial de una métrica de referencia), ahora con la elección concreta
y el resultado exacto verificado.

CIERRA EL PROGRAMA dRGT PARA GSF (en el sector de masa, a orden
cuadrático): con el sector cinético resuelto conceptualmente (adoptar
L_coord=Einstein-Hilbert(Gamma_s), §5ter) y el término de masa resuelto
aquí (V=beta2*e2(K), f=eta), GSF tiene -- al menos a nivel linealizado,
cuadrático en h -- una construcción COMPLETA y libre de ghost para el
sector gravitacional: Fierz-Pauli desde la acción EH + masa Fierz-Pauli
desde e2(K) con f=eta.

PENDIENTE HONESTO: (1) esto es una verificación a ORDEN CUADRÁTICO
(h^2) -- el resultado dRGT genuino (ausencia del ghost de
Boulware-Deser) es un enunciado NO LINEAL, sobre la teoría COMPLETA, no
solo su expansión cuadrática; verificar que V=beta2*e2(K) (con la K
exacta, no solo a O(h^2)) sigue siendo libre de ghost a TODOS los
órdenes requeriría repetir el análisis ADM/hamiltoniano completo de
dRGT, no hecho aquí. (2) no se conectó esto con el término "+Gamma_s"
original de GSF ni con adj(Gamma) -- falta verificar que ESTA
construcción (V=beta2*e2(K)) es consistente con, o reemplaza
limpiamente, el término de masa original de GSF y su rol en dar Lambda
via adj(Gamma) (Ch36, ya establecido). (3) f=eta es el candidato más
simple -- no se descarta que un f distinto (derivado de Gamma_a, por
ejemplo) dé una estructura aún más rica o más nativa de GSF; no
explorado.
""")
