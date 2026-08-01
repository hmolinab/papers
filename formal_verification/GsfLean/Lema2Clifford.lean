import Mathlib.LinearAlgebra.CliffordAlgebra.Basic
import Mathlib.LinearAlgebra.CliffordAlgebra.Grading
import Mathlib.LinearAlgebra.QuadraticForm.Basic
import Mathlib.LinearAlgebra.Basis.Defs
import Mathlib.LinearAlgebra.Basis.Fin
import Mathlib.LinearAlgebra.Pi
import Mathlib.Data.Real.Basic

set_option linter.style.header false

/-!
# Lema 2 (álgebra) -- `papers/weld_clifford`

Lema 2 (`algebra_espaciotemporal_como_teorema_molina2026.md`, §3.3): "En `d=3`, los tres
atributos de grado 1 `{A,I,R}` generan `Cl(3,0)=G(3)` -- 8 dimensiones: grado 0 = S,
grado 1 = A,I,R, grado 2 = los bivectores, grado 3 = pseudoescalar."

## Alcance de esta formalización (ago-1 2026)

**Parte cerrada, sin `sorry`**: la afirmación de GENERACIÓN -- que `{A,I,R}` (una base de
`ℝ³`, el espacio de atributos) generan el álgebra de Clifford completa como subálgebra --
es EXACTAMENTE el teorema general `CliffordAlgebra.adjoin_range_ι` que ya está en
mathlib (para cualquier espacio cuadrático, no específico de `d=3`): la subálgebra
generada por la imagen de los generadores de grado 1 es toda el álgebra. Aquí se
instancia para `Q` la forma cuadrática estándar de `ℝ³` (positiva definida,
correspondiente a `Cl(3,0)`) y se reduce el generador "rango completo de `ι`" a
"los tres elementos `ι A, ι I, ι R`" usando que `{A,I,R}` es una base.

**Parte NO atacada**: el conteo de dimensión (`8 = 2³`, con grado 2 = bivectores y
grado 3 = pseudoescalar como subespacios de dimensión 3 y 1 respectivamente) -- mathlib
no tiene todavía un teorema general de `finrank (CliffordAlgebra Q) = 2 ^ finrank M`
listo para usar (se revisó `CliffordAlgebra/*.lean` y `ExteriorAlgebra/*.lean`, ninguno
lo tiene) -- construirlo desde cero (vía un isomorfismo con el álgebra exterior graduada)
es un desarrollo aparte, no incluido aquí.
-/

open CliffordAlgebra

variable {ι' : Type*} [Fintype ι'] [DecidableEq ι']

/-- El caso general: para CUALQUIER espacio cuadrático `(M, Q)` sobre un anillo conmutativo,
si `{v i}` es una base de `M`, entonces los elementos `{ι Q (v i)}` generan
`CliffordAlgebra Q` como subálgebra. Instancia concreta de `CliffordAlgebra.adjoin_range_ι`
(ya en mathlib para el rango completo de `ι`), reducida a un conjunto GENERADOR finito
vía la base -- el paso que hace falta para leer el enunciado del paper ("A,I,R generan",
tres elementos concretos, no "la imagen completa de ι"). -/
theorem lema_2_generadores_base {R : Type*} [CommRing R] {M : Type*} [AddCommGroup M]
    [Module R M] (Q : QuadraticForm R M) (v : Module.Basis ι' R M) :
    Algebra.adjoin R (Set.range (fun i => CliffordAlgebra.ι Q (v i))) = ⊤ := by
  have hsub : Set.range (CliffordAlgebra.ι Q) ⊆
      ↑(Algebra.adjoin R (Set.range (fun i => CliffordAlgebra.ι Q (v i)))) := by
    rintro _ ⟨m, rfl⟩
    rw [← v.linearCombination_repr m, Finsupp.linearCombination_apply, Finsupp.sum, map_sum]
    apply Submodule.sum_mem (Algebra.adjoin R _).toSubmodule
    intro i _
    rw [map_smul]
    exact Submodule.smul_mem _ _ (Algebra.subset_adjoin (Set.mem_range_self i))
  have hle : Algebra.adjoin R (Set.range (CliffordAlgebra.ι Q)) ≤
      Algebra.adjoin R (Set.range (fun i => CliffordAlgebra.ι Q (v i))) :=
    Algebra.adjoin_le hsub
  rw [CliffordAlgebra.adjoin_range_ι] at hle
  exact top_unique hle

/-- Lema 2 propiamente dicho: la base canónica `A, I, R` de `ℝ³` (identificados con la
base estándar `e₀,e₁,e₂` vía `Fin 3`), con la forma cuadrática estándar (`Cl(3,0)`),
genera el álgebra de Clifford completa. Caso particular de `lema_2_generadores_base`
con `M = Fin 3 → ℝ` y `v` la base estándar. -/
theorem lema_2_AIR_generan_Cl30 (Q : QuadraticForm ℝ (Fin 3 → ℝ)) :
    Algebra.adjoin ℝ (Set.range (fun i => CliffordAlgebra.ι Q (Pi.basisFun ℝ (Fin 3) i))) = ⊤ :=
  lema_2_generadores_base Q (Pi.basisFun ℝ (Fin 3))
