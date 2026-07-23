# Paper: Γ — la viscosidad como amortiguación estructural

DOI: [10.5281/zenodo.21502148](https://doi.org/10.5281/zenodo.21502148)

**"Γ: la viscosidad como amortiguación estructural — Stokes y Navier-Stokes como límites de una
sola ecuación, y la transición subcrítica en tubería"**
Henry Molina — Investigador independiente, Bogotá, Colombia

## Archivos

| Archivo | Descripción |
|---|---|
| `gamma_viscosidad_amortiguacion_estructural_molina2026.md` | Paper principal (español) |
| `gamma_viscosity_structural_damping_molina2026.md` | Paper principal (inglés) |
| `code/` | scripts de verificación numérica citados en el paper (§4, §6) |

## Ejecutar la verificación

```bash
cd code
python pieza2_transient_growth.py            # escalamiento G_max=Re²/C, diagnóstico Γ_a (§6)
python verificacion_razones_viscosidad.py    # tabla de razones de viscosidad, ~24 órdenes (§4.1)
```

Requisitos: `numpy`, `scipy`.

## De interés para ingeniería de tuberías

§6 (transición subcrítica): cadena algebraica cerrada que muestra que el crecimiento transitorio
no-modal que precede a la turbulencia en flujo de tubería requiere estrictamente el sector
antisimétrico Γ_a, no puede provenir del gradiente del potencial (no-go demostrado), y sí
proviene del término convectivo de transporte. Reproduce G_max∼Re² con prefactor geométrico
derivado, consistente en orden de magnitud con Re_c≈2040 observado (constantes de Hof et al. 2003
para el valor numérico exacto; ver §7, tabla de fronteras honestas).

## Papers compañeros

- Molina, H. (2026). Spacetime algebra as a theorem: deriving Cl(3,1) from the structure of a
  dynamical unit. DOI: 10.5281/zenodo.21184515
- Molina, H. (2026). Γ: one equation of motion, three sectors. DOI: 10.5281/zenodo.21496578

Este paper reutiliza el objeto Γ, el álgebra SAIR y la ecuación de movimiento de ambos, sin
re-derivarlos.

## Fuente de trabajo

Cuaderno de proceso (fuera de este paquete público):
`brainstorming/unification/release/pieza2_gamma_fluidos.md` y
`brainstorming/papers/gamma_fluids/cuaderno_trabajo.md` (exploración de la asignación SAIR en
fluidos, sin cerrar — no afecta las claims publicadas aquí, ver el propio cuaderno §7.6/7.9 para
el porqué).

## Zenodo/arXiv

Paquete de envío (metadata, abstract, descripción en español) en
`brainstorming/papers/gamma_fluids/arxiv_zenodo_es.md`.

## Pendiente

- Dos verificaciones citadas de tablas/ajustes publicados (ν∝1/ρ del aire, factor de saturación
  de c²) todavía no tienen script propio; ver Anexo del paper. La tercera (razones de viscosidad,
  §4.1) ya se cerró con `code/verificacion_razones_viscosidad.py`.
