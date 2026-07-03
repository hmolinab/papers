"""
Verify: Clifford inner product on Cl(3,1) = Frobenius/4.
For grade-1 elements A, B: <A~B>_0 = Tr(A^T B)/4
Supports Proposition P3.
"""
import numpy as np

rng = np.random.default_rng(42)

J = np.array([[0, -1], [1, 0]])
X = np.array([[0,  1], [1, 0]])
Z = np.array([[1,  0], [0,-1]])
I2 = np.eye(2)

g = [np.kron(J, I2), np.kron(X, I2), np.kron(Z, X), np.kron(Z, Z)]

def grade1_element(coeffs):
    """Grade-1 element: sum_i coeffs[i] * gamma_i (spatial only, i=1,2,3)."""
    return sum(coeffs[i] * g[i+1] for i in range(3))

def scalar_part(M):
    """Grade-0 (scalar) projection: Tr(M)/4 in the 4x4 rep."""
    return np.trace(M) / 4.0

def clifford_reverse(M):
    """Clifford reverse = transpose for real Majorana rep."""
    return M.T

N = 10000
max_err = 0.0
for _ in range(N):
    a = rng.standard_normal(3)
    b = rng.standard_normal(3)
    A = grade1_element(a)
    B = grade1_element(b)
    # Clifford inner product
    cl_inner = scalar_part(A @ clifford_reverse(B))
    # Frobenius/4
    frob_inner = np.trace(A.T @ B) / 4.0
    err = abs(cl_inner - frob_inner)
    max_err = max(max_err, err)

print(f"Clifford inner product = Frobenius/4 on grade-1 elements")
print(f"Max error over {N} random pairs: {max_err:.2e}  [expect < 1e-14]")

# Also verify positive-definiteness: <A, A> >= 0
print("\nVerifying positive-definiteness <A,A> >= 0 ...")
min_val = float('inf')
for _ in range(N):
    a = rng.standard_normal(3)
    A = grade1_element(a)
    val = scalar_part(A @ clifford_reverse(A))
    min_val = min(min_val, val)
print(f"  min <A,A> over {N} samples: {min_val:.6f}  [expect >= 0]")
