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
polinomio característico de `J` tiene parte imaginaria nula. PROBADO COMPLETO (jul-31
2026, con el REPL de Lean para inspeccionar el estado de la prueba paso a paso): sin
raíz cuadrada de matriz -- extrae el vector propio del espectro (`Matrix.charpoly_map`,
`Matrix.mem_spectrum_iff_isRoot_charpoly`, `Matrix.mulVec_injective_iff_isUnit`), deriva
`Hv = -μGv` multiplicando por `G` a la izquierda, y concluye vía el argumento clásico
del problema de autovalores generalizado: `⟨v,Hv⟩` y `⟨v,Gv⟩` son ambos reales
(`sesquilinear_real_of_isSymm`, aplicado a `H` y a `G`), `⟨v,Gv⟩>0` (positividad de la
forma cuadrática de `G`, descompuesta en partes real/imaginaria de `v` y cerrada con
`Matrix.PosDef.dotProduct_mulVec_pos`), y de `⟨v,Hv⟩ = -μ⟨v,Gv⟩` con ambos lados reales
y el segundo factor no nulo, `μ` es real. -/
theorem lema_1_sin_hopf {G H : Matrix n n ℝ} (hG : G.PosDef) (hH : H.IsSymm) :
    ∀ μ : ℂ, (Polynomial.map (algebraMap ℝ ℂ) (-G⁻¹ * H).charpoly).IsRoot μ → μ.im = 0 := by
  intro μ hμ
  rw [← charpoly_map] at hμ
  rw [← Matrix.mem_spectrum_iff_isRoot_charpoly, spectrum.mem_iff,
      Algebra.algebraMap_eq_smul_one] at hμ
  rw [Matrix.mulVec_injective_iff_isUnit.not.symm, Function.not_injective_iff] at hμ
  obtain ⟨a, b, hab, hne⟩ := hμ
  set v := a - b with hv
  have hv0 : v ≠ 0 := sub_ne_zero.mpr hne
  have key : (μ • 1 - (-G⁻¹ * H).map (algebraMap ℝ ℂ)) *ᵥ v = 0 := by
    rw [hv, Matrix.mulVec_sub, hab, sub_self]
  have step : μ • v = (-G⁻¹ * H).map (algebraMap ℝ ℂ) *ᵥ v := by
    rw [Matrix.sub_mulVec, sub_eq_zero, Matrix.smul_mulVec, Matrix.one_mulVec] at key
    exact key
  have hGdet : IsUnit G.det := isUnit_iff_ne_zero.mpr hG.det_pos.ne'
  have hGinv : G * G⁻¹ = 1 := Matrix.mul_nonsing_inv G hGdet
  have hcancel : ∀ w : n → ℂ,
      (G.map (algebraMap ℝ ℂ)) *ᵥ ((G⁻¹.map (algebraMap ℝ ℂ)) *ᵥ w) = w := by
    intro w
    rw [Matrix.mulVec_mulVec, ← Matrix.map_mul, hGinv,
        Matrix.map_one (algebraMap ℝ ℂ) (map_zero _) (map_one _), Matrix.one_mulVec]
  have final : (H.map (algebraMap ℝ ℂ)) *ᵥ v = (-μ) • ((G.map (algebraMap ℝ ℂ)) *ᵥ v) := by
    have lhs_eq : (G.map (algebraMap ℝ ℂ)) *ᵥ (μ • v) = μ • ((G.map (algebraMap ℝ ℂ)) *ᵥ v) :=
      Matrix.mulVec_smul _ _ _
    rw [step, Matrix.map_mul, Matrix.map_neg (algebraMap ℝ ℂ) (fun a => by simp),
        neg_mul, Matrix.neg_mulVec, Matrix.mulVec_neg] at lhs_eq
    rw [show (G⁻¹.map (algebraMap ℝ ℂ) * H.map (algebraMap ℝ ℂ)) *ᵥ v
        = G⁻¹.map (algebraMap ℝ ℂ) *ᵥ (H.map (algebraMap ℝ ℂ) *ᵥ v) from
        (Matrix.mulVec_mulVec _ _ _).symm, hcancel] at lhs_eq
    rw [neg_eq_iff_eq_neg] at lhs_eq
    rw [lhs_eq, neg_smul]
  set x : n → ℝ := fun i => (v i).re with hx
  set y : n → ℝ := fun i => (v i).im with hy
  have symm_swap : ∀ (p q : n → ℝ),
      ∑ i, ∑ j, p i * (G i j * q j) = ∑ i, ∑ j, q i * (G i j * p j) := by
    intro p q
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl; intro i _
    apply Finset.sum_congr rfl; intro j _
    have hij : G j i = G i j := congrFun (congrFun hG.isHermitian i) j
    rw [hij]; ring
  have hB_eq : dotProduct (star v) ((G.map (algebraMap ℝ ℂ)) *ᵥ v) =
      ((dotProduct x (G *ᵥ x) + dotProduct y (G *ᵥ y) : ℝ) : ℂ) := by
    simp only [dotProduct, mulVec, Pi.star_apply, Matrix.map_apply, Complex.coe_algebraMap]
    push_cast
    simp only [Complex.ext_iff, hx, hy, Complex.mul_re, Complex.mul_im, Complex.conj_re,
      Complex.conj_im, Complex.re_sum, Complex.im_sum, Complex.add_re, Complex.add_im,
      Complex.ofReal_re, Complex.ofReal_im, Complex.star_def, zero_mul, mul_zero, add_zero,
      zero_add, sub_zero, neg_zero, zero_sub]
    constructor
    · rw [← Finset.sum_add_distrib]
      apply Finset.sum_congr rfl; intro i _; ring
    · simp only [Finset.sum_const_zero, mul_zero, add_zero]
      have expand : (∑ i, ((v i).re * ∑ j, G i j * (v j).im + -(v i).im * ∑ j, G i j * (v j).re))
          = ∑ i, ∑ j, x i * (G i j * y j) - ∑ i, ∑ j, y i * (G i j * x j) := by
        rw [← Finset.sum_sub_distrib]
        apply Finset.sum_congr rfl
        intro i _
        simp only [hx, hy, Finset.mul_sum]
        rw [sub_eq_add_neg, ← Finset.sum_neg_distrib]
        simp only [neg_mul]
      rw [expand, symm_swap x y, sub_self]
  have hBpos : 0 < dotProduct x (G *ᵥ x) + dotProduct y (G *ᵥ y) := by
    rcases eq_or_ne x 0 with hx0 | hx0
    · have hy0 : y ≠ 0 := by
        intro hy0
        apply hv0
        funext i
        have h1 : (v i).re = 0 := congrFun hx0 i
        have h2 : (v i).im = 0 := congrFun hy0 i
        apply Complex.ext <;> simp_all
      have hpos := hG.dotProduct_mulVec_pos hy0
      simp only [star_trivial] at hpos
      have hx0' : dotProduct x (G *ᵥ x) = 0 := by rw [hx0]; simp
      linarith
    · have hpos := hG.dotProduct_mulVec_pos hx0
      simp only [star_trivial] at hpos
      have hy0' : 0 ≤ dotProduct y (G *ᵥ y) := by
        rcases eq_or_ne y 0 with hy0 | hy0
        · rw [hy0]; simp
        · have hpos' := hG.dotProduct_mulVec_pos hy0
          simp only [star_trivial] at hpos'
          exact hpos'.le
      linarith
  have hAB : dotProduct (star v) ((H.map (algebraMap ℝ ℂ)) *ᵥ v) =
      (-μ) * dotProduct (star v) ((G.map (algebraMap ℝ ℂ)) *ᵥ v) := by
    rw [final, dotProduct_smul]
    rfl
  have hGsymm : G.IsSymm := by
    ext i j
    have hij := congrFun (congrFun hG.isHermitian i) j
    simpa [Matrix.IsSymm] using hij
  have hHreal := sesquilinear_real_of_isSymm hH v
  have hGreal := sesquilinear_real_of_isSymm hGsymm v
  rw [hAB] at hHreal
  rw [show starRingEnd ℂ (-μ * dotProduct (star v) ((G.map (algebraMap ℝ ℂ)) *ᵥ v))
      = -(starRingEnd ℂ μ) * dotProduct (star v) ((G.map (algebraMap ℝ ℂ)) *ᵥ v) by
    rw [map_mul, map_neg, hGreal]] at hHreal
  have hBne : dotProduct (star v) ((G.map (algebraMap ℝ ℂ)) *ᵥ v) ≠ 0 := by
    rw [hB_eq]; exact_mod_cast hBpos.ne'
  have hconj : starRingEnd ℂ μ = μ := by
    have hcancel := mul_right_cancel₀ hBne hHreal
    exact neg_inj.mp hcancel
  exact Complex.conj_eq_iff_im.mp hconj
