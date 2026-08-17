# Paper: Spacetime Algebra as a Theorem

**"Spacetime Algebra as a Theorem: Deriving Cl(3,1) from the Structure of a Dynamical Unit"**  
Henry Molina — Independent researcher

## Files

| File | Description |
|---|---|
| `paper_en.md` | Main paper (English) |
| `code/verify_cl31.py` | Verifies Cl(3,1) real 4×4 representation (P2, Lemma 4) |
| `code/verify_clifford_metric.py` | Verifies Clifford inner product = Frobenius/4 (P3) |
| `code/verify_frobenius.py` | Verifies Frobenius submultiplicativity + Pythagorean (P3) |
| `code/verify_det_invariance.py` | Verifies det(Γ) invariant under Spin(3,1) (Theorem) |

## Running the verification

```bash
cd code
python verify_cl31.py
python verify_clifford_metric.py
python verify_frobenius.py
python verify_det_invariance.py
```

Requirements: `numpy`. No scipy needed.

## Companion paper

Molina, H. (2024a). The determinant as an orientation invariant and the source of the cubic term in
equivariant matrix gradient flows. DOI: 10.5281/zenodo.20752208

## Working notes

Full formal derivation with calculation history:
`brainstorming/unification/release/fundamentos_gamma_teorema.md`

Book-grade clean version:
`part1/appendix_weld.md`
