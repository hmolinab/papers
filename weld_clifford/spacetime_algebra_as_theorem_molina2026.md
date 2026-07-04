# Spacetime Algebra as a Theorem: Deriving Cl(3,1) from the Structure of a Dynamical Unit

Henry Molina  
Independent researcher
henrymolina@gmail.com
DOI: 10.5281/zenodo.21184515

Self-contained manuscript; requires no external framework beyond standard linear algebra and Clifford algebra
conventions. Numericaa verifications referenced in §7 are at:  
https://github.com/hmolinab/papers/tree/main/weld_clifford/code

---

## Abstract

We derive the real Clifford algebra $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ from three structural axioms
about any operative dynamical unit (ODU). A1 (SAIR): the unit is described by four
intrinsic attributes — a scalar $S$ and three vectors $\mathbf{A}, \mathbf{I}, \mathbf{R}$ in $\mathbb{R}^d$.
A2 (geometric product): structure is governed by the geometric product of those attributes, whose grade-2
part $\mathbf{I}\wedge\mathbf{R}$ is the Field bivector. A3 (continuous evolution): the ODU evolves
smoothly in time and space at finite propagation speed. From these three axioms — without postulating a
spacetime metric or background geometry — we derive: (i) the closure condition
$\binom{d}{2}=d$ forces $d=3$ uniquely (Hodge self-duality of bivectors in $\mathbb{R}^3$, confirmed by
Hurwitz); (ii) smooth evolution (A3) requires a fourth temporal direction independent of the spatial
attributes; (iii) the principal symbol of the resulting second-order PDE is the Minkowski form
$\eta=\mathrm{diag}(-1,+1,+1,+1)$, whose real Clifford algebra is $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$.
Three closing propositions establish that orthonormality is gauge-redundant (P1), that $\gamma_0$ is the
algebraic generator conjugate to $\partial_\tau$ in the Dirac factorization of $\Box$ (P2, without
conflating algebra elements with differential operators), and that the Frobenius norm is the unique
Clifford inner product forced by A2 (P3). The result promotes the Clifford algebra of spacetime from a
geometric postulate to a structural theorem. Classical mechanics and free electrodynamics appear as limits.

**Keywords:** Clifford algebra, geometric algebra, Hurwitz theorem, spacetime signature, dynamical systems,
matrix normal form, Frobenius metric.

---

## 1. Introduction

The Clifford algebra $\mathrm{Cl}_{3,1}$ — equivalently, the spacetime algebra (STA) of Hestenes (1966) — is
the standard algebraic scaffolding for special relativity and Dirac theory. Its standard motivation is
geometric: one postulates a Minkowski spacetime with signature $(3,1)$ and then constructs the associated
Clifford algebra. The question we address is different: *is the Lorentzian signature a theorem, rather than a
postulate, if one asks what algebraic structure a self-describing dynamical unit must have?*

We show that the answer is yes, under three minimal axioms: A1 (attribute structure), A2 (geometric
product), and A3 (smooth evolution at finite speed). The derivation does not require spacetime as an
input; the signature emerges from the principal symbol of the equation of motion dictated by A3.

This paper is part of a larger program — the Gamma Space Framework (GSF) — whose central object is a real
$4\times4$ configuration matrix $\Gamma \in M_4(\mathbb{R})$. The present paper establishes the algebraic
foundation: that $\Gamma$ is an element of $\mathrm{Cl}_{3,1}$, not by postulate but by necessity. The
companion paper (Molina 2024a) establishes the dynamical result: that the determinant of $\Gamma$ is the
source of the cubic term in the soft-mode reduction of the matrix gradient flow.

*Terminology note.* Throughout this paper we use the term **operative dynamical unit (ODU)** as a
self-contained technical term requiring no prior knowledge of the GSF. In the GSF literature (Molina 2025),
the same object is called a **Unit of Coherence (UoC)**; the two terms are synonymous.

**Relation to the geometric algebra literature.** The spacetime algebra program (Hestenes 1966, 1986;
Doran and Lasenby 2003) is the closest antecedent. That program takes Minkowski spacetime as given and
develops physics in terms of $\mathrm{Cl}_{1,3}$ (one time, three space — Hestenes' convention). The
signature choice is not merely a convention: $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$ (quaternionic),
whereas $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ (real). These are non-isomorphic as real algebras. The
present derivation forces $\mathrm{Cl}_{3,1}$ — not $\mathrm{Cl}_{1,3}$ — because we require $\Gamma$ to be
a real matrix (dissipation and gradient flows are real processes); this distinguishes the two conventions at
the algebraic level. The derivation does not compete with the spacetime algebra program; it identifies which
real algebra is forced by the structure of any evolving dynamical unit, and explains why that program works.

**Plan.** §2 states the three axioms. §3 derives the four lemmas. §4 states and proves the main theorem. §5
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
into a symmetric (grade-0) scalar part and an antisymmetric (grade-2) bivector part. Applied to the attributes: the **Force** sector $\Gamma_s$ is the symmetric Gram coupling of the scalar
identity $S$ with the grade-1 attributes $\{\mathbf{A},\mathbf{I},\mathbf{R}\}$, encoding the metric
structure of the unit. The **Field** $\mathcal{F} = \mathbf{I} \wedge \mathbf{R} \in \Lambda^2(\mathbb{R}^d)$
(grade-2, antisymmetric) is the reactive sector. "Force" names the symmetric sector of $\Gamma$; $S$ is
grade-0 and $S\mathbf{A}$ is a grade-1 vector, not a scalar — the symmetric structure enters through the
Gram matrix, not through a grade-0 product. The Force/Field split is algebraically forced by A2, not a
separate postulate.

**Axiom A3 (continuous evolution).** The ODU evolves smoothly in time $\tau$ and space $\mathbf{x}$,
with a finite propagation speed $c > 0$. Treating $\Gamma(\tau,\mathbf{x})$ as a field and expanding to
second order in both $\tau$ and $\mathbf{x}$, consistent with A1 and A2, the generic equation of motion is
$$\ddot\Gamma + \gamma\dot\Gamma - c^2\nabla_{\mathbf{x}}^2\Gamma + \nabla_\Gamma P(\Gamma) = N(\Gamma),$$
where $\gamma\ge0$ is a constitutive damping parameter, $\nabla_{\mathbf{x}}^2 = \partial_{x_1}^2 + \partial_{x_2}^2 + \partial_{x_3}^2$
is the spatial Laplacian (propagation at speed $c$), and $\nabla_\Gamma P$ is the gradient of the
structural potential in configuration space. This is the lowest-order equation coupling inertia
($\ddot\Gamma$), spatial propagation ($-c^2\nabla_{\mathbf{x}}^2\Gamma$), dissipation ($\gamma\dot\Gamma$),
and restoring forces ($\nabla_\Gamma P$); no additional postulate about dynamics is made beyond smoothness
and finite speed.

*Remark 2.2.* The genuine content of A2 is the claim that *structure is the geometric product*. A3 adds
the claim that *evolution is smooth and second-order*: position and velocity are independent degrees of
freedom, so a first-order equation would conflate them. The symmetric/antisymmetric split of the
geometric product is a theorem of geometric algebra, not an additional hypothesis.

---

## 3. Four Lemmas

### Lemma 1 (Closure — dimension is forced to $d=3$)

**Lemma 1.** *Under A1 and A2, the dimension of the vector attribute space is $d = 3$.*

*Proof (closure argument).* A2 says the Field is the grade-2 part of the geometric product:
$\mathcal{F} = \mathbf{I} \wedge \mathbf{R} \in \Lambda^2(\mathbb{R}^d)$, a bivector of dimension
$\binom{d}{2} = \tfrac{d(d-1)}{2}$. For the ODU to be closed — for $\mathcal{F}$ to couple back to the
grade-1 attribute $\mathbf{A}$ without introducing objects of higher rank than those in A1 — the Field
space and the attribute space must be isomorphic as vector spaces:
$$\binom{d}{2} = d \;\Longrightarrow\; \tfrac{d(d-1)}{2} = d \;\Longrightarrow\; d = 3.$$
The unique non-trivial solution is $d = 3$. This isomorphism is the Hodge duality
$\star: \Lambda^2(\mathbb{R}^3) \xrightarrow{\;\sim\;} \mathbb{R}^3$, which maps
$\mathcal{F} = \mathbf{I} \wedge \mathbf{R}$ to the familiar vector cross product
$\mathbf{I} \times \mathbf{R} \in \mathbb{R}^3$.

*Confirmation by Hurwitz.* Once $d=3$ is established by closure, the Eckmann theorem (Eckmann 1943;
Adams 1960) confirms that a non-degenerate vector cross product on $\mathbb{R}^3$ exists — it is the
imaginary part of the quaternion product ($\mathbb{H}$, dimension $d+1=4$). This is a consistency check,
not the source of the derivation: Hurwitz verifies that $d=3$ works, but closure is what forces it.

*The octonionic branch ($d=7$) is structurally distinct.* A cross product on $\mathbb{R}^7$ exists
(Eckmann 1943) as the imaginary part of the octonion product, but it does not arise from the closure
condition $\binom{d}{2}=d$ (since $\binom{7}{2}=21\neq7$). It is not the Hodge dual of a bivector;
it is a genuinely different algebraic structure. This branch is the algebraic home of the *internal*
sector ($\mathrm{Der}(\mathbb{O})=G_2$, three generations) and is treated separately in §8.2.
The remainder of this paper works $d=3$. $\square$

*Corollary 1.1.* "Why exactly three vector attributes" is not a free parametric choice — it is the
answer to "what dimension allows the Field to couple back to the Agents without rank escalation."

### Lemma 2 (Algebra closure)

**Lemma 2.** *In $d=3$, the three grade-1 attributes $\{\mathbf{A}, \mathbf{I}, \mathbf{R}\}$ generate the
full geometric algebra $G(3)$ of dimension $8 = 2^3$.*

*Proof.* Three linearly independent vectors in $\mathbb{R}^3$ generate $G(3)$ by definition: the basis
elements are $\{1, e_1, e_2, e_3, e_1e_2, e_2e_3, e_3e_1, e_1e_2e_3\}$ (grade 0 through 3). $S$ occupies
grade 0; $\{\mathbf{A}, \mathbf{I}, \mathbf{R}\}$ occupy grade 1; the bivectors (grade 2) and the
pseudoscalar (grade 3) are generated by their products. No fifth grade-1 generator is available in $G(3)$:
the grade-1 subspace has dimension 3. $\square$

### Lemma 3 (Time as a fourth direction)

**Lemma 3.** *Under A3, the smooth evolution of the ODU requires a temporal direction $\partial_\tau$
that is independent of the three spatial attribute directions of A1. Together they span a
$4$-dimensional vector space $V^4$.*

*Proof.* By A3, the configuration $\Gamma(\tau,\mathbf{x})$ is smooth in time $\tau$ and space
$\mathbf{x}$. Smoothness implies the existence of partial derivatives $\partial_\tau$ and $\nabla$
(the spatial gradient along the attribute directions). Lemma 2 establishes that the spatial attribute
space is $\mathbb{R}^3$, spanned by $\{\mathbf{A}, \mathbf{I}, \mathbf{R}\}$. The temporal direction
$\partial_\tau$ is independent of these three generators for three reasons: (i) it cannot be expressed
as a spatial combination of $\mathbf{A}, \mathbf{I}, \mathbf{R}$, since it differentiates the temporal
argument, not the attribute frame; (ii) $S$ is grade-0 (scalar), not a grade-1 direction; (iii)
promoting one spatial attribute to the temporal role would break the closure condition $\binom{d}{2}=d$
that forces $d=3$ in Lemma 1. Therefore $\partial_\tau$ is a genuinely fourth independent direction.

Together $\{\mathbf{A}, \mathbf{I}, \mathbf{R}, \partial_\tau\}$ span a 4-dimensional vector space $V^4$.
The Clifford algebra $\mathrm{Cl}(V^4, q)$ has dimension $2^4=16$; its smallest faithful real matrix
representation is $4\times4$ (Bott periodicity, once the signature $q$ of $V^4$ is fixed by Lemma 4).
The ODU has a time axis because it evolves smoothly — not because spacetime is postulated. $\square$

### Lemma 4 (Lorentzian signature from the wave operator)

**Lemma 4.** *The Lorentzian signature $(3,1)$ is forced by the principal symbol of the EOM (A3), not postulated.*

*Proof.* By A3, the EOM explicitly contains the spatial Laplacian $-c^2\nabla_{\mathbf{x}}^2\Gamma$.
The principal part — the highest-derivative terms, which govern propagation — is therefore the wave operator
$\Box\Gamma = \ddot\Gamma - c^2\nabla_{\mathbf{x}}^2\Gamma$. Isotropy of the Laplacian across the three
spatial directions follows directly from P1: since all physical invariants of $\Gamma$ are $SO(3)$-invariant
under rotations of $\{\mathbf{A},\mathbf{I},\mathbf{R}\}$, no spatial direction is preferred, and the
spatial part of the principal symbol must be $c^2|\mathbf{k}|^2$ (scalar in $\mathbf{k}$, not a
directionally biased tensor). This rules out any anisotropic operator. (A parabolic operator such as the
heat equation $\partial_\tau\Gamma = c^2\nabla_{\mathbf{x}}^2\Gamma$ is first-order in time and does not
treat $\partial_\tau$ as an independent generator on equal footing with the spatial ones; it is excluded.)
Taking the Fourier symbol
($\partial_\tau \to i\omega$, $\nabla \to i\mathbf{k}$):
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
- *$\Gamma_s = \mathrm{Gram}(\mathbf{A}, \mathbf{I}, \mathbf{R}; S)$ — the symmetric metric coupling
  structure of the attributes (Force sector; $S$ is the grade-0 identity, not a grade-1 generator)*
- *$\Gamma_a$ = magnetic part ($\mathbf{I}\wedge\mathbf{R}$, spatial bivector, from SAIR) $\oplus$
  electric part ($\partial_\tau\wedge\nabla$, spacetime bivector, coupling structure$\leftrightarrow$evolution)*

*Proof.* Lemma 1 forces $d = 3$ by closure. Lemma 2 establishes $G(3)$. Lemma 3 adds the temporal
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

Three technical choices appear in the proof — the orthonormality of the attribute frame, the identification
of the temporal generator, and the metric on $M_4(\mathbb{R})$. Each is forced, not free.

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
$\gamma_0^2 = -\mathbf{1}$ is the unique grade-1 generator assigned to the temporal direction such that
the linear differential operator $\mathcal{D} = \gamma^\mu\partial_\mu$ factorizes the wave operator:
$\mathcal{D}^2 = \Box$.*

*Proof.* The symbol of the wave operator $\Box = \partial_\tau^2 - c^2\nabla^2$ is $\eta^{\mu\nu}p_\mu p_\nu$
with $\eta = \mathrm{diag}(-1,+1,+1,+1)$. This defines the anticommutation relations $\{\gamma_\mu, \gamma_\nu\}
= 2\eta_{\mu\nu}$, with $\gamma_0^2 = -\mathbf{1}$ forced by $\eta_{00} = -1$. The assignment of $\gamma_0$
to the temporal direction $\partial_\tau$ is the unique one that makes $(\gamma^\mu\partial_\mu)^2 = \Box$
(the Dirac factorization). Here $\gamma_0$ is an algebra element and $\partial_\tau$ is a differential
operator; P2 does not claim they are the same object — it claims $\gamma_0$ is the algebraic generator
conjugate to $\partial_\tau$ in the factorization of $\Box$. Verified numerically: a real $4\times4$
representation satisfying $\{\gamma_\mu, \gamma_\nu\}/2 = \eta_{\mu\nu} = \mathrm{diag}(-1,+1,+1,+1)$
exists with $\gamma_0^2 = -I$, $\gamma_i^2 = +I$ (residual $< 10^{-14}$; see `code/verify_cl31.py`). $\square$

*Note.* P2 does not conflate categories: $\gamma_0$ is an element of $\mathrm{Cl}_{3,1}$; $\partial_\tau$
is a differential operator acting on functions $\Gamma(\tau,\mathbf{x})$. What P2 establishes is a
canonical pairing between the two, mediated by the Dirac factorization of the wave operator given by A3.

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

The main theorem and propositions establish the algebraic structure. Two physical theories appear as
limiting cases, showing the algebra has concrete content.

### 6.1 Newton's second law (Force sector, det > 0)

In the operationally active sector ($\det\Gamma > 0$, $\Gamma_s \succ 0$), the dominant dynamics is along
the soft mode of $\Gamma$ — the direction of smallest singular value. Project the EOM onto the soft-mode
scalar $x$ (dominant singular value of $\Gamma$ along $\mathbf{A}$):
$$\ddot{x} + \gamma\dot{x} + \partial_x P = F_\text{ext}$$
This is Newton's second law for a damped oscillator: mass is the inertia of the soft mode, $\gamma$ is the
damping of the ODU, and $P$ is the potential landscape. Newton's law is not a special case built into the
framework — it is what the EOM becomes when projected onto the dominant mode. **Status: structural correspondence
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
| $\{\gamma_\mu, \gamma_\nu\}/2 = \eta_{\mu\nu}$ in real $4\times4$ rep | [`verify_cl31.py`](https://github.com/hmolinab/papers/tree/main/weld_clifford/code/verify_cl31.py) | $< 10^{-14}$ |
| $\gamma_0^2 = -I$, $\gamma_i^2 = +I$ | [`verify_cl31.py`](https://github.com/hmolinab/papers/tree/main/weld_clifford/code/verify_cl31.py) | $< 10^{-14}$ |
| $\langle A, B\rangle_\mathrm{Cl} = \mathrm{Tr}(A^\top B)/4$ on grade-1 elements | [`verify_clifford_metric.py`](https://github.com/hmolinab/papers/tree/main/weld_clifford/code/verify_clifford_metric.py) | $< 10^{-14}$ |
| Frobenius submultiplicativity: $\|\Gamma\Gamma'\|_F \leq \|\Gamma\|_F\|\Gamma'\|_F$ (0 violations); Pythagorean: $\|\Gamma\|^2 = \|\Gamma_s\|^2 + \|\Gamma_a\|^2$ | [`verify_frobenius.py`](https://github.com/hmolinab/papers/tree/main/weld_clifford/code/verify_frobenius.py) | $0$ violations; error $< 10^{-13}$ |
| $\det\Gamma$ as invariant under $SO(3,1)$ conjugation | [`verify_det_invariance.py`](https://github.com/hmolinab/papers/tree/main/weld_clifford/code/verify_det_invariance.py) | $< 10^{-12}$ |

---

## 8. Discussion

### 8.1 What is new

The spacetime algebra program (Hestenes 1966; Doran and Lasenby 2003) takes $\mathrm{Cl}_{3,0}$ or
$\mathrm{Cl}_{1,3}$ as the algebra of physical space or spacetime, motivated by the known geometry.
The present work reverses this logic: $\mathrm{Cl}_{3,1}$ is derived as the forced algebraic structure
of any self-describing dynamical unit, without assuming a spacetime background. The key steps are:
(i) the closure condition $\binom{d}{2}=d$ forces the dimension of the vector attribute space (Hurwitz confirms consistency); (ii) the wave operator fixes the signature.
Neither step is obvious from the physics-first perspective.

The closest antecedent is the observation (Lounesto 2001, §17) that the Clifford algebra of the symbol
of the wave operator is $\mathrm{Cl}_{3,1}$. Here that observation becomes a theorem: it is the
*only* Clifford algebra consistent with A1 and A2.

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

The residues that remain open after P1/P2/P3 are exactly A1, A2, and A3 — the three axioms. Everything
else in the derivation is a theorem. The cost of explicitness: three axioms instead of two. The gain:
no premiss enters the derivation undeclared.

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

From three structural axioms — SAIR attribute structure (A1), geometric product (A2), and continuous
smooth evolution (A3) — the real Clifford algebra $\mathrm{Cl}_{3,1}$ emerges as a structural theorem
rather than a geometric postulate. The derivation chain is:

$$\underbrace{\text{SAIR}}_\text{A1} + \underbrace{\text{geom. product}}_\text{A2}
\xrightarrow{\binom{d}{2}=d} d=3
\xrightarrow{G(3)} \{\mathbf{A},\mathbf{I},\mathbf{R}\}=\gamma_i
\xrightarrow{\text{A3: smooth, finite }c} \partial_\tau \perp \mathbb{R}^3
\xrightarrow{\sigma(\Box)=\eta} (3,1)
\xrightarrow{\text{P1/P2/P3}} \Gamma = \Gamma_s\oplus\Gamma_a \in M_4(\mathbb{R})$$

Three propositions close the technical residues: orthonormality is a representational gauge (P1);
$\gamma_0$ is the unique algebraic generator conjugate to $\partial_\tau$ in the Dirac factorization
of $\Box$ — not the operator itself (P2); Frobenius is the canonical Clifford metric forced by A2 (P3).
The irreducible axioms are A1, A2, and A3. Classical mechanics (§6.1) and free electrodynamics (§6.2)
appear as structural limits.

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
