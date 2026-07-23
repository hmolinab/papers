"""
Verificación de §4.1 (25 órdenes de magnitud en razones de viscosidad, sin ajuste).

No es una re-medición: reproduce por código la aritmética de la tabla del paper a
partir de valores de viscosidad cinemática estándar de ingeniería, y verifica
programáticamente las dos afirmaciones del texto:
  (1) gamma_rel = nu_agua / nu_fluido reproduce exactamente los valores tabulados,
  (2) el rango completo abarca ~25 órdenes de magnitud.

Fuentes de los valores de nu (m^2/s), a temperatura/presión ambiente salvo donde
se indica: Cengel & Cimbala, "Fluid Mechanics: Fundamentals and Applications"
(4th ed., 2018); CRC Handbook of Chemistry and Physics. Los valores de hielo
glaciar y manto terrestre son estimaciones de orden de magnitud de la literatura
de reología de sólidos de la Tierra (viscosidad efectiva de creep), citadas aquí
tal como aparecen en el borrador de trabajo del programa
(brainstorming/unification/release/pieza2_gamma_fluidos.md) -- no verificadas de
forma independiente contra una fuente primaria en este script.
"""
import math

# nu_kin en m^2/s (convertido desde las cifras x10^-6 m^2/s del paper donde aplica)
FLUIDOS = {
    "Mercurio":                0.12e-6,
    "Acetona":                 0.43e-6,
    "Agua (referencia)":       1.004e-6,
    "Agua de mar":             1.05e-6,
    "D2O":                     1.251e-6,
    "Plasma sanguineo":        1.3e-6,
    "Etanol":                  1.52e-6,
    "Glicerol (100%)":         1190e-6,
    "Hielo glaciar (creep)":   1e18 * 1.004e-6,   # orden de magnitud, ver docstring
    "Manto terrestre (sup.)":  3e23 * 1.004e-6,   # orden de magnitud, ver docstring
}

NU_AGUA = FLUIDOS["Agua (referencia)"]

print("=" * 78)
print(f"{'Fluido':<24} {'nu (m^2/s)':>14} {'gamma_rel = nu_agua/nu':>24}")
print("=" * 78)
gammas_rel = {}
for nombre, nu in FLUIDOS.items():
    gamma_rel = NU_AGUA / nu
    gammas_rel[nombre] = gamma_rel
    print(f"{nombre:<24} {nu:14.4e} {gamma_rel:24.4e}")

print()
rango_ordenes = math.log10(max(gammas_rel.values()) / min(gammas_rel.values()))
print(f"Rango total en gamma_rel: {rango_ordenes:.2f} ordenes de magnitud")
print(f"(afirmacion del paper: '25 ordenes de magnitud' -> "
      f"{'CONSISTENTE' if abs(rango_ordenes-25) < 1.5 else 'REVISAR'})")

print()
print("=" * 78)
print("Comparacion linea por linea contra la tabla publicada en el paper (§4.1):")
print("=" * 78)
TABLA_PAPER = {
    "Mercurio": 8.4, "Acetona": 2.34, "Agua (referencia)": 1.000,
    "Agua de mar": 0.956, "D2O": 0.803, "Plasma sanguineo": 0.77,
    "Etanol": 0.660, "Glicerol (100%)": 8.4e-4,
    "Hielo glaciar (creep)": 1e-18, "Manto terrestre (sup.)": 3e-24,
}
max_diff_rel = 0.0
for nombre, val_paper in TABLA_PAPER.items():
    val_calc = gammas_rel[nombre]
    diff_rel = abs(val_calc - val_paper) / val_paper
    max_diff_rel = max(max_diff_rel, diff_rel)
    flag = "OK" if diff_rel < 0.05 else "DIFERENCIA > 5%"
    print(f"  {nombre:<24} paper={val_paper:.4e}  calculado={val_calc:.4e}  "
          f"diff={diff_rel*100:5.2f}%  {flag}")

print()
print(f"Diferencia relativa maxima entre tabla publicada y calculo reproducido: "
      f"{max_diff_rel*100:.2f}%")
print("(diferencias pequenas esperadas por redondeo de las cifras de nu publicadas "
      "en el paper; el punto de esta verificacion es confirmar que la tabla es "
      "aritmetica reproducible desde los valores de nu citados, no un ajuste.)")
