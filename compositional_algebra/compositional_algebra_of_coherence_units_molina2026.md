# A compositional algebra for coherence-unit configurations: closure, entropy balance, and inertia additivity

Henry Molina
Independent researcher, Bogotá, Colombia
henrymolina@gmail.com
DOI: pending (submitted to Zenodo)

**Note on dependencies.** This paper presupposes the object $\Gamma\in M_4(\mathbb R)$ and the Coherence Unit (CU), and uses the structural potential $P(\Gamma,\rho)=\|\Gamma\|_F^2+\mu(\rho)\det\Gamma$ from Ch13 (Part II) without re-deriving it — both come from earlier, still-unpublished work of the same program. The self-contained summary below covers what this paper needs from that earlier work; the reader does not need to consult it to follow the argument.

**Self-contained minimum.** A Coherence Unit (CU) is an entity — physical, chemical, biological, or social — described by a symmetric matrix $\Gamma\in M_4(\mathbb R)$ that encodes its structural attributes as a Gram matrix; $\rho=-\log|\det\Gamma|$ measures how confined/structured it is (higher $\rho$ = more structure, $\det\Gamma\to0$ = dissolution). $P(\Gamma,\rho)$ is a potential whose minimum characterizes the CU's equilibrium configuration (Ch13); $\mu(\rho)$ is a level-dependent coupling, fixed in Ch13 by a self-consistency condition. This paper takes these three objects as given and attacks the question of what happens when **two or more** CUs compose — why $P$ has this specific form is a question for Ch13, not for here (§1).

---

### How this document is written (two voices)

- **The narrative thread (plain text).** The story and intuition behind each result.
- **The formal boxes (▣).** The precise statement, with **register** — **〔DEF〕** definition/postulate · **〔THM〕** theorem with proof · **〔SC〕** structural correspondence (algebraic isomorphism with a known object, not a physical derivation) · **〔PI〕** physical interpretation — and **status** — **[D]** proved · **[V]** numerically verified · **[A]** asserted (to be proved) · **[F]** frontier/open. When a [D] result depends on a hypothesis beyond the base axioms (A1)-(A4), it is explicitly marked **[D, conditional on named hypothesis]**, with the hypothesis stated in the claim itself — this is not a separate status category, it is a scope annotation on a [D].

---

### Abstract

Twelve compositional operations that appear, under different names, in physics, chemistry, biology and social systems — union, coupling, fusion, fission, absorption, dissolution, among others, formally defined in §9ter — collapse here into five primitives (forming the set, coupling, decoupling, marginalizing, copying, relaxing) and a single linear-algebra identity: the Schur block-determinant formula, applied to the configuration object $\Gamma\in M_4(\mathbb R)$. From that single identity, without a per-operation postulate, follows the complete entropy balance, an exact minimum-work bound (a Jarzynski-Crooks analogue), and a domain-agnostic measure of irreducible structural cohesion. The paper's central contribution is that proven reduction — not a new operation per domain, but a handful of primitives generating all twelve. Later work on the continuous-field front (§5bis) found two additional primitives of genuine, repeated use (Self-Coupling, reflexive; Slaving, a sibling of marginalization) absent from the original catalogue; their appearance leaves the proven closure intact, but turns the completeness of the primitive basis into an open question, no longer an established fact.

Around that core, two extensions inside the main body. Removing the restriction to positive-definite matrices, Haynsworth's (1968) inertia additivity extends the algebra to any signature, revealing that the determinant-sign classification used throughout the paper is the coarsest possible partition of a symmetric matrix's inertia, for any dimension. A second result (Theorem 9) shows that no conjugation-invariant potential can structurally distinguish sub-sectors sharing that phase. A third, more incipient line, with findings already closed separately but not yet assembled into a single formal structure, proposes that the full algebra is an entropy-enriched category — documented in Appendix A as work in progress, not in the main body. The paper does not claim to derive particle physics; its examples (Coulomb/Lorentz, ideal gas, chemical bonding) are illustrative correspondences, meant to show the algebra's applicability to already-known cases.

---

## 1. Scope and scoping decisions

**What this paper is.** A proven reduction: twelve composition operations, so far catalogued case by case across different domains, close into five primitives and a single algebraic identity (the Schur block-determinant formula) plus **two facts already established** in earlier program work (the extensivity of co-presence and the Lyapunov monotonicity of the potential $P$). That closure — Theorem 2, with the complete entropy balance derived in §6 — is the paper's central result. Around it, two structural extensions that were not part of the original plan: the determinant-sign classification used throughout the paper turns out to be, for any dimension, the **coarsest possible** partition of a symmetric matrix's inertia (Corollary 8.1) — a fact of real algebraic geometry — and no conjugation-invariant potential can break that classification between sub-sectors sharing phase (Theorem 9). A third, more incipient line proposes that the full algebra is an entropy-enriched category — documented in Appendix A as work in progress, not in the main body, precisely because its status is [A] while this body stays [D]/[V].

**Placement and scope.** A result in algebra and dynamical systems, in `math-ph` / `nlin.AO` (Adaptation and Self-Organizing Systems) — not particle physics. The examples in §11 (Coulomb/Lorentz, ideal gas, chemical bonding) are **illustrative correspondences 〔SC〕** showing the algebra's applicability to already-known cases.

**Dimension note.** Unless stated otherwise (Theorems 8, 9, and Corollary 8.1, formulated for arbitrary $n$), $n=4$ in Theorems 1–7 is a choice **specific to the SAIR construction** ($\Gamma\in M_4(\mathbb R)$), not a general result about the dimension. Where the argument genuinely is dimension-agnostic (Haynsworth, the det-sign tripartition, Theorem 9), the statement says so explicitly with $n$ free.

**Scope audit (style-guide checklist).** The abstract avoids "theory of everything" claims; every claim carries register+status; every reduction declares its $\Gamma$ before its dynamics; the domain of validity is in the statement; there is a self-audit section (§12); every load-bearing result has a script in `models/calcs/brainstorming/ch7/` and `models/calcs/brainstorming/ch10/`.

---

## 2. Related work

This paper sits at the intersection of three already-established literatures, without claiming novelty in any of them separately: the contribution is the specific synthesis (Schur + Haynsworth inertia + compositional thermodynamics) over the configuration object $\Gamma$, applying known tools to a concrete object rather than proposing a new method of analysis.

**Category theory of open dynamical systems.** Baez and Fong's program on "compositional thermodynamics" (networks of open thermodynamic systems composed via operads/monoidal categories) attacks a structurally parallel question — which composition operations are admissible between open thermodynamic systems, and how does entropy balance propagate through them. This paper's main body (§4–§10) does not go through the categorical apparatus: it derives compositionality directly from a linear-algebra identity (Schur) on a concrete configuration object. Appendix A revisits this relation more precisely — not as a methodological analogy, but by showing that the underlying operation (the Schur complement) exactly matches the composition rule of their *black-box functor* for passive linear networks.

**Schur complements in Gaussian graphical models.** This paper's central identity (Proposition 1, and Theorem 1's admissibility) is, at its core, the standard fact that the Schur complement of a Gaussian precision matrix is exactly that distribution's marginalization — textbook material in the graphical-models literature (Lauritzen, *Graphical Models*, and its descendants in structured Gaussian inference). What this paper contributes is its application to a physical configuration object ($\Gamma$), with a thermodynamic interpretation ($\rho=-\log|\det\Gamma|$ as structural entropy) absent from the purely statistical context — the identity itself is textbook.

**Stochastic thermodynamics of coupled systems.** Theorem 5 ($W_{\min}=\Delta P$) is a direct analogue of the Jarzynski (1997) and Crooks (1999) relations — minimum-work bounds via a Lyapunov/free-energy function, generalized here to the structural composition of CUs rather than to a single thermodynamic system under an external protocol. Seifert's (2012, *Stochastic thermodynamics, fluctuation theorems and molecular machines*) review is the standard reference for that terrain. The parallel with Theorem 5 is direct, with a different derivation route: this paper obtains the bound from the Lyapunov monotonicity of $P$, already established in the program, not from stochastic fluctuation theory.

The three literatures serve here as reference and contrast points, more than as directly imported machinery: the specific contribution is the joint application of these already-known tools to the object $\Gamma$, producing the closed compositional balance of §6 and the Haynsworth generalization of §8.

---

## 3. Introduction — the problem this paper solves

The Coherence Unit (CU) — a physical, chemical, biological, or social entity, described by a configuration matrix $\Gamma\in M_4(\mathbb R)$ whose determinant measures how "closed"/confined its structure is ($\rho=-\log|\det\Gamma|$, the structural entropy) — almost never exists in isolation: two atoms bond, two market agents couple, a cell divides, an organism absorbs another. The question motivating this paper is simple to state and, until now, without a systematic answer within the program: **given two or more CUs, which composition operations between them are structurally admissible, and what happens to entropy when they compose?**

The naive answer would be to catalogue case by case — union, fusion, absorption, fission, dissolution — and postulate an entropy-balance rule for each, tailored to the domain. This paper shows that is unnecessary: **the twelve phenomenological operations that appear in physics, chemistry, biology and social systems are not twelve independent rules** — they are compositions of a handful of primitive operations (forming the set, coupling, decoupling, marginalizing, copying, relaxing), and their entropy balance **is derived** from a single linear-algebra identity (the Schur block-determinant formula) plus two facts already established in the program. There is no new rule per operation — there is one rule, applied twelve times.

The rest of the paper follows this order: §4-§5 establish the joint representation and show that admissible operations close into five primitives (Theorem 2); §6-§7 derive the complete entropy balance and the work/spontaneity bounds; §8-§9 extend the algebra beyond the originally admissible regime, revealing two structural results about how coarse, and how blind, the determinant-sign classification used throughout the paper can be; §10-§11 give the complete classification and three illustrative correspondences; §12-§13 document the verification process with full honesty, including what was tried and did not work; §14 closes. Appendix A collects, separately, a line of work in progress (the algebra as a categorical structure) that does not yet reach the main body's [D]/[V] status.

---

## 4. The joint representation and coupling admissibility

Two CUs $A,B$ with configurations $\Gamma_A,\Gamma_B\in M_4(\mathbb R)$ combine through the **joint matrix**:

$$\Gamma_{\mathrm{joint}} = \begin{pmatrix}\Gamma_A & C_{AB}\\ C_{AB}^T & \Gamma_B\end{pmatrix}$$

where $C_{AB}$ is the **coupling block** — the only new degree of freedom that composition introduces. Every compositional operation in this paper is a transformation of this object.

> **▣ 〔THM〕 Theorem 1 (Coupling admissibility bound). [D]** Let $\Gamma_A,\Gamma_B\succ0$ (force sector, $\det>0$) with structural levels $\rho_A=-\log\det\Gamma_A$, $\rho_B=-\log\det\Gamma_B$. A coupling block $C_{AB}$ is **structurally admissible** ($\Gamma_{\mathrm{joint}}\succ0$) if and only if
> $$\sigma_{\max}\!\left(\Gamma_A^{-1/2}C_{AB}\Gamma_B^{-1/2}\right)<1.$$
> *Proof.* $\Gamma_{\mathrm{joint}}\succ0 \iff$ Schur complement $\Gamma_B-C_{AB}^T\Gamma_A^{-1}C_{AB}\succ0 \iff$ eigenvalues of $\Gamma_A^{-1/2}C_{AB}\Gamma_B^{-1}C_{AB}^T\Gamma_A^{-1/2}<1$. $\blacksquare$

The threshold $\sigma_{\max}=1$ is also the **fusion boundary**: at that point $\det\Gamma_{\mathrm{joint}}=0$ and the sub-CUs stop being recoverable by projection — the same $\det=0$ boundary that separates the Newtonian/Maxwell/Relativistic sectors of a single CU, already established in earlier program work.[^delta_rho]

[^delta_rho]: **Corollary ($\delta_\rho$), heuristic estimate [A].** The bound translates, approximately, into a level-separation threshold: $\delta_\rho\approx4\ln(1/c_0)$ nats, where $c_0=\|C_{AB}\|_F$ (the factor $4$ is $\Gamma$'s dimension, not a rigorously derived constant — this corollary is an order-of-magnitude estimate, not a theorem; it is marked [A] explicitly for that reason, unlike Theorem 1 from which it derives). **Numerically verified caveat [V]:** the Frobenius-norm bound is exact for rank-1 coupling, and **conservative** for full-rank coupling — $\|C_{AB}\|_F\geq\sigma_{\max}(C_{AB})$ in general, so dense coupling can exceed the Frobenius threshold and still be admissible (0/2000 rank-1 violations; 100% of dense cases that exceed it remain admissible; script: `delta_rho_admissibility_bound.py`).

**Where does $C_{AB}$ come from? Partial closure (jul-11 2026).** Theorem 1 says how much coupling is admissible, but not where the concrete value of $C_{AB}$ comes from — a direct desk proof showed that a coupling with no declared physical origin passes the admissibility bound exactly as well as a real one, as long as it stays under $\sigma_{\max}=1$: the theorem filters mathematical consistency, not physical plausibility. Applying Ch13's EOM to $\Gamma_{\mathrm{joint}}$ itself gives the **exact** identity (not just to leading order, for any block size) $\mathrm{adj}(\Gamma_{\mathrm{joint}})_{AB}=-\mathrm{adj}(S_A)\,C_{AB}\,\mathrm{adj}(\Gamma_B)$, which closes a nonlinear system for $C_{AB}$ itself: with no external forcing, the only generic fixed point (scalar case) is $C_{AB}=0$ — coupling decays unless it is sustained by forcing with a traceable physical origin, or the system sits exactly at a critical $\mu$. For $2\times2$ blocks there exist nontrivial, self-sustained fixed points across a wide range of $\mu$, not only at the isolated critical point of the scalar case. This gives the plausibility criterion that was missing, though the general stability of those fixed points remains open. (`brainstorming/physics/oq71_derivacion_C_AB_desde_P_gamma.md`, `brainstorming/physics/oq71_cierre_no_lineal_completo.md`.)

---

## 4bis. The distinguishability criterion

The axioms and classification that follow (§5, (A4); §10) use "identity preserved/lost" — this section defines it before it is used, so it does not float as intuition until the classification.

**▣ 〔DEF〕 Distinguishability.** Two sub-CUs $A,B$ are structurally distinguishable within a compound $C$ (configuration $\Gamma_C$) if there exist projections $\pi_A,\pi_B:V_C\to V_C$ with $\pi_A+\pi_B=\mathrm{Id}$, $\pi_A^2=\pi_A$, $\pi_B^2=\pi_B$, such that:
- **(static content)** $\|\pi_A\Gamma_C\pi_A^T-\Gamma_A\|_F\leq\epsilon_{AB}$, $\epsilon_{AB}=\|C_{AB}\|_F$ (exact if $C_{AB}=0$);
- **(dynamical localization)** every eigenmode $v_k$ of $\Gamma_s$ assigned to block $i$ has participation ratio $\mathrm{PR}(k)=1/\sum_ip_i(k)^2<\tau$, $p_i(k)=\|\pi_iv_k\|^2/\|v_k\|^2$, for some threshold $\tau\in(1,n)$.

The two conditions measure different things and neither subsumes the other: the first is operative for Union/Absorption/Fusion (where the diagonal blocks do change); the second is the only informative one for Coupling/Resonance, where the diagonal block is fixed by construction (the first condition gives $\epsilon_{AB}=0$ always, trivially) — the minimal example is two coupled oscillators at exact degeneracy: any nonzero coupling mixes the modes 50/50 ($\mathrm{PR}\to n$) even though the diagonal block never moves. If no such projection exists, or either condition fails, $A$ and $B$ are indistinguishable in $C$. Verified: $\mathrm{PR}$ is invariant under block relabeling, consistent with Theorem 9 (§9) (`part1/07_compositional_operations.md` §7.2).

---

## 5. The primitive basis and the closure theorem

**Axioms (admissible compositional operation).** A map $O$ on collection-states $(N,\{\Gamma_i\},\{C_{ij}\})$ is admissible if:

- **(A1) Joint action:** $O$ acts on $\Gamma_{\mathrm{joint}}$; every output block is a function of the input blocks.
- **(A2) Closure in $M_4(\mathbb R)$:** every output is a valid $4\times4$ element of the correct algebraic type (note: Ch7 uses the label "$G(3)$" for this axiom, inherited from Ch3's Clifford-algebra notation $\mathrm{Cl}(3,0)$ — a distinct object, not used in this paper; it is avoided here to prevent confusion).
- **(A3) No external information:** $O$ only combines, separates, duplicates, or evolves its operands; it never injects external configuration (sole exception: the explicit choice of sub-structure in the fission direction, supplied as data, not invented).
- **(A4) Two-axis consistency:** $O$ respects the identity×sign-of-$\Delta\rho$ classification (§10).

> **▣ 〔THM〕 Lemma 1 (Uniqueness of the $\Omega$ closure). [D]** Among maps that reduce cardinality by integrating out a subspace under (A1)-(A2), the Schur complement is the only one that preserves the retained block's effective description, for quadratic $P$. *Proof: for quadratic $P$, $\Gamma_{\mathrm{joint}}$ is a Gaussian's precision matrix; marginalizing yields exactly the Schur complement (standard Gaussian marginalization); any other map (e.g. the naive projection $\Gamma_{kk}$) discards $C$'s back-reaction and differs numerically.* $\blacksquare$

> **▣ 〔THM〕 Theorem 2 (Closure of the primitive basis). [D, conditional on named hypothesis: quadratic $P$]** Under (A1)-(A4) and quadratic $P$, every admissible compositional operation factors, up to composition, into five primitives: **JOIN** ($\oplus$, form the set), **COUPLE/DECOUPLE** (fix $C_{AB}\neq0/=0$), **$\Omega$** (marginalize, Schur complement), **COPY** ($\Gamma_B^{(0)}\leftarrow\Gamma_A$), **RELAX** (gradient flow to $\arg\min P$).
>
> *Proof.* A collection-state is the triple $(N,\{\Gamma_i\},\{C_{ij}\})$ — cardinality, block content, and coupling. By (A1), $O$ acts only on $\Gamma_{\mathrm{joint}}$, so any change it produces must be expressible in terms of these three degrees of freedom; there is no fourth available axis. It is shown that $O$ factors along them, and that each axis, restricted by (A2)-(A4), admits exactly the listed primitives:
>
> **Cardinality axis ($N$).** By (A3), $O$ cannot inject external configuration — it can only *increase* $N$ by copying an already-existing block (**COPY**, the only way to add a degree of freedom without new information) or *decrease* it by integrating out a subspace. By Lemma 1, the only cardinality reduction that preserves the retained block's effective description (under quadratic $P$) is the Schur complement (**$\Omega$**). No other cardinality-reduction map satisfies (A2) without discarding information about $C$ that (A4) requires preserving in the $\Delta\rho$ balance.
>
> **Coupling axis ($C_{ij}$).** With $N$ fixed, the only remaining degree of freedom between blocks is whether $C_{ij}=0$ or $C_{ij}\neq0$ — a binary value per pair of blocks. Imposing it in one direction or the other are, by definition, **COUPLE** and **DECOUPLE**; (A2) requires the result to remain a valid $\Gamma_{\mathrm{joint}}$, which both operations satisfy trivially (fixing a submatrix to zero or to an admissible value does not break the block structure).
>
> **Block-content axis ($\Gamma_i$).** With $N$ and $\{C_{ij}\}$ fixed, the only change admissible under (A3) (without injecting external information) is moving each $\Gamma_i$ toward $\arg\min P$ via the gradient flow already established in the program — **RELAX**. Any other change to $\Gamma_i$ would require either external information (excluded by A3) or a simultaneous change of $N$ or $C_{ij}$, which already belongs to the other two axes.
>
> **Forming the initial set.** $\oplus$ (**JOIN**) is the case $N\to N+k$ with $C_{ij}=0$ for every new pair — pure co-presence, the starting point on which the other primitives act.
>
> Since the three axes are independent (changing one does not force a change in the other two) and each is fully covered by the primitives above, any admissible $O$ is a composition of these five. $\blacksquare$
>
> **Honest scope:** the theorem is conditional on quadratic $P$ — the program's real potential (Ch13) has a cubic term ($\mu\det\Gamma$). For $P=$quadratic$+\varepsilon\cdot$cubic, $\Omega$ remains the leading-order marginalization, with controlled deviations $O(\varepsilon)$ — the algebra is **exact** in the linear limit and a **controlled approximation** outside it.
>
> **Precision about what is bounded and what is not.** The verified $O(\varepsilon)$ control (`tranquilidad_asociatividad_nolineal_prediccion.py`) is a **pointwise/kinematic** claim: at a given configuration, $\Omega$ computed with quadratic $P$ deviates from the exact value (with the cubic term present) by an amount that grows continuously with $\varepsilon$. This is **not** a claim about the global stability of the flow under non-quadratic $P$ — in nonlinear dynamical systems, a small perturbation to the potential can qualitatively alter the phase portrait (bifurcations, new fixed points, loss of $\arg\min P$'s uniqueness) without $\Omega$'s pointwise error at one instant reflecting it. The theorem closes algebraic closure **in the exact quadratic limit**. Whether that closure persists under the full nonlinear dynamics is a different question, belonging to dynamical systems more than to compositional algebra, and lies outside this paper by design.

Nine phenomenological operations (Union, Nesting, Coupling, Fusion, Absorption, Fission, Decoupling, Reproduction, Dissolution) are compositions of these five primitives plus identity — verified by parameter counting and explicit construction.

**How do we know there is no sixth primitive?** The closure proof factors along the three degrees of freedom that (A1)-(A2) allow a collection-state — cardinality, coupling, block content — rather than enumerating known operators and ruling out the rest by brute force. A sixth primitive would have to act on a **fourth** degree of freedom; by (A1), $O$ acts only on $\Gamma_{\mathrm{joint}}$, so that fourth axis simply does not exist within the joint representation as defined: the complete set is derived from the object's structure, not obtained by filtering candidates.

This has a limit worth marking precisely. A strong-sense universality theorem — a Cayley-type representation, or freeness of the generated monoid — would prove that *no* alternative representation of "CU composition" can reveal a fourth axis. What is proved here is more modest: within **this** specific representation ($N$ sub-CUs, blocks $\Gamma_i$, couplings $C_{ij}$) there is no fourth axis. It is closure relative to a fixed representation, and it is left marked as such, rather than inflated to absolute universality.

---

## 5bis. After closure: two more primitives found on the working frontier, and a genuine completeness question replacing the earlier certainty

Theorem 2 closes the **catalogue**: the nine phenomenological operations known at the time it was proved factor into five primitives. Later work, applying this same algebra to continuous field configurations (a boundary declared in §1, outside this paper), found **two more operations of genuine, repeated, necessary use** that were not in the original list — their absence does not break Theorem 2 (which is correct about the catalogue it closed), but it does show that "closed" and "complete" are different claims, and that the second was never proved (this was already noted as a limit in "How do we know there is no sixth primitive?" above: the proof closes against the three axes of *this* representation, not against any future operation on the same object).

**▣ 〔DEF〕 Self-Coupling (Definition 7.19, Ch7).** A CU is **self-coupled** when its own configuration content re-enters its source term: $\Gamma_\mathrm{eff}=\Gamma+\lambda\,\mathcal E[\Gamma]$, with $\mathcal E[\Gamma]$ a functional of the CU's own state (e.g. its energy content) and the *same* coupling constant $\lambda$ that governs its coupling to external partners. It is Coupling with $A=B$ — excluded by the letter of Definition 7.5 (which requires two distinct CUs) but required by consistency once coupling is universal: if everything that shifts $\Gamma_\mathrm{eff}$ couples, the CU's own content cannot be exempt. *Verified instance:* in the continuous extension, the field's own gradient energy re-entering its source is exactly what produces the correct second-order self-interaction (the bootstrap step), with the coefficient fixed by universality, not tuned. Self-Coupling is the compositional face of **reflexivity** — the property the program assigns to $\gamma$; until now the algebra had no reflexive operation while the EOM already had a reflexive term. Its full development (does iterated Self-Coupling generate the $\gamma\dot\Gamma$ term? does it interact with Copy?) remains open. [D] the definition and its verified instance; [F] its full development.

**▣ 〔DEF〕 Slaving (Definition 7.20, Ch7) — sibling of $\Omega$.** A mode $u$ of a CU is **slaved** to a slot $s$ when the dynamics eliminates it not by marginalization but by **restriction**: $u=f(s)$, with $u$'s own dynamics degenerate or unstable, so that the restriction is imposed rather than chosen. Distinct from $\Omega$: marginalization integrates a degree of freedom outward (Schur; loses information; produces entropy, §6), while slaving *ties* the mode (no entropy production; the mode remains present, expressed through $s$). *Verified instance:* the conformal (scale) mode of a configuration field is tachyonic when free and must be slaved to the contextual slot $\rho$ — in the continuous extension this is a **stability obligation**. This operation already existed in the program as a *selection* mechanism (covariance criterion, functional/slaving dependence); this definition promotes it from a selection heuristic to a compositional operation. [D] the definition and its verified instance.

**Two sub-operations of Coupling, not new primitives, but whose lack of a name caused a concrete error.** Every worked instance of Coupling in this paper shares a trait: $\Gamma_A,\Gamma_B$ are formed separately from their own SAIR quadruples *before* $C_{AB}$ enters, and coupling adds a cross-block term *afterward*. A different pattern — found when attempting to couple two CUs' own bivector fields directly, an initial attempt that failed and was corrected by deriving from a known reference free energy instead of assuming the wedge channel — does not fit that template:

- **External-Coupling** (Definition 7.5, as in §4): $\Gamma_A,\Gamma_B$ computed independently; $C_{AB}$ is a genuinely new block, orthogonal to both diagonal blocks. This is what composes every operation in §§4–11, including Theorem 4's $n$-ary "glue" mechanism (marginalizing an intermediate block induces an *external* cross term between the survivors).
- **Internal-Coupling** (new, without changing Definition 7.5, only naming an already-used case): a sub-CU's own vector attribute is replaced by a combination with the *other's* vector, **before** forming $\Gamma$: $R^A\to R^A-q\,I^B$ (minimal substitution — physics's gauge-coupling recipe, applied here as a compositional primitive rather than assumed). Expanding $|R^A_\mathrm{eff}|^2$ produces a cross term living *inside* $\Gamma_s^A$ (never $\Gamma_a^A$, because it comes from a dot product, not a wedge) — there is no new off-diagonal block; the coupling is invisible to $\Gamma_\mathrm{joint}$'s block structure until $\Gamma_A$'s own entries are expanded. *Verified instance:* a phase order parameter ($R^A=\nabla\theta$) coupled to a vector potential via $\nabla\theta\to\nabla\theta-qB$ reproduces exactly the Meissner/London mass (Anderson-Higgs mechanism) — not a wedge-wedge coupling ($\Gamma_a$-$\Gamma_a$) as first conjectured.
- **Gauge-Absorption** (distinct from Absorption, §11 note): when Internal-Coupling introduces a redundant degree of freedom in $A$ that a compensating transformation of $B$ can eliminate entirely (it "eats" it), fixing that redundancy collapses exactly *one* degree of freedom of $A$ into $B$'s own $\Gamma_s$ (typically as a mass term), while the rest of $A$ (its scalar $S^A$) survives and fixes the scale of what $B$ gained. Unlike Theorem 8/§10's Absorption (where $B$ is lost entirely, irreversibly), here only the redundant vector direction is lost, not the whole sub-CU.

None of the three is a new primitive — both Coupling sub-operations reduce to Coupling plus a choice of *where* the cross term enters (before or after forming $\Gamma$), and Gauge-Absorption adds a partial, single-direction $\Omega$ reduction. They are named here because leaving them unnamed is exactly what produced the original error (assuming Coupling always means External-Coupling, and consequently proposing a $\Gamma_a$-$\Gamma_a$ wedge for a mechanism that actually needed Internal-Coupling).

> **Open question (completeness of generation, not just of the catalogue).** This paper proves that its catalogued operations reduce to a small basis of primitives — completeness *of the catalogue* (Theorem 2). It does not prove that every $\Gamma_\mathrm{joint}$-preserving-admissibility transformation is *generated* by the primitives — completeness *of the algebra*. The missing theorem: characterize the semigroup generated by {Identity, Join, Couple (external/internal), $\Omega$, Slave, Copy, Relax, Self-Couple} within the monoid of admissibility-preserving maps, and prove generation or exhibit an admissible transformation outside it. Until then, "the algebra is complete" is a conjecture that the catalogue's success makes plausible, not an established fact — the same distinction, applied to itself, that Corollary 8.1 and Theorem 9 (§9) draw between what a coarse invariant can and cannot see. [F].

---

## 5ter. Algebraic type, and why there is no annihilation operation

**Algebraic type. [D]** Co-presence $\oplus$ is associative and commutative: $(\{\mathrm{CU}\},\oplus,\varnothing)$ is a **commutative monoid**. Full composition, including the $\Omega$ collapse, is **non-associative**: fusion fails $(A\circ B)\circ C=A\circ(B\circ C)$ (numerically verified). The precise structure is a **commutative, flexible, power-associative magma**: commutative ($A\circ B=B\circ A$), flexible ($(A\circ B)\circ A=A\circ(B\circ A)$), and power-associative ($(A\circ A)\circ A=A\circ(A\circ A)$) — but neither associative nor Jordan. Three consequences: **(i)** power-associativity makes self-iteration (repeated self-fusion, recursive level towers) well-defined with no grouping ambiguity — non-associativity only bites when fusing three or more *distinct* CUs in different groupings; **(ii)** non-associativity is intrinsic to lossy $\Omega$ collapse (the marginalized relative mode is lost path-dependently) — this is the same phenomenon as irreversibility $\Delta\rho\geq0$ (§6) and composition's arrow of time; JOIN, COUPLE, and $\oplus$ (without collapse) do associate; **(iii)** there is an order-free canonical compound: simultaneous $n$-ary collapse (marginalizing all relative modes at once) is permutation-invariant — the well-defined compound of many CUs is the simultaneous collapse, of which pairwise grouping is a path-dependent approximation. Verified (`models/calcs/brainstorming/ch7/`, see §7.2.3 of `part1/07_compositional_operations.md`).

**Annihilation is not an operation. [D]** No operation in this catalogue sends content to nothing ($\Gamma\to0$ with its attributes destroyed): each one preserves the set, redistributes content between levels ($\Omega$, Fission), or disperses it to the next level (Dissolution) — content is always conserved. This follows from two conservation laws already established: thermodynamically, degrees of freedom cannot vanish without trace (second law; Landauer bound), so Dissolution disperses content with growing entropy instead of erasing it; and by mass-energy conservation (Noether, time-translation symmetry), content transforms rather than disappears — as in particle-antiparticle annihilation, which produces photons, not nothing. The absence of an annihilation operation is, with this, a consistency property of the algebra.

---

## 6. The generating identity and the entropy balance

All of composition's thermodynamics derives from a single identity:

> **▣ 〔THM〕 Proposition 1 (Schur identity). [D]** With $\rho=-\log|\det\Gamma|$ and $\Xi=\Gamma_A^{-1/2}C_{AB}\Gamma_B^{-1/2}$ ($\sigma_i(\Xi)\in[0,1)$ by admissibility):
> $$\rho_{AB} = \rho_A+\rho_B+\Delta_{\mathrm{couple}}, \qquad \Delta_{\mathrm{couple}}=-\log\det(I-\Xi^T\Xi)\geq0.$$
> *Proof:* $\det\Gamma_{\mathrm{joint}}=\det\Gamma_A\det\Gamma_B\det(I-\Xi^T\Xi)$; take $-\log$. $\blacksquare$

Together with co-presence's extensivity ($\rho_{A\oplus B}=\rho_A+\rho_B$, diagonal block, $\det=\prod\det\Gamma_i$) and the autonomous flow's Lyapunov monotonicity ($\dot P\leq0$, already established in the program), this identity **generates** — rather than postulates — the entropy balance of all twelve operations:

| Operation | $\Delta\rho$ | Sign | Derivation |
|---|---|---|---|
| Union | $\Delta_{\mathrm{couple}}$ | $\geq0$ | direct Schur — same formula as Coupling, but here it does describe the set's real dynamics (Union forms a genuine compound) |
| Coupling | $\Delta_{\mathrm{couple}}$ | $\geq0$ | direct Schur — a static fact about the block; see precision below |
| Decoupling (Schur) | $0$ | $=0$ | exact entropic inverse |
| Decoupling (SVD) | $\leq0$ | $\leq0$ | minimizes algebraic, not entropic, loss |
| Fusion | $\Delta_{\mathrm{couple}}$ | $\geq0$ | identical to Coupling |
| Fission | $-\Delta_{\mathrm{couple}}(B,C')$ | $\leq0$ | exact algebraic inverse of Fusion |
| Absorption | $\Delta_{\mathrm{couple}}-\rho_B$ | $\pm$ | Schur with $S=B$ |
| Dissolution | $\to+\infty$ | $\geq0$ | $\det\Gamma\to0$ |
| Co-presence $\oplus$ | $0$ | $=0$ | diagonal block |
| Copy | $\rho_B$ | $\geq0$ | extensivity of $\oplus$ |
| Reproduction | $\rho_B+\Delta\rho_{\mathrm{relax}}(B)$ | $\geq0$ | Copy + Relax |
| Relaxation | $\int\sigma_{\mathrm{struct}}\,dt=P_i-P_f$ | $\geq0$ | Lyapunov |
| Nesting | $0$ | $=0$ | projection, no new degrees of freedom |

**All entries are [D]** (Union added jul-11 2026). None requires a new postulate per operation — they all read off the same Schur identity plus the two facts already cited. Numerically verified over 5000–10000 random SPD samples per claim, zero violations (`thm73_cohesion_entropy_bound.py`, `algebra_termodinamica_cierre.py`).

**Precision on the "Coupling" entry (jul-10 2026).** The Coupling row uses the same Schur identity as Union — this correctly describes $\Delta_{\mathrm{couple}}$ as a purely algebraic property of the block $\Gamma_{\mathrm{joint}}=\begin{pmatrix}\Gamma_A&C_{AB}\\C_{AB}^T&\Gamma_B\end{pmatrix}$ (a matrix identity, true regardless of what dynamics is later applied to it). **It does not imply**, however, that genuine Coupling (in the phenomenological sense, "without forming a compound CU") makes $\rho_A,\rho_B$ evolve according to $\rho_{AB}=\rho_A+\rho_B+\Delta_{\mathrm{couple}}$ under one shared EOM — that reading corresponds to Union (or to the strong-coupling limit, "Coupling approaches the Union regime," already noted in the two-axis table). For Coupling proper, each CU keeps its own dynamics, modulated by the other — this table row describes the entropic cost *of the joint block viewed as a static object*, useful as a bound and as an analytical tool, not a claim about each $\rho_i$'s time evolution under Coupling. This distinction became concrete this week when applying the algebra to a real physical composition problem (three bodies via Ch7): treating Coupling as if it solved a joint EOM produced a result that stopped reproducing real physics — see the corresponding resolution note in Ch7 (Definition 7.5, §7.3.3 of `part1/07_compositional_operations.md`).

**Two-layer resolution, numerically verified (jul-11 2026).** The apparent tension — does Coupling have a shared EOM or not? — resolves by recognizing two coexisting dynamical layers, not a single-answer question. **(i) State layer:** each CU keeps its own dynamics and identity, modulated by the other — this is never in question. **(ii) Configuration layer:** the coupling block $C_{AB}$ itself is an emergent object with its own dynamics, governed by its components ($\Gamma_A,\Gamma_B,\mu$) and by context (an external structural forcing $N_{AB}(t)$) — exactly the EOM Ch13 postulates for any $\Gamma$, now applied to the joint block. A worked example (two oscillators coupled by $\kappa(t)$, `models/calcs/brainstorming/ch7/coupling_dos_capas_prueba.py`) confirms both regimes: with constant $N_{AB}$, $\kappa(t)$ relaxes to the fixed value $\kappa^*=N_{AB}/(1-\mu/2)$ (error $5\times10^{-4}$) — exactly recovering the standard reading of a fixed-stiffness spring; with $N_{AB}$ varying faster than $\kappa$'s own relaxation, it shows genuine, never-settling dynamics — the regime of a chemical bond responding to an ongoing reaction, or a plastic synapse. Neither reading is universally correct; each is the appropriate limit depending on the context's relative speed.

**Irreducible cohesion.** When decoupling redistributes $C_{AB}$ via SVD projection (not via Schur), a residue may remain unattributed to either sub-CU:

> **▣ 〔THM〕 Theorem 3 (Cohesion and reversibility). [D]** $\mathcal B(A,B)=\|P^\perp_{\mathrm{span_{GS}}(\mathcal E_A\cup\mathcal E_B)}C_{AB}\|_F$ (Gram-Schmidt orthogonal projection onto both blocks' SVD modes) satisfies: (i) $\mathcal B=0\iff C_{AB}$ is exactly recoverable from $(\Gamma_{A'},\Gamma_{B''})$; (ii) $\Delta\rho_{\mathrm{couple}}\geq\mathcal B^2/\|\Gamma_{AB}\|_F^2\geq0$.
>
> *Proof (i).* $(\Rightarrow)$ Let $\mathcal E_A\cup\mathcal E_B$ be the (Gram-Schmidt orthonormalized) set of $\Gamma_A,\Gamma_B$'s singular modes. If $\mathcal B=0$, the SVD redistribution (Gram-Schmidt projection of $C_{AB}$ onto $\mathrm{span}(\mathcal E_A)$ and $\mathrm{span}(\mathcal E_B)$ separately) recovers $C_{AB}$ exactly, since $C_{AB}$ lives entirely in $\mathrm{span_{GS}}(\mathcal E_A\cup\mathcal E_B)$: $\delta\Gamma_A+\delta\Gamma_B=C_{AB}$. Re-coupling from $(\Gamma_{A'},\Gamma_{B''})=(\Gamma_A+\delta\Gamma_A,\Gamma_B+\delta\Gamma_B)$ exactly reconstructs $\Gamma_{AB}$.
> $(\Leftarrow)$ Contrapositive: if $\mathcal B>0$, the residue $C_{AB}-P^\perp_{\mathrm{span_{GS}}}C_{AB}\neq0$ is orthogonal to $\mathrm{span}(\mathcal E_A\cup\mathcal E_B)$ by construction. By (A3) (no admissible operation injects external configuration), that residue cannot be absorbed into $\Gamma_{A'}$ or $\Gamma_{B''}$ — any reconstruction $\tilde C$ from $(\Gamma_{A'},\Gamma_{B''})$ lives in $\mathrm{span}(\mathcal E_{A'}\cup\mathcal E_{B''})$, and since mode perturbations are $O(\|\delta\Gamma\|)$ (Theorem 2), $\|\tilde C-C_{AB}\|_F\geq\mathcal B-O(\|\delta\Gamma\|^2)>0$ for admissible coupling. $\blacksquare$
>
> *Proof (ii).* From Proposition 1, $\Delta\rho_{\mathrm{couple}}=-\log\det(I-\Xi^T\Xi)=\sum_i-\log(1-\sigma_i^2)$ where $\sigma_i=\sigma_i(\Xi)\in[0,1)$ are $\Xi=\Gamma_A^{-1/2}C_{AB}\Gamma_B^{-1/2}$'s singular values.
>
> *First inequality.* $-\log(1-x)\geq x$ for $x\in[0,1)$; summing over singular values: $\Delta\rho_{\mathrm{couple}}\geq\sum_i\sigma_i^2=\|\Xi\|_F^2$.
>
> *Second inequality, corrected.* $\|\Xi\|_F^2=\|\Gamma_A^{-1/2}C_{AB}\Gamma_B^{-1/2}\|_F^2\geq\|C_{AB}\|_F^2/(\lambda_{\max}(\Gamma_A)\cdot\lambda_{\max}(\Gamma_B))$ — the standard minimum-singular-value inequality for a matrix product (not the joint Frobenius norm used in an earlier version of this proof, which incorrectly mixed operator norm and Frobenius norm). Since $\lambda_{\max}(\Gamma_A)\cdot\lambda_{\max}(\Gamma_B)\leq\|\Gamma_A\|_F\|\Gamma_B\|_F\leq\tfrac12(\|\Gamma_A\|_F^2+\|\Gamma_B\|_F^2)\leq\|\Gamma_{AB}\|_F^2$ (the last inequality because $\Gamma_{AB}$ contains $\Gamma_A,\Gamma_B$ as diagonal blocks, plus coupling), it follows that $\|\Xi\|_F^2\geq\|C_{AB}\|_F^2/\|\Gamma_{AB}\|_F^2$.
>
> *Closing.* $\mathcal B\leq\|C_{AB}\|_F$ (a projection's residue never exceeds the original's norm), so $\|C_{AB}\|_F^2\geq\mathcal B^2$. Chaining: $\Delta\rho_{\mathrm{couple}}\geq\|\Xi\|_F^2\geq\|C_{AB}\|_F^2/\|\Gamma_{AB}\|_F^2\geq\mathcal B^2/\|\Gamma_{AB}\|_F^2\geq0$. $\blacksquare$ Numerically verified over 5000 random SPD samples, 0 bound violations (`thm73_cohesion_entropy_bound.py`).

$\mathcal B(A,B)$ is a domain-agnostic measure of structural integration that requires no probability distributions — for chemical bonds it measures orbital non-separability.

---

## 7. Cascade composition, work, and spontaneity

> **▣ 〔THM〕 Theorem 4 (Cascade composition). [D]** For three sequentially coupled CUs: $\rho_{ABC}=\rho_A+\rho_B+\rho_C+\Delta_{\mathrm{couple}}(A,B)+\Delta_{\mathrm{couple}}(AB,C)$. **Corollary:** this sum is identical under any grouping order (verified, 0 difference over 2000 samples) — the *total* entropy produced by coupling three CUs is order-independent, though the specific *residual structure* (what is lost in each collapse) does depend on order.

> **▣ 〔THM〕 Theorem 5 (Work bound via Lyapunov). [D]** For any operation taking $P$ from $P_i$ to $P_f>P_i$, the minimum external work is $W_{\min}=\Delta P=P_f-P_i$. *Proof:* $\dot P=-\|\nabla P\|^2_M+\dot W\Rightarrow W=\Delta P+\int\|\nabla P\|^2 dt\geq\Delta P$, GSF's analogue of Jarzynski-Crooks.

> **▣ 〔THM〕 Theorem 6 (Spontaneity criterion). [D]** An operation is spontaneous iff $\Delta P\leq0$. $\Delta\rho$ (Prop. 1) and $\Delta P$ (Thm. 5) are **independent quantities** — one can be $>0$ while the other is $\leq0$, exactly the profile of a bond that forms spontaneously while producing structural entropy.

**Exact $\rho\leftrightarrow P$ relation.** Using Ch13's explicit potential ($P=\|\Gamma\|_F^2+\mu(\rho)\det\Gamma$) and the overdamped flow ($\dot\Gamma\approx-\frac1{2\gamma}\nabla_\Gamma P$):

> **▣ 〔THM〕 Theorem 7. [D]** $\dot\rho = \frac{n}{\gamma}+\frac{\mu(\rho)}{2\gamma}\det\Gamma\,\|\Gamma^{-1}\|_F^2$ ($n=4$), via Jacobi's formula $\nabla_\Gamma\det\Gamma=\det\Gamma\cdot\Gamma^{-T}$.

Verified by finite differences (error $<10^{-8}$, `rho_P_exact_relation.py`). The honest result: **$\rho$ and $P$ are genuinely distinct entropy currencies** — the coefficient of variation of their ratio over random samples is $\approx1.45$, not zero. There is no hidden $\rho\propto P$ identity; there are two complementary conservation laws over the same flow.

**This is the result: two laws, not one.** Theorem 7 **proves** that no linear identity ties $\rho$ and $P$ for this flow, with the same rigor as any other [D] result in this paper — non-proportionality is proved, not pending discovery of a missing unifying principle. $\rho$ (via Schur, kinematic) and $P$ (via Lyapunov, dynamic) measure genuinely distinct aspects of the same flow, exactly like energy and entropy in classical thermodynamics: two laws coupled through free energy, each with its own dynamics.

---

## 8. Beyond the admissible regime: inertia additivity (Haynsworth)

Theorems 1–6 restrict composition to the force sector: $\Gamma_A,\Gamma_B\succ0$. This section removes that restriction with a classical tool from 1968.

> **▣ 〔THM〕 Theorem 8 (Haynsworth inertia additivity). [D]** For $\Gamma_{\mathrm{joint}}=\begin{pmatrix}\Gamma_A & C_{AB}\\ C_{AB}^T & \Gamma_B\end{pmatrix}$ with $\Gamma_A$ symmetric **invertible** (any signature, not restricted to $\succ0$):
> $$\mathrm{In}(\Gamma_{\mathrm{joint}}) = \mathrm{In}(\Gamma_A) + \mathrm{In}(S_A), \qquad S_A=\Gamma_B-C_{AB}^T\Gamma_A^{-1}C_{AB}$$
> where $\mathrm{In}(M)=(n_+,n_-,n_0)$ is the inertia (count of positive/negative/zero eigenvalues). *Proof:* the congruence $\begin{pmatrix}I&0\\-C_{AB}^T\Gamma_A^{-1}&I\end{pmatrix}\Gamma_{\mathrm{joint}}\begin{pmatrix}I&-\Gamma_A^{-1}C_{AB}\\0&I\end{pmatrix}=\mathrm{diag}(\Gamma_A,S_A)$ block-diagonalizes $\Gamma_{\mathrm{joint}}$; by Sylvester's law of inertia, congruent matrices share inertia, and inertia is additive over a direct sum. $\blacksquare$ Verified (2000 binary samples + 3000 in a 3-body cascade, 0 violations; `haynsworth_inertia_cascade.py`).

**Theorem 1 is the special case** $\mathrm{In}(\Gamma_A)=\mathrm{In}(\Gamma_B)=(n,0,0)$: the only possible sum is $(2n,0,0)$ — exactly why the naive mixed-sign cascade conjecture (§12, item 3) died *within* the SPD regime. Relaxing that restriction is what reopens the question.

### 8bis. Regularized $\Omega$ in the massless sector ($\det\Gamma_B=0$), jul-11 2026

Theorem 8 requires $\Gamma_A$ invertible but does not restrict signature — however, marginalization itself ($\Omega$, Schur complement) requires $\Gamma_B$ invertible, a requirement the underlying physical theory makes fail in exactly one of its three proper sectors: the massless sector ($\det\Gamma_B=0$). Absorbing or fusing a sub-CU living there was, until now, an unresolved division by zero.

> **▣ 〔THM〕 Theorem 8bis (Regularized $\Omega$). [D]** Let $\Omega_B:=\lim_{\varepsilon\to0^+}[\Gamma_A-C_{AB}(\Gamma_B+\varepsilon I)^{-1}C_{AB}^T]$. This limit **exists (is finite) if and only if** $C_{AB}$ vanishes on $\ker(\Gamma_B)$ (Albert's condition: $C_{AB}q=0\ \forall q\in\ker(\Gamma_B)$), in which case it matches **exactly** the Moore–Penrose formula $\Gamma_A-C_{AB}\Gamma_B^+C_{AB}^T$. If the condition fails, the limit diverges **exactly as $1/\varepsilon$**. *Proof (one line):* diagonalizing $\Gamma_B=Q\,\mathrm{diag}(\lambda_1,\ldots,\lambda_{n-1},0)\,Q^T$ and $C'=C_{AB}Q$, $C_{AB}(\Gamma_B+\varepsilon I)^{-1}C_{AB}^T=\sum_{i<n}\frac{c_i'(c_i')^T}{\lambda_i+\varepsilon}+\frac{c_n'(c_n')^T}{\varepsilon}$; the last term diverges unless $c_n'=0$, exactly Albert's condition. $\blacksquare$ Numerically verified (exact $1/\varepsilon$ divergence rate, consecutive ratio $10.00\pm0.03$ per decade).

**Physical reading.** The divergence is genuine, not an artifact: coupling with a finite component non-orthogonal to a mode with no structural stiffness (massless) costs infinite structural energy — the compositional analogue of resonantly exciting an undamped oscillator at its own frequency. Albert's condition is exactly the statement that a photon is absorbed via its energy/polarization, never by pushing against its own massless propagation direction.

**The entropy balance generalizes without new machinery.** $\rho_C=\rho_A+\Delta_{\mathrm{int}}$ stays exact (verified to $<10^{-15}$) by substituting only $\Gamma_B^{-1}\to\Gamma_B^+$ in $\Delta_{\mathrm{int}}=-\log|\det(I-\Gamma_A^{-1}C_{AB}\Gamma_B^+C_{AB}^T)|$; the admissibility bound $\Delta_{\mathrm{int}}\geq0$ is exactly Theorem 1's ($\lambda_{\max}<1$), not a new bound. A complementary identity, $\mathrm{pdet}(\Gamma_{\mathrm{joint}})=\mathrm{pdet}(\Gamma_B)\det(\Gamma_C)$ and $\mathrm{rank}(\Gamma_{\mathrm{joint}})=\mathrm{rank}(\Gamma_A)+\mathrm{rank}(\Gamma_B)$ (pseudo-determinant/rank, exact under Albert's condition), shows that **$\Gamma_B$'s massless mode survives intact** as an exact null mode of the compound — it is never absorbed, only the sub-CU's massive degrees of freedom are. The doubly-singular case ($\Gamma_A$ also at $\det=0$) closes the same way under the double Albert condition, with both massless modes surviving unmixed. (`brainstorming/physics/omega_regularizado_sector_masa_nula.md`, `brainstorming/physics/delta_int_generalizado_sector_masa_nula.md`, `brainstorming/physics/caso_doblemente_singular.md`.)

> **▣ 〔THM〕 Corollary 8.1 (The det-sign tripartition is the coarsest possible inertia classification, for any $n$). [D]** $\mathrm{sign}(\det\Gamma_s)\in\{+,0,-\}$ divides $\mathrm{Sym}(n,\mathbb R)$ into exactly two **open, generic** regions ($n_-$ even / $n_-$ odd) separated by the **codimension-1, non-generic** hypersurface $n_0\geq1$. True for any dimension $n$ — a classical fact of real algebraic geometry ($\{\det=0\}$ is a codimension-1 algebraic variety), not a numerical conjecture, nor specific to $n=4$ or to GSF.

This is the paper's sharpest statement about the determinant-sign classification used in Theorems 1–7: the tripartition is not an arbitrary three-way cut — it is the *forced*, coarsest-possible partition of inertia into generic phases plus a separatrix, independent of dimension. It is coarser than the full signature $(n_+,n_-,n_0)$, which for $n=4$ admits up to 15 distinct classes.

**Precision (jul-11 2026) — this "open question" is not a well-posed question of the algebra.** Asking whether the sign tripartition "hides" the fine 15-class structure confuses the algebra with what runs on top of it: any coarse invariant is, by construction, blind to what it discards — arithmetic that sums money is indifferent to whether it is counted in bills or coins. That blindness is not a gap to close; it is what makes the invariant an invariant. Theorem 9 (§9) confirms this from the other side: no conjugation-invariant potential can recover that fine structure at the level of local (Hessian) geometry — the static/kinematic layer this algebra captures is, demonstrably, unable to select it. If dynamically relevant fine structure exists, it lives in the **topology of $P$'s gradient flow** (basins, separatrices, Morse-Smale classification) — a legitimate question, but of dynamics, not of this compositional algebra.

---

## 9. The dynamical companion: no sub-sector receives algebraic privilege

Corollary 8.1 is a **static/kinematic** claim: it classifies which shapes $\Gamma_s$ can take. A natural question follows immediately: given an object composed of several blocks sharing the same phase, does any reasonable dynamics distinguish one block's role from another's — or is Corollary 8.1's blindness inherited intact by the dynamics built on top of it? This section answers: for a broad and natural class of potentials, it is inherited exactly. Discovered while attacking a concrete three-sector composition — unpublished exploratory notes by the author — and recorded here in general form because the argument uses nothing specific to that construction.

> **▣ 〔THM〕 Theorem 9 (No privileged sub-sector under conjugation-invariant potentials). [D]** Let $\mathcal M$ be a space of matrices ($\mathrm{Sym}(n,\mathbb R)$ or general $M_n(\mathbb R)$) and $G$ a group acting on $\mathcal M$ leaving $P:\mathcal M\to\mathbb R$ invariant: conjugation $P(S\Gamma S^T)=P(\Gamma)$, $S\in O(n)$, if $\mathcal M=\mathrm{Sym}(n,\mathbb R)$; or the two-sided action $P(U\Gamma V)=P(\Gamma)$, $(U,V)\in O(n)\times O(n)$, $\det(U)\det(V)=1$, if $\mathcal M=M_n(\mathbb R)$ general. Both $\|\Gamma\|_F^2$ and $\det\Gamma$ are invariant under their respective action, so any $P$ built from them — in particular $P(\Gamma)=\|\Gamma\|_F^2+\mu\det\Gamma$ — meets the hypothesis. Let $\Gamma^\ast\in\mathcal M$ be a critical point of $P$. Then:
>
> **(a)** The tangent space to $\Gamma^\ast$'s $G$-orbit lies entirely in the kernel of $P$'s Hessian at $\Gamma^\ast$. *Proof:* invariance implies $\nabla P(g\cdot\Gamma^\ast)=0$ for every $g\in G$ (the whole orbit is critical, not just the point). Differentiating this identity along a curve $g(t)\in G$: $H(\Gamma^\ast)\cdot v=0$ for $v$=the orbit's tangent. $\blacksquare$ This step needs no block structure — it is the general Goldstone-type fact for any critical point of any invariant $P$.
>
> **(b)** If additionally $\Gamma^\ast=\mathrm{blockdiag}(\Gamma_1,\dots,\Gamma_k)$, the internal-rotation generator of **any** block $\Gamma_i$ is a particular case of (a).
>
> **(c) Corollary — no privileged sub-sector.** By (b), the internal gauge freedom of every block has exactly the same algebraic character for all $i$ — $P$ cannot structurally distinguish one block from another. If the blocks are labeled by physical role, no label receives special treatment from $P$'s local geometry.

**Verification, three independent instances:**

| $n$ | Object | $\mathcal M$ / group $G$ | Expected orbit dim. | Verified |
|---|---|---|---|---|
| 4 | $\Gamma$ (general Lorentzian fixed point) | $M_4(\mathbb R)$, $O(4)\times O(4)$ | $12-\mathrm{stab.}=6$ | 6 exact zero modes |
| 3 | $G_3$ (abstract 3-sector composition) | $\mathrm{Sym}(3,\mathbb R)$, $O(3)$ | $\dim SO(3)-\dim(O(2)\times O(1))=2$ | 2 exact zero modes |
| 6 | $\Gamma_{\mathrm{joint}}=\mathrm{blockdiag}(\Gamma_1,\Gamma_2,\Gamma_3)$, symmetric | $\mathrm{Sym}(6,\mathbb R)$, $O(6)$ | $\dim O(6)-\dim(O(3)\times O(3))=9$ | 9 of 15 zero modes (exact rank) |

The $n=6$ case confirms (c) directly: each of the three blocks' internal rotation aligns at an **exact 100%** with the zero-mode subspace, identical for all three — no block stands out.

**Scope and honesty.** Theorem 9 is a structural negative result for a specific and natural class of potentials — it does not claim that no dynamics can ever distinguish sectors, only that this broad, symmetric class cannot. Breaking the conclusion requires an ingredient explicitly *not* invariant under $G$ (candidates: a non-scalar dissipation rate differing by sector; an external reference structure; an inherently directional relational term, not symmetric between sectors). Extending the weak-coupling reduction used in the $n=6$ verification to strong coupling is a separate, unresolved task — with three blocks (not two) coupling generates a genuine third-order (triangular) term absent with only two blocks, connecting to the already-recorded "purely three-dimensional" effect (item 3, §12). Neither route is attempted in this paper.

**Two concrete candidates were already tried and failed.** In the author's unpublished exploratory notes, it was directly attacked whether (a) sector-dependent weights in the potential, or (b) the non-associative structure of the octonionic Jordan algebra $J_3(\mathbb O)$ (the natural frame for a symmetric three-sector composition) break Theorem 9's conclusion *forcibly*, without an external ingredient. **Neither succeeds.** (a) Raises Hessian curvature at a specific critical point, but verified via the Noether theorem associated with conjugation symmetry, the conserved charge survives intact: the observed breaking is an indirect effect, not a violation of invariance. (b) $J_3(\mathbb O)$ preserves the full $S_3$ permutation symmetry despite octonionic non-associativity (consistent with the Freudenthal cubic form belonging to the $F_4$ automorphism group). As far as explored, the ingredient that would break the conclusion has to be genuinely external to $\Gamma$, not an intrinsic property of any tested candidate algebra.

This theorem is Corollary 8.1's dynamical twin: that corollary shows the *static* classification of shapes is as coarse as algebraically possible; Theorem 9 shows that a broad, natural class of *dynamics* built on that classification inherits the same blindness between same-phase sub-sectors.

---

## 9bis. Bivector invariance under elimination of a symmetric partner

Discovered by stress-testing the algebra outside this paper's usual domains: mapping real tabulated physical data (electronegativity, bond dissociation energy) for a hydrogen and an oxygen atom onto SAIR→Γ objects, and composing them via Union+Ω to see whether the algebra distinguishes the OH radical from H₂O (`brainstorming/physics/uoc_st_toroide/h2o_prueba_fuego_sair_gamma.md`).

> **▣ 〔THM〕 Theorem 10 (Bivector invariance). [D]** Let $\Gamma_A,\Gamma_B\in M_4(\mathbb R)$, $\Gamma_A=\Gamma_s^A+\Gamma_a^A$ (symmetric+antisymmetric decomposition), and $C_{AB}$ **any** coupling block (no structural restriction). If $\Gamma_a^B=0$ — i.e. $\Gamma_B$ is symmetric — then $\Omega$-marginalization (Schur complement) of $B$ leaves the antisymmetric part of $A$'s effective configuration exactly unchanged:
> $$\Gamma_a\!\left(\Gamma_A - C_{AB}\,\Gamma_B^{-1}\,C_{AB}^T\right) = \Gamma_a^A$$

*Proof.* $\Gamma_B^{-1}$ is symmetric whenever $\Gamma_B$ is. For any matrix $C$ and any symmetric $M$, $(CMC^T)^T=CM^TC^T=CMC^T$ — so the correction term $C_{AB}\Gamma_B^{-1}C_{AB}^T$ is symmetric regardless of $C_{AB}$. Subtracting a symmetric matrix from $\Gamma_A$ only alters $\Gamma_s^A$; $\Gamma_a^A$ is untouched. $\blacksquare$

**The converse, now derived (closed ago-6 2026) — see Theorem 11 below.** When $\Gamma_a^B\neq0$, the correction term is generically **not** symmetric, and $\Gamma_a^A$ generically changes — even when $A$ started with $\Gamma_a^A=0$ (a zero bivector can be genuinely created, not just preserved or destroyed). Numerically verified over 2000 random samples of admissible $(\Gamma_A,\Gamma_B,C_{AB})$ with initial $\Gamma_a^A=0$: eliminating a bivector-free block leaves the survivors' bivectors frozen to machine precision ($<10^{-15}$) under fully general (unrestricted) coupling; eliminating a block with its own bivector injects a genuine, growing bivector into a partner that started at exactly zero. Until this closure round, this subsection had limited itself to reporting that bivector creation as a **verified, not derived**, fact — Theorem 11 identifies the exact mechanism producing it.

**Scope and honesty.** This is a structural fact about $\Omega$/Schur elimination, independent of any domain interpretation — it holds for any admissible $(\Gamma_A,\Gamma_B,C_{AB})$ satisfying Theorem 1's positive-definiteness (or its Haynsworth generalization, Theorem 8, for other signatures). It sharpens, with a proof instead of an observation, the earlier informal finding that "$\Gamma_a$ never mixes" under restricted (R-R only) couplings: that finding was not a fact about the restriction, but a special case of this theorem, since the restricted examples happened to eliminate an object with no bivector content in the relevant directions. The theorem does **not** say $\Omega$ never affects the symmetric channel — $\det$ and $\rho$ generically do change (§7 of this paper); only the antisymmetric part of the object that **survives** is protected, and only when the object being **eliminated** contributes no antisymmetric part.

This theorem is Theorems 8–9's structural companion: where Theorem 8 classifies inertia under collapse and Theorem 9 shows that symmetric dynamics does not distinguish sub-sectors, Theorem 10 identifies a third invariant — protected algebraically, not dynamically — of the collapse process itself.

---

## 9bis2. The exact bivector-creation mechanism: reciprocal/non-reciprocal decomposition

**Gap closed this round (ago-6 2026).** Theorem 10 left its converse as a merely verified fact: that eliminating a partner *with* a bivector injects a genuine bivector into the survivor, without saying *why* or *how much*. `part1/07_compositional_operations.md` §7.3.3 already had, since jul-26 2026, the theorem that closes exactly that question — it had not been incorporated into this paper. It is incorporated here, with no change to the statement, and the update propagates to §10, §13, and Appendix B.

All the coupling machinery used so far (Theorems 1, 2, 7, 8) assumes symmetric $\Gamma_{\mathrm{joint}}$ — $C_{BA}=C_{AB}^T$, **reciprocal** coupling. That assumption is the norm in this paper (chemical bonds, coupled springs, Coulomb force), but not universal: Stokes drag on a dilute particle in a fluid, for instance, pushes the fluid without appreciable back-reaction — both directions are nonzero (literally satisfying Definition 7.5) but not reciprocal in magnitude.

> **▣ 〔THM〕 Theorem 11 (Reciprocal/non-reciprocal decomposition of the joint configuration). [D]** For $\Gamma_{\mathrm{joint}}=\begin{pmatrix}K_A&C_{AB}\\C_{BA}&K_B\end{pmatrix}$ with $K_A,K_B,C_{AB},C_{BA}$ **arbitrary** (no symmetry, no $C_{BA}=C_{AB}^T$ assumed anywhere), define $C_{\mathrm{eff}}=(C_{AB}+C_{BA}^T)/2$ (the reciprocal/Hamiltonian-consistent part of the coupling) and $D_{\mathrm{eff}}=(C_{AB}-C_{BA}^T)/2$ (the non-reciprocal excess). Then, exactly:
> $$\Gamma_s(\Gamma_{\mathrm{joint}})=\begin{pmatrix}\Gamma_s^A&C_{\mathrm{eff}}\\C_{\mathrm{eff}}^T&\Gamma_s^B\end{pmatrix},\qquad\Gamma_a(\Gamma_{\mathrm{joint}})=\begin{pmatrix}\Gamma_a^A&D_{\mathrm{eff}}\\-D_{\mathrm{eff}}^T&\Gamma_a^B\end{pmatrix}$$
>
> *Proof.* Immediate from $\Gamma_{\mathrm{joint}}^T=\begin{pmatrix}K_A^T&C_{BA}^T\\C_{AB}^T&K_B^T\end{pmatrix}$ and $\Gamma_s=(\Gamma_{\mathrm{joint}}+\Gamma_{\mathrm{joint}}^T)/2$, $\Gamma_a=(\Gamma_{\mathrm{joint}}-\Gamma_{\mathrm{joint}}^T)/2$ applied blockwise — no Schur complement, no positivity, no reciprocity at any step. $\blacksquare$ Verified: `models/sair/tests/test_state_system.py` (`test_reciprocity_theorem_gamma_s_*`, `test_reciprocity_theorem_gamma_a_*`); **formalized in Lean 4, with no `sorry`** (`lean/CompositionalAlgebra/Theorem11.lean`, verified with `#print axioms` — depends only on mathlib's standard axioms).

**Consequence — the mechanism that was missing.** Theorems 1/8 (admissibility, Haynsworth) apply *unmodified* to $\Gamma_s(\Gamma_{\mathrm{joint}})$, using $C_{\mathrm{eff}}$ in place of the raw coupling — the classical machinery never needed generalizing, only identifying the correct channel. **The corollary that closes Theorem 10:** two purely symmetric blocks ($\Gamma_a^A=\Gamma_a^B=0$, genuine potential wells) coupled **non-reciprocally** generate a nonzero $\Gamma_a(\Gamma_{\mathrm{joint}})=\begin{pmatrix}0&D_{\mathrm{eff}}\\-D_{\mathrm{eff}}^T&0\end{pmatrix}$ — non-reciprocity alone is a **source** of rotational/gyroscopic structure that neither subsystem possessed. This gives a derivation (not merely a verified instance) of the converse Theorem 10 left open: $D_{\mathrm{eff}}$ **is** the injection mechanism, identified here at the level of the joint configuration, before any elimination.

**A second closed form, unconditional even after elimination.** $\det(\Gamma_{\mathrm{joint}})=\det(K_A)\cdot\det(\Omega)$, $\Omega=K_B-C_{BA}K_A^{-1}C_{AB}$, is the classical block-LU determinant identity — it requires only $K_A$ invertible, never symmetry or reciprocity, so it survives $\Omega$-elimination intact. This is what underwrites §6's entropy balance ($\rho=-\log|\det\Gamma|$) even outside the reciprocal regime.

**What does NOT survive elimination.** Theorem 11's clean decomposition does not propagate through $\Omega$: $\Gamma_a(\Omega)$ is, in general, not a simple function of $D_{\mathrm{eff}}$ alone (numerically verified — $K_A^{-1}$ genuinely entangles the reciprocal and non-reciprocal channels during elimination, because inverting a non-symmetric matrix does not preserve the symmetric/antisymmetric split of what it multiplies). This pins down *exactly* where Theorem 8 (a statement about $\Omega$, not about $\Gamma_{\mathrm{joint}}$) stops generalizing: not at composition (Theorem 11 is exact there), specifically at elimination. For that regime the honest answer remains the case-by-case linear composition `models/sair/core/state_system.py` (`StateSystem`) provides, not a closed form. Verified: `models/calcs/brainstorming/ds/algebra_bloques_no_simetricos/03_teorema_reciprocidad.py`.

This theorem also precisely fixes a scope limit of Definition 7.5 (Coupling) this paper had not marked: that definition only requires both coupling directions to be nonzero, but the Schur machinery underlying Theorems 1/2/7/8 requires the **stronger** condition of reciprocity in magnitude ($C_{BA}=C_{AB}^T$) the moment either block's own $\Gamma$ stops being symmetric or the physical coupling is genuinely one-directional. A non-reciprocal coupling (a bath forcing a subsystem, rather than two subsystems mutually modulating each other) is not yet in the catalogue of primitives (§5); whether it admits a Theorem 1/8-style closed form, or only the case-by-case linear composition, remains open — not attacked in this paper.

---

## 9ter. The nine catalogued operations: formal definitions

The preceding sections prove results *about* the twelve operations cited in the Abstract without yet defining them within this paper — they relied on the name and their row in the entropy table (§6). This section closes that debt: it defines, compactly, using §4bis's distinguishability and §5's primitives, the nine named operations from which the twelve derive (the remaining three — Copy, Co-presence, Relaxation — are primitives, already defined in §5). Full version, with domain examples and the external/internal Coupling variants, in `part1/07_compositional_operations.md` §§7.3–7.8.

**▣ 〔DEF〕 Union.** $U=A\cup B$ with $\Gamma_U=\Gamma_\mathrm{joint}$ (§4), $A,B$ distinguishable in $U$. Reversible: separable if $C_{AB}\to0$. Requires $\rho$-proximity ($|\rho_A-\rho_B|\leq\delta_\rho$, Theorem 1's corollary); compound level $\rho_U=\max(\rho_A,\rho_B)$. Example: two atoms before bonding; a temporary coalition.

**▣ 〔DEF〕 Nesting.** $B$ is nested in $A$ ($B\triangleleft A$) if $V_B\subsetneq V_A$ is a subspace stable under $\Gamma_A$ ($\Gamma_AV_B\subseteq V_B$) and $\Gamma_B=\Gamma_A|_{V_B}$; asymmetric ($B\triangleleft A\not\Rightarrow A\triangleleft B$), and not synonymous with "being contained": it requires $A$ to *actively* modulate $B$'s dynamics (an eggshell does not nest the egg — it is a passive boundary, not a structural host). Example: an enzyme's active site; a galaxy nested in spacetime.

**▣ 〔DEF〕 Coupling.** $A\rightleftharpoons B$ if they exert mutual epistemic modulation ($\Gamma_E^{A\to B}\neq0$, $\Gamma_E^{B\to A}\neq0$) without forming a compound: each keeps its own $\Gamma,\rho,\xi^*$, modulated by the other. It is a persistent state, not an event. Distinct from Union: in Union a single $\Gamma_\mathrm{joint}$ is resolved; in Coupling there are two coexisting layers — the state layer (each CU keeps its own dynamics, never in question) and the configuration layer (the coupling block $C_{AB}$ itself has its own emergent dynamics, governed by §4's EOM applied to the block). Example: a sustained interpersonal relationship; two coupled oscillators.

**▣ 〔DEF〕 Fusion.** $F$ such that $\{S,A,I,R\}_F$ are new variables (not sums of $A,B$'s), $\Gamma_F$ with no recoverable block — $A,B$ indistinguishable in $F$, cease to exist separately. Generally irreversible. Example: fertilization (two gametes → one zygote).

**▣ 〔DEF〕 Absorption.** $A\leftarrow B$: $A$ persists modified, $\Gamma_{A'}=\Gamma_A-C_{AB}\Gamma_B^{-1}C_{AB}^\top$ (the Schur complement — the explicit form of the modification map, previously unspecified); $B$ loses identity. Asymmetric: $A\leftarrow B\not\cong B\leftarrow A$. Example: mitochondrial endosymbiosis.

**▣ 〔DEF〕 Fission.** Separation of $C$ into $\{A,B,\ldots\}$, exhaustive ($V_A\oplus V_B\oplus\cdots=V_C$), with $\Gamma_i=\pi_i\Gamma_C\pi_i^T$ by restriction and the cross blocks discarded. For quadratic $P$, $\|\Gamma_C\|_F^2=P(\Gamma_A)+P(\Gamma_B)+2\|\pi_A\Gamma_C\pi_B^T\|_F^2\geq P(\Gamma_A)+P(\Gamma_B)$: free energy does not increase under fission — a theorem, not a conjecture, in that regime (subadditivity conjectured for non-quadratic $P$). Example: cell division.

**▣ 〔DEF〕 Decoupling.** $C_{AB}\to0$ with the coupling energy redistributed toward $\Gamma_{A'},\Gamma_{B''}$ — it does not leave the blocks intact; the exact rule is multi-mode SVD modal projection (`part1/07_compositional_operations.md`, Definitions 7.9a–f), and the residue not attributable to either is Theorem 3's irreducible cohesion $\mathcal B(A,B)$ (§6). Example: breaking a van der Waals bond ($\mathcal B=0$, exact) vs. a covalent one ($\mathcal B=\|C_{AB}\|_F$, irreducible).

**▣ 〔DEF〕 Reproduction.** $A$ generates $B$ with $\Gamma_B^{(0)}\approx\Gamma_A$ (or $\Gamma_A(\xi^*_A)$); $A$ persists (possibly modified); $B$ subsequently evolves independently — distinct from Copy (here $B$ is not tied to remaining a copy) and from Fission (here $A$ persists, is not consumed in the separation). Example: cell division with imperfect inheritance (mutation).

**▣ 〔DEF〕 Dissolution.** $A$ dissolves when, with no external forcing ($F_\mathrm{ext}\to0$), the gradient flow drives $\Gamma_A$ to $P$'s global minimum, losing its local attractor. It is dispersal, not annihilation (§5ter): terminal and non-generative — unlike Fission, it produces no new identifiable sub-CUs. Example: an organism's death — its maintained structure relaxes once forcing ceases; components disperse rather than disappear.

---

## 10. Structural classification (two axes, three values each)

The original classification (identity preserved/lost × reversible/irreversible) under-represented the algebra: Fission has $\Delta\rho\leq0$, a third sign not covered by the binary dichotomy. The full version:

| | $\Delta\rho<0$ | $\Delta\rho=0$ | $\Delta\rho>0$ |
|---|---|---|---|
| **Identity preserved** | Decoupling (SVD, $\mathcal B>0$) | Co-presence; Decoupling (Schur); Nesting | Union; Coupling |
| **Identity lost** | Absorption ($\Delta_{\mathrm{couple}}<\rho_B$) | Absorption (boundary, non-generic) | Fusion; Absorption; Dissolution |
| **Generative (cardinality changes)** | Fission | — (excluded) | Reproduction; Copy |

Two cells are empty, and both are **generic falsifiable predictions** (not measure-zero boundary exclusions): identity-lost×$\Delta\rho=0$ only occurs at Absorption's exact point $\Delta_{\mathrm{couple}}=\rho_B$; generative×$\Delta\rho=0$ requires $\rho_B\to0$ (structureless, degenerate copy).

**Invariant table.** The classification above organizes operations by their effect on identity and entropy; the following table organizes them by which algebraic quantities they preserve — a complementary reading, closer to how this algebra would read in the standard language of invariant theory.

| Operation | Rank | Signature/inertia | $\det$ | Spectrum | $\|\cdot\|_F$ | $\mathcal B$ |
|---|---|---|---|---|---|---|
| Co-presence $\oplus$ | preserved (direct sum) | preserved per block | multiplicative | union of spectra | $\|\Gamma_A\|_F^2+\|\Gamma_B\|_F^2$ | n/a ($C=0$) |
| Coupling/Union | preserved | preserved if admissible (Thm. 1) | grows ($\times\det(I-\Xi^T\Xi)^{-1}$, Prop. 1) | mixed, not preserved | grows | defines $\mathcal B$ |
| Decoupling (Schur) | preserved | preserved | exact inverse of coupling | recovered exactly | recovered exactly | $\mathcal B=0$ by construction |
| Decoupling (SVD) | preserved | preserved | approximate | approximate | approximate | $\mathcal B\geq0$, measures the failure |
| Fusion/Absorption | reduced ($\Omega$ collapse) | $S_A$'s (Haynsworth, Thm. 8) | Schur complement's | $S_A$'s, not $\Gamma_{AB}$'s | not preserved | not applicable post-collapse |
| Copy | duplicated | duplicated | duplicated | duplicated | duplicated | n/a |
| Relaxation (RELAX) | generically preserved | can change near $\det=0$ (Thm. 8/Cor. 8.1) | $\to\arg\min P$ | flows along the gradient | decreases monotonically ($P$, not necessarily $\|\cdot\|_F$) | n/a |

The most informative row is Fusion/Absorption: Theorem 8 (Haynsworth) is exactly the statement that **inertia** — not rank, not the determinant alone — is the quantity preserved additively under collapse, generalizing what Theorem 1 already showed in the case restricted to $\Gamma_A,\Gamma_B\succ0$.

---

## 11. Illustrative correspondences 〔SC〕

These three examples show that the algebra is *applicable* — not that it derives new physics from scratch. Each uses exclusively the machinery of §§4–10, with no additional postulates.

### 11.1 Coulomb and Lorentz force from the Coupling morphism 〔SC〕 [D]

**The case's Γ (SAIR):** two charged CUs $A,B$ with coupling block $C_{12}=q\,A_\mu\otimes u_\nu$ (exterior product between potential and four-velocity).

**Decomposition:** $\Gamma_s(C_{12})\to$ conservative force (Coulomb), $\Gamma_a(C_{12})\to$ reactive force (magnetic/Lorentz). Numerically verified to machine precision: the pure Coulomb case ($v=0$) gives $\|\Gamma_s\|=1$, $\|\Gamma_a\|=0$; the magnetic case gives the full Lorentz force $f=q(E+v\times B)$; the observable $\mathcal C(C_{12})$ (coherence, Ch5) transitions from $0$ (Coulomb, symmetric block) to $1$ (Josephson, antisymmetric block) — a clean signature of the interaction type.

### 11.2 Statistical independence via co-presence $\oplus$ 〔SC〕 [D]

> **▣ 〔SC〕** $Z_{AB}=Z_A\cdot Z_B \iff \Gamma_{AB}=\Gamma_A\oplus\Gamma_B$, with $Z_\mathrm{Gauss}(\Gamma)=(\det\Gamma)^{-1/2}$ (Lemma 7.1, Ch7 — $\Gamma_\mathrm{joint}$ read as a Gaussian precision matrix) and $\rho=2\log Z_\mathrm{Gauss}$, **exact, without postulating $\beta=\rho$** (correction jul-11/12 2026: an earlier version of this row used $Z(\rho)=\mathrm{tr}(e^{-\rho\Gamma})$, which does require $\beta=\rho$ — a postulate refuted by 6+ independent routes elsewhere in the program, see `insight_t3_status.md`; that construction was never needed here). *Proof:* diagonal block $\Rightarrow\det$ factorizes $\Rightarrow Z_\mathrm{Gauss}$ factorizes; the converse follows because $\det\Gamma$ determines the joint Gaussian volume.

The ideal gas of $N$ particles is $\Gamma_N=\Gamma_1^{\oplus N}$, $Z_N=Z_1^N$ — the standard result, now as iterated co-presence. The fusion boundary ($\det\Gamma_{\mathrm{joint}}\to0$) is exactly the thermodynamic condition for bound-state formation.

### 11.3 The chemical-bond spectrum via cohesion $\mathcal B$ 〔SC〕 [D]

Van der Waals ($\mathcal B=0$, exact decoupling) → ionic ($0<\mathcal B<\|C_{AB}\|_F$, partial residue) → covalent ($\mathcal B=\|C_{AB}\|_F$, irreducible) is Theorem 3's direct reading over a continuum of coupling blocks, with no new parameter.

**Honesty — this is a shape correspondence, not validated against data.** $\mathcal B$ was never evaluated here on real tabulated atomic data — the vdW→ionic→covalent progression is a qualitative analogy about the *shape* of the $\mathcal B/\|C_{AB}\|_F\in[0,1]$ spectrum, not a fit to concrete molecules. §11.4, which does use real data for a different question (Theorem 10), found that reproducing real chemical behavior from tabulated constants is sensitive to the SAIR→Γ mapping and did not work at physically realistic parameters without a narrow, non-principled normalization. The two questions are distinct ($\mathcal B$ classifies the coupling block's own decomposability; Theorem 10 concerns whether $\Omega$ can alter a partner's bivector) and not in conflict, but this subsection's [D] status should be read as "derived given the coupling block," not as "validated against real chemistry."

### 11.4 OH vs. H₂O — Theorem 10 in a concrete example, and its limits 〔SC〕 [D]/[V]

**The case's Γ (SAIR), with real tabulated data, not illustrative:** $\rho_H=2.20$, $\rho_O=3.44$ (Pauling electronegativity); $\Gamma_a^H=0$ (H is $1s^1$, $l=0$, no angular momentum); $\Gamma_a^O=$ two rotations in orthogonal planes (O is $2p^4$, Hund's rule: 2 unpaired electrons); $q_{HO}=D_{OH}/D_{HH}=463/436\approx1.062$ (bond energies from thermochemistry tables). Each O–H bond splices H's electron with the plane of O's angular momentum that bond saturates.

**Direct application of Theorem 10:** since $\Gamma_a^H=0$, the theorem **forbids, on purely structural grounds**, any change in O's orbital/bivector character upon bonding to hydrogens — regardless of how the coupling is modeled. Verified exactly: O's antisymmetric residue stays frozen at $<5\times10^{-16}$ for OH (1 bond) and H₂O (2 bonds), at any coupling strength.

**What the theorem does not guarantee — and where the example reveals the program's real limit:** the symmetric channel ($\det$) does qualitatively distinguish OH from H₂O (at coupling strength $\lambda=2.0$, OH crosses to $\det<0$ while H₂O stays just positive), but **only at twice the real bond-energy scale** — at $\lambda=1$ (the real physical coupling) neither crosses. A reverse diagnostic (`brainstorming/physics/uoc_st_toroide/h2o_reversa_algebra_vs_sair.md`), fixing the algebra and varying only the SAIR mapping, found: (i) the success window is narrow ($\sim10\%$ relative) and the most natural normalizations for $q_{HO}$ (typical H-H, C-H, N-H bond energies) all fall outside it; (ii) switching $\rho$ from electronegativity to ionization energy (where H and O are nearly identical) kills H₂O's crossing entirely; (iii) even with identical $\rho$ for H and O (no real physical asymmetry at all) the algebra **already** produces a qualitative transition — evidence that the composition itself has the necessary structural capacity.

**Verdict:** the failure to reproduce H₂O's stability at real physical scale is predominantly a problem of the **SAIR mapping** (there is not yet a principle that fixes, non-arbitrarily, the units and scale of $\rho,q$ for a new domain like chemistry), not of the **algebraic composition** (Union+$\Omega$), which is the same machinery already verified in Theorems 1–9 with no modification.

### 11.5 Operational closure (autopoiesis) — how far the five-primitive basis reaches 〔DEF〕[D]

Let $\Phi=\textsf{RELAX}\circ\Omega\circ\textsf{COUPLE}\circ\textsf{JOIN}\circ\textsf{COPY}$ be a **production cycle**: a CU copies a template of its own configuration ($\textsf{COPY}$), reintegrates it with its own decaying state ($\textsf{JOIN}+\textsf{COUPLE}+\Omega$), and maintains the result against wear ($\textsf{RELAX}$). A CU is **operationally closed** (autopoietic) if its configuration is a fixed point of its own production cycle: $\Phi(\Gamma^\ast)=\Gamma^\ast$.

Three precisions fix its status. **(i)** It is not a new primitive — $\Phi$ is built entirely from the five primitives already closed in Theorem 2; operational closure is a fixed point of the existing algebra (verified: since $\Omega$ is homogeneous of degree 1, the cycle's multiplier is exact and closure is the marginal point between proliferation and dissolution; `models/calcs/brainstorming/ch7/autopoiesis_punto_fijo.py`). **(ii)** By this algebra's second law ($\Delta\rho\geq0$, §6), every $\Omega$ collapse raises structural entropy, so closure cannot be a passive equilibrium — it is a dissipative steady state that demands continuous structural work, just like a single CU's persistence under external forcing. **(iii)** The fixed-point condition alone is finely tuned (multiplier exactly one); the robust version — the condition sustained within a viability band by homeostatic regulation — is closure's living form, and lies outside this paper's purely algebraic scope.

This result is the five-primitive basis's natural closure: with $\Omega$ giving the system→individual collapse and $\Phi$ giving the self-regenerating fixed point, the arithmetic of composition manages to express not only how a structure is built, but how it can sustain itself — the algebraic, not yet dynamical, threshold where composition becomes persistent organization. Full development (viability-band dynamics, homeostatic regulation): `part1/07_compositional_operations.md` §7.8.3.

---

## 12. Self-audit (gaps found and their resolution)

This section documents the actual verification process, including what was discarded — following the principle that a negative result is information, not noise.

1. **Duplicate numbering (serious, corrected).** The book-version's Definitions 7.10–7.15 collided with six pre-existing definitions of the same number; renamed to a collision-free scheme before this writing.
2. **Conflation of two entropy currencies (corrected).** An earlier version cited Theorem 5 ($\Delta P$) to justify claims about $\Delta\rho$ (Prop. 1) — two quantities §7 (Theorem 6) proves are independent. Corrected: every balance claim in this paper explicitly cites which of the two currencies it uses, without mixing them.
3. **Mixed-sign cascade conjecture — dead in its simple form, generalized via Haynsworth. [D]+[V]** It was investigated whether the nested determinants of a three-body cascade (Thm. 4) could take independent signs (+/0/−). **Result within the admissible regime (Thm. 1): the Schur complements of a positive-definite matrix are always positive definite** (standard linear-algebra fact) — the three nested determinants are always $(+,+,+)$; the only crossing to a negative sign coincides with the already-known $\sigma_{\max}=1$ boundary. Verified: 3000 samples, 0 exceptions (`schur_cascade_signs_check.py`). **This negative result led to Theorem 8 (§8):** the SPD restriction is exactly what forces $(+,+,+)$; removing it gives Haynsworth's (1968) general law, which composes inertia *additively* for any input signature — not a new numerical conjecture but a classical theorem, verified here in the compositional context (2000+3000 samples, 0 violations). The result reveals that the det-sign tripartition is the coarsest possible inertia classification (two generic phases + a thin boundary), but leaves open a purely mathematical question about whether $P$'s dynamical flow selects finer structure within that coarse classification.
4. **Unexplained omission in the two-axis classification (corrected).** Fission and Reproduction did not fit the original binary dichotomy; generalized to three values per axis (§10), with the two empty cells re-verified as mutually consistent generic exclusions.
5. **Item 3's open question, attacked — partial answer via Theorem 9 (§9). [D]+[V]** Item 3 left open whether $P$'s dynamical flow selects finer structure within Haynsworth's coarse classification. Attacked from a specific angle: can a conjugation-invariant potential (the class $P(\Gamma)=\|\Gamma\|_F^2+\mu\det\Gamma$ belongs to) distinguish sub-sectors sharing phase? **Result: no, never, for this class of potentials** (Theorem 9, verified at $n=3,4,6$). This does not close item 3's question — it sharpens it: any dynamical selection of fine structure would require explicitly breaking conjugation invariance, an ingredient absent from $P$ as used in this paper.
6. **A trial by fire with real data — revealed an unsought theorem, not the expected physics. [D]+[V]/negative, see §9bis and §11.4.** The algebra was tried against a concrete chemical fact (H₂O stable, OH unstable) with real tabulated data (electronegativity, bond energy). The direct attempt **failed** at physically realistic parameters (§11.4) — but the attempt surfaced Theorem 10 (§9bis), a genuine structural fact about $\Omega$-elimination that had not been sought. Honest diagnosis (`h2o_reversa_algebra_vs_sair.md`): the failure is the SAIR→Γ mapping's (units/normalization with no fixing physical principle), not the algebraic composition's — the same machinery (Union+$\Omega$) that gives Theorems 1–9 unchanged.

---

## 13. Honesty by register and status

| Result | Register | Status |
|---|---|---|
| Coupling admissibility bound (Thm. 1) | 〔THM〕 | [D] |
| Closure of the primitive basis (Thm. 2) | 〔THM〕 | [D, conditional on named hypothesis: quadratic $P$] |
| Schur identity (Prop. 1) | 〔THM〕 | [D] |
| Entropy balance, 12 operations | 〔THM〕 | [D] + [V] (all numerically verified) |
| Cohesion and reversibility (Thm. 3) | 〔THM〕 | [D] + [V] |
| Cascade, work, spontaneity (Thms. 4–6) | 〔THM〕 | [D] + [V] |
| Exact $\rho\leftrightarrow P$ relation (Thm. 7) | 〔THM〕 | [D] + [V] |
| Haynsworth inertia additivity (Thm. 8, §8) | 〔THM〕 | [D] + [V] — classical (1968), applied here to the compositional case |
| No privileged sub-sector under invariant potentials (Thm. 9, §9) | 〔THM〕 | [D] + [V] ($n=3,4,6$) — structural negative, explicit scope |
| Det-sign tripartition = coarsest inertia classification, any $n$ | 〔THM〕 | [D] — real algebraic geometry fact |
| Naive mixed-sign cascade conjecture | — | **discarded [V negative]**, see Thm. 8 |
| Fine inertia structure (15 classes, $n=4$) dynamically selected by $P$ | — | **[F] open mathematical question, not attacked** |
| Coulomb/Lorentz, ideal gas, chemical bonding via $\mathcal B$ (§11.1–11.3) | 〔SC〕 | [D] — shape correspondence, not validated against real data |
| Bivector invariance under Ω-elimination of a symmetric partner (Thm. 10, §9bis) | 〔THM〕 | [D] — converse now **derived**, not merely verified (see Thm. 11) |
| Reciprocal/non-reciprocal decomposition of $\Gamma_{\mathrm{joint}}$ (Thm. 11, §9bis2) | 〔THM〕 | [D] + [V] — formalized in Lean 4 with no `sorry`; closes Thm. 10's converse |
| OH vs. H₂O, concrete application of Thm. 10 with real data (§11.4) | 〔SC〕 | [D] (theorem) + **honest negative** (symmetric channel does not reproduce real-scale stability; failure traced to the SAIR mapping) |
| Self-Coupling (Def. 7.19, §5bis) | 〔DEF〕 | [D] the definition + verified instance; [F] its full development (relation to $\gamma\dot\Gamma$, to Copy) |
| Slaving (Def. 7.20, §5bis) | 〔DEF〕 | [D] the definition + verified instance |
| External/internal Coupling and gauge-absorption (§5bis) | 〔DEF〕 | [D] — not new primitives, names for uses already present in Coupling |
| Completeness of generation of the primitive basis (§5bis) | — | **[F] open question, distinct from catalogue completeness (Thm. 2), not attacked** |
| Distinguishability (projections + participation ratio) (§4bis) | 〔DEF〕 | [D] |
| The nine catalogued operations, formally defined (§9ter) | 〔DEF〕 | [D] — closes §5–§10's debt, which used them without defining them in this paper |
| Algebraic type (commutative, flexible, power-associative magma) (§5ter) | 〔THM〕 | [D] + [V] |
| Absence of an annihilation operation (§5ter) | 〔THM〕 | [D] — consequence of conservation (thermo + Noether), not a design choice |
| Operational closure / autopoiesis (§11.5) | 〔DEF〕 | [D] the algebraic fixed point; [F] its living/regulated form (out of scope) |

**Named frontiers:** (i) non-quadratic $P$ leaves $\Omega$ as an approximation, not exact marginalization; (ii) the exact relation between the two entropy currencies remains two complementary laws, not one identity; (iii) the kinetic layer (rates, barriers, catalysis) is out of scope — the algebra is kinematic, not rate dynamics; (iv) completeness of *generation* of the primitive basis (§5bis) remains open, distinct from the catalogue completeness Theorem 2 already closes. The algebra as a categorical structure (Appendix A) is a fifth frontier, treated separately for its [A] status.

---

## 14. Discussion and closing

The introduction's (§3) promise was that the twelve phenomenological compositional operations would reduce to a handful of primitives and a single entropy-balance identity. That promise is fulfilled with no [A]-marked exceptions in the main body: closure (Theorem 2), the complete balance (§6), and the work/spontaneity bounds (§7) are all [D]+[V]. The two extensions beyond the originally admissible regime (Haynsworth, §8; Theorem 9's structural negative, §9) were not part of the original plan — they arose from investigating why a naive cascade-sign conjecture died (§12, item 3), and ended up revealing something more interesting than the conjecture itself: the determinant-sign classification, used throughout this program from the start, is the coarsest possible partition of inertia, and no conjugation-invariant potential can break it dynamically between sub-sectors sharing phase. Neither result was anticipated; both are, in retrospect, direct consequences of taking seriously what $\Gamma_s$ actually is as an algebraic object.

**What this paper leaves open, explicitly.** Four named frontiers (§13) mark where what is proved ends: the non-quadratic $P$ regime, the relation between the two entropy currencies, the full kinetic layer, and the completeness of *generation* of the primitive basis (§5bis) — distinct from the catalogue completeness Theorem 2 does close: two primitives found on the continuous-field frontier (Self-Coupling, Slaving) after proving that theorem show the primitive list may not have been complete from the start, and there is still no argument ruling out a seventh. Added to these is the question closing Theorem 9 — what ingredient, explicitly not conjugation-invariant, would be needed to break the blindness between sub-sectors — which this paper leaves unattacked by design: it is a question of concrete physics (what that ingredient is in a real system), not of compositional algebra in the abstract, and belongs to the program's next level, not to this paper. Appendix A's categorical line is a sixth frontier, with real progress already made but not closed.

**Where the program goes next.** The next paper in this series extends the compositional machinery to continuous systems — fluids and fields, where $\Gamma$ stops being a finite matrix and composition becomes an operation on fields coupled in space. The central question stays identical in spirit: which operations are admissible, and how does entropy balance when they compose? — only now over an infinite-dimensional configuration space. If this paper's algebra is, as argued here, a consequence of the block structure and the Schur identity rather than of $\Gamma$'s specific finite dimension, it should survive that step — but that, like everything else in this program, is stated to be verified, not assumed. Two further routes are flagged: (i) finishing the formalization of Appendix A's categorical bridge — in particular, the cocycle law of the $\Delta_2$ 2-cell and its assembly into the standard axioms of a lax 2-category; (ii) investigating whether the rest of the fine inertia signature (beyond the sign tripartition, §8) — e.g. whether $P$'s gradient flow preferentially stabilizes specific signatures like $(2,2,0)$ over $(3,1,0)$ at $n=4$ — has dynamical content, the question Corollary 8.1 leaves explicitly open.

---

## Appendix A — Work in progress: the algebra as a category enriched over $\Delta\rho$ [A]

*This section stays outside the main body (§1–§14) because its status is [A] overall, not [D]/[V] — it is documented here rather than omitted, under the same honesty policy governing the rest of the paper (§12), but it is not part of what this paper certifies as closed.*

Building an interactive worked-example instrument for the five primitives (§5) surfaced something absent from both the standard categorical treatments of composition (Baez-Fong, Span/Cospan, PROPs, operads) and from classical process thermodynamics: an **explicit kinematics**. Moving a continuous physical parameter does not jump between discrete operations — it flows continuously from Union to Coupling to Fusion, with $\Delta\rho$ varying smoothly throughout. Ordinary (Set-enriched) categories have no native way to carry that kinematics — their morphisms are arrows without magnitude.

**The fit.** Lawvere (1973) showed that a metric space $(X,d)$ is a category enriched over $([0,\infty],+,\geq)$: the "hom" between two points is the number $d(x,y)$, not a set of arrows, and categorical composition is the triangle inequality. This paper's Proposition 1 ($\rho_{AB}=\rho_A+\rho_B+\Delta_{\mathrm{couple}}$, $\Delta_{\mathrm{couple}}\geq0$) is already exactly that ingredient — additivity of a non-negative cost under composition.

*Numbering note: this section's results are not labeled "Theorem 12, 13..." — unlike Theorems 1–11 in the main body (all [D]), this appendix stays [A] overall, so its individual pieces remain unpromoted to formal numbering until the full structure closes.*

**▣ 〔DEF〕 Entropic multicategory $\mathcal U$.** Objects: CUs, $\Gamma\in M_4(\mathbb R)$. An $n$-ary morphism $(A_1,\dots,A_n)\to B$: an admissible simultaneous collapse, where $B$ is the Schur complement of one retained input after eliminating the remaining $n-1$ as a single joint block. Weight: $w(A_1,\dots,A_n\to B):=\rho(B)-\rho(A_{\mathrm{retained}})$ — generalizes $\Delta_{\mathrm{couple}}$ directly for $n=2$.

**▣ 〔THM〕 Weight non-negativity. [D]** For positive-definite $\Gamma_{\mathrm{joint}}$, $w\geq0$. *Proof.* Splitting $\Gamma_{\mathrm{joint}}$ into two blocks — the retained one and the joint block of the $n-1$ eliminated ones (with their mutual couplings) — Fischer's inequality (Hadamard's block generalization, valid for any PD matrix) gives $\det\Gamma_{\mathrm{joint}}\leq\det(\text{eliminated block})\cdot\det(A_{\mathrm{retained}})$, i.e. $\rho_{\mathrm{joint}}\geq\rho(\text{eliminated block})+\rho(A_{\mathrm{retained}})$. The Schur identity gives $\rho(B)=\rho_{\mathrm{joint}}-\rho(\text{eliminated block})$ exactly. Combining: $\rho(B)\geq\rho(A_{\mathrm{retained}})$. $\blacksquare$ Verified on 2995 confirmed-PD random configurations ($n\in[2,5]$), zero violations (`correccion_peso_n_ario.py`). **Positive-definiteness of $\Gamma_{\mathrm{joint}}$ is a necessary hypothesis** — an earlier version of this definition summed all $n$ inputs' entropy (not just the retained one) and claimed non-negativity "by generalized Hadamard"; that formula gives $w<0$ in ~3% of PD configurations for $n\geq3$, corrected before this section was written (self-audit, jul-06 2026).

**Fusion's non-associativity is the strict triangle inequality, not a defect.** Two binary-composition sequences reaching the same final objects are two distinct factorizations of the same $n$-ary morphism, and Lawvere enrichment only guarantees $w(\text{direct})\leq w(\text{via intermediate})$, not equality — exactly where $\Omega$ acts irreversibly; it vanishes where composition is reversible (Union, Coupling without collapse, Schur-based Decoupling).

**Two additional pieces, verified but not assembled into a single formal structure.** (i) **Unit law [D]:** $\mathrm{id}_A$ is the degenerate $n=1$ case of the same machinery ($w=0$ exact), and substituting it into any slot of a larger morphism leaves the object and total weight unchanged — verified in 6 independent configurations, exact to machine precision.

(ii) **RELAX does not commute with $\Omega$, with a closed-form correction 2-cell [D].** Relaxing two inputs separately under their own potential before collapsing genuinely differs from collapsing first and relaxing the result. This gap is not a generic failure: it scales exactly as $O(\|C\|^2)$ (log-log fit, exponent $2.0014\pm0.0006$ over 10 random configurations, `ley_intercambio_2categoria.py`) — the signature of a **lax 2-category** (an established categorical object), not a strict category. Moreover, this correction 2-cell has a **closed form, exactly verified**: writing $C=\varepsilon\tilde C$, the Schur complement is exactly quadratic in $C$, and to leading order

$$\Delta_2(A,B,C,t) = J_B(t)\!\left[\tilde C^T A^{-1}\tilde C\right] - \tilde C^T A_t^{-1}\tilde C,$$

where $J_B(t)$ is the directional derivative of RELAX's flow at $B$ — the discrepancy between evaluating the coupling correction on the already-relaxed block versus pushing the original correction through the flow's linearization. Verified: relative error $0.0000$ between this formula and the actual numerical difference across 8 independent configurations (`forma_cerrada_2celda.py`). RELAX is that 2-cell: a continuous deformation *within* a fixed combinatorial shape, governed by $P$'s gradient, with the $n$-ary collapses as 1-morphisms. Only the full lax structure's higher-order coherence laws remain missing — that stays [A].

Finally, the underlying Schur operation matches, verified on two circuit topologies against two independent methods (a closed-form star–mesh transform and direct nodal analysis), the composition rule of Baez-Fong's *black-box functor* for passive linear networks (their "Kron reduction") — $\mathcal U$ appears to be a genuine enriched lift of that categorical framework, not merely adjacent to it.

**Status.** [A] overall — each individual piece (weight non-negativity, unit law, RELAX's non-commutation with its quadratic scaling and closed form, the Jacobian cocycle governing its temporal coherence, the Baez-Fong match) verified separately, with the $\Delta_2$ correction 2-cell being the finding closest to a genuinely new property of this algebra, not an application of already-known mathematics. Honestly pending: the $\Delta_2$ cocycle law itself (how it accumulates over split relaxation) is not yet precisely formulated — an initial attempt turned out to be a mis-posed comparison, not a verification — and the final assembly into the standard axioms of a lax 2-category from the categorical literature. Developed at length in `brainstorming/papers/draft_algebra_uoc/multicategoria_lawvere.md` (private working notes).

---

## Appendix B — Numerical verification

All load-bearing results in the main body (§1–§14) and Appendix A are verified in (private repository paths, part of the same research program's internal codebase):
- `models/calcs/brainstorming/ch7/thm73_cohesion_entropy_bound.py`
- `models/calcs/brainstorming/ch7/algebra_termodinamica_cierre.py`
- `models/calcs/brainstorming/ch7/delta_rho_admissibility_bound.py`
- `models/calcs/brainstorming/ch10/rho_P_exact_relation.py`
- `models/calcs/brainstorming/uoc_st/schur_cascade_signs_check.py` (negative result, §12.3)
- `models/calcs/brainstorming/uoc_st/haynsworth_inertia_cascade.py` (Theorem 8, §8)
- `models/sair/tests/test_state_system.py` (Theorem 11, §9bis2 — `test_reciprocity_theorem_gamma_s_*`/`_gamma_a_*`)
- `models/calcs/brainstorming/ds/algebra_bloques_no_simetricos/03_teorema_reciprocidad.py` (Theorem 11, non-survival of the decomposition under $\Omega$, §9bis2)
- `lean/CompositionalAlgebra/Theorem11.lean` (Theorem 11, Lean 4 formalization, no `sorry` — included with this paper)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/correccion_peso_n_ario.py` (weight non-negativity, Appendix A)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/ley_unidad_prueba.py` (unit law, Appendix A)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/relax_vs_colapso.py` (RELAX's non-commutation, Appendix A)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/ley_intercambio_2categoria.py` ($O(\|C\|^2)$ scaling of the exchange gap, Appendix A)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/forma_cerrada_2celda.py` (closed form of the $\Delta_2$ correction 2-cell, Appendix A)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/coherencia_orden_superior.py` (Jacobian cocycle, Appendix A)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/funtor_baez_fong.py` (Baez-Fong functor/Kron reduction, Appendix A)

## References

This paper builds on earlier, still-unpublished work of the same research program (the object $\Gamma$ and the Coherence Unit; the structural potential $P(\Gamma,\rho)$ from Ch13) — summarized self-contained at the start of this document, requiring no external source from the reader. No citable entries with a DOI yet; these will be added here once that work is published.
- Chapter 7 and Chapter 10 of the GSF manuscript (Part I), from which this paper extracts and re-derives material in self-contained form.
