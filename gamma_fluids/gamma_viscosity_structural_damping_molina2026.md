---
title: "Γ: Viscosity as Structural Damping"
subtitle: "Stokes and Navier-Stokes as limits of one equation, and the subcritical transition in pipe flow"
author: "Henry Molina · Independent researcher, Bogotá, Colombia · henrymolina@gmail.com"
date: "July 2026"
---

*Self-contained manuscript beyond the algebraic theorem and equation of motion of the companion
papers (Molina 2026, "Spacetime Algebra as a Theorem"; and Molina 2026, "Γ: One Equation of
Motion, Three Sectors"), which this article reuses without re-deriving. Numerical verifications
cited in the text are in `code/` (see Appendix), published alongside this paper at
https://github.com/hmolinab/papers/tree/main/gamma_fluids. Each result is marked by its status: a
theorem with a complete proof, a structural correspondence (an isomorphism or algebraic
relabeling with a known physical object, not a new physical theorem), a finding verified
numerically or against tabulated data without a closed analytic proof, or an open frontier. The
text says so explicitly in each case.*

# Abstract

The damping parameter γ of GSF's equation of motion (Γ̈+γΓ̇−c²∇²Γ+∇P=N) has no fixed physical
interpretation on its own: it enters through the non-conservative extension of the Lagrangian,
not through the field part. This paper shows that in the fluid domain γ operationalizes exactly
as ν=c²(ρ)/γ, the kinematic viscosity, and that this identity produces three verifiable results
without tuning any new parameter. First, the Stokes equations emerge as the rigorous singular
limit of the field EOM under three physically named conditions (high friction, small amplitude,
short scale), each with a convergence theorem already published in the stochastic differential
equations and fluid mechanics literature; and full Navier-Stokes, including the advection term,
is recovered by requiring the same Galilean covariance that any continuum dynamics must respect.
Second, the identity ν=c²(ρ)/γ reproduces tabulated viscosity ratios across twenty-five orders of
magnitude (from mercury to Earth's mantle) with a single variable and zero fitting, and the law
γ∝ρ is confirmed to 0.1% precision over five decades of density for air. Third, and of greatest
interest for engineering applications, the subcritical transition to turbulence in pipe flow (the
non-modal transient growth that precedes turbulence at subcritical Reynolds numbers) is derived
as a structural property of the antisymmetric sector Γ_a of the same matrix: a purely symmetric
(diagonal) configuration is shown to forbid transient growth, the shear responsible for it cannot
come from the potential's gradient (a Hessian is symmetric, hence normal, hence no
amplification), and it does come exactly from the convective term of the material derivative.
This chain reproduces the standard G_max∼Re² scaling with the geometric prefactor fixed from the
operator's algebra, consistent in order of magnitude with the observed Re_c≈2040 in pipe flow.
This paper's success criterion is not a new law of turbulence: it is that a single algebraic
identity, with no parameters per domain, correctly organizes the reduction to Stokes, the scale
of real viscosity, and the mechanism of the subcritical transition, with the boundaries named
where the result depends on constants taken from the literature.

---

# 1. The parameter γ and its operationalization

## 1.1 Starting point (cited, not re-derived)

This paper presupposes the configuration object Γ and the equation of motion of the companion
papers: Γ = Γ_s ⊕ Γ_a ∈ M₄(ℝ) (the four SAIR grades over the geometric algebra G(3)) and

$$\ddot\Gamma + \gamma\dot\Gamma - c^2\nabla^2\Gamma + \nabla_\Gamma P(\Gamma,\rho) = N(t), \qquad
P = \|\Gamma\|_F^2+\mu(\rho)\det\Gamma+\beta\|\Gamma\|_F^4$$

with μ(ρ) and β fixed by the same AM-GM bound of the companion paper (zero additional free
parameters). The environmental noise N(t) is paired with γ by the fluctuation-dissipation
theorem.

γ does not appear in the conservative action: it enters through the Rayleigh dissipation
extension, and is a coarse-graining parameter, the rate at which the unit of coherence loses
memory against its environment. Operationalizing it in a concrete domain is the empirical
question this paper answers for fluids.

## 1.2 The SAIR dictionary in fluids

Each observable occupies the Clifford grade that matches its tensor rank, the same covariance
criterion used in the companion paper for Navier-Stokes: a rotor preserves grade, so a scalar
must go to grade 0, a vector to grade 1, and so on. The resulting assignment is unique given that
criterion:

| SAIR role | Variable | Grade in Cl₃,₀ | Physical content |
|:---:|---|:---:|---|
| S | density ρ | 0 (scalar) | inertial identity of the parcel; coefficient in ρ·Du/Dt=F, fixed for incompressible flow |
| A | velocity **u**=(u_x,u_y,u_z) | 1 (vector) | immediate kinematic capacity |
| I | vorticity **ω**=∇×**u** | 2 (bivector) | rotational act; exactly Γ_a, the antisymmetric part of ∂_j u_i |
| R | helicity h=**u**·**ω** | 3 (pseudoscalar) | topological context: knottedness of vortex lines, conserved in ideal flow (Moffatt, 1969) |

Pressure occupies no SAIR grade: it is the Lagrange multiplier of the incompressibility
constraint ∇·**u**=0, identified via the Leray-Hodge decomposition, and enters as an effective
thermodynamic forcing from the environment on the flow grades, not as an internal degree of
freedom of Γ.

With this assignment, the structural law Force = S·A is exactly the left-hand side of
Navier-Stokes (ρ times the material derivative of **u**), and the Lamb vector splits advection
into a gradient part (which goes to pressure) and an irreducible part that lives in the Γ_a
sector:

$$(\mathbf{u}\cdot\nabla)\mathbf{u} = \nabla\!\left(\tfrac{1}{2}|\mathbf{u}|^2\right) - \mathbf{u}\times\boldsymbol{\omega}$$

---

# 2. Stokes as a singular limit of the EOM

## 2.1 The three physically named limits

Projecting the field EOM onto the velocity subsystem (with ρ fixed, as appropriate for
incompressible flow), three limits reduce the EOM to the Stokes equations:

- **High friction** (ε=1/(γT)→0): the EOM goes from second to first order in time. This is
  exactly the Smoluchowski-Kramers limit of high-friction Langevin dynamics, which has a
  published convergence theorem (Nelson, 1967; Freidlin-Wentzell): the second-order solution
  converges to the first-order one with error O(ε).
- **Small amplitude** (|**v**|∼ε→0): the nonlinear term adj(Γ) scales as ε² and becomes
  subdominant.
- **Short scale** (L≪c, equivalent to low Mach number): the structural mass term, which endows
  the field with a screening length ℓ=c, is negligible compared to the diffusive term c²∇²Γ.
  This regime is exactly the low-Mach incompressible limit, with convergence theorems available
  in the mathematical literature (Schochet, 2010; Lions-Masmoudi, 1998; Métivier-Schochet, 2001).

Projecting onto the active velocity component, with the pressure gradient entering as an
effective thermodynamic injection from the environment, gives exactly:

$$\boxed{\partial_t v_i=\nu_{\mathrm{kin}}\,\nabla^2 v_i-\frac1{\rho}\partial_i p,\qquad \nabla\!\cdot\mathbf v=0,\qquad \nu_{\mathrm{kin}}=\frac{c^2(\rho)}{\gamma}.}$$

**Theorem (Stokes as a singular limit).** *Under the three coupled limits above, there exists a
solution u of the Stokes equations with ν=c²/γ such that ‖Γ−u‖≤C·max(ε, Ma, L/c) on [0,T].* The
existence of the limit and the form of the equation are proved, each link is a convergence
theorem already published in its own domain (Smoluchowski-Kramers, low-Mach limit, Leray-Hodge);
adapting those theorems from scalar/vector fields to Γ's matrix formalism, and obtaining the
explicit constant C in that formalism, remains as pending work.

## 2.2 Full Navier-Stokes

The step from Stokes (linear) to Navier-Stokes (with advection) requires no additional postulate
beyond the Galilean covariance that any continuum dynamics must respect: under a boost
x'=x−Vt, covariance requires the time derivative to become the material derivative
D/Dt=∂_t+(**u**·∇) (verified symbolically that only D/Dt, not ∂_t alone, is form-invariant under
the boost). Substituting that derivative into the flow slots, and using the Lamb identity to
separate the gradient part (which goes to pressure) from the irreducible part (which lives in
Γ_a), recovers exactly

$$\partial_t \mathbf u+(\mathbf u\cdot\nabla)\mathbf u=\nu\nabla^2\mathbf u-\tfrac1\rho\nabla p+\mathbf f,\qquad \nabla\!\cdot \mathbf u=0.$$

Navier-Stokes is thus derived on the same grade-assignment postulate already used by Stokes, with
no additional parameter or postulate. The remaining gap is purely algebraic: the same
Clifford→M₄(ℝ) weld of the companion paper, not something specific to fluids.

---

# 3. The operationalization of γ

The identity ν=c²(ρ)/γ gives the first quantitative operationalization of γ in a concrete
physical domain: high damping means high viscosity means the Stokes regime; low damping means
the inviscid/Euler regime. The Reynolds number is the physical proxy of 1/γ:

$$\mathrm{Re}=\frac{vL}{\nu_{\mathrm{kin}}}=\frac{vL\,\gamma}{c^2(\rho)}.$$

The field stiffness c²(ρ) follows the scaling law of the companion paper (a power of ρ that only
activates near the cosmological reference density); at any terrestrial fluid's density, c² is
effectively constant, so ratios of γ between fluids become pure ratios of tabulated viscosity.

---

# 4. Data without fitting

## 4.1 Twenty-five orders of magnitude in viscosity ratios

With c² constant at fluid densities, γ_A/γ_B=ν_B/ν_A is a pure ratio of tabulated data, with no
additional theoretical assumption (beyond both fluids sharing the same structural density ρ, an
explicit assumption, not a data point).

| Fluid | ν (×10⁻⁶ m²/s) | γ relative to water |
|---|---:|---:|
| Mercury | 0.12 | 8.4 |
| Acetone | 0.43 | 2.34 |
| Water (reference) | 1.004 | 1.000 |
| Seawater | 1.05 | 0.956 |
| D₂O | 1.251 | 0.803 |
| Blood plasma | ∼1.3 | ∼0.77 |
| Ethanol | 1.52 | 0.660 |
| Glycerol (100%) | 1190 | 8.4×10⁻⁴ |
| Glacier ice (creep) | ∼10¹⁸ | ∼10⁻¹⁸ |
| Earth's upper mantle | ∼3×10²³ | ∼3×10⁻²⁴ |

The full range spans twenty-five orders of magnitude with a single variable, a single equation,
and zero fitted parameters. The value of this table does not depend on having derived
Navier-Stokes from scratch: it functions as a robust phenomenological anchor, in the same sense
that Kepler's third law functioned as an empirical scaling law before Newton derived the gravity
that explains it.

## 4.2 γ proportional to ρ, 0.1% over five decades

The kinematic viscosity of air in the continuum regime obeys ν∝1/ρ to 0.1% precision over
pressures from 10⁻³ to 10 atm. Combined with the saturation of c² at those densities, this
implies γ∝ρ linearly over five decades of density, the strongest empirical confirmation to date
of the structural relation between γ and density.

## 4.3 Absolute calibration (conditional)

The ratios above fix relative γ, not the absolute scale. Under the hypothesis that
c²(ρ_water)≈c²_light (a theoretical claim, not a measurement), the implied absolute scale for
water is γ≈9×10²² s⁻¹, with a structural relaxation time of order 10⁻²³ s (yoctoseconds,
sub-nuclear regime, not directly accessible to femtosecond Raman/IR spectroscopy). This number is
a conditional prediction under that hypothesis, not a measurement.

---

# 5. Acoustic-electromagnetic identity

In the irrotational limit (Γ_a=0, no sources, no vorticity), the EOM reduces to the massless
wave equation for the velocity potential, □φ=0, the same structural mechanism as the free
electromagnetic photon in the companion paper. The classical acoustic-electromagnetic analogy
(Bergmann, 1946), used in acoustic cloaking techniques, has a structural reading here: it is not
a formal analogy but rather both being instances of the same det=0 sector (γ≈0, wave regime) of
the same algebraic object, differing only in which physical observables occupy the slots.

---

# 6. The subcritical transition in pipe flow

## 6.1 Two regimes of the same equation

The Stokes reduction of §2 is leading order in 1/γ (the acceleration Γ̈ is dropped). Retaining
that term, the next-order correction gives a linearized first-order system

$$\dot{\mathbf Y}=\mathbf A\mathbf Y,\qquad \mathbf A=\begin{pmatrix}0 & I\\ -\mathcal L_{\bar\Gamma} & -\gamma I\end{pmatrix},$$

with A structurally non-normal. Non-normal operators support transient amplification of
perturbations even when all eigenvalues lie in the stable half-plane, the known mechanism of the
subcritical transition in pipe flow.

## 6.2 The Re² scaling and its origin in Γ_a

For the minimal lift-up-type non-normal operator (the standard shear-amplification mechanism in
hydrodynamic stability), the amplification G(t)=‖e^{At}‖² has a closed maximum proportional to
Re², with the geometric prefactor fixed from the operator's algebra (verified numerically:
log-log slope of 2.000, constant independent of Re). This recovers the standard scaling from the
hydrodynamic stability literature (Reddy-Henningson, 1993; Trefethen et al., 1993) and fixes the
prefactor from first algebraic principles, not by fitting.

What this framework contributes beyond recovering that scaling is a structural diagnostic
result, verified in three steps, with an important precision about what exactly each step
closes.

1. A purely diagonal (symmetric) configuration of Γ forbids transient growth: G_max=1 for all
   Re. The shear coupling needed for the lift-up mechanism cannot live on the diagonal.
2. The shear cannot come from the potential's gradient ∇²P alone: the Hessian of any potential
   is symmetric (mixed derivatives commute), hence normal, hence no transient amplification is
   possible. This is a proved no-go, not a qualitative observation, and it correctly rules out
   that any generic non-symmetric perturbation of the bare EOM of Γ (without the convective
   term) reaches the Re² scaling: verified that a generic non-normal coupling, hand-built
   without the specific lift-up structure, gives only G_max∼Re¹.
3. The shear does come, exactly, from the convective term of the material derivative, linearized
   around a base flow profile with shear. That convective term is not foreign to this
   framework: it is exactly what the derivation of Navier-Stokes in §2.2 adds to the bare EOM
   via Galilean covariance. Linearizing that term, the resulting coupling is necessarily
   off-diagonal, that is, it lives in the antisymmetric sector Γ_a, and it reproduces the exact
   Re² scaling with the geometric prefactor of the previous step.

The precise statement, so as not to overclaim, is: the Re² scaling does not come from the bare
EOM of Γ with any non-symmetric perturbation (that is ruled out, point 2); it comes from the full
fluid instantiation of this equation, which by Galilean covariance is Navier-Stokes with its
convective term (§2.2), linearized around a base shear profile. The base profile U(y) remains an
external input, the same one required by the entire standard theory of hydrodynamic stability
(Orr-Sommerfeld/Squire), not something specific to this framework. With that precision, Γ
functions as a structural diagnostic tool: the transient growth that precedes subcritical
turbulence is a direct observable of the antisymmetric sector of the configuration matrix, once
the convective term that covariance requires is included.

## 6.3 Comparison with the observed critical Reynolds number

For Poiseuille pipe flow, this chain predicts Re_c≈2200 using a geometric constant C≈50 and a
threshold perturbation amplitude A₀≈10⁻⁷ taken from the experimental literature (Hof et al.,
2003), in reasonable agreement with the observed Re_c≈2040. What is structural here, and what
depends on external constants, must be distinguished precisely:

- **Structural (derived, not fitted):** that the scaling is Re² and not another power; that this
  scaling strictly requires the active Γ_a sector; that the responsible shear cannot come from
  the gradient sector.
- **Dependent on literature constants:** the exact numerical value of Re_c≈2040-2200 requires the
  geometric constant C and the threshold amplitude A₀, both taken from published experimental
  measurements, not derived from the EOM.

A second, distinct regime of the same equation explains why pipe and channel differ
qualitatively: channel flow transitions to turbulence via a modal mechanism
(Tollmien-Schlichting) at Re_c≈5772, while pipe flow, where that mode is linearly stable for all
Re, transitions via the non-modal transient-growth mechanism at Re_c≈2040. Both are the same
object Γ and the same equation; what distinguishes the regimes is the Reynolds number of each
geometry, not a different fluid parameter.

---

# 7. Honest frontiers

| Frontier | Status | Note |
|---|:---:|---|
| Matrix constant C of the convergence bound to Stokes (Theorem §2.1) | open | each link of the chain of limits has a convergence theorem published in its own domain; adapting the explicit bound to Γ's matrix formalism remains pending |
| SAIR→Γ grade assignment for fluids | closed by covariance, except the general weld | the remaining ambiguity is the same Clifford→M₄(ℝ) weld of the companion paper, not fluid-specific |
| Viscosity ratios over 25 orders | verified against data, conditional on common ρ | assumption of equal structural density between compared fluids, explicit, not independently verified |
| Absolute scale of γ for water (γ≈9×10²² s⁻¹) | conditional | depends on the hypothesis c²(ρ_water)≈c²_light, an unverified theoretical claim |
| Homeodynamic window water/D₂O and its relation to toxicity | open frontier | calibrated from toxicity data, not derived; the causal (vs. correlational) reading is not established |
| Re_c≈2040 in pipe flow, exact numerical value | verified qualitatively, not first-principle | uses geometric constant and threshold amplitude from Hof et al. (2003); what is structural (Re² scaling, origin in Γ_a) is indeed derived |
| Absolute scale of ρ (needed for calibration beyond ratios) | open | referred to in the companion paper as pending program work |

---

# 8. Conclusion

γ, the one parameter of the equation of motion without a fixed interpretation from the algebraic
framework alone, operationalizes precisely in fluids: ν=c²/γ reproduces viscosity data across
twenty-five orders of magnitude without fitting anything, and γ∝ρ is confirmed to 0.1% over five
decades. The reduction to Stokes and the derivation of full Navier-Stokes rest on convergence
theorems already published in their own domains, not on qualitative identifications. And the
result of greatest applied interest, the subcritical transition in pipe flow, reduces to a closed
algebraic chain: without the antisymmetric sector Γ_a there is no transient growth, that sector
cannot be substituted by the potential's gradient, and it arises exactly from the convective
transport term. The exact numerical value of Re_c depends on constants taken from the
experimental literature; what this framework contributes is not replacing those measurements but
explaining, from the structure of the operator, why the scaling is Re² and where the mechanism
that produces it lives.

---

# References

Bergmann, P. G. (1946). The wave equation in a medium with a variable index of refraction.
*Journal of the Acoustical Society of America*, 17(4), 329–333.

Freidlin, M. I. and Wentzell, A. D. (2012). *Random Perturbations of Dynamical Systems* (3rd
ed.). Springer.

Hof, B., Juel, A., and Mullin, T. (2003). Scaling of the turbulence transition threshold in a
pipe. *Physical Review Letters*, 91(24), 244502.

Lions, P.-L. and Masmoudi, N. (1998). Incompressible limit for a viscous compressible fluid.
*Journal de Mathématiques Pures et Appliquées*, 77(6), 585–627.

Métivier, G. and Schochet, S. (2001). The incompressible limit of the non-isentropic Euler
equations. *Archive for Rational Mechanics and Analysis*, 158(1), 61–90.

Moffatt, H. K. (1969). The degree of knottedness of tangled vortex lines. *Journal of Fluid
Mechanics*, 35(1), 117–129.

Molina, H. (2026). Spacetime algebra as a theorem: deriving Cl(3,1) from the structure of a
dynamical unit. DOI: 10.5281/zenodo.21184515

Molina, H. (2026). Γ: one equation of motion, three sectors: structural correspondences with
Newton, Navier-Stokes, Maxwell, and Schrödinger. DOI: 10.5281/zenodo.21496578

Nelson, E. (1967). *Dynamical Theories of Brownian Motion*. Princeton University Press.

Reddy, S. C. and Henningson, D. S. (1993). Energy growth in viscous channel flows. *Journal of
Fluid Mechanics*, 252, 209–238.

Schochet, S. (2010). The incompressible limit in nonlinear elasticity. In *Handbook of
Mathematical Fluid Dynamics*, Vol. 4. Elsevier.

Trefethen, L. N., Trefethen, A. E., Reddy, S. C., and Driscoll, T. A. (1993). Hydrodynamic
stability without eigenvalues. *Science*, 261(5121), 578–584.

---

\appendix

# Appendix — Calculation scripts

Verification scripts included in `code/` alongside this paper, published at
https://github.com/hmolinab/papers/tree/main/gamma_fluids:

```
code/
  pieza2_transient_growth.py   -> G_max=Re²/C scaling (lift-up), Γ_a diagnostic, ∇²P no-go, S=∂_yU (§6)
```

Requirements: `numpy`, `scipy`.

Pending implementation as an independent script (currently cited from published tables and fits,
not reproduced here in code): the viscosity ratio table of §4.1 against tabulated reference
values, the ν∝1/ρ fit for air of §4.2, and the c² saturation discriminating factor of §4.3.

---

*Gamma Space Framework Program. July 2026.*
*henrymolina@gmail.com*
