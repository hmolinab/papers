# Verificación formal (Lean 4 + mathlib) — papers públicos

Cubre `papers/determinant_cubic_source` y `papers/weld_clifford`. El material de
`brainstorming/papers/draft_algebra_uoc` (no público) vive en un proyecto Lean
SEPARADO, `brainstorming/papers/formal_verification/` — separación física deliberada
(jul-31 2026, pedido de HM), porque `papers/` puede terminar reflejado en
`public_github/` y `brainstorming/` nunca debe filtrarse ahí. Cada proyecto tiene su
propia copia de mathlib (sin dependencia cruzada, para no arriesgar la separación).

Origen (jul-31 2026, pedido de HM): "¿tiene sentido usar Lean para probar nuestros
papers?" — sí, para el subconjunto de resultados puramente algebraicos/formales que ya
llevan etiqueta `[teorema]`/`[D]` (álgebra lineal, álgebra de Clifford de dimensión
finita), NO para resultados que dependen de interpretación física, verificación
numérica contra datos, o elecciones de modelado.

## Setup

- `elan` instalado en `~/.elan/bin` — NO está en el PATH por defecto:
  `export PATH="$HOME/.elan/bin:$PATH"`.
- `lake init gsf_lean math` (plantilla con mathlib) — paquete `GsfLean`, mathlib fijado
  a `v4.32.2` en `lakefile.toml`.
- `.lake/` (caché de mathlib, ~7.4GB) en `.gitignore`, no se versiona. Reproducir:
  `lake exe cache get` + `lake build`.

## Estado

- `GsfLean/NoHopf.lean` — **Lema 1 (sin Hopf)**, `determinant_cubic_source` §6: el
  Jacobiano `J=-G⁻¹H` de un flujo métrico-gradiente (`G≻0` simétrica, `H` simétrica)
  tiene espectro real. Enunciado formalizado y BIEN TIPADO (compila), prueba PENDIENTE
  (`sorry` explícito) — bloqueado por falta de raíz cuadrada de matriz en mathlib para
  el camino de prueba del paper (`J=G^{1/2}SG^{-1/2}`, `S` simétrica). Camino
  alternativo identificado, no intentado todavía: `G` induce un producto interno nuevo
  donde `G⁻¹H` es autoadjunto — mathlib sí tiene espectro real para operadores
  autoadjuntos en espacios de producto interno de dimensión finita.

## Candidatos no atacados todavía

- **Lema 2** (`weld_clifford`, A,I,R generan Cl(3,0)) — requiere la API de álgebras de
  Clifford de mathlib (`Mathlib.LinearAlgebra.CliffordAlgebra`), no explorada todavía.
- Lemas 1, 3, 4 de `weld_clifford` y Teoremas 1-2 de `determinant_cubic_source`:
  dependen de axiomas físicos (A1-A3) o de teoría de bifurcaciones/variedad central —
  mucho más pesados de formalizar, no priorizados.

## Convención de honestidad

Nunca dejar un `theorem ... := by sorry` sobre un enunciado que no es el real (p.ej.
`True`) -- eso simula una formalización que no existe. El enunciado debe ser el
resultado real del paper, bien tipado; el `sorry` marca solo la prueba pendiente.
