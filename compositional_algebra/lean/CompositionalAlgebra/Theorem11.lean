import Mathlib.Data.Matrix.Block
import Mathlib.Algebra.Group.Even

set_option linter.style.header false

/-!
# Theorem 11 -- reciprocal/non-reciprocal decomposition of the joint configuration

`compositional_algebra_of_coherence_units_molina2026.md` §9bis2 / `part1/07_compositional_
operations.md` §7.9bis.5 (public book, same result, numbered Theorem 7.10 there).

For `Γ_joint = [[K_A, C_AB], [C_BA, K_B]]` with `K_A,K_B,C_AB,C_BA` ARBITRARY (no
symmetry assumed, no `C_BA=C_ABᵀ`), defining `C_eff=(C_AB+C_BAᵀ)/2` (the reciprocal
part of the coupling) and `D_eff=(C_AB-C_BAᵀ)/2` (the non-reciprocal excess):

`Γ_s(Γ_joint) = [[Γ_s^A, C_eff], [C_effᵀ, Γ_s^B]]`,
`Γ_a(Γ_joint) = [[Γ_a^A, D_eff], [-D_effᵀ, Γ_a^B]]`

This closes the paper's Theorem 10 converse (bivector creation under Ω-elimination of a
non-symmetric partner): `D_eff` is the exact injection mechanism.

## Status: CLOSED (no `sorry`)

Pure block identity (transpose + sum) -- no Schur complement, no positivity, no
reciprocity hypothesis anywhere. Closed with `ext` entry-by-entry + `ring`.
-/

open Matrix

variable {m n R : Type*} [Fintype m] [Fintype n] [DecidableEq m] [DecidableEq n] [Field R]
  [Invertible (2 : R)]

/-- Symmetric part of a square matrix, `(M+Mᵀ)/2`. -/
noncomputable def symPart (M : Matrix m m R) : Matrix m m R := (⅟(2 : R)) • (M + Mᵀ)

/-- Antisymmetric part of a square matrix, `(M-Mᵀ)/2`. -/
noncomputable def antisymPart (M : Matrix m m R) : Matrix m m R := (⅟(2 : R)) • (M - Mᵀ)

noncomputable def Ceff (CAB : Matrix m n R) (CBA : Matrix n m R) : Matrix m n R :=
  (⅟(2 : R)) • (CAB + CBAᵀ)

noncomputable def Deff (CAB : Matrix m n R) (CBA : Matrix n m R) : Matrix m n R :=
  (⅟(2 : R)) • (CAB - CBAᵀ)

/-- Theorem 11 -- reciprocal/non-reciprocal decomposition, symmetric half. -/
theorem theorem_11_sym (KA : Matrix m m R) (KB : Matrix n n R)
    (CAB : Matrix m n R) (CBA : Matrix n m R) :
    symPart (Matrix.fromBlocks KA CAB CBA KB) =
      Matrix.fromBlocks (symPart KA) (Ceff CAB CBA) (Ceff CAB CBA)ᵀ (symPart KB) := by
  ext (i | i) (j | j) <;>
    simp [symPart, Ceff, Matrix.fromBlocks, Matrix.transpose_apply, mul_comm] <;> ring

/-- Theorem 11 -- reciprocal/non-reciprocal decomposition, antisymmetric half. -/
theorem theorem_11_antisym (KA : Matrix m m R) (KB : Matrix n n R)
    (CAB : Matrix m n R) (CBA : Matrix n m R) :
    antisymPart (Matrix.fromBlocks KA CAB CBA KB) =
      Matrix.fromBlocks (antisymPart KA) (Deff CAB CBA) (-(Deff CAB CBA)ᵀ) (antisymPart KB) := by
  ext (i | i) (j | j) <;>
    simp [antisymPart, Deff, Matrix.fromBlocks, Matrix.transpose_apply, mul_comm, sub_eq_add_neg]
    <;> ring
