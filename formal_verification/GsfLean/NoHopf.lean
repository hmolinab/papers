import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Analysis.Matrix.PosDef
import Mathlib.LinearAlgebra.Eigenspace.Basic
import Mathlib.LinearAlgebra.Matrix.Charpoly.Basic

set_option linter.style.header false

/-!
# Lema 1 (sin Hopf) -- `papers/determinant_cubic_source`

Lema 1 (`determinante_cubico_flujos_gradiente_molina2026.md`, §6): "En un equilibrio
`Γ_*`, el Jacobiano de `Γ̇ = -G⁻¹∇P`, para cualquier métrica simétrica definida positiva
`G ≻ 0`, tiene espectro real. Ningún par complejo cruza el eje imaginario -- mientras la
dinámica es metric-gradiente, el modo blando solo admite bifurcaciones estacionarias."

Enunciado matemático (el Jacobiano `J = -G⁻¹H`, `G ≻ 0` simétrica, `H` simétrica):
`J` tiene espectro REAL -- ningún autovalor (complejo, viendo `J` como matriz compleja)
tiene parte imaginaria no nula.

## Estado (jul-31 2026, honestidad de alcance)

**NO probado en esta sesión** -- se deja como `sorry` explícito sobre el enunciado REAL
(no sobre `True`), porque el enunciado está bien tipado y compila. Dos caminos de prueba
identificados, ninguno cerrado todavía:

1. **El que usa el paper**: escribir `J = G^(1/2) * S * G^(-1/2)` con
   `S = -G^(-1/2) H G^(-1/2)` simétrica, y usar que matrices semejantes comparten
   espectro. Bloqueado hoy: mathlib no tiene (encontrado en esta búsqueda) una raíz
   cuadrada de matriz simétrica definida positiva lista para usar -- construirla
   (vía descomposición espectral) es trabajo aparte, no incluido aquí.
2. **Alternativa mathlib-idiomática, sin raíz cuadrada**: `G` define un producto interno
   nuevo `⟨x,y⟩_G = xᵀGy` sobre `ℝⁿ` (válido porque `G ≻ 0`); el operador
   `x ↦ G⁻¹Hx` es AUTOADJUNTO respecto a `⟨,⟩_G` (se verifica directo:
   `⟨G⁻¹Hx,y⟩_G = xᵀHy = ⟨x,G⁻¹Hy⟩_G` usando `H` simétrica) -- los operadores
   autoadjuntos en un espacio de producto interno de dimensión finita tienen espectro
   real, resultado ya desarrollado en mathlib (`Mathlib.Analysis.InnerProductSpace.
   Spectrum` / teoría espectral de `IsSelfAdjoint`). Requiere instanciar la estructura
   de espacio de producto interno inducida por `G` -- no trivial pero más cercano a lo
   que mathlib ya tiene, candidato mas prometedor para la proxima sesion.
-/

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- Enunciado del Lema 1 (sin Hopf): con `G` simétrica definida positiva y `H`
simétrica, el Jacobiano `J = -G⁻¹H` tiene espectro real -- toda raíz COMPLEJA del
polinomio característico de `J` (el mismo polinomio de coeficientes reales, mapeado a
`ℂ[X]`) tiene parte imaginaria nula. PENDIENTE de prueba (ver docstring del módulo). -/
theorem lema_1_sin_hopf {G H : Matrix n n ℝ} (hG : G.PosDef) (hH : H.IsSymm) :
    ∀ μ : ℂ, (Polynomial.map (algebraMap ℝ ℂ) (-G⁻¹ * H).charpoly).IsRoot μ → μ.im = 0 := by
  sorry
