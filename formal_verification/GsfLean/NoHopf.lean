import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Analysis.Matrix.PosDef
import Mathlib.LinearAlgebra.Eigenspace.Basic
import Mathlib.LinearAlgebra.Matrix.Charpoly.Basic
import Mathlib.LinearAlgebra.Matrix.Charpoly.Eigs
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse

set_option linter.style.header false

/-!
# Lema 1 (sin Hopf) -- `papers/determinant_cubic_source`

Lema 1 (`determinante_cubico_flujos_gradiente_molina2026.md`, §6): "En un equilibrio
`Γ_*`, el Jacobiano de `Γ̇ = -G⁻¹∇P`, para cualquier métrica simétrica definida positiva
`G ≻ 0`, tiene espectro real."

## La solución al bloqueo de mathlib (jul-31 2026)

La sesión anterior identificó que mathlib no tiene raíz cuadrada de matriz lista para
usar, bloqueando el camino de prueba literal del paper
(`J = G^(1/2) S G^(-1/2)`, `S` simétrica). **La solución no es construir esa raíz
cuadrada -- es evitarla por completo**, reformulando el problema como el PROBLEMA DE
AUTOVALORES GENERALIZADO clásico (Golub & Van Loan, *Matrix Computations*, §8.7):

`det(μI - G⁻¹H) = 0 ⟺ det(μG - H) = 0`

(identidad polinomial en `μ`: `μI - G⁻¹H = G⁻¹(μG - H)`, `det` multiplicativo,
`det(G⁻¹)` constante no nula independiente de `μ` -- ambos polinomios en `μ` tienen
exactamente las mismas raíces). El lado derecho SÍ es tratable sin raíz cuadrada: para
`v ≠ 0` con `Hv = μGv`, tomando el producto sesquilineal con `v̄`: `v̄ᵀHv = μ·v̄ᵀGv`. El
lado izquierdo es real (`H` real simétrica ⟹ forma sesquilineal real -- hecho elemental,
intentado formalizar en esta sesión, ver más abajo). El lado derecho es `v̄ᵀGv > 0`
(real, positivo, por `G≻0`) multiplicado por `μ`. Un real dividido por un real positivo
es real ⟹ `μ` es real.

## Estado (jul-31 2026, honestidad de alcance)

**Intentado y NO cerrado en esta sesión**: `sesquilinear_real_of_isSymm` (el hecho
elemental "forma sesquilineal de matriz real simétrica es real", que hace funcionar
todo el argumento de arriba). Se probaron varias versiones de la manipulación de sumas
con `starRingEnd`/`star`/`Finset.sum_comm` -- cada intento avanzó pero no cerró
completamente; el paso de normalizar `starRingEnd ℂ (star (v i))` de vuelta a `v i`
(dos conjugaciones se cancelan) resultó más delicado de lo esperado sin inspección
interactiva del estado de la prueba (goal state), que este entorno no tiene disponible
(solo compilación por lote vía `lake build`, sin editor Lean con feedback en vivo).
Queda como el siguiente paso concreto para retomar con un editor interactivo (VS Code +
extensión Lean 4), donde cada paso de `simp`/`rw` se puede verificar contra el estado
real de la prueba en vez de a ciegas.

- `lema_1_sin_hopf`: enunciado real, bien tipado, compila. Prueba PENDIENTE (`sorry`) --
  depende de `sesquilinear_real_of_isSymm` (también pendiente) más ensamblaje de API
  estándar de mathlib (`Matrix.mem_spectrum_iff_isRoot_charpoly`,
  `Matrix.mulVec_injective_iff_isUnit`).
-/

open Matrix Polynomial

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- Pieza clave que resuelve el bloqueo de mathlib (ver docstring del módulo): la forma
sesquilineal `v̄ᵀMv` de una matriz REAL SIMÉTRICA `M`, complejizada, toma siempre un
valor real -- es su propio conjugado. Intentado y NO cerrado en esta sesión (ver
docstring del módulo) -- enunciado correcto, prueba pendiente. -/
theorem sesquilinear_real_of_isSymm {M : Matrix n n ℝ} (hM : M.IsSymm) (v : n → ℂ) :
    starRingEnd ℂ (star v ⬝ᵥ ((M.map (algebraMap ℝ ℂ)) *ᵥ v)) =
      star v ⬝ᵥ ((M.map (algebraMap ℝ ℂ)) *ᵥ v) := by
  sorry

/-- Enunciado del Lema 1 (sin Hopf): con `G` simétrica definida positiva y `H`
simétrica, el Jacobiano `J = -G⁻¹H` tiene espectro real -- toda raíz COMPLEJA del
polinomio característico de `J` tiene parte imaginaria nula. Prueba PENDIENTE (ver
docstring del módulo). -/
theorem lema_1_sin_hopf {G H : Matrix n n ℝ} (hG : G.PosDef) (hH : H.IsSymm) :
    ∀ μ : ℂ, (Polynomial.map (algebraMap ℝ ℂ) (-G⁻¹ * H).charpoly).IsRoot μ → μ.im = 0 := by
  sorry
