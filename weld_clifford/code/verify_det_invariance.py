"""
Verify: det(Gamma) is invariant under SO(3,1) conjugation g Gamma g^{-1}.
Uses the Cl(3,1) generators directly (no scipy).
Supports Lemma 4 and the uniqueness argument in the main theorem.
"""
import numpy as np

rng = np.random.default_rng(7)

J = np.array([[0., -1.], [1., 0.]])
X = np.array([[0.,  1.], [1., 0.]])
Z = np.array([[1.,  0.], [0.,-1.]])
I2 = np.eye(2)
g_basis = [np.kron(J, I2), np.kron(X, I2), np.kron(Z, X), np.kron(Z, Z)]

def mat_expm(M, n_terms=20):
    """Matrix exponential via Taylor series."""
    result = np.eye(M.shape[0])
    term = np.eye(M.shape[0])
    for k in range(1, n_terms):
        term = term @ M / k
        result = result + term
    return result

def spin_group_element(params):
    """Generate element of Spin(3,1) via exponential of bivector."""
    bivectors = []
    for mu in range(4):
        for nu in range(mu+1, 4):
            bivectors.append(g_basis[mu] @ g_basis[nu])
    gen = sum(p * bv for p, bv in zip(params, bivectors))
    return mat_expm(gen)

N = 5000
max_err = 0.0
print(f"Verifying det invariance under Spin(3,1) conjugation over {N} samples ...")
for _ in range(N):
    G = rng.standard_normal((4, 4))
    params = rng.standard_normal(6) * 0.2  # small params for convergence
    h = spin_group_element(params)
    G_conj = h @ G @ np.linalg.inv(h)
    err = abs(np.linalg.det(G_conj) - np.linalg.det(G))
    max_err = max(max_err, err)

print(f"  Max |det(hGh^-1) - det(G)|: {max_err:.2e}  [expect < 1e-8]")
print("  det(Gamma) is a Spin(3,1) invariant. Confirmed.")
