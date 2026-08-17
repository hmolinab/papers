# Paper: A compositional algebra for coherence-unit configurations: closure, entropy balance, and inertia additivity

**"Un álgebra composicional para configuraciones de Unidades de Coherencia: clausura, balance de entropía, y aditividad de inercia" / "A compositional algebra for coherence-unit configurations: closure, entropy balance, and inertia additivity"**
Henry Molina — Independent researcher

Twelve compositional operations found under different names across physics, chemistry, biology
and social systems collapse into five primitives and a single linear-algebra identity — the
Schur block-determinant formula — applied to a configuration object $\Gamma\in M_4(\mathbb R)$.
Eleven theorems follow, including a Haynsworth-inertia extension beyond the positive-definite
regime, a no-privileged-sub-sector result, and an exact reciprocal/non-reciprocal decomposition
(Theorem 11) formalized in Lean 4.

## Files

| File | Description |
|---|---|
| `algebra_composicional_unidades_coherencia_molina2026.md` / `.pdf` | Main paper (Spanish, primary version). |
| `compositional_algebra_of_coherence_units_molina2026.md` / `.pdf` | English translation. |
| `arxiv_zenodo_es.md` | Submission metadata: Zenodo (ready) and arXiv (prepared, not submitted). |
| `lean/CompositionalAlgebra/Theorem11.lean` | Lean 4 formalization of Theorem 11 (reciprocal/non-reciprocal decomposition), closed with no `sorry`. |

## Running the Lean verification

This paper's Lean source lives here but builds against the shared public engine
(`papers/formal_verification/`, one mathlib cache for all public papers — see that
directory's README):

```bash
cd papers/formal_verification
lake build CompositionalAlgebra
```

Then, to confirm no hidden `sorry` (only standard mathlib axioms):

```bash
# via the REPL, or directly in a .lean file:
#print axioms theorem_11_sym
#print axioms theorem_11_antisym
# expected: [propext, Classical.choice, Quot.sound]
```

## Companion work

- Book chapter covering the same core results (Corollary 8.1, Theorem 9, Theorem 11 —
  numbered 7.7.1, 7.8, 7.10 there): `part1/07_compositional_operations.md` (public, Zenodo,
  same program).
- This paper's working notes (proof process, self-audit, step-by-step verification guide) are
  private, not included here by design: `brainstorming/papers/draft_algebra_uoc/` (internal
  only — `cuaderno_trabajo.md`, `guia_estudio_cuaderno_limpio.md`, exploratory material).

## Honesty convention

Same as the rest of the program: no result is marked closed ([D]/[V]) that is not, and no
genuinely open question is forced shut. Four named frontiers and one categorical appendix
([A], work in progress) are documented as open in §13-§14 and Appendix A of the paper itself.
