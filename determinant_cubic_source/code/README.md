# Verification scripts

Self-contained Python scripts that reproduce the numerical statements of the paper
*The determinant as the source of the cubic term: normal-form reduction in a matrix gradient flow*
(`../paper_en.md`, `../paper_es.md`). Each script is standalone and prints its own checks.

## Requirements

- Python ≥ 3.9
- NumPy, SciPy, Matplotlib (see `requirements.txt`)

```bash
pip install -r requirements.txt
python pieza1_teorema_4x4.py      # run any script directly
```

Random seeds are fixed inside each script, so results are deterministic.

## Map to the paper (Table §7)

| Row | Script | Verifies |
|-----|--------|----------|
| 1 | `pieza1_bifurcaciones_rigor.py` | fold/pitchfork as invariant objects; Var∼1/k; Monte Carlo over 10³ matrices |
| 2 | `pieza1_reduccion_normal_forms.py` | exact reduction on the invariant ray; threshold μ=16β |
| 3 | `pieza1_centro_manifold_generico.py` | generic center manifold; B = 2Σgᵢ²/ωᵢ − b |
| 4 | `pieza1_kramers_continuacion.py` | Kramers escape law + pseudo-arclength continuation through the fold |
| 5 | `pieza1_teorema_4x4.py` | Theorem 1 in 16-dim: simple zero, τ, a₃, real saddle-node |
| 6 | `pieza1_cuspide_codim2.py` | Theorem 2 (cusp): versal unfolding + 3/2 law |
| 7 | `pieza1_bogdanov_takens.py` | Theorem 3 (Bogdanov–Takens): Jordan block, Hopf curve, limit cycle |
| 8 | `pieza1_homoclinica_caos.py` | homoclinic (period divergence) + Shilnikov chaos (Lyapunov ≈ 0.055) |
| 9 | `pieza1_caos_EOM_2modos.py` | energy obstruction (Lyapunov) + active-damping limit cycle (2 modes) |
| 10 | `pieza1_robustez_teorema.py` | structural stability under random (a, β, b₆, J) |

## Figures

- `pieza1_figuras_paper.py` → `../figs/` (Spanish labels, used by `paper_es.md`)
- `pieza1_figuras_paper_en.py` → `../figs_en/` (English labels, used by `paper_en.md`)
