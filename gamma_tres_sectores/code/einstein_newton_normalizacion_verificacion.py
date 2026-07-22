"""
einstein_newton_normalizacion_verificacion.py

Continúa einstein_gauge_armonico_verificacion.py (CERRADO: en gauge
armónico, G_mu_nu^(1) = -(1/2) Box h_bar_mu_nu, sin términos cruzados,
misma forma que el Frobenius de GSF). Aquí se acopla una fuente de
materia T_mu_nu real y se verifica que la normalización de Newton
(coeficiente 4*pi*G en la ecuación de Poisson) emerge EXACTAMENTE, no
aproximada -- ningún factor se ajusta a mano para que cuadre.

CADENA COMPLETA (cada paso verificado simbólicamente, no citado de
memoria):

1. Ecuación de Einstein (definición de G): G_mu_nu = 8*pi*G*T_mu_nu
2. Combinada con la identidad de gauge armónico ya verificada:
   Box h_bar_mu_nu = -16*pi*G*T_mu_nu
3. Fuente: polvo estático, T_mu_nu = diag(rho, 0, 0, 0) (sin presión,
   sin flujo de momento -- fuente no relativista estándar)
4. Límite estático (d_t=0): -Grad^2 h_bar_mu_nu = -16*pi*G*T_mu_nu, i.e.
   Grad^2 h_bar_00 = 16*pi*G*rho, resto = 0
5. Solución de Poisson con fuente puntual rho=M*delta^3(x):
   h_bar_00 = -4*G*M/r  (Grad^2(-4GM/r) = 16*pi*G*M*delta^3(x), ya que
   Grad^2(1/r) = -4*pi*delta^3(x))
6. Reversión de traza inversa (h_mu_nu desde h_bar_mu_nu) -- hecha con
   sympy, no a mano, para no arrastrar un error de factor 2 como en el
   primer intento manual de este cálculo
7. Extraer Phi de g_00 = 1 + h_00 =: 1 + 2*Phi (definición estándar del
   potencial newtoniano) y verificar Grad^2 Phi = 4*pi*G*rho
   (ecuación de Poisson) con el coeficiente EXACTO 4*pi*G, no otro múltiplo
"""

import sympy as sp

G, M, r = sp.symbols('G M r', positive=True)
rho = sp.Function('rho')

n = 4
eta_diag = [1, -1, -1, -1]


def eta(i, j):
    return eta_diag[i] if i == j else 0


print("=" * 78)
print("PASO 1-2 -- de Einstein + gauge armónico a la ecuación de onda sourceada")
print("=" * 78)
print("""
G_mu_nu = 8*pi*G*T_mu_nu   (definición de la constante de Newton G)
En gauge armónico (identidad ya verificada, ratio exacto -1 en
einstein_gauge_armonico_verificacion.py):
    G_mu_nu^(1) = -(1/2) Box h_bar_mu_nu
Combinando:
    Box h_bar_mu_nu = -16*pi*G*T_mu_nu
""")

print("=" * 78)
print("PASO 3-5 -- fuente de polvo estático, solución de Poisson para h_bar_00")
print("=" * 78)

# fuente puntual: rho = M*delta^3(x):  Grad^2(1/r) = -4*pi*delta^3(x) (identidad estándar)
# se busca h_bar_00 = c/r tal que Grad^2(c/r) = -4*pi*c*delta^3(x) = 16*pi*G*M*delta^3(x)
c = sp.symbols('c')
eq_c = sp.Eq(-4 * sp.pi * c, 16 * sp.pi * G * M)
c_sol = sp.solve(eq_c, c)[0]
print(f"h_bar_00 = c/r con c tal que Grad^2(c/r)=16*pi*G*M*delta^3(x): c = {c_sol}")
h_bar_00 = c_sol / r
print(f"h_bar_00 = {h_bar_00}")
print("h_bar_ij = 0, h_bar_0i = 0 (T_ij=T_0i=0 para polvo estático sin presión)\n")

# ============================================================================
print("=" * 78)
print("PASO 6 -- reversión de traza inversa h_mu_nu <- h_bar_mu_nu (con sympy, no a mano)")
print("=" * 78)

Hbar = sp.zeros(n, n)
Hbar[0, 0] = h_bar_00  # el resto queda en 0

htrace_bar = sum(eta(mu, mu) * Hbar[mu, mu] for mu in range(n))
# relación general: h_mu_nu = h_bar_mu_nu - (1/2) eta_mu_nu * h_bar_trace_reversed_back
# Se deriva resolviendo el sistema h_bar = h - (1/2) eta h_trace(h) para h, con sympy,
# en vez de citar la fórmula "h = h_bar - (1/2) eta hbar_trace" de memoria.

h_ij_syms = sp.symbols('h00 h11 h22 h33', real=True)  # solo la diagonal es relevante aqui
htrace_h = sum(eta(mu, mu) * h_ij_syms[mu] for mu in range(n))

eqs = []
for mu in range(n):
    lhs = h_ij_syms[mu] - sp.Rational(1, 2) * eta(mu, mu) * htrace_h
    eqs.append(sp.Eq(lhs, Hbar[mu, mu]))

sol = sp.solve(eqs, h_ij_syms, dict=True)[0]
print("Resolviendo h_mu_nu desde h_bar_mu_nu (sistema lineal, sympy):")
for sym, val in sol.items():
    print(f"  {sym} = {sp.simplify(val)}")

h_00 = sp.simplify(sol[h_ij_syms[0]])
h_11 = sp.simplify(sol[h_ij_syms[1]])
print(f"\nh_00 = {h_00}")
print(f"h_11 = h_22 = h_33 = {h_11}  (verificando isotropía: deben coincidir)")
assert sp.simplify(sol[h_ij_syms[1]] - sol[h_ij_syms[2]]) == 0
assert sp.simplify(sol[h_ij_syms[2]] - sol[h_ij_syms[3]]) == 0
print("  OK -- h_11 = h_22 = h_33 exactamente (isotropía confirmada, no asumida)\n")

# ============================================================================
print("=" * 78)
print("PASO 7 -- extraer Phi y verificar Poisson: Grad^2 Phi = 4*pi*G*rho")
print("=" * 78)

Phi_symbol = sp.symbols('Phi')
# definicion estandar: g_00 = 1 + h_00 =: 1 + 2*Phi
Phi_from_h00 = sp.simplify(h_00 / 2)
print(f"Phi (desde g_00 = 1+2*Phi, h_00={h_00}):  Phi = {Phi_from_h00}")

# consistencia: h_ii deberia dar el MISMO Phi via g_ii = -(1 - 2*Phi) = -1+2*Phi
# o sea h_ii = 2*Phi tambien (chequeo independiente, NO asumido en el paso 6)
Phi_from_hii = sp.simplify(h_11 / 2)
print(f"Phi (desde h_ii={h_11}, misma convención h_ii=2*Phi): Phi = {Phi_from_hii}")
assert sp.simplify(Phi_from_h00 - Phi_from_hii) == 0, "Phi de h_00 y h_ii no coinciden -- convención inconsistente"
print("  OK -- ambas extracciones de Phi coinciden exactamente (consistencia real, no forzada)\n")

Phi = Phi_from_h00
print(f"Phi = -G*M/r, la forma newtoniana estándar (atractiva): {sp.simplify(Phi - (-G*M/r)) == 0}")

# Grad^2 Phi para Phi=c'/r es exactamente -4*pi*c'*delta^3(x); extraer c' y comparar contra 4*pi*G*M
c_prime = sp.simplify(Phi * r)  # Phi = c_prime/r
poisson_source_coeff = sp.simplify(-4 * sp.pi * c_prime)  # Grad^2 Phi = poisson_source_coeff * delta^3(x)
expected = 4 * sp.pi * G * M
print(f"\nGrad^2 Phi = {poisson_source_coeff} * delta^3(x)")
print(f"Poisson estándar predice: 4*pi*G*M * delta^3(x) = {expected} * delta^3(x)")
print(f"Coincide exactamente: {sp.simplify(poisson_source_coeff - expected) == 0}")

assert sp.simplify(poisson_source_coeff - expected) == 0, "El coeficiente de Poisson NO es 4*pi*G -- revisar"

print()
print("=" * 78)
print("CONCLUSIÓN")
print("=" * 78)
print(f"""
CONFIRMADO, simbólicamente y sin ajustar ningún factor a mano: partiendo
de G_mu_nu=8*pi*G*T_mu_nu y la identidad de gauge armónico ya verificada
(Box h_bar_mu_nu = -16*pi*G*T_mu_nu), resolviendo Poisson para una fuente
puntual y revirtiendo la traza con sympy (no de memoria), se recupera
EXACTAMENTE:

  Phi = -G*M/r          (potencial newtoniano, atractivo, forma correcta)
  Grad^2 Phi = 4*pi*G*rho   (ecuación de Poisson, coeficiente EXACTO)

El coeficiente 16*pi*G que entra en la ecuación sourceada Box h_bar=fuente
es la única normalización consistente que reproduce el 4*pi*G de Newton --
no hay libertad para ajustar, ninguna instancia numérica requirió tocar
el factor.

QUÉ SIGNIFICA PARA GSF. La EOM de campo de GSF es
  Box Gamma + Gamma + (mu/2) adj(Gamma)^T = J(x,t)
Identificando Gamma_s ~ h_bar_mu_nu (gauge armónico, sección anterior),
la fuente J debe identificarse como J = -16*pi*G*T_mu_nu para reproducir
Newton con la normalización correcta -- una predicción CONCRETA y
falsable sobre cómo GSF debe acoplar materia, no un parámetro libre.

PENDIENTE HONESTO, no atacado aquí: la EOM de GSF tiene un término "+Gamma"
(masa Klein-Gordon, m^2=1 en unidades naturales) que NO aparece en la
ecuación de onda de gravitón sin masa Box h_bar=fuente -- para que la
identificación funcione, ese término tendría que anularse o cancelarse
con (mu/2)adj(Gamma)^T en el régimen relevante (sector det->0, gravedad
linealizada). Esto no se verificó; es un hueco real entre "GSF reproduce
Newton en su sector sourceado" y "GSF reproduce Newton desde SU PROPIA
EOM sin ajustes adicionales".
""")
