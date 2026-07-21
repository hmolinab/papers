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

We derive the real Clifford algebra $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ from four structural axioms
about any operative dynamical unit (ODU) — the fourth making explicit a co-location premise used implicitly
in an earlier draft. A1 (SAIR): the unit is described by four
intrinsic attributes — a scalar $S$ and three vectors $\mathbf{A}, \mathbf{I}, \mathbf{R}$ in $\mathbb{R}^d$.
A2 (geometric product): structure is governed by the geometric product of those attributes, whose grade-2
part $\mathbf{I}\wedge\mathbf{R}$ is the Field bivector. A3 (continuous evolution): the ODU evolves
smoothly in time and space at finite propagation speed, with the attribute space and the propagation
coordinates identified (A3$'$, co-location). From these four axioms — without postulating a
spacetime metric or background geometry — we derive: (i) the closure condition
$\binom{d}{2}=d$ forces $d=3$ uniquely (Hodge self-duality of bivectors in $\mathbb{R}^3$, confirmed by
Hurwitz); (ii) smooth evolution (A3) requires a fourth temporal direction independent of the spatial
attributes; (iii) the principal symbol of the resulting second-order PDE is the Minkowski form
$\eta=\mathrm{diag}(-1,+1,+1,+1)$, whose real Clifford algebra is $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$.
Three closing propositions establish that orthonormality is gauge-redundant (P1), that $\gamma_0$ is the
algebraic generator conjugate to $\partial_\tau$ in the Dirac factorization of $\Box$ (P2, without
conflating algebra elements with differential operators), and that the Frobenius norm is the unique
Clifford inner product forced by A2 (P3). Within the SAIR framework, Cl(3,1) is a derived consequence rather than a geometric postulate.
Classical mechanics and free electrodynamics appear as structural limits.

**Keywords:** Clifford algebra, geometric algebra, Hurwitz theorem, spacetime signature, dynamical systems,
matrix normal form, Frobenius metric.

---

## 1. Introduction

The Clifford algebra $\mathrm{Cl}_{3,1}$ — equivalently, the spacetime algebra (STA) of Hestenes (1966) — is
the standard algebraic scaffolding for special relativity and Dirac theory. Its standard motivation is
geometric: one postulates a Minkowski spacetime with signature $(3,1)$ and then constructs the associated
Clifford algebra. The question we address is different: *is the Lorentzian signature a theorem, rather than a
postulate, if one asks what algebraic structure a self-describing dynamical unit must have?*

We show that the answer is yes, under four minimal axioms: A1 (attribute structure), A2 (geometric
product), A3 (smooth evolution at finite speed), and A3$'$ (co-location of the attribute space with the
propagation coordinates). The derivation does not require spacetime as an
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
real algebra is forced by the structure of any evolving dynamical unit, and provides a structural basis for that program.

**Plan.** §2 states the four axioms. §3 derives the four lemmas. §4 states and proves the main theorem. §5
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
structural slots $\{S, \mathbf{A}, \mathbf{I}, \mathbf{R}\}$ is claimed to be structurally unique (no two
inequivalent assignments produce structurally identical predictions for the same entity) — but this paper
establishes that claim only at the level of the *container*, not of *instances*, and the two should not be
conflated (see the qualification at the end of Remark 2.1).

*Remark 2.1.* A1 is the foundational axiom of the framework; it is not derived from simpler premises
within this paper. Its justification is the structural argument that $\{S, \mathbf{A}, \mathbf{I}, \mathbf{R}\}$
are the grades of a geometric algebra of minimal dimension consistent with A2 — a circularity resolved by
the mutual consistency of A1 and A2, not by an independent proof of A1. The role of A1 in this structure
is analogous to that of natural selection in Darwinian theory: a minimal posit that generates the rest.

*Qualification (what "structurally unique" means here, and what it does not).* A1's uniqueness clause is
proved in this paper only for the **container**: given that an ODU has one grade-0 and three grade-1
attributes at all, Lemmas 2–4 show the algebra hosting them is forced to $\mathrm{Cl}_{3,1}$, uniquely — a
Schur-type argument (representation compatibility) that is exactly why the grades cannot be reshuffled once
fixed. This paper does **not** establish uniqueness at the level of **instances**: given a specific ODU (a
particle, a cell, a market), which observable quantity fills $S$ versus $\mathbf{A}$ versus $\mathbf{I}$
versus $\mathbf{R}$ is an assignment problem the container theorem is silent on. A necessary condition for
that assignment (candidates must share the slot's representation under the domain's covariance group) is
the same Schur argument specialized to instances, and a companion line of work develops sufficient
selection criteria and tests them against seven worked domains — but that work is at an earlier stage of
rigor than this paper's closed lemmas and is deliberately not imported here (see §8.3). The word "unique"
in A1 should be read as "unique at the container level, proved; open at the instance level" until that
companion work matures. This is not a retreat from A1 — it is the same discipline §8.3 applies elsewhere:
say exactly what is proved, and do not let a strong word in an axiom imply more than the theorem delivers.

*A second, prior qualification: existence, not just uniqueness.* Everything above concerns *uniqueness*
of the slot assignment given that a well-posed SAIR quadruple already exists for a domain. A separate and
more basic question is *existence*: does a given domain admit $\mathbf A,\mathbf I,\mathbf R$ as grade-1
vectors at all? **The theorem of this paper is conditional on a positive answer, and does not itself
supply one.** This is not automatic: a systematic scan of chemical and biological kinetics (companion
work, `brainstorming/physics/veinte_dominios_quimica_biologia.md`) found that 13 of 20 domains tested
have **no** vector candidate for $\mathbf A,\mathbf I,\mathbf R$ — the native variables are scalars
(concentrations, rates, occupation numbers) with no natural embedding into $\mathbb R^3$ or a grade-1
Clifford subspace. For those domains, $\Gamma$ as constructed here simply does not arise; a different
object (a spectral/Schur reduction of a Jacobian, outside this paper's scope) is used instead. **Read
correctly, the Main Theorem (§4) says: "if a domain has grade-1 $\mathbf A,\mathbf I,\mathbf R$, then
their host algebra is forced to $\mathrm{Cl}_{3,1}$" — not "every domain has such attributes."** The
container theorem is proved unconditionally as a piece of algebra; its applicability to a specific
domain is not, and should never be read off this paper alone.

An ODU is not merely a system with four labelable slots. The attributes are intrinsic in the operational
sense: they are the generators of the geometric product of A2, not observational labels assigned from
outside. A threshold relay (e.g., a thermostat) has four assignable properties but satisfies neither A2
(its dynamics are a discontinuous switching rule, not a geometric product) nor A3 (its evolution is not
smooth). The word "intrinsic" in A1 is therefore grounded by A2 and A3 together, not declared by fiat.

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

**Definition (SAIR embedding — the matrix construction named, gauge closed).** The phrase "Gram coupling"
above names an operation without writing it; we write it once, explicitly. Embed the vector attributes as
the columns of $W = [\,\mathbf{A}\mid\mathbf{I}\mid\mathbf{R}\,] \in \mathbb{R}^{4\times3}$ inside the
ambient $4$-dimensional space carrying a bilinear form $q$, and complete $W$ to a basis with a scalar
direction $\mathbf{e}_0$ for $S$: $V = [\,S\mathbf{e}_0\mid W\,]$.

$\mathbf{e}_0$ is not a free choice. Whenever the $3\times3$ Gram $W^{\mathsf T}qW$ is non-degenerate
(the same invertibility hypothesis Corollary 4.2 already requires), the $q$-orthogonal complement of
$\mathrm{span}\{\mathbf{A},\mathbf{I},\mathbf{R}\}$ is exactly one-dimensional — a standard fact of
bilinear algebra: for non-degenerate $q$ on the full $4$-space, $\dim W + \dim W^{\perp_q} = 4$, and
$W\cap W^{\perp_q}=\{0\}$ precisely because $q|_W$ is non-degenerate. **We fix $\mathbf{e}_0$ to be this
unique direction** (normalized, with the residual sign ambiguity the same harmless kind as P1's gauge).
With this choice, $\Gamma_s := V^{\mathsf T}qV$ is automatically block-diagonal:
$$\Gamma_s = \begin{pmatrix}S^2\,q(\mathbf{e}_0,\mathbf{e}_0) & 0\\ 0 & W^{\mathsf T}qW\end{pmatrix},$$
i.e. the **congruence reading** collapses, by construction, to the **per-slot reading**
$\Gamma_s=\mathrm{diag}\big(q_S(S\mathbf{e}_0),q_A(\mathbf{A}),q_I(\mathbf{I}),q_R(\mathbf{R})\big)$ used
in the companion instantiation work — the two are not independent alternatives licensed separately by A2;
the per-slot reading *is* the congruence reading evaluated at the one gauge consistent with treating $S$
as grade-0 (no cross-coupling to the vector slots, matching the grade-mismatch fact that $S$ and a
grade-1 attribute cannot pair under a grade-respecting product). Any other choice of $\mathbf{e}_0$ gives
the same signature by Sylvester (Corollary 4.2 below does not depend on which invertible $V$ is used) but
populates spurious $S$–$\mathbf{A}$, $S$–$\mathbf{I}$, $S$–$\mathbf{R}$ cross-entries with no counterpart
anywhere they are actually used — so the orthogonal $\mathbf{e}_0$ is not merely *a* valid gauge, it is
the canonical one, singled out by consistency with every explicit construction in this program.
Verification (existence, uniqueness, and the block-diagonal collapse, 5 random trials):
`models/calcs/brainstorming/papers/weld_clifford/puente_simbolo_gram_sylvester_prueba.py`, part IV.

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

*Remark 2.3 (the EOM does not retire $\Gamma_s,\Gamma_a$).* A3's equation is written for the undivided
$\Gamma$, and from here on the paper works mostly with $\Gamma$ as a single matrix — it is easy to read
this as A2's Force/Field split being used once, in §2, and then abandoned. It is not: every term of the
EOM acts on both sectors simultaneously, because $\ddot\Gamma=\ddot\Gamma_s+\ddot\Gamma_a$,
$\nabla^2_{\mathbf x}\Gamma=\nabla^2_{\mathbf x}\Gamma_s+\nabla^2_{\mathbf x}\Gamma_a$, and likewise for
$\gamma\dot\Gamma$, by linearity of $\Gamma\mapsto\Gamma_s,\Gamma_a$. The one term that is *not*
sector-blind is the potential: $P(\Gamma)$ in this paper's scope (§6, and Definition 2.1 of the
companion atlas work) is a functional of $\Gamma_s$ alone — the Force sector supplies the restoring
force, and $\Gamma_a$ is source-free and dissipation-free at this order, evolving only by inertia and
propagation. So the decomposition is not lost; it reappears as a statement about which terms of the EOM
each sector feels. This is used below without further comment (§6.1–6.2 recover Newton and Maxwell as,
respectively, the $\Gamma_s$-only and $\Gamma_a$-only limits of the same equation) and is made fully
explicit, with the spectral consequence at $\det\Gamma_s=0$, in the companion atlas work.

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
it is a genuinely different algebraic structure. This branch is not pursued further in this paper.
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

**Postulate A3′ (co-location — named explicitly, not derived).** A3 writes $\Gamma(\tau,\mathbf{x})$ as
a field over external coordinates $\mathbf{x}$ with a spatial Laplacian $\nabla_{\mathbf{x}}^2$, while
A1/Lemma 1 give an *internal* attribute space $\mathrm{span}\{\mathbf{A},\mathbf{I},\mathbf{R}\}$. Lemma
3's phrase "the spatial attribute directions of A1" silently identifies the two. This identification is
not forced by A1–A3 as stated: an ODU could in principle carry internal grade-1 attributes without those
attributes coinciding, as a vector space, with the coordinates over which it propagates. We name the
identification a fourth postulate, since the derivation genuinely needs it and it was previously used
without being declared:

> **A3′.** *The grade-1 attribute directions $\{\mathbf{A},\mathbf{I},\mathbf{R}\}$ are realized as
> tangent vectors of the same physical space over which $\Gamma$ propagates; i.e. the internal attribute
> space of A1 and the external coordinate space of A3 are one and the same $\mathbb{R}^3$.*

This is the natural reading whenever the attributes are ordinary spatial vectors (velocity, angular
momentum, a relational displacement) — objects that already transform as $SO(3)$ vectors under rotations
of the physical space the unit occupies, which is what "grade-1" was meant to capture in A1. It stops
being automatic once an attribute is not literally a spatial vector (e.g. the per-slot norms of §2's
Definition, where $q_S,q_I,q_R$ need not come from the coordinate metric at all). A3′ is therefore load-
bearing precisely at the joint the referee identified in Lemma 3 (§8.3): without it, Lemma 4 constrains
only the coordinate space $\mathbf{x}$, and says nothing about $\{\mathbf{A},\mathbf{I},\mathbf{R}\}$.
With it, the $(3,1)$ conclusion of Lemma 4 transfers onto the attribute space itself, which is what
Corollary 4.2 (below) requires to even be a meaningful question.

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

*Remark 3.2 (The ladder $\mathrm{Cl}_{3,0}\to\mathrm{Cl}_{3,1}\to\mathrm{Cl}_{4,1}$).* Lemma 3 is the
general mechanism by which a UoC's host algebra grows: a new generator is added exactly when A3's
smoothness condition exposes a genuinely independent direction that the existing generators cannot
express. Newton's second law (§6.1) is the $d=3$, no-time-generator floor: it needs no $\partial_\tau$
beyond an ordinary scalar time parameter, so its host is $\mathrm{Cl}_{3,0}$. Promoting $\partial_\tau$
to an independent grade-1 generator — forced once the EOM couples space and time symmetrically through
the wave operator $\Box$ (Lemma 4) — is exactly the step that produces $\mathrm{Cl}_{3,1}$, the host of
free electrodynamics (§6.2). A further UoC, explored outside this paper under the name UoC$_\mathrm{st}$
(spacetime as a dynamical unit in its own right, with $\rho$ as a genuine fifth attribute rather than a
derived quantity), exposes a *second* independent direction beyond the four of $\mathrm{Cl}_{3,1}$ — a
conformal/scale direction, verified numerically to require a spacelike generator ($e_\rho^2=+1$) to keep
the Gram signature Lorentzian, $(3,1)$, rather than degrading to $(2,2)$ under a timelike choice
($\mathrm{Cl}_{3,2}$). This fixes the host to $\mathrm{Cl}_{4,1}$, which contains $\mathrm{Cl}_{3,1}$ as
the even subalgebra of its Clifford grading (§30.3 of the companion exploration). The pattern across all
three steps is the same: *the temporal/scale component is never postulated — each new generator is forced
by a smoothness or signature-consistency condition applied to the previous algebra.* The full numerical
verification of the $\mathrm{Cl}_{4,1}$ vs. $\mathrm{Cl}_{3,2}$ signature comparison is given in the
companion code repository (§7); this extension is not part of the closed theorem of this paper and is
flagged as such in §8.3.

---

## 4. Main Theorem

**Theorem (Γ is forced).** *Given axioms A1, A2, and A3, the configuration of any operative dynamical unit
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
part of $F_{\mu\nu}$, and the electric part arises from the $\partial_\tau\wedge\nabla$ coupling. In the free-field sector, charge
conservation $\partial^\mu J_\mu = 0$ follows from the antisymmetry of $F$ without additional assumptions.
**Status: free Maxwell $\langle\mathrm{TEO}\rangle[\mathrm{D}]$; source equation $\langle\mathrm{A}\rangle$
(requires closing the cross-coupling block).**

*Remark 6.1 (reconciling two decompositions of $F$).* $\mathbf{I},\mathbf{R}$ here are ordinary grade-1
generators of $V^4$ (Lemma 3) — the same status as $\mathbf{A},\mathbf{I},\mathbf{R}$ in A1 — and
$\mathbf{I}\wedge\mathbf{R}$ is a genuine wedge of two grade-1 vectors, exactly the mechanism that
produces $\mathbf{L}=\mathbf{I}\wedge\mathbf{R}$ in the Newton limit (§6.1) or vorticity in the
Navier–Stokes correspondence. $B$ is grade-2 already in $\mathbb{R}^3$ (it is dual to the ordinary
grade-1 magnetic vector, i.e. an axial vector), so identifying it with $\mathbf{I}\wedge\mathbf{R}$
requires no change to A1. $E$, by contrast, is grade-1 in $\mathbb{R}^3$; it only becomes a bivector
component once lifted to $V^4$ by wedging with the temporal generator ($\partial_\tau\wedge\nabla$,
not $\mathbf{I}\wedge\mathbf{R}$). A companion exploration (Pieza 4, `pieza4_electromagnetismo.md`)
labels the two covariant halves of the *already-assembled* Faraday bivector $F$ as "$I=E$, $R=B$" under
a work-based criterion (which component does work on a charge). That labeling answers a different
question — how to split $F$ once it exists — and is not in tension with the derivation here, which
answers how $F$'s magnetic half is *built* from two grade-1 generators. The two readings share names
but not referents; they should not be conflated.

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
(i) the closure condition $\binom{d}{2}=d$ forces the dimension of the vector attribute space (Hurwitz confirms consistency); (ii) the wave operator fixes the signature; (iii) the reality of $\Gamma$ selects
$\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$ over the vector-space-isomorphic but algebra-distinct
$\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$. Step (iii) is a selection between signature conventions that a
metric-first derivation does not face and that other emergent-signature routes (§8.2) do not make; it is
specific to the demand that the configuration and its dissipative dynamics be real.
Neither step is obvious from the physics-first perspective.

The closest algebraic antecedent is the observation (Lounesto 2001, §17) that the Clifford algebra of
the symbol of the wave operator is $\mathrm{Cl}_{3,1}$. Here that observation becomes a theorem: within
axioms A1–A3 it is the *only* Clifford algebra consistent with a real, smoothly-evolving self-describing
unit.

### 8.1bis Corollary: the signature result exhausts the alternatives

Lemma 4 selects $(3,1)$. It is worth recording that the same argument, run over the full space of
candidate symbols rather than only the one A3 produces, *classifies* the alternatives rather than
merely excluding them — which strengthens the theorem at no additional cost.

**Corollary 4.1 (completeness of the regimes).** *Let $q$ be the principal symbol of a second-order
EOM on $V^4$, i.e. a real quadratic form on a $4$-dimensional space. Then:*
*(i) by Sylvester's law of inertia, $q$ falls into exactly one of $15$ congruence classes indexed by
$(n_+,n_0,n_-)$ with $n_++n_0+n_-=4$; the non-degenerate ones form $5$ connected components of the
space of such forms, since the inertia is a complete and locally constant invariant;*
*(ii) modulo the global sign convention $(n_+,\cdot,n_-)\sim(n_-,\cdot,n_+)$, exactly three regimes
remain — elliptic $(4,0)$, hyperbolic $(3,1)$, ultrahyperbolic $(2,2)$;*
*(iii) of these, exactly one, the Lorentzian $(3,1)$, yields a well-posed Cauchy problem. The
elliptic case is well-posed as a boundary-value problem but describes equilibrium, not evolution; the
ultrahyperbolic case has two temporal directions and is Hadamard ill-posed.*

*Proof.* (i) is Sylvester's law together with continuity of eigenvalues: a path between forms of
different inertia must pass through a degenerate form, so each class is open and closed in the
non-degenerate stratum. (ii) is the identification of a form with its negative. (iii) is the standard
PDE classification by principal symbol (Courant and Hilbert 1962, vol. II): all eigenvalues of one
sign gives an elliptic operator; exactly one of opposite sign gives a hyperbolic operator with
well-posed Cauchy data; two or more of each gives an ultrahyperbolic operator, for which the Cauchy
problem is ill-posed. $\square$

Two consequences for the reading of Lemma 4. First, the uniqueness of $(3,1)$ is not a statement
about a short list of physically motivated candidates: the list of *all* real signatures on $V^4$ is
finite, is exhausted above, and $(3,1)$ is the only survivor. Second, the excluded cases acquire
meaning rather than merely being ruled out — the elliptic class is the static/equilibrium regime, and
the ultrahyperbolic class is the genuine pathology. This matters because $\det$-based classifications
cannot see the distinction: $\det q>0$ holds for both $(4,0)$ and $(2,2)$, so the determinant sign
merges a physical regime with a pathological one, and only the full inertia separates them. A
companion paper uses precisely this stratification to organise the dynamical regimes of $\Gamma$.

*Scope.* Corollary 4.1 concerns the principal symbol — the object that fixes PDE type and
well-posedness. It should not be conflated with the inertia of the Gram matrix $\Gamma_s$ of A2,
which is a different object built from the attribute slots. The two signatures are, in general,
independent invariants of different objects; Corollary 4.2 states exactly when they must agree.

**Corollary 4.2 (when the Gram inherits the symbol's signature).** *Let $\eta$ be the symbol's
$(3,1)$ form (Lemma 4, under A3′) and let $\Gamma_s$ be built by the congruence reading of the
Definition in §2 (Axiom A2), $\Gamma_s = V^{\mathsf T}\eta V$ with $V=[S\mathbf{e}_0\mid\mathbf{A}\mid
\mathbf{I}\mid\mathbf{R}]$. Then $\mathrm{signature}(\Gamma_s)=\mathrm{signature}(\eta)=(3,1)$
whenever $V$ is invertible, with no further condition.*

*Proof.* This is exactly Sylvester's law of inertia: congruence by an invertible matrix preserves
signature. $\square$

The condition is sharp. With $\mathbf e_0$ fixed by the gauge closure of §2, the per-slot reading with
*heterogeneous* forms $q_S,q_I,q_R\neq\eta$ — used whenever the four attributes are not all measured
under the one form $\eta$, e.g. $S,\mathbf{I},\mathbf{R}$ carrying ordinary positive-definite norms with
no Minkowski content — is not a congruence of $\eta$ at all (it is still a congruence of *some* block
form, namely $q_S\oplus q_A\oplus q_I\oplus q_R$, but not of the single $\eta$ Corollary 4.2 requires).
Corollary 4.2 does not apply there, and $\Gamma_s$'s signature is free to range over all five classes of
Corollary 4.1(i); this is confirmed numerically in the companion instantiation work, where a massive
(particle) state lands on $(4,0)$, a photon state on the degenerate boundary, and a general-relativistic
state — where the attribute $\mathbf{A}$ genuinely *is* a Minkowski four-velocity, satisfying $\langle
\mathbf{A},\mathbf{A}\rangle_\eta=-c^2$ — on $(3,1)$, the one case closest to satisfying Corollary 4.2's
hypothesis. Verification:
`models/calcs/brainstorming/papers/weld_clifford/puente_simbolo_gram_sylvester_prueba.py`.

**Remark (no residual mystery).** The apparent tension — "the symbol forces $(3,1)$" versus "the Gram
ranges over five sectors" — dissolves once the two constructions of §2 are told apart. There is no
hidden inconsistency: the symbol's $(3,1)$ is a fixed background fact about the operator (governs
whether *evolution of the field* $\Gamma(\tau,\mathbf{x})$ is well-posed); the Gram's signature is a
state-dependent fact about the *value* $\Gamma_s$ takes at an instant (classifies the *regime of that
state*). They coincide, by theorem, exactly on the congruence reading with $V$ invertible; they are
free to differ, also by theorem (Sylvester simply does not constrain a non-congruence construction),
under the per-slot reading. Which reading a given physical domain uses is a modelling fact about that
domain, not a gap in the algebra.

### 8.2 Relation to emergent-signature approaches

The idea that the Lorentzian signature should be *derived* rather than *postulated* is not new, and this
paper does not claim priority for that program; it contributes a specific route. Two comparisons fix the
position of the present derivation.

Singh (2025) obtains a Lorentzian signature within an octonionic pre-spacetime theory by adopting *split*
division algebras: the split-complex unit $\omega$ with $\omega^2=+1$ gives a magnitude $x^2-y^2$
(Lorentzian) in place of $x^2+y^2$ (Euclidean), and split bioctonions then generate a base of signature
$(3,3)$ carrying embedded $4$-dimensional Lorentzian spacetimes. The signature there is a consequence of
*choosing split algebras*, a choice motivated by the target signature. The present derivation differs in
two respects. First, the mechanism: the signature is fixed by the requirement that the second-order
equation of motion (A3) admit a well-posed Cauchy problem — a Lorentzian principal symbol is the only one
that does (Lemma 4; Hadamard) — rather than by selecting a split number system. No split-ness is assumed;
the sign flip is forced by hyperbolicity of the evolution. Second, the target algebra is pinned to
$\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$ *specifically* — not the isomorphic-as-vector-space but
distinct-as-algebra $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$ — by the reality of $\Gamma$ (dissipative and
gradient dynamics are real processes; §8.1, §4). Singh's construction lives in higher dimension $(3,3)$
with embedded Lorentzian slices and does not make this reality-of-configuration selection between the two
signature conventions. The two derivations are therefore complementary: both answer "yes" to the
theorem-vs-postulate question, by independent mechanisms, and the present one is arguably the more
economical in its premisses (well-posedness of a real evolution, rather than a chosen split algebra).

More broadly, the view of an emergent Lorentzian signature has a long tradition in analogue and induced
gravity (Sakharov 1967; Barceló, Liberati and Visser 2011; Volovik 2003), where the effective Lorentzian
metric arises from the low-energy behaviour of a non-relativistic substrate. The present result is narrower
and purely algebraic: it does not construct an effective metric from a substrate, but identifies which real
Clifford algebra the structure of a self-describing dynamical unit forces. It is offered as a structural
companion to those programs, not a replacement.

### 8.3 Honest scope

This paper establishes the algebraic structure. It does not:
- Prove uniqueness of the SAIR attribute structure independent of A1 (that is the content of A1 itself,
  which we take as foundational rather than derived)
- Close the $d=7$ (octonionic) branch (open problem; not pursued in this paper)
- Close the further ladder step $\mathrm{Cl}_{3,1}\to\mathrm{Cl}_{4,1}$ sketched in Remark 3.2: the
  conformal/scale generator's necessity is verified numerically in the companion exploration but not yet
  derived from A1–A3 with the same rigor as Lemmas 1–4
- Establish instance-level **uniqueness** of the SAIR slot assignment (Remark 2.1's qualification): which
  observable quantity of a given ODU fills $S$ versus $\mathbf{A},\mathbf{I},\mathbf{R}$ is not decided by
  the container theorem. A necessary condition (representation compatibility, Schur) follows from the same
  argument as Lemmas 2–4; sufficient selection criteria are the subject of a companion, less mature line of
  work (seven domains checked by blind retrodiction and active rejection of incorrect-but-compatible
  assignments) that is intentionally kept out of this paper rather than diluting its closed lemmas with an
  open one
- Establish, for a given domain, **existence** of a SAIR quadruple in the first place (Remark 2.1's second
  qualification): whether $\mathbf{A},\mathbf{I},\mathbf{R}$ arise as grade-1 vectors at all is empirical,
  not algebraic, and fails in most domains tested (13/20 in a companion scan). This is logically prior to,
  and independent of, the uniqueness question above — the container theorem is conditional on existence and
  proves nothing about it

Two structural gaps were identified in an earlier draft; both are now named and given precise
(partial) resolutions rather than left as bare admissions, since a named gap that is only asserted
open, without stating exactly what would close it, is not yet doing its job.

**(a) The attribute space and the coordinate space were identified without argument — now Postulate
A3′.** A1 and Lemma 1 give an *internal* attribute space $\mathbb{R}^3$ spanned by
$\{\mathbf{A},\mathbf{I},\mathbf{R}\}$. A3 treats $\Gamma(\tau,\mathbf{x})$ as a field over an
*external* coordinate space carrying $\nabla_{\mathbf{x}}^2$, and Lemma 4 reads the signature off that
Laplacian. The step identifying the two spaces is now named explicitly, immediately after Lemma 3, as
**Postulate A3′**: the resolution is not to derive the identification from A1–A3 (it is not derivable
from them; an ODU could in principle carry internal attributes that do not coincide with its
propagation coordinates) but to state it as a fourth, independent premise, exactly as A1's own
irreducibility is handled in Remark 2.1. This is a genuine strengthening, not a rebranding: the
theorem's reach was always conditional on A3′; the reader can now see that condition and evaluate it,
rather than absorb it silently inside "the spatial attribute directions of A1" in Lemma 3.

**(b) Two distinct objects were both called "the signature" — now Corollary 4.2.** Lemma 4 and
Corollary 4.1 concern the inertia of the *principal symbol* on
$V^4=\mathrm{span}\{\mathbf{A},\mathbf{I},\mathbf{R},\partial_\tau\}$. A2 independently supplies a Gram
matrix $\Gamma_s$ of the slots $\{S,\mathbf{A},\mathbf{I},\mathbf{R}\}$ (§2, Definition), which also
carries an inertia. These need not agree in general — they are different $4$-spaces, and the Gram's
construction admits two readings (§2). Corollary 4.2 closes this with an exact condition rather than
a bridge asserted or merely hoped for: the Gram inherits the symbol's $(3,1)$ signature, by Sylvester's
law of inertia, precisely when it is built as an authentic congruence $V^{\mathsf T}\eta V$ with $V$
invertible; under the alternative per-slot construction (also licensed by A2, and the one used whenever
an attribute carries no Minkowski structure of its own) no such inheritance is claimed or needed, and
the signature is free to range over all admissible classes — which is exactly what a companion paper
observes when it reads dynamical regimes off the Gram. Nothing here was contradictory; the two readings
of the Definition in §2 were simply not told apart before.

The residues that remain open after P1/P2/P3 are the three original axioms A1, A2, A3, together with
the newly named Postulate A3′. Gap (a) is resolved by declaring A3′ as a premise — its truth for a
given physical domain remains a modelling question, not a theorem, and is flagged as such. Gap (b) is
resolved outright: Corollary 4.2 is a theorem with a checkable hypothesis, not an open problem. The
cost of explicitness: four axioms instead of two, and one corollary earning its keep instead of a
promissory note. The gain: no premiss enters the derivation undeclared, and the one place where two
different "signatures" could be silently conflated no longer can be.

### 8.4 Related work

- Hurwitz (1898): normed division algebras in dimensions 1, 2, 4, 8.
- Eckmann (1943): cross products in $\mathbb{R}^n$ exist only for $n = 1, 3, 7$.
- Atiyah, Bott and Shapiro (1964): Clifford modules and Bott periodicity.
- Hestenes (1966, 1986): spacetime algebra as the language of physics.
- Doran and Lasenby (2003): geometric algebra for physicists (Cambridge).
- Lounesto (2001): Clifford algebras and spinors (Cambridge).
- Adams (1960): vector fields on spheres; confirms Hurwitz via K-theory.
- Sakharov (1967): induced gravity; the metric as an emergent elastic response.
- Barceló, Liberati and Visser (2011): analogue gravity (Living Rev. Relativity); emergent Lorentzian
  metrics from non-relativistic substrates.
- Volovik (2003): *The Universe in a Helium Droplet* (Oxford); emergent relativity and effective metric
  in quantum liquids.
- Singh (2025): trace dynamics, octonions and unification; Lorentzian signature from split bioctonions.
  arXiv:2501.18139.
- Molina (2024a): the determinant as the source of the cubic term in matrix gradient flows. DOI: 10.5281/zenodo.20752208

---

## 9. Conclusions

From four structural axioms — SAIR attribute structure (A1), geometric product (A2), continuous
smooth evolution (A3), and co-location of the attribute space with the propagation coordinates (A3$'$) —
the real Clifford algebra $\mathrm{Cl}_{3,1}$ emerges as a structural theorem rather than a geometric
postulate. The derivation chain is:

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

The result provides a structural basis for the spacetime algebra program: not "given Minkowski
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
