# Spacetime Algebra as a Theorem: Deriving Cl(3,1) from the Structure of a Dynamical Unit

Henry Molina  
Independent researcher, Bogotá, Colombia  
henrymolina@gmail.com

Self-contained manuscript; requires no external framework beyond standard linear algebra and Clifford algebra
conventions. Numerical verifications referenced in §7 are in `code/` (companion to this file).

---

## Abstract

We exhibit a derivation of the real Clifford algebra $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ from two
structural axioms about the minimal description of any operative dynamical unit. The first axiom (A1) asserts
that such a unit is characterized by four intrinsic attributes: a scalar $S$ (identity), and three
vectors $\mathbf{A}$, $\mathbf{I}$, $\mathbf{R}$ (agency, impulse, relation). The second axiom (A2) asserts
that the dynamics is governed by the geometric product of those attributes. From these two axioms — without
postulating a spacetime metric, a Lagrangian, or a background geometry — we derive, via the Eckmann–Hurwitz
theorem and the symbol of the wave operator, that the configuration object of the unit is necessarily an
element of $M_4(\mathbb{R}) = \mathrm{Cl}_{3,1}$, equipped with Lorentzian signature $(3,1)$. Three closing
propositions establish that orthonormality of the attribute frame is gauge-redundant (P1), that the temporal
generator is the evolution operator of the equation of motion (P2), and that the Frobenius metric is the
unique Clifford inner product forced by the geometric product (P3). The result promotes the Clifford algebra
of spacetime from a geometric postulate to a structural theorem. Classical mechanics and free electrodynamics
appear as limiting cases.

**Keywords:** Clifford algebra, geometric algebra, Hurwitz theorem, spacetime signature, dynamical systems,
matrix normal form, Frobenius metric.

---

## 1. Introduction

The Clifford algebra $\mathrm{Cl}_{3,1}$ — equivalently, the spacetime algebra (STA) of Hestenes (1966) — is
the standard algebraic scaffolding for special relativity and Dirac theory. Its standard motivation is
geometric: one postulates a Minkowski spacetime with signature $(3,1)$ and then constructs the associated
Clifford algebra. The question we address is different: *is the Lorentzian signature a theorem, rather than a
postulate, if one asks what algebraic structure a self-describing dynamical unit must have?*

We show that the answer is yes, under two minimal axioms about the attribute structure and dynamics of such a
unit. The derivation does not require spacetime as an input; the signature emerges from the symbol of the
equation of motion that the unit must satisfy.

This paper is part of a larger program — the Gamma Space Framework (GSF) — whose central object is a real
$4\times4$ configuration matrix $\Gamma \in M_4(\mathbb{R})$. The present paper establishes the algebraic
foundation: that $\Gamma$ is an element of $\mathrm{Cl}_{3,1}$, not by postulate but by necessity. The
companion paper (Molina 2024a) establishes the dynamical result: that the determinant of $\Gamma$ is the
source of the cubic term in the soft-mode reduction of the matrix gradient flow.

**Relation to the geometric algebra literature.** The spacetime algebra program (Hestenes 1966, 1986;
Doran and Lasenby 2003) is the closest antecedent. That program takes Minkowski spacetime as given and
develops physics in terms of $\mathrm{Cl}_{1,3}$ (one time, three space — Hestenes' convention). The
signature choice is not merely a convention: $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$ (quaternionic),
whereas $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ (real). These are non-isomorphic as real algebras. The
present derivation forces $\mathrm{Cl}_{3,1}$ — not $\mathrm{Cl}_{1,3}$ — because we require $\Gamma$ to be
a real matrix (dissipation and gradient flows are real processes); this distinguishes the two conventions at
the algebraic level. The derivation does not compete with the spacetime algebra program; it identifies which
real algebra is forced by the structure of any evolving dynamical unit, and explains why that program works.

**Plan.** §2 states the two axioms. §3 derives the four lemmas. §4 states and proves the main theorem. §5
establishes the three closing propositions. §6 illustrates with two physical limits (Newton and Maxwell). §7
gives numerical verification of key steps. §8 discusses scope, related work, and open problems.

---

## 2. Axioms

We consider an **operative dynamical unit** (ODU): an entity that (i) exists as a coherent whole distinct
from its environment, (ii) acts upon its environment, (iii) has an intrinsic drive, and (iv) is embedded
in a relational context. No further phenomenological content is assumed.

**Axiom A1 (SAIR attribute structure).** Any ODU is completely described at the structural level by four
intrinsic attributes:
- $S \in \mathbb{R}$ (Singularity, grade 0 — identity / self-measure)
- $\mathbf{A}, \mathbf{I}, \mathbf{R} \in \mathbb{R}^d$ (Agency, Impulse, Relation — grade-1 vectors)

where $d$ is to be determined. The mapping from observable properties of any coherent entity to the four
structural slots $\{S, \mathbf{A}, \mathbf{I}, \mathbf{R}\}$ is structurally unique (no two inequivalent
assignments produce structurally identical predictions for the same entity).

*Remark 2.1.* A1 is the foundational axiom of the framework; it is not derived from simpler premises
within this paper. Its justification is the structural argument that $\{S, \mathbf{A}, \mathbf{I}, \mathbf{R}\}$
are the grades of a geometric algebra of minimal dimension consistent with A2 — a circularity resolved by
the mutual consistency of A1 and A2, not by an independent proof of A1. The role of A1 in this structure
is analogous to that of natural selection in Darwinian theory: a minimal posit that generates the rest.

**Axiom A2 (geometric product dynamics).** The dynamics of an ODU is governed by the **geometric product**
of its attributes. In a geometric algebra $G(d)$ over $\mathbb{R}^d$, the geometric product of two grade-1
elements $u, v$ decomposes canonically:
$$uv = u \cdot v + u \wedge v$$
into a symmetric (grade-0) scalar part and an antisymmetric (grade-2) bivector part. Applied to the
attributes: the **Force** $F = S \cdot \mathbf{A}$ (grade-0 coupling, symmetric) and the **Field**
$\mathcal{F} = \mathbf{I} \wedge \mathbf{R}$ (grade-2 coupling, antisymmetric via the Hodge dual $= \mathbf{I} \times \mathbf{R}$
in $d=3$). The Force/Field decomposition is algebraically forced by A2 — it is not an independent postulate.

*Remark 2.2.* The genuine content of A2 is the claim that *dynamics is the geometric product*. The
symmetric/antisymmetric split of that product is a theorem of geometric algebra, not an additional hypothesis.

---

## 3. Four Lemmas

### Lemma 1 (Hurwitz — dimension is forced)

**Lemma 1.** *Under A1 and A2, the dimension of the vector attribute space is $d = 3$ or $d = 7$.*

*Proof.* A2 requires $\mathcal{F} = \mathbf{I} \times \mathbf{R}$ to be a **vector cross product** on
$\mathbb{R}^d$: a bilinear, antisymmetric map $\mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}^d$
satisfying the norm identity $|\mathbf{u} \times \mathbf{v}|^2 = |\mathbf{u}|^2|\mathbf{v}|^2 - (\mathbf{u}\cdot\mathbf{v})^2$.
By the Eckmann theorem (Eckmann 1943; see also Adams 1960), such a product exists if and only if
$d \in \{1, 3, 7\}$, equivalently if and only if $d+1$ is the dimension of a normed division algebra over
$\mathbb{R}$ (Hurwitz 1898): $\mathbb{C}$ ($d=1$), $\mathbb{H}$ ($d=3$), $\mathbb{O}$ ($d=7$).
The case $d=1$ is degenerate: in $\mathbb{R}^1$ the norm identity forces $|\mathbf{u} \times \mathbf{v}|^2 =
u^2v^2 - (uv)^2 = 0$, so the cross product is identically zero. Excluding this trivial case, the admissible
non-degenerate dimensions are:
- $d = 3$ (quaternionic branch, $\mathbb{H}$): the **space-time branch**
- $d = 7$ (octonionic branch, $\mathbb{O}$): the **internal/atemporal branch**

*The choice of branch is not free.* The $d = 3$ branch admits a temporal extension: one can adjoin a fourth
generator $\partial_\tau$ (Lemma 3) without breaking the cross product structure, because $G(3)$ already
exhausts the grade-1 space and the fourth direction belongs to a distinct grade. The $d = 7$ branch does not
admit an analogous temporal extension: the geometric algebra $G(7)$ has all grade-1 elements squaring to
$+1$ (positive definite base metric), and there is no canonical grade-1 element squaring to $-1$ within
$G(7)$ itself; a temporal direction would have to be adjoined externally, breaking the octonionic product
structure (non-associativity of $\mathbb{O}$ precludes the Clifford algebra factorization used in Lemma 4).
This branch is the algebraic home of the *internal* sector (three generations, $\mathrm{Der}(\mathbb{O}) = G_2$).
The remainder of this paper works the $d=3$ branch. $\square$

*Corollary 1.1.* "Why exactly three vector attributes" is not a free parametric choice — it is the
answer to "why is the field a cross product", which is Hurwitz.

### Lemma 2 (Algebra closure)

**Lemma 2.** *In $d=3$, the three grade-1 attributes $\{\mathbf{A}, \mathbf{I}, \mathbf{R}\}$ generate the
full geometric algebra $G(3)$ of dimension $8 = 2^3$.*

*Proof.* Three linearly independent vectors in $\mathbb{R}^3$ generate $G(3)$ by definition: the basis
elements are $\{1, e_1, e_2, e_3, e_1e_2, e_2e_3, e_3e_1, e_1e_2e_3\}$ (grade 0 through 3). $S$ occupies
grade 0; $\{\mathbf{A}, \mathbf{I}, \mathbf{R}\}$ occupy grade 1; the bivectors (grade 2) and the
pseudoscalar (grade 3) are generated by their products. No fifth grade-1 generator is available in $G(3)$:
the grade-1 subspace has dimension 3. $\square$

### Lemma 3 (Time as evolution)

**Lemma 3.** *An operative ODU requires a temporal direction $\partial_\tau$ that is not an attribute. This
direction is provided by the equation of motion.*

*Proof.* An ODU evolves; its configuration satisfies a second-order equation of motion (EOM):
$$\ddot\Gamma + \gamma\dot\Gamma + \nabla P(\Gamma) = N(\Gamma)$$
where $\gamma > 0$ is a constitutive damping parameter and $P(\Gamma)$ is the structural potential. (The
EOM is second-order because the ODU has both a configuration and a rate of change as independent degrees of
freedom; first-order equations would conflate the two. The gradient-flow term $\nabla P$ is required for
dissipation to be consistent with Lyapunov stability, and the wave term $\ddot\Gamma$ is required for
oscillatory behavior — both are structural requirements, not additional postulates.)

Lemma 2 establishes that the spatial attribute space is generated by three grade-1 vectors $\{\mathbf{A},
\mathbf{I}, \mathbf{R}\}$ spanning $\mathbb{R}^3$. This is a 3-dimensional space. However, the EOM contains
$\partial_\tau$, a differentiation operator that is not a spatial attribute — it acts on the temporal
argument $\tau$ of $\Gamma(\tau, \mathbf{x})$. This operator is distinct from the spatial generators: (i)
it cannot be expressed as a linear combination of $\mathbf{A}, \mathbf{I}, \mathbf{R}$; (ii) $S$ is
grade-0 (scalar), not grade-1; (iii) promoting one spatial attribute to the temporal role would miscategorize
it and break the cross product (Lemma 1). Therefore $\partial_\tau$ is a genuinely fourth independent
direction. Together $\{\mathbf{A}, \mathbf{I}, \mathbf{R}, \partial_\tau\}$ span a 4-dimensional vector
space $V^4$. The Clifford algebra $\mathrm{Cl}(V^4, q)$ of any 4-dimensional space has dimension $2^4 = 16$;
its smallest faithful real matrix representation is $4\times4$ (this follows from Bott periodicity, once the
signature $q$ of $V^4$ is fixed by Lemma 4). The ODU has a time axis because it evolves — not because
spacetime is postulated. $\square$

### Lemma 4 (Lorentzian signature from the wave operator)

**Lemma 4.** *The Lorentzian signature $(3,1)$ is the symbol of the equation of motion, not a postulate.*

*Proof.* The principal part of the EOM is the wave operator $\Box\Gamma = \ddot\Gamma - c^2\nabla^2\Gamma$.
Taking the Fourier symbol ($\partial_\tau \to i\omega$, $\nabla \to i\mathbf{k}$):
$$\sigma(\Box) = -\omega^2 + c^2|\mathbf{k}|^2 = \eta^{\mu\nu}p_\mu p_\nu, \quad
\eta = \mathrm{diag}(-1, +1, +1, +1)$$
This is the Minkowski quadratic form with signature $(3,1)$. The real Clifford algebra of this form
(Atiyah, Bott and Shapiro 1964; Lounesto 2001) is $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$.

*Uniqueness of the real representation.* The Bott periodicity classification gives $\mathrm{Cl}_{3,1}$
as a *real* matrix algebra. Requiring $\Gamma$ to be a real matrix (the gradient flow $\dot\Gamma = -\nabla P$
is real; dissipation is a real process) pins the signature to $(3,1)$ and excludes $(1,3)$ (which gives
$\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$, quaternionic), $(4,0)$ (which gives $\mathrm{Cl}_{4,0} \cong
M_2(\mathbb{H})$, also quaternionic), and all other real signatures that fail to give $M_4(\mathbb{R})$.
The only signature that yields a *real* $4\times4$ matrix algebra with three spatial and one temporal
generator is $(3,1)$. $\square$

*Remark 3.1.* The step "$d=3$ forces real $4\times4$" is the logical bridge: asking for three spatial
generators in a real matrix algebra forces exactly $M_4(\mathbb{R}) = \mathrm{Cl}_{3,1}$. The Lorentzian
signature is not a choice — it is what remains after demanding reality and three spatial dimensions.

---

## 4. Main Theorem

**Theorem (Γ is forced).** *Given axioms A1 and A2, the configuration of any operative dynamical unit
is necessarily*
$$\boxed{\Gamma = \Gamma_s \oplus \Gamma_a \;\in\; M_4(\mathbb{R}) = \mathrm{Cl}_{3,1}}$$
*where $\Gamma_s = \tfrac{1}{2}(\Gamma + \Gamma^\top)$ (symmetric, 10 independent entries — the Force
sector) and $\Gamma_a = \tfrac{1}{2}(\Gamma - \Gamma^\top)$ (antisymmetric, 6 independent entries —
the Field sector), with:*
- *$\Gamma_s = \mathrm{Gram}(\mathbf{A}, \mathbf{I}, \mathbf{R}; S)$ — the metric coupling structure of
  the attributes (Force = $S \cdot \mathbf{A}$, symmetric)*
- *$\Gamma_a$ = magnetic part ($\mathbf{I}\wedge\mathbf{R}$, spatial bivector, from SAIR) $\oplus$
  electric part ($\partial_\tau\wedge\nabla$, spacetime bivector, coupling structure$\leftrightarrow$evolution)*

*Proof.* Lemma 1 (Hurwitz) forces $d = 3$. Lemma 2 establishes $G(3)$. Lemma 3 adds the temporal
generator $\partial_\tau$, extending $G(3)$ to a 4-generator algebra. Lemma 4 identifies the resulting
algebra as $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ via the wave operator symbol.

*Uniqueness of $\Gamma = \Gamma_s \oplus \Gamma_a$.* A positive-definite symmetric matrix (metric) carries
only Force ($\Gamma_s \succ 0$, no antisymmetric part). A symplectic form carries only Field ($\Gamma_a$,
no symmetric part). The object $\Gamma = \Gamma_s \oplus \Gamma_a$ is the **unique minimal object** that
carries both Force and Field simultaneously — the unique decomposition of a real $4\times4$ matrix into
symmetric and antisymmetric parts. $\square$

*Remark 4.1.* The theorem does not claim that $\mathrm{Cl}_{3,1}$ is the algebra of spacetime as a physical
background. It claims that any operative dynamical unit that satisfies A1 and A2 has a configuration
object that is an element of $\mathrm{Cl}_{3,1}$. Physical spacetime is not an input — it is a limit
(the space-time branch of the framework; see §6.2).

---

## 5. Three Closing Propositions

The proof of the main theorem rests on three technical choices — the orthonormality of the attribute frame,
the identification of the temporal generator, and the choice of metric on $M_4(\mathbb{R})$ — that might
appear to be additional postulates. The following propositions show that each is in fact forced.

### Proposition P1 (Orthonormality is gauge-redundant)

**Proposition P1.** *The physical invariants of $\Gamma$ — its determinant, trace, eigenvalues, and
singular values — are independent of the choice of orthonormal frame for $\{\mathbf{A}, \mathbf{I}, \mathbf{R}\}$.
Orthonormality is a representational gauge, not a physical postulate.*

*Proof.* Let $M \in SO(3)$ be the Gram-Schmidt rotation mapping any linearly independent triple
$\{\mathbf{A}, \mathbf{I}, \mathbf{R}\}$ to an orthonormal frame $\{\hat{\mathbf{A}}, \hat{\mathbf{I}},
\hat{\mathbf{R}}\}$ spanning the same subspace. Under this rotation, $\Gamma \mapsto M\Gamma M^\top$.
The spectrum of $\Gamma$ (equivalently, $\det\Gamma$, $\mathrm{tr}\,\Gamma$, and all eigenvalues) is
invariant under conjugation by any $M \in SO(3)$. The orthonormal frame fixes the explicit matrix
entries of $\Gamma_s$ (diagonal in that frame) but not its spectrum. $\square$

### Proposition P2 (The temporal generator is the evolution operator)

**Proposition P2.** *The temporal Clifford generator $\gamma_0 \in \mathrm{Cl}_{3,1}$ satisfying
$\gamma_0^2 = -\mathbf{1}$ is canonically identified with the time derivative $\partial_\tau$ of the EOM.*

*Proof.* The symbol of the wave operator $\Box = \partial_\tau^2 - c^2\nabla^2$ is $\eta^{\mu\nu}p_\mu p_\nu$
with $\eta = \mathrm{diag}(-1,+1,+1,+1)$. This defines the anticommutation relations $\{\gamma_\mu, \gamma_\nu\}
= 2\eta_{\mu\nu}$, with $\gamma_0^2 = -\mathbf{1}$ forced by $\eta_{00} = -1$. The identification
$\partial_\tau \leftrightarrow \gamma_0$ is the unique one that makes $\Box = (\gamma^\mu\partial_\mu)^2$
(the Dirac factorization). Verified numerically: a real $4\times4$ representation satisfying $\{\gamma_\mu,
\gamma_\nu\}/2 = \eta_{\mu\nu} = \mathrm{diag}(-1,+1,+1,+1)$ exists with $\gamma_0^2 = -I$, $\gamma_i^2 = +I$
(residual $< 10^{-14}$; see `code/verify_cl31.py`). $\square$

*Note.* P2 does not introduce a new temporal variable. The EOM already contains $\partial_\tau$. P2 says
that the Clifford temporal generator *is* that operator — not a new geometric structure, but the evolution
already present in the framework.

### Proposition P3 (Frobenius is the canonical Clifford metric)

**Proposition P3.** *The metric on the space of configurations $\Gamma \in M_4(\mathbb{R}) = \mathrm{Cl}_{3,1}$
is the Frobenius norm $\|\Gamma\|^2 = \mathrm{Tr}(\Gamma^\top\Gamma)$, already determined by A2.*

*Proof.* The geometric product of A2 defines the canonical inner product on any Clifford algebra:
$$\langle A, B \rangle_{\mathrm{Cl}} := \langle A\tilde{B} \rangle_0$$
the grade-0 (scalar) component of the geometric product of $A$ with the Clifford reverse $\tilde{B}$.
In the real $4\times4$ representation of $\mathrm{Cl}_{3,1}$, the Clifford reverse corresponds to matrix
transposition ($\tilde{B} = B^\top$), giving $\langle A, B\rangle_{\mathrm{Cl}} = \tfrac{1}{4}\mathrm{Tr}(A^\top B)$,
which is the Frobenius inner product up to the normalization $\tfrac{1}{4}$.

*Uniqueness.* $\mathrm{Spin}(3,1)$ acts on $\mathrm{Cl}_{3,1}$ by adjoint conjugation $g\cdot\Gamma = g\Gamma g^{-1}$.
Any physical metric must be invariant under this action. The grade decomposition
$\Lambda^0 \oplus \Lambda^1 \oplus \Lambda^2 \oplus \Lambda^3 \oplus \Lambda^4$ of $\mathrm{Cl}_{3,1}$
consists of pairwise non-isomorphic irreducible representations of $\mathrm{Spin}(3,1)$. By Schur's lemma,
any $\mathrm{Spin}(3,1)$-invariant bilinear form is proportional to $\mathrm{Tr}(A^\top B)$ on each
grade-block, with a possibly different constant on each grade. The submultiplicativity constraint —
$\|\Gamma\Gamma'\| \leq \|\Gamma\|\|\Gamma'\|$ for all $\Gamma, \Gamma' \in \mathrm{Cl}_{3,1}$, required for
$P(\Gamma) = \|\Gamma\|^2$ to be compatible with the algebra product — forces equal scaling across all
grades (a different scale per grade would violate submultiplicativity for mixed-grade products). The
result is Frobenius, uniquely. $\square$

*Extension to $\mathrm{Cl}_{4,1}$.* The spacetime configuration in the GSF framework lives in $\mathrm{Cl}_{4,1} \cong M_4(\mathbb{C})$
(Bott periodicity: $p-q = 3$). The same argument applies with the Clifford reverse replaced by the Hermitian
conjugate: $\langle A, B\rangle = \tfrac{1}{4}\mathrm{Tr}(A^\dagger B)$, giving the Hilbert-Schmidt norm
$\|\Gamma\|^2 = \mathrm{Tr}(\Gamma^\dagger\Gamma)$, real and non-negative. P3 holds without modification.

---

## 6. Two Physical Limits

The main theorem and propositions establish the algebraic structure. We exhibit two physical theories as
limiting cases of the framework, to confirm that the abstract structure is not vacuous.

### 6.1 Newton's second law (Force sector, det > 0)

In the operationally active sector ($\det\Gamma > 0$, $\Gamma_s \succ 0$), the dominant dynamics is along
the soft mode of $\Gamma$ — the direction of smallest singular value. Project the EOM onto the soft-mode
scalar $x$ (dominant singular value of $\Gamma$ along $\mathbf{A}$):
$$\ddot{x} + \gamma\dot{x} + \partial_x P = F_\text{ext}$$
This is Newton's second law for a damped oscillator, with $\gamma$ the constitutive damping and $F_\text{ext}$
an external force term. The structural identification is: mass $\sim$ inertia of the soft mode;
$\gamma$ the damping coefficient of the ODU; $P$ the potential landscape. Newton is not a special case
of the framework — it is a limiting projection onto the dominant mode. **Status: structural correspondence
$\langle\mathrm{CE}\rangle$, not a derivation from first principles.**

### 6.2 Free electrodynamics (Field sector, det = 0 boundary)

At the boundary $\det\Gamma = 0$, the configuration loses rank: one or more singular values of $\Gamma$
approach zero. When $\gamma \to 0$ (non-dissipative limit) and the configuration lives in the grade-2
(bivector) sector $\Gamma_a$ of $\mathrm{Cl}_{3,1}$, the EOM reduces to:
$$\Box\Gamma_a = 0 \quad\Rightarrow\quad \Box F_{\mu\nu} = 0$$
which is the free Maxwell equation in the absence of sources ($\partial^\mu F_{\mu\nu} = 0$), together
with the Bianchi identity $\partial_{[\mu}F_{\nu\rho]} = 0$ (automatic from $F = \mathrm{d}A$). The
bivector $F_{\mu\nu}$ is the Faraday tensor; the identification of $\Gamma_a$ with the grade-2 sector
of $\mathrm{Cl}_{3,1}$ makes the Field $\mathbf{I}\wedge\mathbf{R}$ correspond to the spatial (magnetic)
part of $F_{\mu\nu}$, and the electric part arises from the $\partial_\tau\wedge\nabla$ coupling. Charge
conservation $\partial^\mu J_\mu = 0$ follows from the antisymmetry of $F$ without additional assumptions.
**Status: free Maxwell $\langle\mathrm{TEO}\rangle[\mathrm{D}]$; source equation $\langle\mathrm{A}\rangle$
(requires closing the cross-coupling block).**

---

## 7. Numerical Verification

The following steps in the derivation are numerically confirmed; scripts are in `code/`:

| Result | Script | Residual |
|---|---|---|
| $\{\gamma_\mu, \gamma_\nu\}/2 = \eta_{\mu\nu}$ in real $4\times4$ rep | `verify_cl31.py` | $< 10^{-14}$ |
| $\gamma_0^2 = -I$, $\gamma_i^2 = +I$ | `verify_cl31.py` | $< 10^{-14}$ |
| $\langle A, B\rangle_\mathrm{Cl} = \mathrm{Tr}(A^\top B)/4$ on grade-1 elements | `verify_clifford_metric.py` | $< 10^{-14}$ |
| Frobenius submultiplicativity: $\|\Gamma\Gamma'\|_F \leq \|\Gamma\|_F\|\Gamma'\|_F$ (0 violations); Pythagorean: $\|\Gamma\|^2 = \|\Gamma_s\|^2 + \|\Gamma_a\|^2$ | `verify_frobenius.py` | $0$ violations; error $< 10^{-13}$ |
| $\det\Gamma$ as invariant under $SO(3,1)$ conjugation | `verify_det_invariance.py` | $< 10^{-12}$ |

---

## 8. Discussion

### 8.1 What is new

The spacetime algebra program (Hestenes 1966; Doran and Lasenby 2003) takes $\mathrm{Cl}_{3,0}$ or
$\mathrm{Cl}_{1,3}$ as the algebra of physical space or spacetime, motivated by the known geometry.
The present work reverses this logic: $\mathrm{Cl}_{3,1}$ is derived as the forced algebraic structure
of any self-describing dynamical unit, without assuming a spacetime background. The key steps are:
(i) Hurwitz forces the dimension of the vector attribute space; (ii) the wave operator fixes the signature.
Neither step is obvious from the physics-first perspective.

The closest structural antecedent we are aware of is the observation (Lounesto 2001, §17) that the
Clifford algebra of the symbol of the wave operator is $\mathrm{Cl}_{3,1}$. We make this observation
a theorem by showing it is the *only* Clifford algebra consistent with A1 and A2.

### 8.2 The octonionic branch

Lemma 1 identifies a second branch: $d = 7$ (octonions). As argued in Lemma 1, this branch does not
admit a canonical temporal extension compatible with the octonionic product structure. It is the algebraic
home of the *internal* structure of the ODU: the derivation algebra $\mathrm{Der}(\mathbb{O}) = G_2$
(with $\mathrm{SU}(3) \subset G_2$), three generations encoded in the exceptional Jordan algebra
$h_3(\mathbb{O})$, and color symmetry. The two branches ($d=3$ with time, $d=7$ without) are algebraically
orthogonal: the temporal generator of the $d=3$ branch does not act on the $d=7$ sector. This structural
orthogonality may explain why internal quantum numbers appear to be independent of spacetime dynamics, but
the connection remains conjectural and is open for future work.

### 8.3 Honest scope

This paper establishes the algebraic structure. It does not:
- Derive the specific metric of physical spacetime (GR is a limit; the derivation requires additional
  steps developed in Molina 2025, Part V)
- Prove uniqueness of the SAIR attribute structure independent of A1 (that is the content of A1 itself,
  which we take as foundational rather than derived)
- Close the $d=7$ (octonionic) branch identification (open problem; partial results in Molina 2025, §Q)

The residues that remain open after P1/P2/P3 are exactly A1 and A2 — the two axioms. Everything
else in the derivation is a theorem.

### 8.4 Related work

- Hurwitz (1898): normed division algebras in dimensions 1, 2, 4, 8.
- Eckmann (1943): cross products in $\mathbb{R}^n$ exist only for $n = 1, 3, 7$.
- Atiyah, Bott and Shapiro (1964): Clifford modules and Bott periodicity.
- Hestenes (1966, 1986): spacetime algebra as the language of physics.
- Doran and Lasenby (2003): geometric algebra for physicists (Cambridge).
- Lounesto (2001): Clifford algebras and spinors (Cambridge).
- Adams (1960): vector fields on spheres; confirms Hurwitz via K-theory.
- Molina (2024a): the determinant as the source of the cubic term in matrix gradient flows. DOI: 10.5281/zenodo.20752208

---

## 9. Conclusions

From two structural axioms about the minimal description of an operative dynamical unit — SAIR attribute
structure (A1) and geometric product dynamics (A2) — the real Clifford algebra $\mathrm{Cl}_{3,1}$
emerges as a structural theorem rather than a geometric postulate. The derivation chain is:

$$\underbrace{\text{SAIR}}_\text{A1} + \underbrace{\text{geometric product}}_\text{A2}
\xrightarrow{\text{Hurwitz}} d=3
\xrightarrow{G(3)} \{\mathbf{A},\mathbf{I},\mathbf{R}\}=\gamma_i
\xrightarrow{\text{EOM: }\Box} \gamma_0=\partial_\tau,\ (3,1)
\xrightarrow{\text{P1/P2/P3}} \Gamma = \Gamma_s\oplus\Gamma_a \in M_4(\mathbb{R})$$

Three propositions close the technical residues (orthonormality is gauge, temporal generator is the
evolution operator, Frobenius is the canonical Clifford metric). The only irreducible axioms remaining
are A1 and A2. Classical mechanics (Newton projection, §6.1) and free electrodynamics (Maxwell limit,
§6.2) appear as structural correspondences.

The result supplies a structural foundation for the spacetime algebra program: not "given Minkowski
space, use $\mathrm{Cl}_{3,1}$", but "from the structure of a dynamical unit, $\mathrm{Cl}_{3,1}$ is
the forced representation."

---

## References

Adams, J. F. (1960). Vector fields on spheres. *Annals of Mathematics*, 75(3), 603–632.

Atiyah, M. F., Bott, R., and Shapiro, A. (1964). Clifford modules. *Topology*, 3(S1), 3–38.

Doran, C. and Lasenby, A. (2003). *Geometric Algebra for Physicists*. Cambridge University Press.

Eckmann, B. (1943). Stetige Lösungen linearer Gleichungssysteme. *Commentarii Mathematici Helvetici*,
15(1), 318–339.

Hestenes, D. (1966). *Space-Time Algebra*. Gordon and Breach.

Hestenes, D. (1986). A unified language for mathematics and physics. In *Clifford Algebras and their
Applications in Mathematical Physics*. D. Reidel.

Hurwitz, A. (1898). Über die Komposition der quadratischen Formen von beliebig vielen Variabeln.
*Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen*, 309–316.

Lounesto, P. (2001). *Clifford Algebras and Spinors* (2nd ed.). Cambridge University Press.

Molina, H. (2024a). The determinant as an orientation invariant and the source of the cubic term in
equivariant matrix gradient flows. DOI: 10.5281/zenodo.20752208

Molina, H. (2025). *Gamma Space Framework* (working manuscript). Available at:
https://github.com/hmolinab/gamma-space-framework
