# Verificación formal (Lean 4 + mathlib) — motor compartido, papers públicos

**Estructura (ago-4 2026, pedido de HM):** el CÓDIGO FUENTE vive dentro de cada paper
(`papers/<paper>/lean/`), no aquí — este directorio es solo el "motor" compartido: un
único `lakefile.toml` + una única caché de mathlib (~7.4GB), para no pagar ese costo
por cada paper por separado. Se confirmó que Lake soporta `srcDir` apuntando a un
directorio hermano (`../<paper>/lean`) sin problema — los `.olean` compilados siguen
viviendo en `.lake/` de este directorio, el código fuente en el paper.

- `papers/determinant_cubic_source/lean/` — Lema no-Hopf.
- `papers/weld_clifford/lean/` — Lema 2 (Clifford).

El material de `brainstorming/papers/` (no público) vive en un proyecto Lean SEPARADO,
`brainstorming/papers/formal_verification/` — separación física deliberada (jul-31
2026, pedido de HM), porque `papers/` puede terminar reflejado en `public_github/` y
`brainstorming/` nunca debe filtrarse ahí. Mismo patrón de motor-compartido +
código-por-paper, aplicado ahí también.

Origen (jul-31 2026, pedido de HM): "¿tiene sentido usar Lean para probar nuestros
papers?" — sí, para el subconjunto de resultados puramente algebraicos/formales que ya
llevan etiqueta `[teorema]`/`[D]` (álgebra lineal, álgebra de Clifford de dimensión
finita), NO para resultados que dependen de interpretación física, verificación
numérica contra datos, o elecciones de modelado.

## Setup

- `elan` instalado en `~/.elan/bin` — NO está en el PATH por defecto:
  `export PATH="$HOME/.elan/bin:$PATH"`.
- `lake init gsf_lean math` (plantilla con mathlib) — mathlib fijado a `v4.32.2` en
  `lakefile.toml`.
- `.lake/` (caché de mathlib, ~7.4GB) en `.gitignore`, no se versiona. Reproducir:
  `lake exe cache get` + `lake build` (desde ESTE directorio, no desde el paper).
- **REPL de Lean** (jul-31 2026): `leanprover-community/repl` clonado y compilado
  contra el mismo toolchain (`v4.32.2`, se sobreescribe su `lean-toolchain` propio antes
  de `lake build`). No vive en este repo (herramienta de desarrollo local, en `/tmp` en
  la máquina donde se usó). Da feedback interactivo del estado de la prueba (goal state)
  vía JSON por stdin/stdout, sin necesitar GUI/VS Code.

## Cómo agregar un paper nuevo

1. `mkdir papers/<paper>/lean/<NombreLib>` (el nombre de librería en PascalCase).
2. Escribir el archivo raíz `papers/<paper>/lean/<NombreLib>.lean` con los `import
   <NombreLib>.<Archivo>` de cada teorema.
3. En `lakefile.toml` (aquí), agregar:
   ```toml
   [[lean_lib]]
   name = "<NombreLib>"
   srcDir = "../<paper>/lean"
   ```
   y agregar `<NombreLib>` a `defaultTargets`.
4. `lake build` desde este directorio.

## Estado

- `papers/determinant_cubic_source/lean/DeterminantCubicSource/NoHopf.lean` —
  **Lema 1 (sin Hopf)**, §6: el Jacobiano `J=-G⁻¹H` de un flujo métrico-gradiente
  (`G≻0` simétrica, `H` simétrica) tiene espectro real. **CERRADO COMPLETO** (jul-31
  2026, sin ningún `sorry`). Bloqueo de mathlib RESUELTO: el camino de prueba del paper
  necesita raíz cuadrada de matriz (`J=G^{1/2}SG^{-1/2}`), que mathlib no tiene lista
  para usar -- la solución no fue construirla, fue evitarla del todo reformulando como
  el problema de autovalores generalizado clásico (`det(μI-G⁻¹H)=0 ⟺ det(μG-H)=0`),
  resuelto con un argumento sesquilineal elemental (`sesquilinear_real_of_isSymm`,
  probado completo) más positividad de la forma cuadrática de `G` (descomposición
  real/imaginaria de `v` + `Matrix.PosDef.dotProduct_mulVec_pos`). `lema_1_sin_hopf`
  ensambla todo: extrae el vector propio del espectro (`Matrix.charpoly_map`,
  `Matrix.mem_spectrum_iff_isRoot_charpoly`, `Matrix.mulVec_injective_iff_isUnit`),
  deriva `Hv=-μGv`, y concluye `μ.im=0` por cancelación. Primer teorema de este
  programa cerrado íntegramente con ayuda del REPL de Lean.

- `papers/weld_clifford/lean/WeldClifford/Lema2Clifford.lean` — **Lema 2** (§3.3): en
  `d=3`, `{A,I,R}` generan `Cl(3,0)=G(3)` como subálgebra. **CERRADO COMPLETO** (ago-1
  2026, sin `sorry`). La parte de GENERACIÓN es exactamente el teorema general
  `CliffordAlgebra.adjoin_range_ι`, ya en mathlib para cualquier espacio cuadrático —
  se instancia para una base cualquiera `{v i}` de un módulo `M`
  (`lema_2_generadores_base`, caso general) y para `A,I,R` = base estándar de `ℝ³`
  (`lema_2_AIR_generan_Cl30`, caso concreto del paper). **NO atacado**: el conteo de
  dimensión (`8=2³`, grado 2 = bivectores de dim 3, grado 3 = pseudoescalar de dim 1) —
  mathlib no tiene `finrank (CliffordAlgebra Q) = 2^finrank M` listo para usar
  (revisado `CliffordAlgebra/*.lean` y `ExteriorAlgebra/*.lean`, ninguno lo tiene);
  construirlo es un desarrollo aparte (isomorfismo con el álgebra exterior graduada).

## Candidatos no atacados todavía

- Lemas 1, 3, 4 de `weld_clifford` (dimensión forzada por Hurwitz/clausura, tiempo como
  evolución, firma de Lorentz vía símbolo principal) y Teoremas 1-2 de
  `determinant_cubic_source` (reducción de variedad central, cúspide $A_3$): dependen
  de axiomas físicos (A1-A3) sin formalizar, o de teoría de bifurcaciones/variedad
  central — mucho más pesados, no priorizados. El Lema 1 en particular usa el teorema
  de Hurwitz/Eckmann (producto cruz solo en dim 1,3,7 ↔ álgebras de división normadas),
  que no parece estar en mathlib.

## Convención de honestidad

Nunca dejar un `theorem ... := by sorry` sobre un enunciado que no es el real (p.ej.
`True`) -- eso simula una formalización que no existe. El enunciado debe ser el
resultado real del paper, bien tipado; el `sorry` marca solo la prueba pendiente.
