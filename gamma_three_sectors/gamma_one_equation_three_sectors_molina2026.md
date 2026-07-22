---
title: "Γ: One Equation of Motion, Three Sectors"
subtitle: "Structural correspondences with Newton, Navier-Stokes, Maxwell, and Schrödinger"
author: "Henry Molina · Independent researcher, Bogotá, Colombia · henrymolina@gmail.com"
date: "July 2026"
---

DOI: 10.5281/zenodo.21496578  

*Self-contained manuscript beyond the algebraic theorem of the companion paper (Molina 2026,
"Spacetime Algebra as a Theorem"), which this article reuses without re-deriving. Numerical
verifications cited throughout the text are in `code/` (see Appendix B), and in
`models/calcs/brainstorming/` for additional exploratory calculations.*

**Notation convention.** Every claim carries two independent tags. The first names the
**register**: 〔DEF〕 definition, 〔TEO〕 theorem or lemma, 〔CE〕 structural correspondence
(isomorphism or algebraic relabeling with a known physical object, not a new physical theorem),
〔IF〕 finding/hypothesis under investigation, 〔A〕 claim not yet closed. The second, in square
brackets, names the **degree of certainty**: [D] proved analytically, [V] verified numerically
(without a closed analytic proof), [A] open/unresolved, [F] frontier outside the scope of this
paper. For example, 〔TEO〕[D] is a theorem with a complete proof; 〔CE〕[V] is a structural
correspondence confirmed by numerical verification, not by an analytic proof that the
correspondence is exact in general.

# Abstract

This paper does three things in a single argument. First, it derives — not postulates — why the
configuration of any operative dynamical unit (ODU) lives in $M_4(\mathbb{R})$
given two minimal axioms (the SAIR ontology and the geometric product as the coupling law) plus an
explicit minimality criterion: the Hurwitz/Eckmann theorem forces the dimension, the Clifford
algebra $\mathrm{Cl}_{3,1}$ is fixed by the signature of the equation-of-motion symbol, and the
Frobenius norm emerges as the unique metric compatible with that structure. Second, it shows that
the coupling matrix $\Gamma$, subjected to the gradient dynamics of a potential $P(\Gamma,\rho)$,
organizes into three sectors separated by a single topological condition —
$\mathrm{sign}(\det\Gamma)$ — and that crossing that boundary is a mathematically rigorous
bifurcation (the $\Gamma\to\xi$ theorem), not a qualitative observation. Third, it walks through
the resulting catalog of dynamical recoveries: Newton, Navier-Stokes, free Maxwell, and free
Schrödinger as closed, verified structural correspondences; and, for the linearized Einstein
regime in harmonic gauge, it carefully separates a fact of standard general relativity —
$\nabla^2\Phi=4\pi G\rho$ traversed without adjusting any factor by the program's own machinery —
from the **conditional** restriction specific to GSF: *if* the correspondence
$\Gamma_s\sim\bar h_{\mu\nu}$ holds, the matter-coupling coefficient is forced, not adjustable. For
the nonlinear regime (the full Einstein equations) we report the actual state of the program: two
closed ingredients of Jacobson's thermodynamic route, a third precisely bounded but open, and a
recent positive finding on the mass sector (a dRGT-type construction with reference metric
$f=\eta$) that reproduces exact Fierz-Pauli at quadratic order. This paper's success criterion is
not the prediction of new physics: it is that a single algebraic object, with a single equation of
motion, correctly organizes four centuries of physics under precise and verifiable conditions —
with the boundaries named where the program does not yet close.

---

# 1. Foundation — why $\Gamma \in M_4(\mathbb{R})$

## 1.1 The two axioms

**〔DEF〕 A1 (SAIR — ontology).** Any dynamical unit is characterized by four intrinsic attributes:
**S** (scalar, grade 0 — *what it is*, essence) and **A, I, R** (vectors, grade 1 —
*what it can do*, capacity; *what it does*, act; *context*, relation). This is a postulated minimal
decomposition, not derived from prior physics — it is Aristotelian in spirit, and is read in third
person (domain-neutral), not as psychological phenomenology.

**〔DEF〕 A2 (geometric product — force/field).** The dynamics of an ODU is governed by the
**geometric product** of its attributes. In the geometric algebra $G(3)$, the product of two
grade-1 elements decomposes canonically into a symmetric grade-0 part and an antisymmetric grade-2
part: $uv = u\cdot v + u\wedge v$. Applied to SAIR, this gives **Force**
$F=S\cdot A$ (symmetric) and **Field** $\mathcal{F}=I\wedge R$ (antisymmetric, Hodge dual of the
cross product $I\times R$). This force/field decomposition is not an additional postulate — it is
an automatic algebraic consequence of A2 in $G(3)$. The only genuine postulate of A2 is: *dynamics
uses the geometric product*.

**〔IF〕 Genuine-ODU criterion — the program's falsifiable hypothesis.** A1+A2 fix what
*the container* is algebraically; they do not guarantee that a given system fills it. The working
hypothesis of the whole program, made explicit here so that it is falsifiable, is stronger than
"a vector candidate exists": **an ODU/UoC is characterized by the four SAIR attributes
intrinsically, with Force and Field inherent, and with a characterizable kinematics and
dynamics** — that is, if $S,A,I,R$ genuinely exist (not as a relabeling of some arbitrary variable)
and $F,\mathcal F$ are inherent to the system (not imposed), then the system exhibits the
kinematics/dynamics that the EOM of §4 predicts for its sector. The counterexample that would
falsify this is not a domain *without* a vector candidate (that simply says the container does not
apply there, see §8.1) — it is a domain *with* genuinely detectable SAIR and F/E that nonetheless
fails to follow the characteristic kinematics/dynamics of its sector. No such case has been found
so far among the domains resolved (§3, §5); none has been sought systematically either — it
remains an explicit falsification criterion, not a result.

Everything that follows in this section is a chain of four lemmas — each a forced consequence of
A1+A2, not an additional choice.

## 1.2 Lemma 1 (dimension) — Hurwitz forces dim 3

〔TEO〕[D]. By A2, the Field is $\mathcal F=I\wedge R\in\Lambda^2(\mathbb R^d)$, a bivector of
dimension $\binom{d}{2}$ — not yet a cross product: that has to be earned. For the ODU to be
**closed** (for $\mathcal F$ to couple back to the grade-1 attribute $A$ without introducing an
object of higher rank than those of A1), the Field space and the attribute space must be
isomorphic as vector spaces: $\binom{d}{2}=d\Rightarrow d(d-1)=2d\Rightarrow d=3$ (the only
nontrivial solution). That isomorphism *is* the Hodge duality $\star:\Lambda^2(\mathbb R^3)
\xrightarrow{\sim}\mathbb R^3$, which turns $\mathcal F=I\wedge R$ into the cross product
$I\times R$ — the identification "Field = cross product" is the **conclusion** of closure, not its
starting point. Only then does Hurwitz enter, as a consistency confirmation: by the
Eckmann/Hurwitz theorem, a vector cross product ($V\times V\to V$, bilinear, antisymmetric, with
$|u\times v|^2=|u|^2|v|^2-(u\cdot v)^2$) exists uniquely in dimension 1, 3, or 7 — equivalent to
the existence of a normed division algebra of dimension $n+1$: $\mathbb{R},\mathbb{C},
\mathbb{H},\mathbb{O}$ — and confirms that $d=3$ indeed admits a nondegenerate one; Hurwitz is not
the source of the derivation, closure is (Hurwitz alone would not rule out $d=1$ or $d=7$ either,
which closure does rule out). Dimension 1 is degenerate (the cross product vanishes); dimension 2
gives a scalar, not a vector. Exactly two nontrivial branches remain:

- **Dim 3 ($\mathbb{H}$ branch):** unique cross product $\Rightarrow$ $A,I,R$ = orthonormal basis
  of $\mathbb{R}^3$. The spacetime branch — where all the physics of this paper lives.
- **Dim 7 ($\mathbb{O}$ branch):** octonionic cross product $\Rightarrow$ an internal/atemporal
  realization, a candidate for color/generation structure (open frontier, outside the scope here).

*Why exactly three vector attributes* reduces to closure $\binom{d}{2}=d$, not to
Hurwitz — Hurwitz confirms that $d=3$ works, closure is what forces it. It is not a choice.

## 1.3 Lemma 2 (algebra) — $A,I,R$ generate $\mathrm{Cl}_{3,0}=G(3)$

〔TEO〕[D]. In dimension 3, the three grade-1 vectors (linearly independent) generate the full
geometric algebra $G(3)$: $8=2^3$ dimensions — grade 0 = $S$, grade 1 = $A,I,R$,
grade 2 = the bivectors (Field, via Hodge dual), grade 3 = pseudoscalar. No fifth grade-1
generator is needed.

## 1.4 Lemma 3 (time) — dynamics adds a fourth direction

〔TEO〕[D]. The equation of motion (§4) is second order; its principal part is the wave operator
$\Box\Gamma=\ddot\Gamma-c^2\nabla^2\Gamma$. The fourth (temporal) direction is
$\gamma_0=\partial_\tau$ — the ODU's own evolution — not a fifth attribute. The rank of
$\{A,I,R\}$ is exactly 3; $S$ is grade 0 (scalar, not a vector); promoting any of
$A,I,R$ to a fourth independent direction would break the symmetry and miscategorize the
attribute. The fourth direction has to come from outside the set of attributes, and dynamics
— which the framework already possesses — provides it.

## 1.5 Lemma 4 (signature) — Lorentz is read, not postulated

〔TEO〕[D]. The Fourier symbol of $\Box$ ($\partial_\tau\to i\omega$,
$\nabla\to ik$) is $-\omega^2+c^2|k|^2$ — exactly the Minkowski quadratic form, signature
$(3,1)$. The Lorentzian signature **is not postulated: it is read** from the equation of motion. The
real Clifford algebra of that signature is $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$: verified that
the real $4\times4$ representation satisfies $\{\gamma_\mu,\gamma_\nu\}=2\eta_{\mu\nu}$ with
$\gamma_0^2=-1$ forced by reality and $\gamma_i^2=+1$.

## 1.6 Theorem (Γ) — the configuration is forced

**〔TEO〕[D] Theorem.** *Given A1 and A2, the configuration of an ODU is necessarily*
$$\boxed{\;\Gamma \;=\; \Gamma_s \oplus \Gamma_a \;\in\; M_4(\mathbb{R}) \;=\; \mathrm{Cl}_{3,1}\;}$$
*where $\Gamma_s=\mathrm{Gram}(S,A,I,R)$ (Force sector, symmetric, 10 components) is the unique
canonical map from the algebra, and $\Gamma_a$ (Field sector, antisymmetric, 6 components)
decomposes into magnetic ($I\wedge R$, space-space) and electric ($\partial_\tau\wedge\nabla$,
spacetime).*

**Why $\Gamma$ and nothing else.** A metric (symmetric form) carries only Force; a
symplectic form (antisymmetric) carries only Field. $\Gamma=\Gamma_s\oplus\Gamma_a$ is the
unique **minimal** object that carries both simultaneously. The real $4\times4$
structure ($\mathrm{Cl}_{3,1}$) is forced by: dimension 3 (Lemma 1) + time as evolution (Lemma 3) +
reality (Lemma 4).

*Honest precision about "minimal".* The word "minimal" in the preceding paragraph is an
additional criterion, not a consequence of A1+A2 alone: A1+A2 make it fertile and coherent to
carry Force and Field in a single object, but they do not formally exclude a *larger* object that
also does so (e.g., with redundant structure). "Forced" in this theorem means *forced
given the minimality criterion*, not forced absolutely and independently of that criterion —
minimality is not the same as logical necessity. This is the one point in the chain where an
aesthetic/economy criterion (and not algebra alone) comes into play; it is named here explicitly
instead of being left implicit in the word "unique".

**Proposition (Frobenius, [D]).** The metric on the space of configurations is the Frobenius
norm, $\langle A,B\rangle=\tfrac14\mathrm{Tr}(A^\top B)$ — the canonical Clifford inner product
($\langle A\tilde B\rangle_0$, the scalar component of the geometric product with the
reverse). By Schur's lemma applied to the action of $\mathrm{Spin}(3,1)$ on the
grade decomposition, any $\mathrm{Spin}(3,1)$-invariant bilinear form is
proportional to this trace on each grade block; the submultiplicativity condition equalizes
the constants across blocks. Frobenius is not a choice made after constructing
$\Gamma$ — it is determined by A2.

The two remaining axioms (A1: SAIR is the minimal decomposition of any dynamical description;
A2: dynamics uses the geometric product) are the genuine foundation of the chain —
they are not derived from anything deeper, and should not be. With them, everything else —
dimension, algebra, time, signature, metric, and the very existence of $\Gamma$ — is theorem, not postulate.

---

# 2. Sector dynamics — crossing $\det\Gamma=0$ is a bifurcation

## 2.1 The potential and its invariants

**〔DEF〕.** The dynamics of $\Gamma$ is governed by a potential that depends on exactly
two invariants:
$$P(\Gamma,\rho) = \|\Gamma\|_F^2 + \mu(\rho)\det\Gamma + \beta\|\Gamma\|_F^4, \qquad \beta\geq|\mu|/16$$
The bound $\beta\geq|\mu|/16$ (AM-GM) is not a choice: it is the condition for $P$ to be
bounded below in the presence of a $\mu\det\Gamma$ term of either sign.

**〔TEO〕[D] (exact curvature formula).** For $\Gamma_0=\mathrm{diag}(\lambda_1,\ldots,
\lambda_4)$ and an antisymmetric fluctuation in direction $(i,j)$ (entries $(i,j)$ and $(j,i)$,
rest zero), the normalized curvature of the potential in that direction is *exactly*
$$m_{\rm eff}^2 = 2 + \mu\frac{\det\Gamma_0}{\lambda_i\lambda_j} + 4\beta\|\Gamma_0\|_F^2$$
*Proof.* With $E^{ij}$ the unit antisymmetric generator of that direction
($\|E^{ij}\|_F^2=2$) and $\Gamma(\varepsilon)=\Gamma_0+\varepsilon E^{ij}$: $\|\Gamma(\varepsilon)
\|_F^2=\|\Gamma_0\|_F^2+2\varepsilon^2$ (the linear term vanishes, $\Gamma_0$ is diagonal and
$E^{ij}$ off-diagonal); the determinant, restricted to the perturbed $2\times2$ block,
is $\det\Gamma(\varepsilon)=(\lambda_i\lambda_j+\varepsilon^2)\prod_{k\neq i,j}\lambda_k=
\det\Gamma_0(1+\varepsilon^2/\lambda_i\lambda_j)$ (direct block computation, not a cited
formula); and $\beta\|\Gamma(\varepsilon)\|_F^4=\beta(\|\Gamma_0\|_F^2+2\varepsilon^2)^2$. Summing
the three second-order-in-$\varepsilon$ contributions and dividing by $\|E^{ij}\|_F^2=2$ gives
the formula. Verified symbolically without approximation
(`models/calcs/brainstorming/papers/draft_atlas/verificacion_cota_amgm.py`). $\blacksquare$

**Honest finding: the bound $\beta\geq|\mu|/16\Rightarrow m_{\rm eff}^2\geq2$ for *every*
diagonal $\Gamma_0$, as stated in earlier program material, is FALSE.**
Explicit counterexample, verified symbolically (same script): with $\lambda_i=\lambda_j=
\delta\to0$ (the perturbed pair) and $\lambda_k=\lambda_l=t$ (the other pair, fixed), $\det\Gamma_0/
(\lambda_i\lambda_j)\to t^2$ while $\|\Gamma_0\|_F^2\to2t^2$ — both terms scale the same
with $t$, and for $\mu<0$ with $\beta=|\mu|/16$ (the limiting case of the bound), $m_{\rm eff}^2\to
2+t^2\mu/2\to-\infty$ as $t\to\infty$. The step that fails in the original proof
(not reproduced here since it is incorrect) is bounding $\|\Gamma_0\|_F^2$ as if it always
controlled the relevant ratio $\det\Gamma_0/(\lambda_i\lambda_j)=\lambda_k\lambda_l$ — but
$\|\Gamma_0\|_F^2$ can grow proportionally to $\lambda_k\lambda_l$ without the bound
$\beta\geq|\mu|/16$ (a fixed, scale-free ratio) being able to compensate for it.

**What was confirmed:** this counterexample configuration is **not a genuine equilibrium**
($\nabla P=0$) for any admissible $\beta\geq0$ — solving $\nabla P=0$ exactly in the
limit $\delta\to0$ gives $\beta=-1/4$, outside the physical domain.

**〔TEO〕[D] (version restricted to equilibria — CLOSED, jul-08 2026).** *For $\beta\geq|\mu|/16$,
the only equilibrium of $\nabla P=0$ with diagonal $\Gamma_0$ and $\det\Gamma_0\neq0$ is $\Gamma_0=0$
— that is, there is no nontrivial equilibrium in either of the two sectors ($\det>0$ or
$\det<0$).*

*Proof.* For any equilibrium with all $\lambda_i\neq0$, the identity
$$\lambda_i\cdot\partial_{\lambda_i}P - \lambda_j\cdot\partial_{\lambda_j}P = 2(\lambda_i^2-\lambda_j^2)(2\beta\|\Gamma_0\|_F^2+1)$$
(verified by direct expansion, not a cited formula) vanishes at equilibrium. The second
factor, $2\beta\|\Gamma_0\|_F^2+1$, is **always positive** for $\beta\geq0$ (sum of a
nonnegative term plus 1) — it can never vanish. Therefore $\lambda_i^2=\lambda_j^2$ for all $i,j$:
**every nontrivial equilibrium has all four $|\lambda_i|$ equal** to a common value $t>0$, without
exception — there are no "fully asymmetric" equilibria to look for. Only two families remain,
by the parity of the number of negative signs among the four $\lambda_i=\pm t$:

- **Even number of negative signs** ($\det\Gamma_0=+t^4$): the equilibrium equation gives
  $t^2=-2/(\mu+16\beta)$, which requires $\mu+16\beta<0$. But $\beta\geq|\mu|/16\Rightarrow16\beta
  \geq|\mu|\geq-\mu\Rightarrow\mu+16\beta\geq0$ — **contradiction**, no real solution.
- **Odd number of negative signs** ($\det\Gamma_0=-t^4$): the equation gives $t^2=2/(\mu-16\beta)$,
  which requires $\mu>16\beta$. But $\beta\geq|\mu|/16\Rightarrow16\beta\geq|\mu|\geq\mu\Rightarrow
  \mu\leq16\beta$ — **contradiction**, no real solution.

Neither family (which exhaust all possible sign patterns, up to permutation)
has a real solution when $\beta\geq|\mu|/16$. $\blacksquare$ Verified with sympy, without
approximation (`models/calcs/brainstorming/papers/draft_atlas/cota_amgm_restringida_equilibrios.py`).

**What this means, in full honesty.** The original claim of Theorem 3.1
("$P$ is stable in all sectors, including $\det\Gamma<0$") turns out to be **vacuously true**
in the strongest possible sense: for $\beta\geq|\mu|/16$ **there is no equilibrium living in
$\det\Gamma\neq0$** — neither in $\det>0$ nor in $\det<0$ — so there is nothing to "destabilize". The
oscillatory dynamics observed in the $\det<0$ sector (§2.2) cannot, in this regime, be understood
as oscillation *around a static equilibrium* — it must be genuinely transient/dynamical
from the start, or live in the complementary region $\beta<|\mu|/16$ (where nontrivial
equilibria do exist — including $\Gamma_\ast(\sigma)$ of §2.3, which requires $\mu>16\beta$, or
its opposite-sign analogue). This neither requires nor invokes non-equilibrium thermodynamics: it is a
result complete within the pure gradient flow — it simply clarifies *where* the
nontrivial equilibria live (outside this region), not that they cease to be genuine equilibria.

## 2.2 The sectors, counted by signature — completeness theorem

〔TEO〕[D]. A first, purely topological count is this: $\det:M_4(\mathbb{R})\to\mathbb{R}$ is
continuous, its zero set has codimension 1, and the complement has exactly two open connected
components; adding the boundary, three sectors. **That count is correct for
$M_4(\mathbb{R})$ but is not the classifier physics needs**, and it is worth saying why
before using it.

The type of the equation of motion — and with it well-posedness — is determined by the **symmetric
part** $\Gamma_s$, not the sign of $\det\Gamma$. And on $\mathrm{Sym}(4,\mathbb{R})$ the correct
invariant is the **inertia** $(n_+,n_0,n_-)$, which by Sylvester's law is a *complete*
congruence invariant and, by continuity of the eigenvalues, *locally constant*. It follows:

> **Theorem (completeness of sectors).**
> **(i)** *(Sylvester)* The inertia partitions $\mathrm{Sym}(4,\mathbb{R})$ into exactly **15**
> classes — finite and exhaustive by construction — the nondegenerate subset
> $\mathrm{Sym}^*(4,\mathbb{R})$ has **five** connected components, one per class:
> $(4,0)$, $(3,1)$, $(2,2)$, $(1,3)$, $(0,4)$.
> **(ii)** Modulo the global sign convention $(n_+,\cdot,n_-)\sim(n_-,\cdot,n_+)$, **three**
> regimes remain: elliptic, hyperbolic, and ultrahyperbolic.
> **(iii)** *(Hadamard)* Of the three, **exactly one** — the Lorentzian $(3,1)$ — supports a
> well-posed Cauchy problem. The degenerate classes ($n_0\ge1$, $\det\Gamma_s=0$) form the
> codimension-$\ge1$ boundary between them.

| Signature of $\Gamma_s$ | $\det\Gamma_s$ | PDE type | Regime |
|---|:---:|---|---|
| $(4,0)$ *(and its mirror $(0,4)$)* | $>0$ | elliptic | classical equilibrium: Newton, Stokes, Landau–Ginzburg |
| $n_0\ge1$ | $=0$ | degenerate (boundary) | massless wave, photon, criticality |
| $(3,1)$ *(and its mirror $(1,3)$)* | $<0$ | **well-posed hyperbolic** | relativistic evolution, $\Gamma_a$ active, Hopf-type |
| $(2,2)$ | $>0$ | ultrahyperbolic | **excluded**: two time directions, ill-posed Cauchy problem |

**Why the sign of $\det$ is not enough.** Since $\det\Gamma_s=(-1)^{n_-}\prod|\lambda_i|$, the sign
only registers the *parity* of $n_-$: it alternates $+,-,+,-,+$ across the five strata. That is why
$\det>0$ is the **union** of $(4,0)$, $(2,2)$, and $(0,4)$ — it lumps together the classical
equilibrium and the pathological ultrahyperbolic case — and $\det<0$ the union of $(3,1)$ and
$(1,3)$. The sign of $\det$ does not separate the components: it mixes them. It is the coarsest
shadow of the inertia (Corollary 8.1 of Paper C), useful as a coordinate but insufficient as a
classifier.

Moreover, $(4,0)$ and $(2,2)$ **are not adjacent**: moving from one to the other requires *two*
eigenvalues to cross zero, one at a time, so every path first passes through the Lorentzian
stratum $(3,1)$. The pathological region is separated from the classical one *by* the relativistic
region — a structure that the $\det$ axis folds and that `fig_atlas_map.png` now unfolds over
the $n_-$ axis.

*Verified numerically* (`models/calcs/brainstorming/papers/draft_atlas/completitud_sectores_sylvester_hadamard_prueba.py`):
exhaustive enumeration of the 15 classes; 20,000 random symmetric matrices, none with a signature
outside the enumeration; and the impossibility of connecting $(4,0)$ to $(2,2)$ without crossing a
degeneration (the straight segment and 100 random waypoint paths all cross).

**Status.** Part (iii) — the uniqueness of $(3,1)$ by well-posedness — is Lemma 4 of the
companion paper on $\mathrm{Cl}_{3,1}$ (Molina 2026); this theorem frames it by showing that it
also *exhausts* the alternatives and assigns them physical meaning. What remains 〔A〕 is not the
classification — closed, given the $4$ — but **physical completeness**: that classical physics is
exhausted by a single $4\times4$ $\Gamma_s$, which rests on Lemmas 1–3 (dimension), not on the
sector count.

## 2.3 Crossing as a bifurcation — the $\Gamma\to\xi$ theorem

The above describes *where* the three sectors live. What follows establishes that *crossing* the
boundary $\det\Gamma=0$ is not a post-hoc qualitative observation: it is a bifurcation in the
rigorous sense of dynamical systems theory, with explicit normal forms.

**〔TEO〕[D] ($\Gamma\to\xi$ reduction, codimension 1, gradient flow).** Let
$(\Gamma_\ast,\mu_\ast)$ be an equilibrium of $\dot\Gamma=-\nabla P$ with a **simple** soft mode
(a simple zero eigenvalue of the Hessian $H_\ast$, the rest of the spectrum bounded away from
zero) and transversality ($\tau=\langle V,\mathrm{adj}(\Gamma_\ast)^\top\rangle\neq0$, $V$ the
eigenvector of the soft mode). *Why the simple mode is not a free assumption*: the bare potential
($J=0$) depends only on $\|\Gamma\|^2$ and $\det\Gamma$, invariant under the two-sided orthogonal
action $\Gamma\mapsto U\Gamma V^\top$ — it is isotropic under $O(4)\times O(4)$, and its own
degeneracies are therefore *non-generic* (continuous symmetry produces clusters of
soft modes). A generic external field $J$ (entering linearly, without altering the Hessian)
breaks that isotropy and makes the soft mode simple — it is the formalization of
forcing, not a numerical trick. Under that condition, there exists, in a neighborhood, a
1-dimensional center manifold $\Gamma=\Gamma_\ast+\xi V+h(\xi,\mu)$ on which the dynamics
remains gradient, $\dot\xi=-\partial_\xi\Phi(\xi,\mu)$, reducing to the standard normal
forms of bifurcation theory:

- **Generic** ($a_3\neq0$): fold (saddle-node), $\dot\xi=\alpha-c\xi^2$.
- **$\mathbb{Z}_2$-symmetric** ($a_3=0$): pitchfork, $\dot\xi=-a_2'\xi-\tfrac16
  a_4^{\rm eff}\xi^3$.

**The determinant is the structural source of the cubic term**: $a_3=\mu_\ast D^3\!\det(\Gamma_\ast)
[V^{\otimes3}]+24\beta\langle\Gamma_\ast,V\rangle+\cdots$, with the determinant term as the
sole source when the soft mode is transverse to $\Gamma_\ast$. *The geometry of $\Gamma$ — its
determinant — fixes the type of bifurcation, not the size of $\Gamma$ (its norm).*

**〔TEO〕[V] (the AM-GM line is the bifurcation).** On the symmetric ray $\det<0$,
$\Gamma_\ast(\sigma)=\sigma\,\mathrm{diag}(1,1,1,-1)$ (an exact invariant subspace), the reduced
effective quartic coefficient is $(16\beta-\mu)$; its sign change — the pitchfork — occurs exactly at
$\mu=16\beta$, the same critical value that appeared in the Hessian bound of §2.1 (there,
however, we found that the general bound is not provable as previously thought — see the honest
finding of §2.1; this result on the specific invariant ray is independent and is
verified with genuine equilibria) and marks the orientation change $\det>0\to\det<0$. The
numerical coincidence between the two — the value $\mu=16\beta$ appearing in two distinct
calculations — remains intriguing, but can no longer be presented as "three phenomena converging
with no free parameter" until the status of the general Hessian bound is resolved. Verified
numerically, for the invariant ray (`pieza1_teorema_4x4.py`,
`pieza1_reduccion_normal_forms.py`): simple soft mode (gap 0.027), $a_3=5.09$ with a
structural contribution from the determinant ($-11.67$), saddle-node between genuine equilibria of
$\nabla P=0$.

**Honest scope.** The cusp (codimension 2, same gradient flow) and Bogdanov-Takens
(codimension 2, requires the tangent bundle $(\Gamma,\dot\Gamma)$, not a corollary of the
preceding theorem) are closed with numerical certificate, not with the same standard proof. The
homoclinic orbit and chaos of the reactive sector $\Gamma_a$ — where the active/vital regime lives,
$\gamma_{\rm eff}\leq0$ — are a program with model reduction, not a closed theorem: the rigorous
reduction of the 16+16-dimensional space to the reactive jerk, and the global Shilnikov condition,
remain an explicit 〔F〕 frontier.

---

# 3. Kinematics — the SAIR reading by domain

## 3.1 Dictionary by domain

Every physical domain is the same object $\Gamma$, read from the observable variables proper to
that physics:

| Domain | S | A | I | R | $\Gamma_a$ |
|---|---|---|---|---|---|
| Newton/Kepler | mass $m$ | acceleration $\mathbf a=\ddot{\mathbf x}$ (grade 1) | momentum $\mathbf p=m\mathbf v$ (grade 1) | position $\mathbf r$ (grade 1) | $\mathbf L=\mathbf I\wedge\mathbf R=\mathbf p\wedge\mathbf r$ (derived) |
| Navier-Stokes | pressure $p$ | fluid vel. $\mathbf u$ (grade 1, with an honest ambiguity — see source document) | $\mathbf u$ | $\nabla$ | vorticity $=I\wedge R=\nabla\times\mathbf u$ (standard identity, verified symbolically) |
| Statistical mech. | $Z(\rho)$ | energies $\lambda_i(\Gamma_s)$ | fluctuation $\sigma^2$ | temperature $1/\rho$ | $\sim0$ at equilibrium |
| Free Maxwell | charge $\rho_q=0$ | current $\mathbf J$ (grade 1) | $\mathbf A_\mathrm{vec}$ (vector potential) | $\nabla$ | $\mathbf B=I\wedge R=\nabla\times\mathbf A_\mathrm{vec}$ (same identity as NS); electric part $=\partial_\tau\wedge\nabla$ (different mechanism) |
| Schrödinger | charge/mass $q$ | momentum $\mathbf p=m\mathbf v$ (grade 1) | momentum $\mathbf p$ (grade 1, $=$ corrected Newton) | position $\mathbf r$ (grade 1, $=$ Newton) | $\mathbf L=\mathbf I\wedge\mathbf R$ (derived); $E_n\cdot\hat I$ as a derived invariant, $\hat I=e_1e_2e_3$ |
| Lorentz signature | rest energy $mc^2$ | 4-velocity $u^\mu$ (grade 1) | momentum $p^\mu$ (grade 1) | 4-position $x^\mu$ (grade 1) | $F_{\mu\nu}$, $\star^2=-1$ (all four were already grade 1 — this row never had the error) |
| Hopf/reactive | growth rate | reactive capacity | ⚠ dimension mismatch (2D vs 3D), unresolved | ⚠ same | $\omega_H$: the reduction to the normal form lives in 2D, does not fit directly in SAIR's 3D framework — see `correccion_grado_I_R_todos_dominios.md` |

**Foundational correction (jul-11 2026), an advance from this round — see
`brainstorming/physics/correccion_grado_I_R_todos_dominios.md`.** HM pointed out that $I,R$ must be
**both grade 1** (vectors), with the Field $\mathcal F=I\wedge R$ as a **derived** bivector — not
$I$=bivector and $R$=pseudoscalar directly, as in earlier versions of this table (except the Lorentz
signature row, which was already correct). Corrected and verified for Newton, Schrödinger (inherits
from Newton), Navier-Stokes, and Maxwell (the latter two via the standard identity
$\mathrm{curl}=\nabla\wedge(\cdot)$, with $R=\nabla$ playing the same formal role as
$\partial_\tau$ in the electric part of Paper B). Hopf/reactive is left with a genuine structural
discrepancy (2D dimension of the normal form vs. the 3D required by SAIR), not resolved for
convenience. H₂O is the next step.

**Correction (jul-11 2026).** The Newton/Kepler row was corrected to match
`brainstorming/unification/release/pieza1_anexo_newton.md` §1.1, the mapping already reviewed and
used in the three-body problem: $A$ must be the acceleration, not the velocity (formal condition
C5 — $A$ must be invariant under a Galilean boost, and $\mathbf v\to\mathbf v+\mathbf v_0$ while
$\mathbf a=g(\mathbf r)$ does not change), and $R$ occupies the pseudoscalar slot (grade 3, 1
dimension), not a vector — here, the specific orbital energy, not the position.

**Third correction (jul-11 2026) — Schrödinger.** The row used to read "mass $m$ / $\nabla\psi/\psi$ /
$\hbar\omega$ / $|\psi\rangle$", a formal correspondence without rigor. `pieza3_sector_cuantico.md`
§1 already proves a **quantum assignment theorem**: under conditions C1–C5 in $\mathrm{Cl}_{3,0}$
restricted to $\det=0$, the assignment $S=q$, $A=\mathbf p$, $I=\mathbf L=\mathbf r\wedge\mathbf p$,
$R=E_n\cdot I$ (the pseudoscalar $I=e_1e_2e_3$, $I^2=-1$, is Schrödinger's "$i$" without being
postulated) is the **unique** one that satisfies them — the same SAIR as Newton, in the $\det=0$
sector. Corrected.

**Second correction (jul-11 2026) — Navier-Stokes.** This row was also corrected to match
`brainstorming/ds/gamma_a_transporte_navier_stokes.md` (studies 01–05, [D]): the slot assignment is
**not phenomenological, it is forced by rotational covariance** — each observable occupies the
Clifford grade of its tensor rank, verified that rotors preserve grade. Pressure
(scalar) → grade 0 ($S$); velocity (vector) → grade 1 ($A$); **vorticity → grade 2 ($I=\Gamma_a$,
the same sector already listed in the $\Gamma_a$ column, now consistent with $I$ instead of
appearing informally duplicated)**; helicity $\mathbf u\cdot\boldsymbol\omega$ (pseudoscalar) →
grade 3 ($R$). The earlier row (density/vel./vorticity/deformation) did not reflect this derivation
— the deformation $\nabla\mathbf u$ is not a SAIR slot but the full tensor from which $A$ (vector)
and $I$ (vorticity) are extracted by symmetric/antisymmetric decomposition. Moreover, the
Navier-Stokes equation itself (including the self-advection term $(\mathbf u\cdot\nabla)\mathbf u$)
is **derived, not postulated**: Galilean covariance forces $\partial_t\to D/Dt=\partial_t+(\mathbf
u\cdot\nabla)$ (verified symbolically that only $D/Dt$, not $\partial_t$ alone, is form-invariant
under a boost). Euler emerges as the conservative limit $\gamma\to0$. The only remaining open
residue is the matrix-to-vector slot assignment (A-1), shared with Stokes and with the general
Clifford$\to M_4(\mathbb R)$ weld — a foundational gap, not specific to fluids.

**Two readings of SAIR, not in competition.** The foundational axiom A1 (§1.1) reads $A,I,R$ as the
**three abstract grade-1 generators** that force $G(3)$ (Lemma 1/2: why $d=3$, without yet
committing to which physical variable occupies each direction). This domain's table reads
$A,I,R$ already **instantiated** in a concrete physical domain — and there $I$ and $R$ can appear
at higher grades (bivector, pseudoscalar) because what is tabulated is the physical content that
fills each slot of the construction of $\Gamma$ (the Gram/wedge of A1), not the three raw
grade-1 generators of the abstract derivation. These are two levels of description of the same
object, not two alternative mappings — but this table should not be read as if it extended A1
literally grade by grade.

**Practical reading.** To build $\Gamma$ for a given system: identify $S$ (scalar
state variable), $A$ (capacity to act), $I$ (impulse or intrinsic cycle), $R$ (coupling to the
environment). Their geometric product — not any arbitrary $4\times4$ matrix — is the $\Gamma$ of
the atlas.

## 3.2 Dispersion relations by sector

〔CE〕. Linearizing $\Gamma(t,x)=\Gamma_0+\delta\Gamma\,e^{i(kx-\omega t)}$ around an
equilibrium, the tripartition of sectors gives three distinct dispersion branches:

| Sector | Dispersion $\omega(k)$ | Non-relativistic regime |
|---|---|---|
| $\det\Gamma>0$ | $\omega^2=c^2k^2+m_{\rm eff}^2$ | $\omega\approx m_{\rm eff}+c^2k^2/2m_{\rm eff}$ (Newton) |
| $\det\Gamma=0$ | $\omega=ck$ | — (massless by construction) |
| $\det\Gamma<0$ (active) | $\omega=\pm\omega_{\rm Hopf}(k)$ | oscillation without growth |

The complete spectral analysis (static snapshot vs. full propagator movie by sector, with the
corresponding figures) is presented in Appendix D.

---

# 4. The equation of motion

**〔DEF〕.**
$$\boxed{\ddot\Gamma + \gamma\dot\Gamma - c^2\nabla^2\Gamma + \nabla_\Gamma P(\Gamma,\rho) = N(t)}$$
$$\nabla_\Gamma P = \underbrace{2\Gamma}_{\text{elastic}} + \underbrace{\mu(\rho)\,\mathrm{adj}(\Gamma)^\top}_{\text{knows the sector}} + \underbrace{4\beta\|\Gamma\|_F^2\Gamma}_{\text{pins the norm}}$$

The term $\mu\,\mathrm{adj}(\Gamma)^\top=\mu\det(\Gamma)\Gamma^{-1}$ is the one that knows the
sector: it vanishes at $\det\Gamma=0$ (linearizing the EOM exactly there), stabilizes in
$\det\Gamma>0$, and drives the reactive dynamics in $\det\Gamma<0$ with $\mu<0$. It is the same
Lagrangian for all the cases that follow — zero new parameters per domain.

---

# 5. Dynamical recoveries

Each case follows a five-step protocol: (1) define the case's $\Gamma$; (2) spectral
analysis (critical mode, sign of $\det$); (3) bring in the EOM without re-deriving it; (4) reduce
by projecting onto the mode from step 2; (5) classify and name the boundary.

*Register note:* following the program's style guide, identifications of the form "this **is**
Newton/Maxwell/Schrödinger" are structural correspondences 〔CE〕 — an isomorphism or algebraic
relabeling with a known physical object — not new physical theorems. The verifiable contribution
is the mapping from SAIR/$\Gamma$; the internal algebraic reduction (projection, linearization) is
indeed theorem-grade mathematics and is marked separately where it applies.

## 5.1 Newton (〔CE〕[D], $\det\Gamma>0$)

*In the sector $\det\Gamma>0$ with $\Gamma_s\succ0$ and $\|\Gamma_a\|\ll\lambda_{\min}(\Gamma_s)$
(a loading condition — Remark: this does not follow from $\det\Gamma>0$ alone), the
Lyapunov-Schmidt projection onto the soft mode $\xi$ gives*
$$m_{\rm eff}\ddot\xi = F_{\rm eff} - \partial_\xi V_{\rm eff} - \gamma m_{\rm eff}\dot\xi$$
*which in the limit $\gamma\to0$ has the form of Newton's second law.* The projection itself
is 〔TEO〕[D] (Lyapunov-Schmidt, Papers A/B); the identification with Newton is the correspondence.
Verified numerically by sector (`calc1_newton_limit.py`): $a_1>0$ stable in $\det\Gamma>0$,
$a_1\to0$ at the boundary, $a_1<0$ signaling that the diagonal mode ceases to be the correct soft
mode in $\det\Gamma<0$.

## 5.2 Navier-Stokes (〔CE〕[D], $\det\Gamma>0$)

$\Gamma_s$ corresponds to the strain rate; $\Gamma_a$, to the vorticity.
Dispersion $\lambda\sim k^2$ (diffusion), with the non-modal amplification of the linearized
operator
$\mathcal{A}=\begin{psmallmatrix}0&I\\-\mathcal{L}_{\bar\Gamma}&-\gamma I\end{psmallmatrix}$
(generically non-normal) giving $G_{\max}\sim\mathrm{Re}^2$ — consistent in order of magnitude
with the observed $\mathrm{Re}_c^{\rm obs}=2040$ of pipe Poiseuille flow (PR-22).

## 5.3 Free Maxwell (〔CE〕[D], $\det\Gamma=0$)

With $\det\Gamma\to0$: $\mathrm{adj}(\Gamma)\to0$ and the EOM linearizes exactly — this step is
〔TEO〕[D], direct algebra. With $\Gamma_a=F_{\mu\nu}$ (grade-2 bivector) and $\gamma\to0$, the
linearized EOM takes the form
$$\partial_\mu F^{\mu\nu}=0, \qquad dF=0$$
which corresponds to free Maxwell and the Bianchi identity. The Bianchi identity follows from the
antisymmetry of $\Gamma_a$ ($d^2=0$), not from a postulated gauge symmetry. The photon mass
$m_\gamma=0$ is automatic: $\det\Gamma=0$ forces the null mode.

## 5.4 Schrödinger (〔CE〕[D]+[V] for the free particle, $\det\Gamma=0$)

**Actual, corrected status.** This case previously carried an incorrect historical citation
("verified to $\sim10^{-10}$" with no backing script), now corrected. The verified chain:
$\det\Gamma\to0^+$ linearizes the EOM $\Rightarrow$ Klein-Gordon, $(\Box+m^2)\Gamma=0$ with
$m^2=1$ (natural units) $\Rightarrow$ in the non-relativistic limit ($\Gamma=e^{-imt}\Psi$,
$|\partial_t\Psi|\ll m|\Psi|$), $i\partial_t\Psi=-\nabla^2\Psi/2m$. The correct complexification is
the standard positive-frequency projection of a real Klein-Gordon field — **not**
$\Psi=\Gamma_s+i\Gamma_a$, which fails due to dimensional incompatibility ($\mathrm{Sym}(4)$ is
10-dim, $\mathrm{Antisym}(4)$ is 6-dim). Verified with three independent steps (symbolic
Euler-Lagrange, numerical Klein-Gordon dispersion, wavepacket-to-envelope reduction with
decreasing error in $dk/m$): `schrodinger_from_gsf_eom_verificacion.py`.

**Named, honest frontier.** The case with a general external potential $V(x)$ — coupling
$V(x)$ as a position-dependent effective mass, $m^2\to m^2+2mV$ — has the correct analytic
reduction (verified for the harmonic oscillator), but the independent numerical verification did
not close: a residual error not diagnosed within the available time. It remains 〔A〕, not 〔D〕.

**§5.4bis — why the boundary is oscillatory: the spectrum, not the field.** The completeness
theorem (§2.2) classified $\Gamma_s$ by its inertia — correct for the PDE type, but
purely real: Sylvester only speaks of eigenvalues of a symmetric matrix. The imaginary
half is missing, and that is where the structural reason lives for why the boundary
$\det\Gamma_s=0$ is exactly where Schrödinger appears. **Scope clarification, so as not to
reopen an already-closed result:** this does NOT revive $\Psi=\Gamma_s+i\Gamma_a$ (§5.4 correctly
ruled it out, due to the dimensional incompatibility $10\neq6$). The new object is the
**spectrum** of $\Gamma=\Gamma_s+\Gamma_a$, not a recombination of the field. $\Gamma_a=\mathbf
I\wedge\mathbf R$ is real antisymmetric, so its spectrum is **purely imaginary** ($\pm i\lambda$)
by algebraic construction — no computation is needed for this, it is a property of every real
antisymmetric matrix. 〔V〕 sweeping $\Gamma_s(t)$ through $\det\Gamma_s=0$ with $\Gamma_a$ fixed,
the imaginary fraction of the full $\Gamma$ spectrum grows as the vanishing mode stops
contributing real weight, and in the pure limit $\Gamma_s\to0$ the spectrum is guaranteed purely
imaginary. A purely imaginary spectrum is the normal form of an evolution $e^{\pm i\omega t}$ —
phase oscillation with conserved amplitude —, the formal structure Schrödinger requires. 〔IF〕
this is the spectral reason the boundary is oscillatory: not because "Maxwell/the photon is per se
quantum", but because at the boundary the Force sector stops contributing real eigenvalues and the
Field sector — always purely imaginary — takes over. It does not derive Born's rule or $|\psi|^2$
(that remains 〔F〕); it is the precise spectral mechanism, now made explicit. Verified:
`models/calcs/brainstorming/papers/draft_atlas/frontera_det0_espectro_imaginario_prueba.py`.

---

# 6. Linearized Einstein — a conditional restriction, not a GSF theorem

*Register note, before starting.* The identity in this section combines two things of
different nature, and separating them is the central point of this version of the text (corrected
after review): (a) a fact of **standard general relativity**, known, not rediscovered
here; (b) a **GSF-specific** correspondence ($\Gamma_s\sim\bar h_{\mu\nu}$) which §6.3 itself
admits is not guaranteed for an arbitrary $\Gamma_s$. Marking the combination of
both as 〔TEO〕 without distinguishing them — as an earlier version of this text did — overclaims:
a theorem built on an unclosed correspondence is, at best, a
**conditional** result, not a clean theorem. What follows explicitly separates the two parts.

## 6.1 The vacuum in harmonic gauge: a cited GR fact + a GSF consistency check

**Established fact (standard GR, not new here).** Defining $\bar h_{\mu\nu}=h_{\mu\nu}
-\tfrac12\eta_{\mu\nu}h$ (trace-reversed) and imposing the harmonic/Lorenz gauge
$\partial^\mu\bar h_{\mu\nu}=0$, the linearized Einstein tensor reduces, in any
standard treatment of linearized gravity, to
$$G_{\mu\nu}^{(1)} = -\tfrac12\Box\bar h_{\mu\nu}$$
— the plain wave equation, with no cross terms. This is a textbook fact of general relativity;
it is not a contribution of this program.

**〔V〕 What is GSF-specific: a consistency check, not a discovery.** It was confirmed that the
program's own symbolic machinery reproduces this identity with exact rational precision
(30/30 nontrivial comparisons under exactly-imposed harmonic gauge,
`einstein_gauge_armonico_verificacion.py`). The value of this is methodological — it confirms that
the program's calculation tools have no errors in a case where the answer is already
known — not a new theorem.

**〔CE〕, conditional, the real point.** The form $\Box\bar h_{\mu\nu}=$source is *exactly* the
one already produced by GSF's Frobenius term, without modifying the Lagrangian — *if* the
correspondence $\Gamma_s\sim\bar h_{\mu\nu}$ is accepted and *if* the configuration satisfies the
harmonic gauge. Neither condition is established for a generic $\Gamma_s$ (§6.3). This
section establishes a **conditional consistency**, not a derivation.

## 6.2 The matter source: Newton's normalization as a restriction, not a prediction ready to test

**Established fact + consistency check.** Coupling $T_{\mu\nu}=\mathrm{diag}
(\rho,0,0,0)$ (static dust) to the identity of §6.1 via $G_{\mu\nu}=8\pi G\,T_{\mu\nu}$ (the
Einstein equation, the definition of $G$), solving Poisson for a point source and
trace-reversing (with sympy, not by hand, to avoid a sign error already made once in
this same calculation), the standard Newtonian limit is recovered exactly:
$$\Phi = -\frac{GM}{r}, \qquad \nabla^2\Phi = 4\pi G\rho$$
without adjusting any factor (`einstein_newton_normalizacion_verificacion.py`). This is also not a
new physics result — it is the well-known Newtonian limit of GR — what is verifiable here is
that the program's own calculation chain introduces no spurious factor while traversing it.

**〔CE〕, conditional — the real restriction.** *If* the correspondence $\Gamma_s\sim\bar
h_{\mu\nu}$ holds (not proved in general, §6.3) and *if* GSF couples matter to its own
field EOM, the coefficient that correctly reproduces Newton is **forced**:
$J=-16\pi G\,T_{\mu\nu}$, not an adjustable parameter. This is the correct way to present the
result: not "GSF predicts $J=-16\pi G\,T_{\mu\nu}$" flatly, but "*if* the program closes the
gaps of §6.3, the coefficient is forced to this value, and no other would be consistent with
Newton" — a structural restriction falsifiable in the strong sense (if the program closed and the
coefficient that emerged were different, the whole identification would fail), but conditional,
not a prediction ready for empirical testing today.

## 6.3 Honest frontiers of this identification

Three gaps, named with precision, not hidden:

1. **Dynamical reachability of the gauge.** The divergence $D_\nu=\partial^\mu h_{\mu\nu}$
   satisfies a homogeneous massive wave equation (temporal preservation: yes, $D_\nu=0$ is
   consistent), but no GSF-native gauge symmetry has been identified that guarantees, for *any*
   $\Gamma_s$, the existence of a transformation that brings it to satisfy the condition. It is a
   partial, not universal, identification — until §6.4.
2. **GSF's kinetic sector (Frobenius) admits no symmetry of this type**, for
   any generator, verified explicitly (not even as a total derivative of the action).
3. The "$+\Gamma_s$" term of the EOM (Klein-Gordon mass) does not cancel cleanly with
   $(\mu/2)\mathrm{adj}(\Gamma)^\top$ for any single $\mu$ — the effective mass coefficient
   splits between pure and mixed components in an incompatible way.

## 6.4 The identified fix — genuine Einstein-Hilbert + dRGT-type mass

The three gaps of §6.3 turned out to be the **same question**: the gauge freedom that in GR
simultaneously guarantees (a) reaching the harmonic gauge and (b) the ghost-free tuning of
Fierz-Pauli, is a single symmetry (linearized diffeomorphism). Two findings close this at
quadratic order:

**〔CE〕 Kinetic sector.** Adopting $\mathcal{L}_{\rm coord}=\sqrt{-\det\Gamma_s}\,R(\Gamma_s)$
— the genuine Einstein-Hilbert action, instead of $\mathrm{Tr}(\partial\Gamma_s^\top\partial
\Gamma_s)$ — solves the problem by definition: it is diffeomorphism-invariant by being
literally the EH action, with no need to tune any coefficient.

**〔CE〕[V] Mass sector.** With $\mathcal{K}=I-\sqrt{\Gamma_s^{-1}\eta}$ (a dRGT-type
construction, $f=\eta$ solved perturbatively, verified with sympy), the algebraic identity
$V=\beta_2\,e_2(\mathcal{K})=h_{\mu\nu}h^{\mu\nu}-h^2$ (the Fierz-Pauli mass term) is
confirmed exactly — zero residual on an independent instance (`f_como_eta_verificacion.py`) — and
this construction is consistent with $\mu\det(\Gamma)$ (which already gives $\Lambda=\mathrm{adj}(\Gamma)$,
with no interference at background or linear order): $\beta_2=4\mu$ corresponds to a massless
graviton (ordinary GR), consistent with GSF's own calibration ($\mu(\rho_{GR})=2$). The
algebraic identity itself ($V=e_2(\mathcal{K})\equiv$ Fierz-Pauli) is 〔TEO〕[V]; its reading as
"GSF's gravitational mass sector" is the correspondence.

**Real, unclosed remaining items:** (i) verification only at quadratic order — the genuine
statement of Boulware-Deser ghost-freedom is nonlinear, requiring the full
ADM/Hamiltonian analysis (dRGT 2010, Hassan-Rosen 2011), outside the scope of this work; (ii)
a reference candidate derived from $\Gamma_a$ ($f=-\Gamma_a^2$) was ruled out due to Euclidean
signature (a general algebraic fact); (iii) $f=\eta+\kappa\Gamma_a^2$ survives the signature
check but shifts the equilibrium point, requiring the tadpole analysis to be redone.

---

# 7. Full Einstein — the program's actual state

Since the general quadratic-action route did not close (§6), the nonlinear regime is attacked via
Jacobson's (1995) thermodynamic route: the full Einstein equations emerge from the
Clausius relation $\delta Q=T\,dS$ applied to local Rindler horizons, using the
exact Raychaudhuri equation — without linearizing anything.

## 7.1 Closed ingredient — the stress-energy tensor

**〔TEO〕[V].** Built via Noether's theorem from GSF's field Lagrangian, it was verified
exactly (not cited): (i) **conservation**, $\partial_\mu T^\mu_{\ \nu}=\sum_{ij}(\partial_\nu
\Gamma_{ij})\cdot\mathrm{EL}_{ij}$, an algebraic identity that vanishes automatically on
solutions of the EOM; (ii) **symmetry**, $T_{\mu\nu}=T_{\nu\mu}$ off-shell — stronger than what
Jacobson needs, without requiring the Belinfante-Rosenfeld improvement
(`einstein_completo_tensor_energia_momento.py`).

## 7.2 Closed ingredient — the full derivation

**〔CE〕.** The step-by-step derivation that the program's literature stated but
never showed was carried out: exact Raychaudhuri $\to$ area integration $\to$ heat
flux (with the $T_{ab}$ of §7.1) $\to$ Clausius $\to$ coefficient matching for every
null $k^a$ $\to$ Bianchi fixes the integration constant, arriving explicitly at
$$R_{ab}-\tfrac12Rg_{ab}+\Lambda g_{ab}=8\pi G\,T_{ab}$$
without linearizing at any step (`jacobson_raychaudhuri_clausius_derivacion.md`).

## 7.3 Open ingredient — the local area functional (Assumption 36.A)

**〔F〕, precisely bounded.** The argument needs $S_{\rm local}(p)=k_BA_{\rm local}(p)/
4\ell_P^2$ at each point, via a covariant area functional $A_{\rm local}:M\to\mathbb{R}_{>0}$ —
independent of which accelerated observer is chosen. The naive candidate
$\det(\Gamma(p))$ was ruled out with concrete evidence ($\sqrt{-g}$ is a density, not a scalar;
verified with an explicit counterexample, the 2-sphere in two coordinate systems). It was verified
(against two exact cases, $S^2$ and $S^3$) that a genuine curvature scalar, $R(\Gamma_s)$, via the
fixed-proper-radius geodesic-sphere formula, does resolve the observer-dependence; and it was
extended to the Lorentzian case (causal diamond, derived from scratch). Structural finding: "local
Planck $\rho$" and "cosmological global $\rho_{\rm spacetime}$" (already postulated in the program)
are two related but genuinely distinct regimes, with no single formula unifying them
yet.

## 7.4 Self-audit of the Einstein program

| Ingredient | Status |
|---|:---:|
| $\Lambda=\mathrm{adj}(\Gamma)$ (pure algebra) | [D] |
| $T_{ab}$ conserved and symmetric | [D]+[V] |
| Raychaudhuri+Clausius derivation, complete | [CE], not linearized |
| Kinetic sector (genuine Einstein-Hilbert) | [CE] |
| Mass sector (Fierz-Pauli via $e_2(\mathcal{K})$, $f=\eta$) | [V], quadratic order |
| Local area functional (Assumption 36.A) | [F], precisely bounded |
| Ghost-freedom at all orders | [F], out of scope |

---

# 8. Discussion

## 8.1 What is proved and what is not

This paper does not claim to have derived the full Einstein equations, nor a theory of
everything. It claims: (a) that $\Gamma\in M_4(\mathbb{R})$ is forced given two minimal axioms
**and** an explicit minimality criterion (§1.6) — not an arbitrary choice, but not an
absolute logical necessity independent of that criterion either; (b) that the crossing
$\det\Gamma=0$ is a rigorous mathematical bifurcation, not an observation; (c) that four master
physical laws are verifiable structural correspondences of a single EOM; (d) that the linearized
Einstein regime gives an exact quantitative restriction, **conditional** on a correspondence
($\Gamma_s\sim\bar h_{\mu\nu}$) and a few precisely named gauge gaps — not a prediction
ready to test today, and not a vague promise either; and (e) that the whole program is falsifiable
in the precise sense of the genuine-ODU criterion (§1.1): a domain with intrinsic SAIR and F/E
that failed to follow its characteristic kinematics/dynamics would refute it — no such case has
appeared, but none has been sought exhaustively either.

## 8.2 What the atlas does not resolve yet

| Frontier | Status | Note |
|---|:---:|---|
| Standard Model masses | [F] | requires an octonionic extension of $\mathrm{Cl}(3,1)$ |
| Full Einstein equations, all orders | [F] | ADM analysis pending |
| Schrödinger with a general external potential | [A] | correct analytic reduction, numerical verification unclosed |
| Dynamical reachability of the harmonic gauge in GSF | [F] | requires a native gauge symmetry, not yet identified |
| Number of generations (3) | [F] | geometry of $J_3(\mathbb{O})$ |
| AM-GM Hessian bound (original Theorem 3.1) | [A] refuted, [D] corrected version | counterexample for arbitrary $\Gamma_0$ (§2.1); **closed**: for $\beta\geq|\mu|/16$ there is no nontrivial equilibrium in any sector, a stronger result than the original |

---

# 9. Conclusion

Four centuries of physics — Newton, Maxwell, Schrödinger, Einstein — are not four theories awaiting
unification. This paper shows that they are four neighborhoods of a single mapped territory: one
algebraic object ($\Gamma\in M_4(\mathbb{R})$, forced by two axioms), one equation of
motion, and one topological condition ($\det\Gamma=0$) separating the regimes. The
result of greatest numerical precision — Newton's normalization from linearized Einstein in
harmonic gauge — combines a fact of standard GR (not new) with a conditional restriction
specific to GSF: *if* the correspondence $\Gamma_s\sim\bar h_{\mu\nu}$ holds, the
matter-coupling coefficient is forced, not adjustable — a strong structural restriction, but
conditional on named gaps, not a closed prediction. The full-Einstein program has, today,
two closed ingredients, one precisely bounded, and a recent positive finding on the mass sector
that completely reorders what remains to be done. This work's success criterion is not the
prediction of new physics — it is that the structural correspondence holds, with the boundaries
named where it does not close, and without overclaiming where the correspondence remains
conditional.

---

# References

Courant, R. and Hilbert, D. (1962). *Methods of Mathematical Physics*, Vol. II. Wiley.

de Rham, C., Gabadadze, G., and Tolley, A. J. (2010). Resummation of massive gravity. *Physical
Review Letters*, 106, 231101.

Hassan, S. F. and Rosen, R. A. (2011). Resolving the ghost problem in nonlinear massive gravity.
*Physical Review Letters*, 108, 041101.

Jacobson, T. (1995). Thermodynamics of spacetime: the Einstein equation of state. *Physical
Review Letters*, 75, 1260–1263.

Molina, H. (2024a). The determinant as an orientation invariant and the source of the cubic term
in equivariant matrix gradient flows. DOI: 10.5281/zenodo.20752208

Molina, H. (2026). Spacetime algebra as a theorem: deriving Cl(3,1) from the structure of a
dynamical unit. DOI: 10.5281/zenodo.21184515

---

\appendix

# Appendix A — The explicit equation of motion

$$\ddot{\Gamma} + \gamma\dot{\Gamma} - c^2\nabla^2\Gamma
  + \underbrace{2\Gamma}_{\text{elastic}}
  + \underbrace{\mu\,\mathrm{adj}(\Gamma)}_{\text{knows the sector}}
  + \underbrace{4\beta\|\Gamma\|_F^2\Gamma}_{\text{pins the norm}} = N(t)$$

# Appendix B — Calculation scripts

Verification copies included in `code/` alongside this paper (original source in
`models/calcs/brainstorming/`, within the program's repository):

```
code/
  calc1_newton_limit.py                          -> fig_calc1_newton_reduction
  calc2_dispersion_relations.py                  -> fig_calc2_dispersion
  calc2b_antisymmetric_hessian.py                -> fig_calc2b_antisymm_hessian
  calc3_coherence_responsiveness.py              -> fig_calc3_coherence_observables
  calc4_spectral_film.py                         -> fig_calc4_spectral_film
  calc_coulomb_couple.py                         -> fig_coulomb_couple
  verificacion_cota_amgm.py                      -> AM-GM bound, counterexample (§2.1)
  cota_amgm_restringida_equilibrios.py           -> AM-GM bound, version restricted to equilibria (§2.1)
  completitud_sectores_sylvester_hadamard_prueba.py -> sector completeness theorem (§2.2)
  frontera_det0_espectro_imaginario_prueba.py    -> imaginary spectrum at the boundary (§5.4bis)
  atlas_sectores_desde_sair_prueba.py            -> sector validation from SAIR data (§3)
  puente_simbolo_gram_sylvester_prueba.py        -> symbol-Gram bridge, shared with the companion paper
  schrodinger_from_gsf_eom_verificacion.py       -> reduction to Schrödinger (§5.4)
  einstein_gauge_armonico_verificacion.py        -> harmonic-gauge consistency (§6.1)
  einstein_newton_normalizacion_verificacion.py  -> Newton normalization from Einstein (§6.2)
  einstein_completo_tensor_energia_momento.py    -> T_ab conserved and symmetric (§7.1)
  f_como_eta_verificacion.py                     -> mass sector, f=η (§6.4)
  conexion_potencial_completo_lambda_masa.py     -> Λ=adj(Γ) and its connection to the mass sector
```

Requirements: `numpy`, `sympy`. No scipy needed.

# Appendix C — Illustrative example: Coulomb and Lorentz via the Coupling operation (Paper C)

**Status note (downgraded from "result" to illustrative example after review).** What follows
is **not** a general recovery in the sense of §5 — it is a concrete numerical example, on
specific field configurations, with an ad hoc postulated coupling block. It is included
for its pedagogical value (it connects the SAIR vocabulary with Coulomb/Lorentz, very
recognizable cases), not as additional evidence for the paper's central thesis.

**Correct anchoring.** The relevant composition operation between two ODUs is the **Coupling**
of Paper C (`paper_c_algebra_composicional.md`): given $\Gamma_A,\Gamma_B$, the coupling
produces $\rho_{AB}=\rho_A+\rho_B+\Delta_{\rm couple}$ with $\Delta_{\rm couple}=-\log\det(I-\Xi^\top
\Xi)\geq0$ ($\Xi$ the normalized singular values of the cross block $C_{AB}$) — a
well-defined $n$-ary morphism within Paper C's entropic multicategory, not a
Ch7 construction. The example that follows uses a particle-ODU and an EM-field-ODU coupled by
a cross block $C_{AB}$, in the same categorical spirit as Paper C, but **does not**
instantiate the full $\Delta_{\rm couple}$ formalism (Schur complement) — it is a simplification
with a specific coupling ansatz, chosen to reproduce Coulomb/Lorentz, not derived from
Paper C's general formula.

**〔IF〕, with an explicit ansatz.** The coupling block
$$C_{\mu\nu} = q\,A_\mu\,u_\nu$$
(the exterior product of the 4-potential and the 4-velocity) is **postulated** (not derived) —
the standard minimal-coupling form, analogous to gauge theory's minimal coupling. Decomposing via
the Force-Field theorem, $\Gamma_s(C)=(C+C^\top)/2$, $\Gamma_a(C)=(C-C^\top)/2$:

| Case | Configuration | Result |
|---|---|---|
| Static ($v=0$) | only $\Gamma_s(C)\neq0$ | Coulomb force, $q\mathbf E$ |
| Pure magnetic ($v\neq0$, only $B$) | only $\Gamma_a(C)\neq0$ | magnetic Lorentz force, $q(\mathbf v\times\mathbf B)$ |
| General | $\Gamma_s+\Gamma_a$ | full Lorentz, $q(\mathbf E+\mathbf v\times\mathbf B)$ |

Verified numerically (`calc_coulomb_couple.py`): the force computed from $f^\mu=qF^{\mu\nu}
u_\nu$ matches exactly the three expected configurations. The coherence observable
$C$ of the **coupling block** (not of the field $F_{\mu\nu}$, which is always $C=1$) transitions
from $0$ (Coulomb, conservative) to $1$ (magnetic/Josephson, reactive) continuously under
interpolation — the electrostatic-to-radiation transition is a $C(C_{12})$ transition.

**Frontier:** this is an inter-ODU coupling (particle—field), distinct from the intra-ODU
$F=S\cdot A$ of §1.2, which is the free propagator. Formally connecting this construction with
Paper C's $\Delta_{\rm couple}$ (instead of the hand-chosen ansatz $C_{\mu\nu}=qA_\mu u_\nu$), and
the generalization to Coulomb/Lorentz as a recovery *within* a single $\Gamma$ (without coupling
two ODUs), remain open.
Additionally, the magnetic and general cases in the script use vector potentials
$A_\mu$ explicitly marked as "simplified" in the source code itself — not derived
systematically from the given field $F_{\mu\nu}$, but chosen ad hoc to reproduce the expected
result. The static case (pure Coulomb) does use the correct, complete potential. The three cases
are numerical consistency checks on specific field configurations, not a general
derivation of $A_\mu$ from an arbitrary $F_{\mu\nu}$.

**Coherence note (jul-11 2026).** Ch7 (`part1/07_compositional_operations.md`, §7.3.3)
now explicitly distinguishes two coexisting dynamical layers in any Coupling: (i) the
state layer — each ODU retains its own dynamics, identity, and equation of motion,
modulated by the coupling; (ii) the configuration layer — the coupling block itself
$C_{AB}$ (here, $C_{\mu\nu}=qA_\mu u_\nu$) is an object with its own dynamics, governed by its
components and the external context. The $\Delta_{\rm couple}$ formula used above is exact as a
static algebraic fact about the joint block under either reading; a
claim about how the particle-field coupling itself evolves *in time* (beyond
the fixed ansatz $qA_\mu u_\nu$ used here) belongs to layer (ii) and is not developed in this
appendix — see Ch7 §7.11 (OQ7.1) for the general derivation of that dynamics when it applies.

# Appendix D — Spectral analysis: snapshot and movie

The three dispersion branches (§3.2) are complemented here with the full dynamical analysis: the
time evolution of the propagator by sector (the "movie"), contrasted with the static
configuration of $\Gamma$ at a given instant (the "snapshot").

- **Figure D.1** (`fig_calc2_dispersion.png`): the three $\omega(k)$ branches superimposed; a heat
  map of group velocity $v_g=c^2k/\omega$ over $(k,\det\Gamma)$ — the atlas visible in a
  single plane.
- **Figure D.2** (`fig_calc2b_antisymm_hessian.png`): curvature $m_{\rm eff}^2$ by mode and sector
  for the program's original test cases — *note:* after the review of §2.1, this
  figure illustrates particular instances, not a proven general bound; it should be
  reinterpreted in those terms.
- **Figure D.3** (`fig_calc3_coherence_observables.png`): $C(t)$ and $R(t)=\dot C/\gamma$ for the
  three sectors — the $\det\Gamma<0$ sector has the highest $|R|_{\max}$, consistent with
  Hopf-type dynamics.
- **Figure D.4** (`fig_calc4_spectral_film.png`): eigenvalue trajectories in $\mathbb C$
  (top) and phase portrait $(\det\Gamma,C)$ (bottom) — the full movie, not just the
  snapshot.

**Operational reading:** from any trajectory $\Gamma(t)$, compute two scalars —
$\det\Gamma(t)$ and $C(t)$ — and read off the regime, with no parameter tuning and no
prior knowledge of which physics governs the system.

---

*Gamma Space Framework Program. July 2026.*
*henrymolina@gmail.com*
