"""
conexion_potencial_completo_lambda_masa.py

Conecta el resultado de f_como_eta_verificacion.py (V=beta2*e2(K) da
Fierz-Pauli exacto) con el resto de la EOM de GSF: el término "+Gamma"
original (de ||Gamma||_F^2) y adj(Gamma)/Lambda (de mu*det(Gamma)).

PREGUNTA CONCRETA: si se propone el potencial COMBINADO

    P_nuevo = beta2*e2(K(Gamma_s)) + mu*det(Gamma)

(reemplazando SOLO ||Gamma||_F^2 por beta2*e2(K), dejando mu*det(Gamma)
intacto, ya que ESE es el término que da Lambda=adj(Gamma) en Ch36/PR-41)
-- ¿se preserva (a) la identificación Lambda=adj(Gamma) en el fondo
Gamma=eta (orden h^0), y (b) la estructura de Fierz-Pauli limpia en la
perturbación (orden h^2), o el propio det(Gamma) contamina el término de
masa con su propia contribución cuadrática?

MÉTODO: expandir det(Gamma_s) a orden h^2 (Gamma_s=eta+h) exactamente
(sympy, determinante 4x4 real, no fórmula aproximada), y sumar su propia
contribución O(h^2) a la de beta2*e2(K) ya conocida -- verificar si el
TOTAL sigue siendo proporcional a Fierz-Pauli, o si mu*det(Gamma) rompe
la estructura limpia encontrada antes.
"""

import sympy as sp

n = 4
eta_diag = [1, -1, -1, -1]
eta = sp.diag(*eta_diag)

eps = sp.symbols('epsilon')
h = sp.Matrix(n, n, lambda i, j: sp.symbols(f'h{min(i,j)}{max(i,j)}', real=True))
mu, beta2 = sp.symbols('mu beta2', real=True)

Gamma = eta + eps * h

# ============================================================================
print("=" * 78)
print("PASO 1 -- orden 0 (fondo Gamma=eta): ¿Lambda=adj(Gamma) intacto?")
print("=" * 78)

adjGamma_at_eta = eta.adjugate()
print(f"adj(eta) = {adjGamma_at_eta.tolist()}  (debe ser -eta, ya establecido: Lambda=adj(Gamma)|_eta)")
print(f"¿adj(eta) == -eta? {adjGamma_at_eta == -eta}")

detGamma = Gamma.det()
detGamma_series = sp.series(detGamma, eps, 0, 3).removeO()
det_order0 = sp.expand(detGamma_series.coeff(eps, 0))
print(f"\ndet(Gamma) a orden 0: {det_order0}  (= det(eta) = -1, constante -> contribuye a Lambda)")

# K(Gamma_s) construido con f=eta, ya verificado en f_como_eta_verificacion.py
X = eta * h
K1 = X / 2
K2 = -sp.Rational(3, 8) * X * X
K_approx = eps * K1 + eps**2 * K2

lam = sp.symbols('lam')
cp = K_approx.charpoly(lam)
coeffs_K = cp.all_coeffs()
e2_K = coeffs_K[2]
e2_K_order0 = sp.expand(sp.series(e2_K, eps, 0, 1).removeO())
print(f"e2(K) a orden 0 (debe ser 0, K=0 exactamente cuando Gamma_s=eta): {e2_K_order0}")
assert e2_K_order0 == 0, "e2(K) no se anula en el fondo -- contaminaría Lambda"
print("CONFIRMADO: e2(K) no contribuye a Lambda -- la identificación adj(Gamma)=Lambda del fondo queda intacta.\n")

# ============================================================================
print("=" * 78)
print("PASO 2 -- orden 1 (lineal en h): ¿mu*det(Gamma) da un tadpole, y e2(K) lo deja intacto?")
print("=" * 78)


def order(expr, k):
    ser = sp.series(expr, eps, 0, k + 2).removeO()
    return sp.expand(ser.coeff(eps, k))


det_order1 = order(detGamma, 1)
e2_K_order1 = order(e2_K, 1)
print(f"det(Gamma) a orden 1 (lineal en h): {det_order1}")
print(f"e2(K) a orden 1 (debe ser 0, K arranca en O(h)): {e2_K_order1}")
assert e2_K_order1 == 0, "e2(K) contribuye a orden lineal -- contaminaría la condición de equilibrio"
print("CONFIRMADO: e2(K) no contribuye a orden lineal -- el término lineal de la EOM sigue viniendo")
print("SOLO de mu*det(Gamma) (via adj(eta)), sin interferencia del nuevo término de masa.\n")

# ============================================================================
print("=" * 78)
print("PASO 3 -- orden 2 (cuadrático): ¿mu*det(Gamma) contamina la estructura Fierz-Pauli?")
print("=" * 78)

det_order2 = order(detGamma, 2)
e2_K_order2 = order(e2_K, 2)
print(f"det(Gamma) a orden 2 (cuadrático en h): {sp.expand(det_order2)}")
print(f"\ne2(K) a orden 2 (ya conocido de f_como_eta_verificacion.py): {sp.expand(e2_K_order2)}")

P_total_order2 = sp.expand(beta2 * e2_K_order2 + mu * det_order2)
print(f"\nP_total a orden h^2 = beta2*e2(K)_2 + mu*det(Gamma)_2:")
print(f"  {P_total_order2}")

# ============================================================================
print()
print("=" * 78)
print("PASO 4 -- ¿P_total sigue siendo proporcional a Fierz-Pauli (h_mu_nu h^mu_nu - h^2)?")
print("=" * 78)


def hup(i, j):
    return eta_diag[i] * eta_diag[j] * h[i, j]


htrace = sum(eta_diag[m] * h[m, m] for m in range(n))
frob_raised = sp.expand(sum(h[i, j] * hup(i, j) for i in range(n) for j in range(n)))
FP_mass = sp.expand(frob_raised - htrace**2)

c = sp.symbols('c')
import random
random.seed(3)
all_syms = [h[i, j] for i in range(n) for j in range(i, n)]

# con beta2 fijo (=-8, del resultado anterior), resolver que P_total = c*FP_mass + posible remanente
P_total_beta2fixed = P_total_order2.subs(beta2, -8)
eqs = []
for _ in range(3):
    subs_map = {s: sp.Rational(random.randint(-5, 5), random.randint(1, 3)) for s in all_syms}
    eqs.append(sp.Eq(P_total_beta2fixed.subs(subs_map), (mu * c) * FP_mass.subs(subs_map) if False else mu * FP_mass.subs(subs_map) + c))

# Enfoque directo: comparar componente a componente si P_total (beta2=-8) - mu*FP_mass es
# proporcional SOLO a mu (es decir, si el remanente det(Gamma)_2 en si mismo ya es
# proporcional a FP_mass, o si introduce una estructura DISTINTA que rompe la limpieza)
remainder = sp.expand(P_total_beta2fixed - mu * FP_mass)
# ¿es 'remainder' identicamente cero (fierz-Pauli exacto se mantiene)?
print(f"P_total(beta2=-8) - mu*FP_mass = {sp.expand(remainder)}")
print(f"¿Se anula identicamente (es decir, det(Gamma)_2 YA es proporcional a FP_mass con esta mu)? {remainder == 0}")

if remainder != 0:
    # verificar si det(Gamma)_2 POR SI SOLO es proporcional a FP_mass (con su propia constante)
    random.seed(5)
    subs_map2 = {s: sp.Rational(random.randint(-5, 5), random.randint(1, 3)) for s in all_syms}
    det2_val = det_order2.subs(subs_map2)
    fp_val = FP_mass.subs(subs_map2)
    ratio_det2 = sp.simplify(det2_val / fp_val) if fp_val != 0 else None
    print(f"\n¿det(Gamma)_2 es por si solo proporcional a FP_mass? razón de muestra: {ratio_det2}")
    subs_map3 = {s: sp.Rational(random.randint(-5, 5), random.randint(1, 3)) for s in all_syms}
    det2_val2 = det_order2.subs(subs_map3)
    fp_val2 = FP_mass.subs(subs_map3)
    ratio_det2_2 = sp.simplify(det2_val2 / fp_val2) if fp_val2 != 0 else None
    print(f"segunda muestra: {ratio_det2_2}")
    es_proporcional = (ratio_det2 == ratio_det2_2) if (ratio_det2 is not None and ratio_det2_2 is not None) else False
    print(f"¿Coinciden (proporcionalidad universal)? {es_proporcional}")

print()
print("=" * 78)
print("PASO 5 -- reajustar beta2: no hay contaminación, hay REFUERZO consistente")
print("=" * 78)
print("""
det(Gamma)_2 es POR SI SOLO proporcional a FP_mass con razón 1/2 (confirmado
arriba, dos muestras independientes coinciden). Esto significa que
mu*det(Gamma) NO introduce una estructura distinta/incompatible -- suma
MÁS Fierz-Pauli, con su propio coeficiente. El "residuo no nulo" del Paso
4 (con beta2=-8 fijo del resultado anterior) es solo porque beta2=-8 fue
calibrado ANTES de sumar la contribución de mu*det(Gamma) -- no es una
inconsistencia estructural, es una simple recalibración de escala.
""")

beta2_needed = sp.symbols('beta2_needed')
# P_total_2 = beta2*e2(K)_2 + mu*det(Gamma)_2 = beta2*(-1/8)*FP_mass + mu*(1/2)*FP_mass
# se quiere que el coeficiente TOTAL de FP_mass sea 1 (masa canonica)
eq_beta2 = sp.Eq(-beta2_needed / 8 + mu / 2, 1)
sol_beta2 = sp.solve(eq_beta2, beta2_needed)
print(f"Coeficiente de e2(K) en P_total: -beta2/8. Coeficiente de det(Gamma): mu/2.")
print(f"Para que el coeficiente TOTAL de Fierz-Pauli sea exactamente 1 (masa canónica):")
print(f"  beta2 = {sol_beta2[0]}  (depende de mu, no un valor fijo independiente)")

# verificacion final: con este beta2(mu), el total es EXACTAMENTE FP_mass
beta2_val = sol_beta2[0]
P_total_final = sp.expand(beta2_val * e2_K_order2 + mu * det_order2)
residual_final = sp.expand(P_total_final - FP_mass)
print(f"\nVerificación: P_total(beta2={beta2_val}) - FP_mass = {residual_final}")
print(f"¿Se anula identicamente para TODO mu? {residual_final == 0}")
assert residual_final == 0, "no se anula -- revisar"

print()
print("=" * 78)
print("CONCLUSIÓN")
print("=" * 78)
print(f"""
CONFIRMADO -- CONEXIÓN COMPLETA Y CONSISTENTE, para cualquier valor de mu:

1. ORDEN 0 (fondo): e2(K) se anula exactamente en Gamma=eta -- la
   identificación Lambda=adj(Gamma) (Ch36/PR-41) queda TOTALMENTE
   intacta, sin interferencia del nuevo término de masa.

2. ORDEN 1 (lineal): e2(K) se anula exactamente a este orden también --
   el término lineal de la EOM ("+Gamma" original) sigue viniendo
   ÚNICAMENTE de mu*det(Gamma) (via adj(eta)), sin contaminación.

3. ORDEN 2 (masa cuadrática): det(Gamma) NO contamina con una estructura
   incompatible -- es POR SÍ SOLO proporcional a Fierz-Pauli (razón 1/2,
   confirmado independientemente). Reajustando beta2 = 8*(mu/2-1) =
   4*mu-8 (una simple recalibración, NO una inconsistencia), el
   potencial COMBINADO

      P_total = (4*mu-8)*e2(K(Gamma_s)) + mu*det(Gamma)

   da EXACTAMENTE h_mu_nu*h^mu_nu - h^2 (Fierz-Pauli canónico, coeficiente 1)
   a orden h^2, para CUALQUIER valor de mu -- sin tensión con la
   identificación de Lambda ya establecida.

ESTO CIERRA LA CONEXIÓN PEDIDA: el "+Gamma" original de GSF (via
||Gamma||_F^2) se puede reemplazar por beta2*e2(K) [f=eta] sin romper
NADA de lo que mu*det(Gamma) ya hacía (ni el fondo/Lambda, ni el orden
lineal) -- y la masa cuadrática resultante es Fierz-Pauli exacto,
reforzada (no en conflicto) por la propia contribución de det(Gamma).

PENDIENTE HONESTO: esto sigue siendo una verificación a ORDEN CUADRÁTICO
únicamente (igual que f_como_eta_verificacion.py) -- la consistencia a
TODOS los órdenes (el enunciado dRGT genuino sobre ausencia de ghost) no
se verifica aquí. Tampoco se exploró si beta2=4*mu-8 es compatible con
los valores de mu YA fijados en otras partes de GSF (mu=2/sqrt(c) de la
bifurcación Gamma->xi, o el mu(rho) cosmológico de PR-41) -- eso
requeriría revisar si esos mu especificos, sustituidos aquí, dan una masa
efectiva físicamente sensata (por ejemplo, no negativa/taquiónica).
""")
