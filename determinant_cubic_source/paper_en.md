# The determinant as the source of the cubic term: normal-form reduction in a matrix gradient flow

**Henry Molina**
Independent Researcher
hmolinab@unal.edu.co
DOI: 10.5281/zenodo.20752208

*Self-contained manuscript in the language of dynamical systems; it does not require any external
framework. The Spanish version is in `paper_es.md`. Reproducible verification scripts, one per
numerical statement (§7), are in `code/`.*

---

## Abstract

We consider the gradient flow \(\dot\Gamma=-\nabla P(\Gamma;\mu)\) on the real \(4\times4\) matrices,
with potential \(P(\Gamma)=\|\Gamma\|^2+\mu\det\Gamma+\beta\|\Gamma\|^4\) (plus an optional sextic
regularizer), and its damped second-order counterpart \(\ddot\Gamma+\gamma\dot\Gamma+\nabla P=0\).
Near a degeneration of the Hessian —a simple soft mode— center-manifold reduction yields the local
normal forms of bifurcation theory. The cubic coefficient of the reduced flow comes from the
determinant through its cofactor matrix, the only anisotropic nonlinearity of the field; it is the
sole source of the cubic when the soft mode is orthogonal to \(\Gamma_*\). We classify the accessible
organizing centers: fold and pitchfork in codimension 1, the cusp in the gradient sector, and
Bogdanov–Takens in codimension 2, whose existence is topologically obstructed in the gradient limit
and requires lifting the system to the second-order (inertial) flow. A no-Hopf lemma makes the
dichotomy precise and metric-gradient invariant: while the symmetric (dissipative) sector governs,
only steady bifurcations occur, and every oscillatory regime is gated by the antisymmetric reactive
sector. The homoclinic orbit closes the
Bogdanov–Takens portrait, and the non-gradient part of the field, which carries the rotation,
numerically sustains a Shilnikov-type chaotic regime. The analytical results are accompanied by
simulations that verify the critical scalings: the Kramers law, a pseudo-arclength continuation
through the fold, the \(3/2\) law of the cusp, and the Lyapunov exponent of the chaotic regime.

**Keywords:** matrix gradient flow, center-manifold reduction, normal forms, cofactor matrix, cusp,
Bogdanov–Takens, Shilnikov chaos.

---

## 1. Introduction

Bifurcation theory organizes the qualitative changes of a dynamical system around a catalogue of
normal forms: the fold \(\dot\xi=\lambda-\xi^2\), the pitchfork \(\dot\xi=\lambda\xi-\xi^3\), the
cusp, Hopf, Bogdanov–Takens (Guckenheimer–Holmes 1983; Kuznetsov 2004). We study the geometric role
of the determinant in selecting the normal form for matrix-valued gradient flows when the Hessian
degenerates along a soft mode.

Under hypotheses (H1)–(H4), the determinant generates the cubic term of the local reduction. Its
gradient is the cofactor matrix \(\mathrm C(\Gamma)=\operatorname{cof}(\Gamma)\), multilinear in the
entries and anisotropic, whereas the norm terms \(\|\Gamma\|^{2k}\) are isotropic. Upon projection
onto the center manifold of a soft mode, this anisotropy survives as the cubic coefficient of the
normal form, and persists even when the norm terms vanish, i.e. when the soft mode is orthogonal to
\(\Gamma_*\).

We prove a codimension-1 reduction theorem with explicit coefficients (§3–§4); we classify the two
codimension-2 organizing centers, cusp and Bogdanov–Takens, and show that the latter requires the
second-order dynamics (§5); we analyze the loss of gradient structure and its relation to chaos (§6);
and we support each result with reproducible numerical verification (§7).

---

## 2. The system

Let \(V=M_4(\mathbb R)\cong\mathbb R^{16}\) with the Frobenius inner product
\(\langle X,Y\rangle=\operatorname{tr}(X^\top Y)\). We take
$$
P(\Gamma;\mu,J)=\|\Gamma\|^2+\mu\det\Gamma+\beta\|\Gamma\|^4+b_6\|\Gamma\|^6-\langle J,\Gamma\rangle,
\qquad \beta\ge0,\ b_6\ge0,
$$
where \(\mu\in\mathbb R\) is the control parameter and \(J\in M_4(\mathbb R)\) an external field. The
sextic \(b_6\) only bounds the branches globally and plays no role in the local statements. The
field-free potential (\(J=0\)) depends only on \(\|\Gamma\|^2\) and \(\det\Gamma\), both invariant
under the bilateral orthogonal action \(\Gamma\mapsto U\Gamma V^\top\) with \(U,V\in O(4)\) (the same
action as the singular-value decomposition, which reappears in §4). This large isotropy makes its
degeneracies occur in families rather than in isolation. A generic field \(J\) breaks it and places
the equilibrium in a configuration where the soft mode of the bifurcation is simple (hypothesis H2):
the linear term \(\langle J,\Gamma\rangle\) intersects the \(O(4)\times O(4)\) orbits transversally
(Thom transversality), lifting the degeneracy imposed by the continuous symmetry and leaving a single
zero eigenvalue. Since \(J\) enters linearly, it shifts the equilibrium but does not alter the
Hessian. The gradient flow is
$$
\dot\Gamma=-\nabla P,\qquad \nabla P=2\Gamma+\mu\,\mathrm C(\Gamma)+\big(4\beta\|\Gamma\|^2+6b_6\|\Gamma\|^4\big)\Gamma,
$$
with \(\mathrm C(\Gamma)=\operatorname{cof}(\Gamma)=\partial\det\Gamma/\partial\Gamma\). The Hessian
\(H(\Gamma)=D^2P\) is symmetric since the field is a gradient. We also consider the damped
second-order version
$$
\ddot\Gamma+\gamma\dot\Gamma+\nabla P=0,\qquad \gamma\in\mathbb R,
$$
whose overdamped limit \(\gamma\to\infty\) recovers the gradient flow. The system is deterministic;
only to probe the basins of attraction and the escape rates (§7) do we resort, auxiliarily, to the
stochastic Langevin extension \(\dot\Gamma=-\nabla P+\sqrt{2D}\,\eta(t)\), with \(\eta\) matrix white
noise and \(D>0\).

**Remark 2.1 (scope).** Parts 1 and 2 of Theorem 1 are the center-manifold / Lyapunov–Schmidt
reduction for any real-analytic \(P\) under (H1)–(H2), and do not depend on the specific form of
\(P\); only the identification of the cubic coefficient (§3, item 3) and of the effective quartic use
the particular potential. The construction requires a positive-definite inner product —the Frobenius
one— which bounds \(P\) from below and fixes the gradient structure, and is independent of any later
metric reinterpretation of the entries of \(\Gamma\). A Monte Carlo sampling over the coefficients
\((\beta,b_6)\) and the field \(J\) confirms that the simple soft mode and the contribution of the
determinant persist, indicating structural stability of the codimension-1 reduction.

---

## 3. Main result (codimension 1)

We assume at the point \((\Gamma_*,\mu_*)\) the following hypotheses:

- (H1) \(\nabla P(\Gamma_*,\mu_*)=0\);
- (H2) \(H_*=H(\Gamma_*)\) has a simple zero eigenvalue, with unit eigenvector \(V\), and the rest of
  the spectrum bounded away from zero;
- (H3) transversality: \(\tau:=\langle V,\mathrm C(\Gamma_*)\rangle\neq0\), so the control \(\mu\)
  moves the soft mode;
- (H4) nondegeneracy: \(a_3:=D^3P(\Gamma_*)[V,V,V]\neq0\); or else a \(\mathbb Z_2\) involution forces
  \(a_3=0\) and then \(a_4^{\mathrm{eff}}\neq0\).

**Theorem 1 (reduction \(\Gamma\to\xi\)).** *Under (H1)–(H2) there exists, in a neighborhood of
\((\Gamma_*,\mu_*)\), a unique, smooth one-dimensional center manifold
\(\Gamma=\Gamma_*+\xi V+h(\xi,\mu)\) with \(h\in V^\perp\) and \(h=O(\xi^2,\xi\tilde\mu)\), on which the
flow is gradient, \(\dot\xi=-\partial_\xi\Phi(\xi,\mu)\). If moreover (H3)–(H4) hold:*

1. *if \(a_3:=D^3P(\Gamma_*)[V,V,V]\neq0\), the reduced form is the fold
   \(\dot\xi=\alpha-\tfrac12 a_3\xi^2\), with \(\alpha=-\tau(\mu-\mu_*)\) and \(\tau=\langle V,\mathrm C(\Gamma_*)\rangle\);*
2. *if a \(\mathbb Z_2\) involution forces \(a_3=0\), the reduced form is the pitchfork
   \(\dot\xi=-a_2'\xi-\tfrac16 a_4^{\mathrm{eff}}\xi^3\);*
3. *\(a_3=\mu_*\,D^3\!\det(\Gamma_*)[V,V,V]+24\beta\langle\Gamma_*,V\rangle\); within the space of
   invariants of the potential (1), the first term is the sole source of the cubic when
   \(V\perp\Gamma_*\) (a degree-three invariant such as \(\operatorname{tr}\Gamma^3\), absent in (1),
   would also contribute);*
4. *\(a_4^{\mathrm{eff}}=D^4P[V^{\otimes4}]-3\,\langle D^3P[V,V],(H_*|_{V^\perp})^{-1}D^3P[V,V]\rangle\),
   whose sign depends on the spectrum of \(H_*|_{V^\perp}\) (positive-definite on the stable branch,
   indefinite at a saddle).*

In the symmetric sector, \(a_4^{\mathrm{eff}}\) changes sign at \(\mu=16\beta\), the line separating
the single-equilibrium regime from the three-equilibrium one (Figure 1).

![**Figure 1.** Codimension-1 bifurcations: fold \(\dot\xi=\alpha-\xi^2\) and pitchfork
\(\dot\xi=\lambda\xi-\xi^3\). Stable branches in blue, unstable in dashed red. The cubic term comes
from \(\det\Gamma\).](figs_en/fig1_codim1.png)

---

## 4. Proof (Lyapunov–Schmidt)

The reduction is the Lyapunov–Schmidt one for gradient fields (Carr 1981; Golubitsky–Schaeffer 1985).
Write \(\Gamma=\Gamma_*+\xi V+W\) with \(W\in V^\perp\) and \(\mu=\mu_*+\nu\), and let \(Q\) be the
orthogonal projection onto \(V^\perp=\operatorname{ran}H_*\). The equation \(\nabla P=0\) splits into
its components in \(V^\perp\) and in \(V\).

The component in \(V^\perp\), \(Q\nabla P=0\), is solved by the implicit function theorem
—\(H_*|_{V^\perp}\) is invertible by (H2)— and yields the slaving manifold \(W=h(\xi,\mu)\), with
\(h(0,\mu_*)=0\), \(\partial_\xi h(0,\mu_*)=0\) and
\(\partial_\xi^2 h(0)=-(H_*|_{V^\perp})^{-1}\,Q\,D^3P(\Gamma_*)[V,V]\) upon differentiating twice.
Substituting \(h\) into the remaining component gives the bifurcation equation
\(g(\xi,\mu)=\langle V,\nabla P\rangle\), which —since the field is a gradient— equals
\(\partial_\xi\Phi\), \(\Phi=P|_{\text{center mfld}}\); the reduced flow \(\dot\xi=-g\) inherits the
gradient structure. Writing \(a_k=\partial_\xi^k\Phi(0,\mu_*)\):

- \(\partial_\nu a_1|_0=\langle V,\partial_\mu\nabla P\rangle=\langle V,\mathrm C(\Gamma_*)\rangle=\tau\)
  (the second term \(\langle V,H_*\partial_\mu h\rangle\) vanishes because \(H_*\partial_\mu h\perp V\));
- \(a_2(\mu_*)=\langle V,H_*V\rangle=0\) (soft mode);
- \(a_3=\langle V,D^3P[V,V]\rangle=D^3P(\Gamma_*)[V,V,V]\); the slaving term
  \(\langle V,H_*\partial_\xi^2 h\rangle\) vanishes since it is \(\perp V\), so the cubic receives no
  correction.

To identify \(a_3\) one decomposes \(D^3P\) term by term. The \(\|\Gamma\|^2\) term is quadratic and
does not contribute. For the quartic norm, with \(\|V\|=1\),
\(D^3(\|\Gamma\|^4)[V,V,V]=24\,\langle\Gamma_*,V\rangle\). For the determinant, which is degree \(4\)
in \(4\times4\), \(D^3\det\) is linear and \(D^3(\mu\det\Gamma)[V,V,V]=\mu_*\,D^3\!\det(\Gamma_*)[V,V,V]\).
Summing,
\[
a_3=\mu_*\,D^3\!\det(\Gamma_*)[V,V,V]+24\beta\,\langle\Gamma_*,V\rangle,
\]
which is item 3. The first term is generically nonzero even when \(\langle\Gamma_*,V\rangle=0\): there
the norm is silent and, within the invariants of (1), the determinant is the sole source of the cubic.
This has a direct geometric reading in terms of the singular values of \(\Gamma\). The determinant is
their product, \(\det\Gamma=\prod_i\sigma_i\) (up to sign), while the norm is their sum of squares,
\(\|\Gamma\|^2=\sum_i\sigma_i^2\). The product couples the four singular values irreducibly and
supplies the anisotropic part of the cubic; the sum is isotropic and contributes only through
\(\langle\Gamma_*,V\rangle\). The effective quartic is obtained by differentiating \(g\) once more and
substituting \(\partial_\xi^2 h\), giving item 4; the sign of the correction is fixed by the
definiteness of \(H_*|_{V^\perp}\). The fold/pitchfork classification then follows from Sotomayor's
conditions (Sotomayor 1973; Kuznetsov 2004): with \(a_1(\mu_*)=a_2(\mu_*)=0\) and \(a_3\neq0\) one
gets the fold \(\dot\xi=\alpha-\tfrac12 a_3\xi^2\); if a \(\mathbb Z_2\) symmetry annihilates \(a_3\)
(and \(\langle\Gamma_*,V\rangle\)), the leading nontrivial term is the quartic and one gets the
pitchfork. \(\square\)

---

## 5. Codimension-2 organizing centers

**Theorem 2 (cusp, \(A_3\)).** *The point \(a_2=a_3=0\) with \(a_4^{\mathrm{eff}}\neq0\) is a cusp, the
universal unfolding of the pitchfork (Thom 1975; Golubitsky–Schaeffer 1985). In this system \(a_3\)
changes sign, because the determinant and norm contributions compete, so the point exists; adding
\(a_2=0\) fixes it. A two-parameter family \((\mu,s)\) —control and field amplitude— unfolds it
versally, with \(\partial(a_1,a_2)/\partial(\mu,s)\) nonsingular. The three-equilibrium window has
width \(\propto(-a_2)^{3/2}\)* (Figure 2).

![**Figure 2.** The cusp \(A_3\) in the unfolding plane \((a_1,a_2)\). Inside the semicubical wedge
\(4a_2^3+27a_1^2\le0\) there are three equilibria; outside, one. The inset shows the \(3/2\)
law.](figs_en/fig2_cusp.png)

**Lemma 1 (no Hopf in the (metric-)gradient flow).** *The Jacobian of \(\dot\Gamma=-\nabla P\) at an
equilibrium is \(-H_*\), with \(H_*=D^2P\) symmetric; its spectrum is real, so no complex pair can
cross the imaginary axis and no Hopf bifurcation occurs. This persists for the metric-gradient flow
\(\dot\Gamma=-G^{-1}\nabla P\) with any \(G\succ0\) symmetric: the linearization \(-G^{-1}H_*\) is
similar to the symmetric \(-G^{-1/2}H_*G^{-1/2}\), hence real. Consequently, while \(G\) is positive
definite the soft mode admits only steady bifurcations; an oscillatory (Hopf) instability requires
breaking the gradient form — either \(G\) losing positive definiteness or a genuinely non-gradient
reactive term, supplied here by the antisymmetric sector \(\Gamma_a\).*

**Theorem 3 (Bogdanov–Takens).** *In the gradient flow this bifurcation is obstructed (Lemma 1): the
Jacobian \(-H_*\) is symmetric, hence diagonalizable, and a double zero eigenvalue would have geometric
multiplicity 2 rather than a Jordan block. Releasing the Jordan block requires a non-gradient field;
within the dissipative phenomenology we study, this is achieved by lifting the system to the
second-order equation. There the linearization
\(\big(\begin{smallmatrix}0&I\\-H_*&-\gamma I\end{smallmatrix}\big)\) has, on the soft mode,
eigenvalues \(\{0,-\gamma\}\), which at \(\gamma=0\) collapse to a double zero with a Jordan block.
The reduction is \(\ddot\xi+\gamma(\xi)\dot\xi+(a_1+c\,\xi^2)=0\) with \(c=\tfrac12 a_3\); with
state-dependent damping \(\gamma(\xi)=\gamma_0+\gamma_1\xi\), the saddle-node (the fold), Hopf
(\(\gamma_0=-\gamma_1\xi_*\)) and homoclinic curves emanate from the BT point (Bogdanov 1975;
Takens 1974).*

The saddle-node branch of Bogdanov–Takens coincides with the fold of Theorem 1, so both codimension-2
centers are degeneracies of the same soft mode. The BT point marks the boundary between the overdamped
regime —gradient, with fold and cusp— and the oscillatory one (Figure 3).

**Remark (spectral classification).** *Lemma 1 organizes the catalogue by the spectrum of the
degeneration. A simple real eigenvalue crossing zero gives a **steady** bifurcation —fold, pitchfork,
or cusp, with the cubic sourced by the determinant (Theorems 1–2). An **oscillatory** regime —Hopf,
Bogdanov–Takens, Shilnikov— requires a complex pair crossing the axis, which by Lemma 1 is impossible
while the symmetric (dissipative) sector governs alone and demands the non-gradient sector
\(\Gamma_a\) (§6). The type of bifurcation is thus read off the critical spectrum: real \(\Rightarrow\)
steady; complex \(\Rightarrow\) oscillatory, gated by \(\Gamma_a\).*

![**Figure 3.** Bogdanov–Takens unfolding in \((\mu-\mu_f,\gamma_0)\): the saddle-node (the fold),
Hopf and homoclinic curves emanate from BT; the limit cycle lives between the Hopf and homoclinic
curves.](figs_en/fig3_bogdanov_takens.png)

---

## 6. Non-gradient extension and chaos phenomenology

**Proposition 4 (energy obstruction).** *The second-order equation with uniform \(\gamma\ge0\) admits
\(E=\tfrac12\|\dot\Gamma\|^2+P\) as a Lyapunov function, since
\(\dot E=-\gamma\|\dot\Gamma\|^2\le0\); every trajectory relaxes to an equilibrium, so the dissipative
gradient system admits no sustained chaos.*

Chaos therefore cannot emerge from the mere dissipation of the coupled degrees of freedom: it requires
an energy input (\(\gamma_{\mathrm{eff}}\le0\) in some region) paired with the asymmetry of the
reactive sector \(\Gamma_a\), which breaks the symmetry of the Hessian and introduces the rotation
(\(\operatorname{Im}\lambda\neq0\)). That antisymmetric, non-gradient part also supplies the third
dimension that Poincaré–Bendixson requires. Coupling it with active damping, the cubic nonlinearity
induced by the determinant produces a jerk equation with a saddle-focus equilibrium; integrating it,
one observes an attractor with positive Lyapunov exponent (\(\lambda\approx0.055\)) and a limit cycle
that ends in a homoclinic with logarithmically divergent period (Figure 4). The reduction of the
second-order flow in \(16+16\) dimensions to this jerk equation is not proved here; the evidence is
numerical, and we state it as a conjecture.

**Conjecture 1.** *In the inertial extension coupled with the antisymmetric part of the field, the
cubic nonlinearity induced by the determinant suffices to produce a homoclinic connection to a
saddle-focus equilibrium satisfying the Shilnikov condition
(\(|\lambda_{\mathrm{real}}|>|\operatorname{Re}\lambda_{\mathrm{compl}}|\); Shilnikov 1965), and with
it a chaotic attractor. The analytical unfolding of this global bifurcation remains open.*

![**Figure 4.** (a) Shilnikov-type chaotic attractor (saddle-focus) of the quadratic jerk equation.
(b) Sensitive dependence: the separation of two trajectories grows as \(e^{\lambda t}\) with
\(\lambda\approx0.055\).](figs_en/fig4_chaos.png)

---

## 7. Numerical verification

Each statement is accompanied by a self-contained Python (NumPy/SciPy) script that verifies it
reproducibly. Degeneration points are located by solving \(\nabla P=0\) and the soft-mode condition
\(\lambda_{\min}(H)=0\) simultaneously; normal-form coefficients are extracted by polynomial fitting of
\(P\) restricted to the relevant directions; Lyapunov exponents are computed by the Benettin method
(Benettin et al. 1980); escape rates are compared with the Kramers law (Hänggi et al. 1990); and
equilibrium branches are followed by pseudo-arclength continuation (Doedel 1981). The table summarizes
object, result and script.

| # | object | result | script |
|---|--------|--------|--------|
| 1 | fold/pitchfork as invariant objects; Var\(\sim1/k\); Monte Carlo \(10^3\) | genuine critical pitchfork \(k_2=0\); \(k\cdot\)Var\(\approx\)const; sorting of \(10^3\) matrices at 100% | `code/pieza1_bifurcaciones_rigor.py` |
| 2 | exact reduction (invariant ray) | \(\nabla P\parallel\Gamma\); \(P_{\mathrm{red}}\) pitchfork; threshold \(\mu=16\beta\) | `code/pieza1_reduccion_normal_forms.py` |
| 3 | generic center manifold | \(B=2\sum g_i^2/\omega_i-b\); full flow = reduced (not the naive one) | `code/pieza1_centro_manifold_generico.py` |
| 4 | Kramers + continuation | \(\ln\langle\tau\rangle=0.904\,\Delta U/D+1.78\), \(R^2=0.989\); fold traced to \(\mu\approx2.04\) | `code/pieza1_kramers_continuacion.py` |
| 5 | Theorem 1 in 16-dim | simple zero; \(\tau=-12.84\); \(a_3=5.09\) (det \(-11.67\)); real saddle-node | `code/pieza1_teorema_4x4.py` |
| 6 | Theorem 2 (cusp) | \(a_2,a_3\sim10^{-11}\); versal Jacobian \(=1.30\); \(3/2\) law: \(\propto(-a_2)^{1.503}\), \(R^2=1.0\) | `code/pieza1_cuspide_codim2.py` |
| 7 | Theorem 3 (BT) | Jordan block; Hopf curve; limit cycle | `code/pieza1_bogdanov_takens.py` |
| 8 | homoclinic + chaos | \(T=0.738(-\ln\Delta)+2.08\), \(R^2=1.0\); Lyapunov \(\lambda\approx0.055\) (Sprott) | `code/pieza1_homoclinica_caos.py` |
| 9 | energy obstruction + chaos from the EOM | \(\gamma\ge0\Rightarrow E\) Lyapunov \(\Rightarrow\) relaxes; active damping \(\Rightarrow\) limit cycle (2 modes) | `code/pieza1_caos_EOM_2modos.py` |
| 10 | robustness / structural stability | varying \((a,\beta,b_6,J)\): 40/40 keep simple soft mode, fold and determinant contribution | `code/pieza1_robustez_teorema.py` |

---

## 8. Discussion

The central content is that, when the dominant nonlinearity of a matrix gradient flow is the
determinant, the geometry of the matrix —through its cofactor— determines the type of bifurcation of
the soft mode. The sequence fold → cusp → Bogdanov–Takens → chaos is traversed by degenerating a
single mode and adding, at each step, a structure: the determinant supplies the cubic that
distinguishes fold from pitchfork; the damping \(\gamma\) supplies the second Bogdanov–Takens
parameter upon passing to second order; and the non-gradient part supplies the rotation that opens the
door to chaos. The determinant enters as the invariant that generates the cubic, not as a stability
indicator: linear stability is fixed by the spectrum of the symmetric Hessian, while \(\det\Gamma\)
encodes orientation and rank. (Scope note: we do not claim this Lagrangian is *universal* or privileged; it is one **general** potential within a broad class for which the determinant generates the cubic — Remark 2.1. The word "universal" is used here only in the technical sense of the *universal unfolding* of normal forms.)

Three lines remain open. First, the rigorous reduction of the second-order flow in \(16+16\)
dimensions to the reactive jerk equation; the non-gradient model in §6 is illustrative, not an exact
reduction. Second, the full unfolding of the chaotic scenario —cascades, the Shilnikov–Hopf
connection— in the non-gradient sector. Third, the extension to \(M_n(\mathbb R)\) with \(n>4\), where
\(\det\) has degree \(n\) and supplies higher-order nonlinearities.

---

## References

1. J. Carr, *Applications of Centre Manifold Theory*, Applied Mathematical Sciences 35, Springer, 1981.
2. J. Guckenheimer, P. Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields*, Applied Mathematical Sciences 42, Springer, 1983.
3. Yu. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd ed., Applied Mathematical Sciences 112, Springer, 2004.
4. M. Golubitsky, D. G. Schaeffer, *Singularities and Groups in Bifurcation Theory*, vol. I, Applied Mathematical Sciences 51, Springer, 1985.
5. J. Sotomayor, *Generic bifurcations of dynamical systems*, in *Dynamical Systems* (M. M. Peixoto, ed.), Academic Press, 1973, pp. 561–582.
6. R. I. Bogdanov, *Versal deformations of a singular point of a vector field on the plane in the case of zero eigenvalues*, Selecta Math. Soviet. 1 (1981) 389–421 (orig. 1975).
7. F. Takens, *Forced oscillations and bifurcations*, Comm. Math. Inst. Rijksuniversiteit Utrecht 3 (1974) 1–59.
8. R. Thom, *Structural Stability and Morphogenesis*, W. A. Benjamin, 1975.
9. L. P. Shilnikov, *A case of the existence of a countable number of periodic motions*, Soviet Math. Dokl. 6 (1965) 163–166.
10. P. Hänggi, P. Talkner, M. Borkovec, *Reaction-rate theory: fifty years after Kramers*, Rev. Mod. Phys. 62 (1990) 251–341.
11. J. C. Sprott, *Simplest dissipative chaotic flow*, Phys. Lett. A 228 (1997) 271–274.
12. E. J. Doedel, *AUTO: a program for the automatic bifurcation analysis of autonomous systems*, Congr. Numer. 30 (1981) 265–284.
13. G. Benettin, L. Galgani, A. Giorgilli, J.-M. Strelcyn, *Lyapunov characteristic exponents for smooth dynamical systems; a method for computing all of them*, Meccanica 15 (1980) 9–30.
