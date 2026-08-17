# Submission Package — Paper B
## "Spacetime Algebra as a Theorem: Deriving Cl(3,1) from the Structure of a Dynamical Unit"

---

## arXiv

### Metadata

**Título:**
Spacetime Algebra as a Theorem: Deriving Cl(3,1) from the Structure of a Dynamical Unit

**Autores:**
Henry Molina (Independent researcher)

**Categoría primaria:** math-ph (Mathematical Physics and Mathematics)

**Categorías secundarias:** math.RA (Rings and Algebras), hep-th (High Energy Physics — Theory)

**Códigos MSC:**
- 15A66 — Álgebras de Clifford, álgebras de espínores
- 83A05 — Relatividad especial
- 70G45 — Geometría diferencial y dinámica de partículas
- 17B25 — Álgebras de Lie excepcionales (para la rama octoniónica §8.2)

**Keywords:**
Clifford algebra, geometric algebra, Hurwitz theorem, spacetime signature, SAIR framework,
operative dynamical unit, Lorentzian signature, wave operator, Frobenius metric, no-Hopf lemma

**Campo "Comments":**
15 pages, 4 numerical verification scripts (companion repository). Companion paper: arXiv:[det³ ID].
Part of the Gamma Space Framework program; see also Molina (2025), working manuscript.

---

### Abstract (para arXiv — en inglés, ≤ 250 palabras)

We prove that any operative dynamical unit (ODU) is necessarily an element of the real Clifford algebra
$\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$, given four structural axioms, the fourth of which makes explicit
a co-location premise otherwise left implicit. A1 (SAIR attribute structure): the unit is described
by a scalar $S$ and three vectors $\mathbf{A}, \mathbf{I}, \mathbf{R}$ in $\mathbb{R}^d$. A2 (geometric
product): structure is governed by the geometric product of those attributes, whose grade-2 part
$\mathbf{I}\wedge\mathbf{R}$ is the Field bivector; the SAIR-to-$\Gamma$ embedding is written explicitly,
with a canonical, gauge-closed choice of reference direction for the scalar slot. A3 (continuous
evolution): the ODU evolves smoothly in time and space at finite propagation speed $c$, with equation of
motion $\ddot\Gamma + \gamma\dot\Gamma - c^2\nabla_{\mathbf{x}}^2\Gamma + \nabla_\Gamma P = N$. A3$'$
(co-location): the attribute space and the propagation coordinates are identified.

From these four axioms, without postulating a spacetime metric or background geometry, we derive:
(i) the closure condition $\binom{d}{2}=d$ forces $d=3$ uniquely via Hodge self-duality of bivectors
in $\mathbb{R}^3$, confirmed by the Eckmann–Hurwitz theorem; (ii) smooth evolution at finite speed
requires a fourth temporal direction independent of the three spatial attributes; (iii) the principal
symbol of the resulting second-order PDE is the Minkowski quadratic form
$\eta = \mathrm{diag}(-1,+1,+1,+1)$, whose real Clifford algebra is $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$.
A completeness corollary shows this signature is the only one of five inertia classes admitting a
well-posed Cauchy problem, and a second corollary states exactly when the state-dependent Gram matrix
$\Gamma_s$ inherits the symbol's signature (Sylvester's law of inertia, under an invertible congruence).

Three closing propositions establish that orthonormality is gauge-redundant (P1), that $\gamma_0$ is the
unique algebraic generator conjugate to $\partial_\tau$ in the Dirac factorization of $\Box$ (P2), and
that the Frobenius norm is the canonical Clifford metric forced by A2 (P3). Classical mechanics and free
electrodynamics appear as structural limits. Isotropy of the spatial Laplacian is anchored to the
$SO(3)$-invariance of $\Gamma$ under rotations of $\{\mathbf{A},\mathbf{I},\mathbf{R}\}$ (P1). The
theorem is explicitly conditional: existence of a grade-1 SAIR quadruple, with Force and Field genuinely
inherent to the domain, is not established here for any specific domain.

The result promotes the spacetime Clifford algebra from a geometric postulate to a structural theorem:
not "given Minkowski space, use $\mathrm{Cl}_{3,1}$", but "from the structure of any evolving dynamical
unit, $\mathrm{Cl}_{3,1}$ is the forced representation."

---

### Instrucciones de envío a arXiv

1. **Formato:** arXiv acepta PDF directo. Subir `spacetime_algebra_as_theorem_molina2026.pdf`. Si piden fuente, convertir con:
   ```bash
   pandoc spacetime_algebra_as_theorem_molina2026.md -o spacetime_algebra_as_theorem_molina2026.tex --standalone
   ```
   y subir el .tex + figuras.

2. **Endorsement:** Si arXiv rebota por falta de aval en math-ph, opciones:
   - Intentar categoría **math.RA** (menos restrictiva)
   - Buscar aval en https://arxiv.org/auth/endorse — cualquier autor registrado en math-ph puede avalar
   - Alternativamente publicar primero en Zenodo (DOI inmediato) y referenciar desde el paper

3. **Orden recomendado:** subir det³ primero (tiene Zenodo DOI ya) → al aceptarse, usar ese perfil para Paper B → ya no necesita aval la segunda vez.

---

## Zenodo

### Metadata para upload en Zenodo

**Título:** Spacetime Algebra as a Theorem: Deriving Cl(3,1) from the Structure of a Dynamical Unit

**Autores:** Molina, Henry

**Afiliación:** Independent researcher

**Tipo de upload:** Preprint / Journal article

**Descripción (resumen en español para Zenodo):**

Probamos que cualquier unidad dinámica operativa (en el GSF: Unidad de Coherencia, UoC) es
necesariamente un elemento del álgebra de Clifford real $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$,
dados cuatro axiomas estructurales. El Axioma
A1 (estructura de atributos SAIR) postula un escalar $S$ y tres vectores $\mathbf{A},\mathbf{I},\mathbf{R}$
en $\mathbb{R}^d$. El Axioma A2 (producto geométrico) establece que la dinámica se rige por el producto
geométrico de esos atributos, y se escribe explícitamente el embebido SAIR→$\Gamma$, con una elección
canónica y de gauge cerrado para la dirección de referencia del casillero escalar. El Axioma A3
(evolución continua) exige suavidad en tiempo y espacio con velocidad finita $c$. El Axioma A3′
(co-localización) identifica el espacio de atributos con las coordenadas de propagación.

De estos cuatro axiomas, sin postular una métrica de espacio-tiempo, se deriva: (i) la condición de
clausura $\binom{d}{2}=d$ fuerza $d=3$ de forma única; (ii) la evolución suave requiere una cuarta
dirección temporal independiente; (iii) el símbolo principal de la EOP resultante es la forma de
Minkowski con firma $(3,1)$, cuya álgebra de Clifford real es $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$.
Un corolario de completitud muestra que esta firma es la única, de cinco clases de inercia posibles, que
admite un problema de Cauchy bien puesto; un segundo corolario establece exactamente cuándo la matriz de
Gram $\Gamma_s$ (dependiente del estado) hereda la firma del símbolo (ley de inercia de Sylvester, bajo
una congruencia invertible).

El resultado eleva el álgebra de Clifford del espacio-tiempo de postulado geométrico a teorema
estructural. El teorema es explícitamente condicional: la existencia de una cuádrupla SAIR de grado 1,
con Fuerza y Campo genuinamente inherentes al dominio, no se establece aquí para ningún dominio
específico.

**Palabras clave:** álgebra de Clifford, teorema de Hurwitz, firma Lorentziana, marco SAIR, operador de onda

**Licencia:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Comunidades Zenodo sugeridas:** `mathematics`, `mathematical-physics`, `clifford-geometric-algebras`

**Relaciones:**
- "Este preprint está relacionado con" → DOI del det³ (10.5281/zenodo.20752208)

**Archivos a subir:**
- `spacetime_algebra_as_theorem_molina2026.pdf` (versión principal)
- `code/verify_cl31.py`
- `code/verify_clifford_metric.py`
- `code/verify_frobenius.py`
- `code/verify_det_invariance.py`

---

*Preparado: jul-03 2026*
