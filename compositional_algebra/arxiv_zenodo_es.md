# Submission Package
## "Un álgebra composicional para configuraciones de Unidades de Coherencia: clausura, balance de entropía, y aditividad de inercia" / "A compositional algebra for coherence-unit configurations: closure, entropy balance, and inertia additivity"

*Preparado: ago-6 2026. Ambas versiones (ES/EN), PDFs, y la formalización Lean 4 ya están
generados en este directorio — ver `README.md` para el listado completo de archivos.*

---

## Zenodo

### Metadata para upload en Zenodo

**Título:** Un álgebra composicional para configuraciones de Unidades de Coherencia: clausura, balance de entropía, y aditividad de inercia / A compositional algebra for coherence-unit configurations: closure, entropy balance, and inertia additivity

**Autores:** Molina, Henry

**Afiliación:** Independent researcher

**Tipo de upload:** Preprint

**Idioma:** Español (versión principal) + English (traducción incluida)

**Fecha de publicación:** (fijar al momento del upload)

**Descripción (resumen para Zenodo, español):**

Doce operaciones composicionales que aparecen, con nombres distintos, en física, química,
biología y sistemas sociales — unión, acoplamiento, fusión, fisión, absorción, disolución,
entre otras — colapsan en cinco primitivos (formar el conjunto, acoplar, desacoplar,
marginalizar, copiar, relajar) y una sola identidad de álgebra lineal: la fórmula de Schur del
determinante de bloques, aplicada a un objeto de configuración $\Gamma\in M_4(\mathbb{R})$. De
esa única identidad se deriva, sin un postulado por operación, el balance de entropía completo,
una cota exacta de trabajo mínimo (análogo de Jarzynski-Crooks), y una medida domain-agnóstica
de cohesión estructural irreducible.

Alrededor de ese núcleo, el paper prueba once teoremas. Removiendo la restricción a matrices
definidas positivas, la aditividad de inercia de Haynsworth (1968) extiende el álgebra a
cualquier signatura, revelando que la clasificación por signo de determinante usada en todo el
paper es la partición más gruesa posible de la inercia de una matriz simétrica, para cualquier
dimensión (Corolario 8.1). Un resultado relacionado (Teorema 9) muestra que ningún potencial
invariante de conjugación puede distinguir estructuralmente sub-sectores que comparten esa
fase. Dos teoremas adicionales (10 y 11) caracterizan exactamente cuándo y cómo la eliminación
de un componente crea o preserva estructura antisimétrica (bivector) en el sobreviviente —
el segundo, formalizado en Lean 4 sin `sorry`. Una línea más incipiente (Apéndice A) propone
que el álgebra completa es una categoría enriquecida sobre el mismo balance de entropía, en el
sentido de Lawvere (1973); se documenta como trabajo en curso, no como resultado cerrado.

El paper no reclama derivar física de partículas: sus correspondencias ilustrativas (fuerza de
Coulomb/Lorentz, gas ideal, enlace químico) muestran la aplicabilidad del álgebra sobre casos ya
conocidos, no una derivación nueva de esos fenómenos.

**Palabras clave:** álgebra composicional, complemento de Schur, aditividad de inercia de
Haynsworth, entropía estructural, termodinámica composicional, categorías enriquecidas,
sistemas dinámicos abiertos

**Licencia:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Comunidades Zenodo sugeridas:** `mathematics`, `mathematical-physics`, `dynamical-systems`

**Relaciones:**
- Ninguna todavía — el paper depende de trabajo previo no publicado del programa (ver "Nota
  sobre dependencias" en el propio paper); se agregará la relación cuando ese trabajo tenga
  DOI propio. No relacionar con `weld_clifford`/`determinant_cubic_source` — son resultados
  independientes del mismo programa, sin dependencia directa de contenido con este paper.

**Archivos a subir:**
- `algebra_composicional_unidades_coherencia_molina2026.pdf` (versión principal, español).
- `compositional_algebra_of_coherence_units_molina2026.pdf` (traducción, inglés).
- `lean/CompositionalAlgebra/Theorem11.lean` (formalización del Teorema 11, sin `sorry`,
  verificado con `#print axioms`).

---

## arXiv (opcional, más adelante)

### Abstract (para arXiv — en inglés, ≤ 250 palabras)

Twelve compositional operations that appear, under different names, in physics, chemistry,
biology and social systems — union, coupling, fusion, fission, absorption, dissolution, among
others — collapse into five primitives (forming the set, coupling, decoupling, marginalizing,
copying, relaxing) and a single linear-algebra identity: the Schur block-determinant formula,
applied to a configuration object $\Gamma\in M_4(\mathbb{R})$. From that single identity,
without a per-operation postulate, follows the complete entropy balance, an exact minimum-work
bound (a Jarzynski-Crooks analogue), and a domain-agnostic measure of irreducible structural
cohesion.

Around that core, the paper proves eleven theorems. Removing the restriction to positive-definite
matrices, Haynsworth's (1968) inertia additivity extends the algebra to any signature, revealing
that the determinant-sign classification used throughout is the coarsest possible partition of a
symmetric matrix's inertia, for any dimension (Corollary 8.1). A related result (Theorem 9) shows
that no conjugation-invariant potential can structurally distinguish sub-sectors sharing that
phase. Two further theorems (10 and 11) characterize exactly when and how eliminating a component
creates or preserves antisymmetric (bivector) structure in the survivor — the second formalized
in Lean 4 with no `sorry`. A more incipient line (Appendix A) proposes that the full algebra is a
category enriched over the same entropy balance, in the sense of Lawvere (1973); documented as
work in progress, not a closed result.

The paper does not claim to derive particle physics: its illustrative correspondences
(Coulomb/Lorentz force, ideal gas, chemical bonding) show the algebra's applicability to
already-known cases, not a new derivation of those phenomena.

### Metadata

**Categoría primaria:** math.RA (Rings and Algebras)

**Categorías secundarias:** math-ph (Mathematical Physics), math.DS (Dynamical Systems)

**Códigos MSC:**
- 15A24 — Matrix equations and identities (Schur complement)
- 15A63 — Quadratic and bilinear forms, inner products (Sylvester's law of inertia / Haynsworth)
- 18D20 — Enriched categories (Appendix A, Lawvere metric-space-as-category)

**Keywords:** compositional algebra, Schur complement, Haynsworth inertia additivity,
structural entropy, compositional thermodynamics, enriched categories, open dynamical systems

**Comments:** ~30 pages, Lean 4 formalization included (`lean/`). Companion book chapter:
`part1/07_compositional_operations.md` (public, Zenodo, same program).

**Nota:** no se ha ejecutado ninguna submission a arXiv todavía — esta sección queda lista
para cuando HM decida seguir esa vía, después de la publicación en Zenodo (mismo orden que
`weld_clifford`).

---

## Checklist antes de subir

Todo lo de contenido y producción está listo. Solo queda una decisión de HM:

- [x] `build_pdf.sh` — creado, envoltorio local sobre `scripts/build_pdf.sh` del repo.
- [x] PDF generado, ES y EN.
- [x] Versión en inglés — generada ago-6 2026.
- [x] Formalización Lean del Teorema 11 — movida a este directorio público, build limpio,
      verificada con `#print axioms` (solo axiomas estándar de mathlib).
- [ ] **Decisión de HM, único bloqueante real:** ejecutar la subida real a Zenodo (crear la
      cuenta/entrada, subir los archivos de este directorio).
