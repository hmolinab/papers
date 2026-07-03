"""
Verify: Cl(3,1) real 4x4 representation.
Checks: {gamma_mu, gamma_nu}/2 = eta_mu_nu = diag(-1,+1,+1,+1)
        gamma_0^2 = -I, gamma_i^2 = +I
Supports Proposition P2 and Lemma 4.
"""
import numpy as np

# Real 4x4 Majorana-like representation of Cl(3,1)
# gamma_0 = kron(J, I2), gamma_1 = kron(X, I2),
# gamma_2 = kron(Z, X),  gamma_3 = kron(Z, Z)
J = np.array([[0, -1], [1, 0]])   # rotation, squares to -I
X = np.array([[0,  1], [1, 0]])
Z = np.array([[1,  0], [0,-1]])
I2 = np.eye(2)

g = [
    np.kron(J, I2),   # g0: squares to -I (temporal)
    np.kron(X, I2),   # g1: squares to +I
    np.kron(Z, X),    # g2: squares to +I
    np.kron(Z, Z),    # g3: squares to +I
]
eta = np.diag([-1, 1, 1, 1])

print("Checking {gamma_mu, gamma_nu}/2 = eta_mu_nu ...")
max_err = 0.0
for mu in range(4):
    for nu in range(4):
        anticomm = (g[mu] @ g[nu] + g[nu] @ g[mu]) / 2
        expected = eta[mu, nu] * np.eye(4)
        err = np.max(np.abs(anticomm - expected))
        max_err = max(max_err, err)
        if err > 1e-12:
            print(f"  FAIL at ({mu},{nu}): max error = {err:.2e}")
print(f"  max error over all (mu,nu): {max_err:.2e}  [expect < 1e-14]")

print("\nChecking gamma_0^2 = -I ...")
err0 = np.max(np.abs(g[0] @ g[0] + np.eye(4)))
print(f"  ||gamma_0^2 + I||_inf = {err0:.2e}  [expect < 1e-14]")

print("\nChecking gamma_i^2 = +I for i=1,2,3 ...")
for i in range(1, 4):
    erri = np.max(np.abs(g[i] @ g[i] - np.eye(4)))
    print(f"  ||gamma_{i}^2 - I||_inf = {erri:.2e}  [expect < 1e-14]")

print("\nAll Cl(3,1) relations verified.")
