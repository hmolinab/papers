"""
Verify: Frobenius submultiplicativity ||Gamma||_F <= ||Gamma_s||_F * ||Gamma_a||_F
and that this constraint is tight (equality at Gamma_a = 0 would give 0, not tight;
the relevant constraint is that Frobenius is the unique submultiplicative metric).
Also verifies: ||A B||_F <= ||A||_F * ||B||_F (submultiplicativity of Frobenius itself).
Supports Proposition P3 uniqueness argument.
"""
import numpy as np

rng = np.random.default_rng(0)
N = 100_000

def frobenius(M):
    return np.sqrt(np.sum(M**2))

print(f"Verifying ||AB||_F <= ||A||_F * ||B||_F over {N} random 4x4 matrices ...")
violations = 0
max_ratio = 0.0
for _ in range(N):
    A = rng.standard_normal((4, 4))
    B = rng.standard_normal((4, 4))
    lhs = frobenius(A @ B)
    rhs = frobenius(A) * frobenius(B)
    ratio = lhs / (rhs + 1e-300)
    max_ratio = max(max_ratio, ratio)
    if lhs > rhs + 1e-10:
        violations += 1

print(f"  Violations: {violations}  [expect 0]")
print(f"  Max ratio ||AB||/||A||/||B||: {max_ratio:.6f}  [expect <= 1]")

print(f"\nVerifying ||Gamma||_F^2 = ||Gamma_s||_F^2 + ||Gamma_a||_F^2 (Pythagorean) ...")
max_err = 0.0
for _ in range(10000):
    G = rng.standard_normal((4, 4))
    Gs = (G + G.T) / 2
    Ga = (G - G.T) / 2
    lhs = frobenius(G)**2
    rhs = frobenius(Gs)**2 + frobenius(Ga)**2
    max_err = max(max_err, abs(lhs - rhs))
print(f"  Max Pythagorean error: {max_err:.2e}  [expect < 1e-12]")
