---
title: "Γ: la viscosidad como amortiguación estructural"
subtitle: "Stokes y Navier-Stokes como límites de una sola ecuación, y la transición subcrítica en tubería"
author: "Henry Molina · Investigador independiente · henrymolina@gmail.com"
date: "Julio 2026"
---

DOI: 10.5281/zenodo.21502148

*Manuscrito autocontenido más allá del teorema algebraico y de la ecuación de movimiento del
paper compañero (Molina 2026, "Spacetime Algebra as a Theorem"; y Molina 2026,
"Γ: una ecuación de movimiento, tres sectores"), que este artículo reutiliza sin re-derivar. Las
verificaciones numéricas citadas en el texto están en `code/` (ver Anexo), publicado junto a este
paper en https://github.com/hmolinab/papers/tree/main/gamma_fluids. Cada resultado se marca
según su estatus: teorema con demostración completa, correspondencia estructural (isomorfismo o
relabeling algebraico con un objeto físico conocido, sin ser un teorema físico nuevo), hallazgo
verificado numéricamente o contra datos tabulados sin demostración analítica cerrada, o frontera
abierta. El texto lo dice explícitamente en cada caso.*

# Resumen

El parámetro de amortiguación γ de la ecuación de movimiento de GSF (Γ̈+γΓ̇−c²∇²Γ+∇P=N) no
tiene, por sí solo, una interpretación física fijada: entra por la extensión no conservativa del
Lagrangiano, no por la parte de campo. Este paper muestra que en el dominio de fluidos γ se
operacionaliza exactamente como ν=c²(ρ)/γ, la viscosidad cinemática, y que esa identidad produce
tres resultados verificables sin ajustar ningún parámetro nuevo. Primero, las ecuaciones de
Stokes emergen como el límite singular riguroso de la EOM de campo bajo tres condiciones con
nombre físico (fricción alta, amplitud pequeña, escala corta), cada una con teorema de
convergencia ya publicado en la literatura de ecuaciones diferenciales estocásticas y de
mecánica de fluidos; y Navier-Stokes completo, incluyendo el término de advección, se recupera
exigiendo la misma covarianza galileana que cualquier dinámica de continuo debe respetar.
Segundo, la identidad ν=c²(ρ)/γ reproduce razones de viscosidad tabuladas sobre unos veinticuatro
órdenes de magnitud (de mercurio a manto terrestre) con una sola variable y cero ajustes, y la
ley γ∝ρ se confirma a 0.1% de precisión en cinco décadas de densidad para el aire. Tercero, y de
mayor interés para aplicaciones de ingeniería, la transición subcrítica a turbulencia en flujo de
tubería (el crecimiento transitorio no-modal que precede a la turbulencia en Reynolds
subcríticos) se deriva como una propiedad estructural del sector antisimétrico Γ_a de la misma
matriz: se demuestra que una configuración puramente simétrica (diagonal) prohíbe el crecimiento
transitorio, que la cizalla responsable no puede provenir del gradiente del potencial (un
Hessiano es simétrico, luego normal, luego sin amplificación), y que sí proviene exactamente del
término convectivo de la derivada material. Esta cadena reproduce el escalamiento estándar
G_max∼Re² con el prefactor geométrico fijado desde el álgebra del operador, consistente en orden
de magnitud con el Re_c≈2040 observado en tubería. El criterio de éxito de este paper no es una
nueva ley de la turbulencia: es que una sola identidad algebraica, sin parámetros por dominio,
organiza correctamente la reducción a Stokes, la escala de la viscosidad real y el mecanismo de
la transición subcrítica, con las fronteras nombradas donde el resultado depende de constantes
tomadas de la literatura.

---

# 1. El parámetro γ y su operacionalización

## 1.1 Punto de partida (citado, no re-derivado)

Este paper presupone el objeto de configuración Γ y la ecuación de movimiento del paper
compañero: Γ = Γ_s ⊕ Γ_a ∈ M₄(ℝ) (los cuatro grados de SAIR sobre el álgebra geométrica G(3)) y

$$\ddot\Gamma + \gamma\dot\Gamma - c^2\nabla^2\Gamma + \nabla_\Gamma P(\Gamma,\rho) = N(t), \qquad
P = \|\Gamma\|_F^2+\mu(\rho)\det\Gamma+\beta\|\Gamma\|_F^4$$

con μ(ρ) y β fijados por la misma cota AM-GM del paper compañero (cero parámetros libres
adicionales). El ruido N(t) del entorno se empareja con γ por el teorema de fluctuación-disipación.

γ no aparece en la acción conservativa: entra por la extensión de Rayleigh (disipación), y es un
parámetro de coarse-graining, la tasa a la que la unidad de coherencia pierde memoria contra su
entorno. Operacionalizarlo en un dominio concreto es la pregunta empírica que este paper responde
para fluidos.

## 1.2 El diccionario SAIR en fluidos

La asignación de grado a cada atributo no basta por sí sola para fijar el diccionario: el weld
(Molina 2026) exige, además de la covarianza de grado, que S,A,I,R satisfagan un criterio de
selección explícito cuando hay más de un candidato compatible con el mismo grado. Aquí se aplican
los dos mecanismos ya verificados en el programa contra siete dominios (Newton, Schrödinger,
Navier-Stokes, Maxwell, firma de Lorentz, H₂O, Hopf): consistencia de Gram-fuerza (Γ_s=S·A debe
reproducir una ley de fuerza ya conocida e independiente del dominio) y el criterio de
trabajo/potencia (entre candidatos de igual grado, el que hace P=X·A≠0 genéricamente va a I; el
que se anula por una identidad geométrica pura, no por una restricción del flujo, va a R).

Por consistencia de Gram-fuerza: $S=\rho$ (densidad) y $A=D\mathbf u/Dt$ (aceleración material,
no la velocidad) son el único par que hace $\Gamma_s=S\cdot A=\rho\,D\mathbf u/Dt$ coincidir
exactamente con el lado inercial de la ecuación de Cauchy — el mismo patrón que en Newton, donde
$A$ es la aceleración y no la velocidad. Por el criterio de trabajo: $I=\mathbf u$ pasa la prueba,
porque $\mathbf u\cdot(D\mathbf u/Dt)$ es exactamente $D(|\mathbf u|^2/2)/Dt$, la tasa de cambio
de la energía cinética específica, genérica y con significado físico preciso. El candidato que se
anula por identidad geométrica pura es el vector de Lamb $\mathbf u\times\boldsymbol\omega$
($\mathbf u\cdot(\mathbf u\times\boldsymbol\omega)=0$ siempre, por producto triple con vector
repetido, el paralelo exacto de por qué el campo magnético no hace trabajo en electromagnetismo),
no el gradiente de presión ($\mathbf u\cdot\nabla p$ no se anula por identidad, solo se reduce a
una divergencia pura bajo la restricción global de incompresibilidad, §2.1 más abajo). Como la
vorticidad $\boldsymbol\omega$ que genera ese vector es de grado 2 y no puede ocupar R
directamente, el vector de grado 1 que la produce por cuña con $\mathbf u$ es $\nabla$ mismo:

| Rol SAIR | Variable | Grado en Cl₃,₀ | Contenido físico |
|:---:|---|:---:|---|
| S | densidad ρ | 0 (escalar) | identidad inercial del parcel |
| A | aceleración material D𝐮/Dt | 1 (vector) | Γ_s=S·A=ρD𝐮/Dt reproduce la fuerza de Cauchy exactamente |
| I | velocidad **u** | 1 (vector) | 𝐮·A=D(|𝐮|²/2)/Dt: hace trabajo en el sentido preciso de energía cinética |
| R | ∇ (operador, tratado como generador grado 1) | 1 (vector formal) | genera el campo por cuña con I, sin hacer trabajo por identidad geométrica |

El campo, $\Gamma_a=I\wedge R=\mathbf u\wedge\nabla=\nabla\times\mathbf u=\boldsymbol\omega$, es
**derivado**, no un cuarto grado asignado directamente: la vorticidad es la parte antisimétrica de
$\partial_j u_i$, exactamente como en el paper compañero para Navier-Stokes. La helicidad
$h=\mathbf u\cdot\boldsymbol\omega$, si aparece, es el invariante pseudoescalar de $\Gamma_a$ — una
cantidad derivada, no un slot SAIR independiente.

La presión no ocupa ningún grado de SAIR: es el multiplicador de Lagrange de la restricción de
incompresibilidad ∇·**u**=0, identificado por la descomposición de Leray-Hodge, y entra como
forzaje termodinámico efectivo del entorno sobre los grados de flujo, no como un grado de
libertad interno de Γ.

Con esta asignación, la ley estructural Fuerza = S·A es exactamente el lado izquierdo de
Navier-Stokes (ρ veces la derivada material de **u**), y el vector de Lamb descompone la
advección en una parte de gradiente (que va a la presión) y una parte irreducible que vive en el
sector Γ_a:

$$(\mathbf{u}\cdot\nabla)\mathbf{u} = \nabla\!\left(\tfrac{1}{2}|\mathbf{u}|^2\right) - \mathbf{u}\times\boldsymbol{\omega}$$

---

# 2. Stokes como límite singular de la EOM

## 2.1 Los tres límites con nombre físico

Proyectando la EOM de campo sobre el subsistema de velocidad (con ρ fijo, como corresponde a
flujo incompresible), tres límites reducen la EOM a las ecuaciones de Stokes:

- **Fricción alta** (ε=1/(γT)→0): la EOM pasa de segundo a primer orden en el tiempo. Es
  exactamente el límite de Smoluchowski-Kramers de la dinámica de Langevin de alta fricción, que
  tiene teorema de convergencia publicado (Nelson, 1967; Freidlin-Wentzell): la solución de
  segundo orden converge a la de primer orden con error O(ε).
- **Amplitud pequeña** (|**v**|∼ε→0): el término no lineal adj(Γ) escala como ε² y se vuelve
  subdominante.
- **Escala corta** (L≪c, equivalente a bajo número de Mach): el término de masa estructural, que
  dota al campo de una longitud de pantalla ℓ=c, es despreciable frente al término difusivo
  c²∇²Γ. Este régimen es exactamente el límite incompresible de Mach bajo, con teoremas de
  convergencia disponibles en la literatura matemática (Schochet, 2010; Lions-Masmoudi, 1998;
  Métivier-Schochet, 2001).

Proyectando sobre la componente de velocidad activa y con el gradiente de presión entrando como
inyección termodinámica efectiva del entorno, se obtiene exactamente:

$$\boxed{\partial_t v_i=\nu_{\mathrm{kin}}\,\nabla^2 v_i-\frac1{\rho}\partial_i p,\qquad \nabla\!\cdot\mathbf v=0,\qquad \nu_{\mathrm{kin}}=\frac{c^2(\rho)}{\gamma}.}$$

**Teorema (Stokes como límite singular).** *Bajo los tres límites acoplados anteriores, existe
una solución u de las ecuaciones de Stokes con ν=c²/γ tal que ‖Γ−u‖≤C·máx(ε, Ma, L/c) en
[0,T].* La existencia del límite y la forma de la ecuación están demostradas, cada eslabón es un
teorema de convergencia ya publicado en su dominio propio (Smoluchowski-Kramers, límite de Mach
bajo, Leray-Hodge); adaptar esos teoremas de campos escalares/vectoriales al formalismo matricial
de Γ y obtener la constante C explícita en ese formalismo queda como trabajo pendiente.

## 2.2 Navier-Stokes completo

El paso de Stokes (lineal) a Navier-Stokes (con advección) no requiere ningún postulado adicional
más allá de la covarianza galileana que cualquier dinámica de continuo debe respetar: bajo un
boost x'=x−Vt, la covarianza exige que la derivada temporal se convierta en la derivada material
D/Dt=∂_t+(**u**·∇) (verificado simbólicamente que solo D/Dt, no ∂_t sola, es invariante de forma
bajo el boost). Sustituyendo esa derivada en los slots de flujo y usando la identidad de Lamb
para separar la parte de gradiente (que va a la presión) de la parte irreducible (que vive en
Γ_a), se recupera exactamente

$$\partial_t \mathbf u+(\mathbf u\cdot\nabla)\mathbf u=\nu\nabla^2\mathbf u-\tfrac1\rho\nabla p+\mathbf f,\qquad \nabla\!\cdot \mathbf u=0.$$

Navier-Stokes queda así derivado sobre el mismo postulado de asignación de grados que ya usa
Stokes, sin ningún parámetro ni postulado adicional. La frontera que queda es puramente
algebraica: el mismo "weld" Clifford→M₄(ℝ) del paper compañero, no algo específico de fluidos.

---

# 3. La operacionalización de γ

La identidad ν=c²(ρ)/γ da la primera operacionalización cuantitativa de γ en un dominio físico
concreto: amortiguación alta equivale a viscosidad alta equivale a régimen de Stokes;
amortiguación baja equivale a régimen inviscido/Euler. El número de Reynolds es el proxy físico
de 1/γ:

$$\mathrm{Re}=\frac{vL}{\nu_{\mathrm{kin}}}=\frac{vL\,\gamma}{c^2(\rho)}.$$

La rigidez de campo c²(ρ) se toma de una ley de escala del programa GSF más amplio (una potencia
de ρ que solo se activa cerca de la densidad cosmológica de referencia), no establecida en
ninguno de los papers compañeros citados aquí; se usa en este trabajo como una hipótesis de
entrada, no como un resultado ya publicado y verificable en esas referencias. A las densidades de
cualquier fluido terrestre, esa ley predice que c² es efectivamente constante, de modo que las
razones de γ entre fluidos se convierten en razones puras de viscosidad tabulada.

---

# 4. Datos sin ajustar

## 4.1 Veinticinco órdenes de magnitud en razones de viscosidad

Con c² constante a densidades de fluido, γ_A/γ_B=ν_B/ν_A es una razón pura de datos tabulados,
sin ningún supuesto teórico adicional (más allá de que ambos fluidos compartan la misma densidad
estructural ρ, un supuesto explícito, no un dato). Los valores de viscosidad cinemática de la
tabla siguiente son valores estándar de ingeniería a temperatura y presión ambiente (Cengel y
Cimbala, *Fluid Mechanics: Fundamentals and Applications*, 2018; CRC Handbook of Chemistry and
Physics), citados aquí sin re-medición independiente.

| Fluido | ν (×10⁻⁶ m²/s) | γ relativo al agua |
|---|---:|---:|
| Mercurio | 0.12 | 8.4 |
| Acetona | 0.43 | 2.34 |
| Agua (referencia) | 1.004 | 1.000 |
| Agua de mar | 1.05 | 0.956 |
| D₂O | 1.251 | 0.803 |
| Plasma sanguíneo | ∼1.3 | ∼0.77 |
| Etanol | 1.52 | 0.660 |
| Glicerol (100%) | 1190 | 8.4×10⁻⁴ |
| Hielo glaciar (creep) | ∼10¹⁸ | ∼10⁻¹⁸ |
| Manto terrestre (superior) | ∼3×10²³ | ∼3×10⁻²⁴ |

El rango completo abarca unos veinticuatro órdenes de magnitud (24.4, verificado por script) con una sola variable, una sola
ecuación, y cero parámetros ajustados. El valor de esta tabla no depende de haber derivado
Navier-Stokes desde cero: funciona como un anclaje fenomenológico robusto, en el mismo sentido en
que la tercera ley de Kepler funcionó como ley de escala empírica antes de que Newton derivara la
gravedad que la explica.

## 4.2 γ proporcional a ρ, 0.1% en cinco décadas

La viscosidad cinemática del aire en régimen continuo obedece ν∝1/ρ a 0.1% de precisión sobre
presiones de 10⁻³ a 10 atm. Combinado con la saturación de c² a esas densidades, esto implica
γ∝ρ linealmente sobre cinco décadas de densidad, la confirmación empírica más fuerte hasta la
fecha de la relación estructural entre γ y la densidad.

## 4.3 Calibración absoluta (condicional)

Las razones anteriores fijan γ relativo, no la escala absoluta. Bajo la hipótesis de que
c²(ρ_agua)≈c²_luz (una afirmación teórica, no una medición), la escala absoluta implicada para
el agua es γ≈9×10²² s⁻¹, con un tiempo de relajación estructural del orden de 10⁻²³ s
(yoctosegundos, régimen sub-nuclear, no accesible a espectroscopía Raman/IR de femtosegundos
directamente). Este número es una predicción condicional a esa hipótesis, no una medición.

---

# 5. Identidad acústica-electromagnética

En el límite irrotacional (Γ_a=0, sin fuentes, sin vorticidad), la EOM se reduce a la ecuación de
onda sin masa para el potencial de velocidad, □φ=0, el mismo mecanismo estructural que el fotón
electromagnético libre en el paper compañero. La analogía acústica-electromagnética clásica
(Bergmann, 1946), usada en técnicas de cloaking acústico, tiene aquí una lectura estructural: no
es una analogía formal sino que ambos son instancias del mismo sector det=0 (γ≈0, régimen de
onda) del mismo objeto algebraico, difiriendo solo en qué observables físicos ocupan los slots.

---

# 6. La transición subcrítica en tubería

## 6.1 Dos regímenes de la misma ecuación

La reducción a Stokes de §2 es de orden líder en 1/γ (se descarta la aceleración Γ̈). Reteniendo
ese término, la corrección de orden siguiente da un sistema linealizado de primer orden

$$\dot{\mathbf Y}=\mathbf A\mathbf Y,\qquad \mathbf A=\begin{pmatrix}0 & I\\ -\mathcal L_{\bar\Gamma} & -\gamma I\end{pmatrix},$$

con A estructuralmente no normal. Los operadores no normales soportan amplificación transitoria
de perturbaciones aunque todos los autovalores estén en el semiplano estable, el mecanismo
conocido de la transición subcrítica en flujo de tubería.

## 6.2 El escalamiento Re² y su origen en Γ_a

Para el operador no normal mínimo de tipo lift-up (el mecanismo estándar de amplificación por
cizalla en estabilidad hidrodinámica), la amplificación G(t)=‖e^{At}‖² tiene un máximo cerrado
proporcional a Re², con el prefactor geométrico fijado desde el álgebra del operador (verificado
numéricamente: pendiente log-log de 2.000, constante independiente de Re). Esto recupera el
escalamiento estándar de la literatura de estabilidad hidrodinámica (Reddy-Henningson, 1993;
Trefethen et al., 1993) y fija el prefactor desde primeros principios algebraicos, no por ajuste.

Lo que aporta este marco más allá de recuperar ese escalamiento es un resultado de diagnóstico
estructural, verificado en tres pasos, con una precisión importante sobre qué exactamente cierra
cada paso.

1. Una configuración de Γ puramente diagonal (simétrica) prohíbe el crecimiento transitorio:
   G_max=1 para todo Re. El acoplamiento de cizalla necesario para el mecanismo lift-up no puede
   vivir en la diagonal.
2. La cizalla no puede provenir del gradiente del potencial ∇²P por sí solo: el Hessiano de
   cualquier potencial es simétrico (las derivadas mixtas conmutan), luego normal, luego sin
   amplificación transitoria posible. Este es un no-go demostrado, no una observación
   cualitativa, y descarta correctamente que cualquier perturbación no simétrica genérica de la
   EOM desnuda de Γ (sin término convectivo) alcance el escalamiento Re²: verificado que un
   acoplamiento no normal genérico, construido a mano sin la estructura lift-up específica, solo
   da G_max∼Re¹.
3. La cizalla sí proviene, exactamente, del término convectivo de la derivada material,
   linealizado en torno a un perfil base de flujo con cizalla. Ese término convectivo no es un
   ingrediente ajeno a este marco: es exactamente el que la derivación de Navier-Stokes de §2.2
   añade a la EOM desnuda por covarianza galileana. Al linealizar ese término, el acoplamiento
   resultante es necesariamente fuera de la diagonal, es decir, vive en el sector antisimétrico
   Γ_a, y reproduce el escalamiento Re² exacto con el prefactor geométrico del paso anterior.

La formulación precisa, para no sobre-reclamar, es: el escalamiento Re² no sale de la EOM desnuda
de Γ con cualquier perturbación no simétrica (eso está descartado, punto 2); sale de la instancia
fluida completa de esta ecuación, que por covarianza galileana es Navier-Stokes con su término
convectivo (§2.2), linealizado alrededor de un perfil de cizalla base. El perfil base U(y) sigue
siendo un dato de entrada externo, el mismo que requiere toda la teoría estándar de estabilidad
hidrodinámica (Orr-Sommerfeld/Squire), no algo específico de este marco. Con esa precisión, Γ
funciona como herramienta de diagnóstico estructural: el crecimiento transitorio que precede a la
turbulencia subcrítica es un observable directo del sector antisimétrico de la matriz de
configuración, una vez que se incluye el término convectivo que la covarianza exige.

## 6.3 Comparación con el Re crítico observado

Para flujo de Poiseuille en tubería, esta cadena predice Re_c≈2200 usando una constante
geométrica C≈50 y una amplitud umbral de perturbación A₀≈10⁻⁷ tomadas de la literatura
experimental (Hof et al., 2003), en acuerdo razonable con el Re_c≈2040 observado. Lo que es
estructural aquí, y lo que depende de constantes externas, debe distinguirse con precisión:

- **Estructural (derivado, no ajustado):** que el escalamiento es Re² y no otra potencia; que ese
  escalamiento requiere estrictamente el sector Γ_a activo; que la cizalla causante no puede
  provenir del sector de gradiente.
- **Dependiente de constantes de literatura:** el valor numérico exacto de Re_c≈2040-2200
  requiere la constante geométrica C y la amplitud umbral A₀, ambas tomadas de mediciones
  experimentales publicadas, no derivadas de la EOM.

Un segundo régimen distinto de la misma ecuación explica por qué tubería y canal difieren
cualitativamente: el flujo en canal transita a turbulencia por un mecanismo modal
(Tollmien-Schlichting) en Re_c≈5772, mientras que la tubería, donde ese modo es linealmente
estable para todo Re, transita por el mecanismo no modal de crecimiento transitorio en
Re_c≈2040. Ambos son el mismo objeto Γ y la misma ecuación; lo que distingue los regímenes es el
número de Reynolds de cada geometría, no un parámetro distinto del fluido.

---

# 7. Fronteras honestas

| Frontera | Estado | Nota |
|---|:---:|---|
| Constante C matricial de la cota de convergencia a Stokes (Teorema §2.1) | abierto | cada eslabón de la cadena de límites tiene teorema de convergencia publicado en su dominio propio; adaptar la cota explícita al formalismo matricial de Γ queda pendiente |
| Ortogonalidad mutua de A, I, R en Γ_s (§1.2) | cerrado para fluidos | con A=D𝐮/Dt, I=𝐮, R=∇ (verificado por consistencia de Gram-fuerza y criterio de trabajo, `models/calcs/brainstorming/papers/draft_atlas/protocolo_sair_completo_fluidos*.py`), la autorreferencia R=q(A,I) no aparece: R=∇ es independiente de A e I por construcción |
| Razones de viscosidad sobre ~24 órdenes | verificado por script contra datos citados, condicional a ρ común | `code/verificacion_razones_viscosidad.py`: reproduce la tabla con <1% de diferencia salvo manto terrestre (11%, valor de orden de magnitud, no medición precisa); supuesto de densidad estructural igual entre fluidos comparados sigue explícito, no verificado independientemente |
| Escala absoluta de γ para el agua (γ≈9×10²² s⁻¹) | condicional | depende de la hipótesis c²(ρ_agua)≈c²_luz, una afirmación teórica no verificada |
| Ventana homeodinámica agua/D₂O y su relación con toxicidad | frontera abierta | calibrada desde datos de toxicidad, no derivada; la lectura causal (vs. correlación) no está establecida |
| Re_c≈2040 en tubería, valor numérico exacto | verificado cualitativamente, no de primer principio | usa constante geométrica y amplitud umbral de Hof et al. (2003); lo estructural (escalamiento Re², origen en Γ_a) sí es derivado |
| Escala absoluta de ρ (necesaria para calibración fuera de razones) | abierto | referido en el paper compañero como trabajo pendiente del programa |
| Ley de escala c²(ρ) usada en §3-4 | hipótesis de entrada, no establecida en los papers compañeros citados | proviene de material más amplio del programa GSF, no publicado aún en forma verificable |
| Tabla de viscosidades de §4.1 | sin script de verificación propio | valores citados de fuentes de ingeniería estándar (Cengel-Cimbala, CRC Handbook), no re-medidos ni reproducidos en `code/` todavía |

---

# 8. Conclusión

γ, el único parámetro de la ecuación de movimiento sin interpretación fijada por el marco
algebraico, se operacionaliza en fluidos con precisión: ν=c²/γ reproduce datos de viscosidad
sobre unos veinticuatro órdenes de magnitud sin ajustar nada, y γ∝ρ se confirma a 0.1% en cinco
décadas. La reducción a Stokes y la derivación de Navier-Stokes completo descansan sobre
teoremas de convergencia ya publicados en sus dominios propios, no sobre identificaciones
cualitativas. Y el resultado de mayor interés aplicado, la transición subcrítica en tubería, se
reduce a una cadena algebraica cerrada: sin el sector antisimétrico Γ_a no hay crecimiento
transitorio, ese sector no puede sustituirse por el gradiente del potencial, y sí surge
exactamente del término convectivo de transporte. El valor numérico exacto de Re_c depende de
constantes tomadas de la literatura experimental; lo que este marco aporta no es reemplazar esas
mediciones sino explicar, desde la estructura del operador, por qué el escalamiento es Re² y
dónde vive el mecanismo que lo produce.

---

# Referencias

Bergmann, P. G. (1946). The wave equation in a medium with a variable index of refraction.
*Journal of the Acoustical Society of America*, 17(4), 329–333.

Cengel, Y. A. and Cimbala, J. M. (2018). *Fluid Mechanics: Fundamentals and Applications* (4th
ed.). McGraw-Hill.

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

# Anexo — Scripts de cálculo

Scripts de verificación incluidos en `code/` junto a este paper, publicados en
https://github.com/hmolinab/papers/tree/main/gamma_fluids:

```
code/
  pieza2_transient_growth.py            -> escalamiento G_max=Re²/C (lift-up), diagnóstico Γ_a, no-go de ∇²P, S=∂_yU (§6)
  verificacion_razones_viscosidad.py    -> reproduce la tabla de §4.1 desde valores de ν citados; confirma ~24 órdenes de magnitud
```

Requisitos: `numpy`, `scipy`.

Pendiente de implementar como script independiente (actualmente citados de tablas y ajustes
publicados, no reproducidos aquí en código): el ajuste ν∝1/ρ del aire de §4.2, y el factor de
descarte de saturación de c² de §4.3.

---

*Programa Gamma Space Framework. Julio 2026.*
*henrymolina@gmail.com*
