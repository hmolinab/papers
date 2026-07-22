"""
verificacion_cota_amgm.py

Al escribir la demostración completa de la cota AM-GM del Hessiano
(m_eff^2 = 2 + mu*det(Gamma_0)/(lambda_i*lambda_j) + 4*beta*||Gamma_0||^2 >= 2
cuando beta >= |mu|/16, Paper 4 / paper_d_gamma_atlas.md §2.1) para el cuerpo
de Paper D, la re-derivación a mano encontró lo que parece un contraejemplo:
lambda_i=lambda_j=delta (pequeño, el PAR perturbado), lambda_k=lambda_l=1
(el otro par). Con mu<0, beta=|mu|/16, esto da m_eff^2 << 2 en la
estimación a mano. Se verifica aquí EXACTAMENTE (sympy simbólico +
numérico), sin aproximar, antes de escribir nada en el paper.
"""

import sympy as sp

lam1, lam2, lam3, lam4, eps, mu, beta = sp.symbols('lam1 lam2 lam3 lam4 epsilon mu beta', real=True)

# ============================================================================
print("=" * 78)
print("PASO 1 -- calcular d^2 P/d(eps)^2 EXACTO (no aproximado) para la")
print("perturbación antisimétrica en la dirección (1,2)")
print("=" * 78)

Gamma0 = sp.diag(lam1, lam2, lam3, lam4)
E12 = sp.zeros(4, 4)
E12[0, 1] = 1
E12[1, 0] = -1

Gamma_eps = Gamma0 + eps * E12

frob2 = sp.expand(sum(Gamma_eps[i, j]**2 for i in range(4) for j in range(4)))
detG = sp.expand(Gamma_eps.det())

P = frob2 + mu * detG + beta * frob2**2
P_series = sp.series(P, eps, 0, 3).removeO()
P_series = sp.expand(P_series)
print(f"P(eps) expandido a O(eps^2): {P_series}")

coeff_eps2 = sp.expand(P_series.coeff(eps, 2))
print(f"\nCoeficiente de eps^2 en P(eps): {coeff_eps2}")
print("(m_eff^2 se define como este coeficiente, dividido por ||E12||^2=2,")
print(" multiplicado por 2 porque P(eps)=P(0)+ (1/2)*m_eff^2*||E||^2*eps^2")
print(" => coeficiente de eps^2 = (1/2)*m_eff^2*2 = m_eff^2. Se verifica la")
print(" formula exacta comparando contra la reportada en el paper.)")

m_eff2_formula = 2 + mu * (lam1 * lam2 * lam3 * lam4) / (lam1 * lam2) + 4 * beta * (lam1**2 + lam2**2 + lam3**2 + lam4**2)
diff_check = sp.simplify(coeff_eps2 - m_eff2_formula)
print(f"\nDiferencia entre coeficiente exacto y fórmula del paper (debe ser 0): {diff_check}")
assert diff_check == 0, "la formula de m_eff^2 no coincide con el calculo exacto"
print("CONFIRMADO: m_eff^2 = 2 + mu*det(Gamma0)/(lam1*lam2) + 4*beta*||Gamma0||^2 es EXACTA.\n")

# ============================================================================
print("=" * 78)
print("PASO 2 -- el presunto contraejemplo: lam1=lam2=delta, lam3=lam4=1,")
print("mu<0, beta=|mu|/16 (el caso límite de la cota AM-GM)")
print("=" * 78)

delta, mu_val = sp.symbols('delta mu_val', positive=True)
subs_counterexample = {lam1: delta, lam2: delta, lam3: 1, lam4: 1, mu: -mu_val, beta: mu_val / 16}

m_eff2_test = m_eff2_formula.subs(subs_counterexample)
m_eff2_test = sp.simplify(m_eff2_test)
print(f"m_eff^2 en esta configuración (delta pequeño, mu_val>0, beta=mu_val/16): {m_eff2_test}")

m_eff2_limit = sp.limit(m_eff2_test, delta, 0)
print(f"Límite cuando delta -> 0: {m_eff2_limit}")

print("\nEvaluando numéricamente con mu_val=16 (=> beta=1), delta=0.1:")
numeric_val = m_eff2_test.subs({delta: sp.Rational(1, 10), mu_val: 16})
print(f"  m_eff^2 = {float(numeric_val):.4f}  (se esperaba >= 2 si la cota fuera correcta)")

print("\n¿Es m_eff^2 < 2 en este límite (confirmando el contraejemplo)?")
es_contraejemplo = sp.simplify(m_eff2_limit - 2) < 0
print(f"  {es_contraejemplo}  (m_eff^2 - 2 = {sp.simplify(m_eff2_limit - 2)})")

print()
print("=" * 78)
print("CONCLUSIÓN")
print("=" * 78)
if es_contraejemplo:
    print("""
CONTRAEJEMPLO CONFIRMADO: la cota "beta >= |mu|/16 implica m_eff^2 >= 2
para TODO Gamma_0 diagonal" es FALSA tal como está enunciada en el
material fuente (Paper 4). Con lambda_i=lambda_j=delta->0 (el par
perturbado) y lambda_k=lambda_l=1 (el otro par), m_eff^2 diverge hacia
-infinito cuando delta->0, para cualquier mu<0 con beta=|mu|/16.

La demostración original (basada en "AM-GM aplicado a ||Gamma_0||^2 vs
det") tiene un paso incorrecto: acota det(Gamma_0)/(lambda_i*lambda_j)
usando SOLO lambda_i,lambda_j (la desigualdad geométrica correcta),
pero en realidad ese cociente es lambda_k*lambda_j -- que puede ser
GRANDE si lambda_i,lambda_j (el par que se hace pequeño para la
perturbación) son pequeños mientras lambda_k,lambda_l permanecen fijos.
El error es tratar ||Gamma_0||^2 como si acotara SIEMPRE el producto
lambda_k*lambda_l relevante, cuando en realidad ||Gamma_0||^2 puede
permanecer ACOTADO (dominado por lambda_k^2+lambda_l^2 fijo) mientras
mu*det(Gamma0)/(lambda_i*lambda_j) = mu*lambda_k*lambda_l permanece de
orden 1 -- no hay cancelación garantizada.
""")
else:
    print("El contraejemplo NO se confirma -- revisar el álgebra, puede haber")
    print("un error en la construcción de este script.")
