# Paper: Γ — una ecuación de movimiento, tres sectores

**"Γ: una ecuación de movimiento, tres sectores — Correspondencias estructurales con la mecánica
clásica, los fluidos, el electromagnetismo y la mecánica cuántica"**
Henry Molina — Investigador independiente, Bogotá, Colombia

## Archivos

| Archivo | Descripción |
|---|---|
| `gamma_una_ecuacion_tres_sectores_molina2026.md` | Paper principal (español) |
| `gamma_one_equation_three_sectors_molina2026.md` | Paper principal (inglés) |
| `code/` | 17 scripts de verificación numérica citados a lo largo del paper (ver Anexo B) |

## Ejecutar las verificaciones

```bash
cd code
python calc1_newton_limit.py
python completitud_sectores_sylvester_hadamard_prueba.py
python atlas_sectores_desde_sair_prueba.py
# ... (ver Anexo B del paper para la lista completa y a qué sección corresponde cada script)
```

Requisitos: `numpy`, `sympy`. No hace falta scipy.

## Paper compañero

Molina, H. (2026). Spacetime algebra as a theorem: deriving Cl(3,1) from the structure of a
dynamical unit. DOI: 10.5281/zenodo.21184515 — este paper reutiliza ese teorema (§1) sin
re-derivarlo.

## Notas de trabajo

Cuaderno de proceso y guía de estudio (fuera de este paquete público):
`brainstorming/papers/draft_atlas/cuaderno_trabajo.md`,
`brainstorming/papers/draft_atlas/guia_estudio_cuaderno_limpio.md`.

## Pendiente antes de someter a arXiv/Zenodo

- Los marcadores de registro internos (〔TEO〕[D], 〔CE〕, 〔IF〕, 〔A〕, 〔F〕) siguen en el cuerpo del
  paper — ahora con una leyenda de notación al inicio del documento que los explica, pero el weld
  los tradujo enteramente a prosa antes de publicar. Considerar la misma traducción aquí para el
  envío final a arXiv/Zenodo; la leyenda es un mínimo viable, no el estándar del programa.
- No tiene DOI propio todavía (el weld sí, `10.5281/zenodo.21184515`, ya reservado).
