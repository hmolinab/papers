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

**`sesquilinear_real_of_isSymm`: PROBADO COMPLETO** (sin `sorry`) -- el hecho elemental
"forma sesquilineal de matriz real simétrica es real", el ladrillo que de verdad
bloqueaba el argumento. Cerrado usando el REPL de Lean (`leanprover-community/repl`,
instalado y compilado contra el mismo toolchain de este proyecto, `v4.32.2` -- ver
README) para inspeccionar el estado de la prueba paso a paso, en vez de compilar a
ciegas por lote. Prueba: reindexar la doble suma (`Finset.sum_comm`, tras empujar la
multiplicación adentro con `Finset.mul_sum`) y usar la simetría de `M` para hacer
coincidir los términos cruzados -- sin ninguna raíz cuadrada de matriz.

- `lema_1_sin_hopf`: enunciado real, bien tipado, compila. Prueba PENDIENTE (`sorry`) --
  ahora depende SOLO de ensamblaje de API estándar de mathlib
  (`Matrix.charpoly_map` para conectar la raíz del polinomio mapeado con el charpoly de
  la matriz compleja, `Matrix.mem_spectrum_iff_isRoot_charpoly`,
  `Matrix.mulVec_injective_iff_isUnit` para extraer el vector propio no nulo), no de
  ningún hecho matemático nuevo -- el paso matemáticamente difícil
  (`sesquilinear_real_of_isSymm`) ya está cerrado.
-/

open Matrix Polynomial

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- Pieza clave que resuelve el bloqueo de mathlib (ver docstring del módulo): la forma
sesquilineal `v̄ᵀMv` de una matriz REAL SIMÉTRICA `M`, complejizada, toma siempre un
valor real -- es su propio conjugado. PROBADO COMPLETO (jul-31 2026, con ayuda del REPL
de Lean para inspeccionar el estado de la prueba paso a paso -- ver README): la
identidad se cierra reindexando la doble suma (`Finset.sum_comm`) y usando la simetría
de `M` para hacer coincidir los términos cruzados, sin ninguna raíz cuadrada de
matriz. -/
theorem sesquilinear_real_of_isSymm {M : Matrix n n ℝ} (hM : M.IsSymm) (v : n → ℂ) :
    starRingEnd ℂ (star v ⬝ᵥ ((M.map (algebraMap ℝ ℂ)) *ᵥ v)) =
      star v ⬝ᵥ ((M.map (algebraMap ℝ ℂ)) *ᵥ v) := by
  simp only [dotProduct, mulVec, Pi.star_apply, map_sum, map_mul, ← starRingEnd_apply]
  simp only [Complex.conj_conj]
  simp only [Matrix.map_apply, Complex.coe_algebraMap, Complex.conj_ofReal]
  simp only [Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i _
  apply Finset.sum_congr rfl
  intro j _
  have hij : M j i = M i j := congrFun (congrFun hM.symm j) i
  rw [hij]
  ring

/-- Enunciado del Lema 1 (sin Hopf): con `G` simétrica definida positiva y `H`
simétrica, el Jacobiano `J = -G⁻¹H` tiene espectro real -- toda raíz COMPLEJA del
polinomio característico de `J` tiene parte imaginaria nula. Prueba PENDIENTE (ver
docstring del módulo). -/
theorem lema_1_sin_hopf {G H : Matrix n n ℝ} (hG : G.PosDef) (hH : H.IsSymm) :
    ∀ μ : ℂ, (Polynomial.map (algebraMap ℝ ℂ) (-G⁻¹ * H).charpoly).IsRoot μ → μ.im = 0 := by
  sorry
