# El álgebra de espacio-tiempo como teorema: derivación de Cl(3,1) a partir de la estructura de una unidad dinámica

Henry Molina  
Investigador independiente
henrymolina@gmail.com  
DOI: 10.5281/zenodo.21184515

Manuscrito autocontenido; no requiere ningún marco externo más allá del álgebra lineal estándar y las
convenciones del álgebra de Clifford. Las verificaciones numéricas referenciadas en §7 están en:  
https://github.com/hmolinab/papers/tree/main/weld_clifford/code

---

## Resumen

Derivamos el álgebra de Clifford real $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ a partir de cuatro axiomas
estructurales sobre cualquier unidad dinámica operativa (UDO) — el cuarto hace explícita una premisa de
co-localización usada implícitamente en un borrador anterior. A1 (SAIR): la unidad queda descrita por
cuatro atributos intrínsecos — un escalar $S$ y tres vectores $\mathbf{A}, \mathbf{I}, \mathbf{R}$ en
$\mathbb{R}^d$. A2 (producto geométrico): la estructura está gobernada por el producto geométrico de esos
atributos, cuya parte de grado 2, $\mathbf{I}\wedge\mathbf{R}$, es el bivector Campo. A3 (evolución
continua): la UDO evoluciona suavemente en tiempo y espacio a velocidad de propagación finita, con el
espacio de atributos y las coordenadas de propagación identificados (A3$'$, co-localización). A partir
de estos cuatro axiomas — sin postular una métrica de espacio-tiempo ni una geometría de fondo — derivamos:
(i) la condición de clausura $\binom{d}{2}=d$ fuerza $d=3$ de forma única (autodualidad de Hodge de los
bivectores en $\mathbb{R}^3$, confirmada por Hurwitz); (ii) la evolución suave (A3) requiere una cuarta
dirección temporal independiente de los atributos espaciales; (iii) el símbolo principal de la EDP
resultante de segundo orden es la forma de Minkowski $\eta=\mathrm{diag}(-1,+1,+1,+1)$, cuya álgebra de
Clifford real es $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$. Tres proposiciones de cierre establecen que la
ortonormalidad es una redundancia de gauge (P1), que $\gamma_0$ es el generador algebraico conjugado a
$\partial_\tau$ en la factorización de Dirac de $\Box$ (P2, sin confundir elementos algebraicos con
operadores diferenciales), y que la norma de Frobenius es el producto interno de Clifford único forzado
por A2 (P3). En el marco SAIR, Cl(3,1) es una consecuencia derivada más que un postulado geométrico.
La mecánica clásica y la electrodinámica libre aparecen como límites estructurales.

**Palabras clave:** álgebra de Clifford, álgebra geométrica, teorema de Hurwitz, firma del espacio-tiempo,
sistemas dinámicos, forma normal matricial, métrica de Frobenius.

---

## 1. Introducción

El álgebra de Clifford $\mathrm{Cl}_{3,1}$ — equivalentemente, el álgebra de espacio-tiempo (STA) de
Hestenes (1966) — es el andamiaje algebraico estándar para la relatividad especial y la teoría de Dirac.
Su motivación habitual es geométrica: se postula un espacio-tiempo de Minkowski con firma $(3,1)$ y
después se construye el álgebra de Clifford asociada. La pregunta que abordamos es distinta: *¿es la
firma Lorentziana un teorema, más que un postulado, si se pregunta qué estructura algebraica debe tener
una unidad dinámica que se autodescribe?*

Mostramos que la respuesta es afirmativa, bajo cuatro axiomas mínimos: A1 (estructura de atributos), A2
(producto geométrico), A3 (evolución suave a velocidad finita) y A3$'$ (co-localización del espacio de
atributos con las coordenadas de propagación). La derivación no requiere el
espacio-tiempo como entrada; la firma emerge del símbolo principal de la ecuación de movimiento dictada
por A3.

Este artículo forma parte de un programa más amplio — el Gamma Space Framework (GSF) — cuyo objeto
central es una matriz de configuración real $4\times4$, $\Gamma \in M_4(\mathbb{R})$. El presente
artículo establece la fundación algebraica: que $\Gamma$ es un elemento de $\mathrm{Cl}_{3,1}$, no por
postulado sino por necesidad. El artículo compañero (Molina 2024a) establece el resultado dinámico: que
el determinante de $\Gamma$ es la fuente del término cúbico en la reducción al modo blando del flujo
gradiente matricial.

*Nota terminológica.* A lo largo de este artículo se emplea el término **unidad dinámica operativa
(UDO)** como término técnico autocontenido que no requiere conocimiento previo del GSF. En la literatura
del GSF (Molina 2025), el mismo objeto se denomina **Unidad de Coherencia (UoC)**; ambos términos son
sinónimos.

**Relación con la literatura de álgebra geométrica.** El programa de álgebra de espacio-tiempo (Hestenes
1966, 1986; Doran y Lasenby 2003) es el antecedente más cercano. Ese programa toma el espacio-tiempo de
Minkowski como dado y desarrolla la física en términos de $\mathrm{Cl}_{1,3}$ (un tiempo, tres espacios
— convención de Hestenes). La elección de firma no es una mera convención:
$\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$ (cuaterniónica), mientras que
$\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ (real). Son álgebras reales no isomorfas. La presente
derivación fuerza $\mathrm{Cl}_{3,1}$ — no $\mathrm{Cl}_{1,3}$ — porque exigimos que $\Gamma$ sea una
matriz real (la disipación y los flujos gradiente son procesos reales); esto distingue las dos
convenciones al nivel algebraico. La derivación no compite con el programa de álgebra de espacio-tiempo;
identifica qué álgebra real es forzada por la estructura de cualquier unidad dinámica en evolución, y
provee una base estructural para ese programa.

**Plan.** §2 enuncia los cuatro axiomas. §3 deriva los cuatro lemas. §4 enuncia y prueba el teorema
principal. §5 establece las tres proposiciones de cierre. §6 ilustra con dos límites físicos (Newton y
Maxwell). §7 presenta la verificación numérica de los pasos clave. §8 discute alcance, trabajo
relacionado y problemas abiertos.

---

## 2. Axiomas

Consideramos una **unidad dinámica operativa** (UDO): una entidad que (i) existe como un todo coherente
distinto de su entorno, (ii) actúa sobre su entorno, (iii) tiene un impulso intrínseco y (iv) está
inmersa en un contexto relacional. No se asume ningún contenido fenomenológico adicional.

**Axioma A1 (estructura de atributos SAIR).** Cualquier UDO queda descrita completamente al nivel
estructural por cuatro atributos intrínsecos:
- $S \in \mathbb{R}$ (Singularidad, grado 0 — identidad / auto-medida)
- $\mathbf{A}, \mathbf{I}, \mathbf{R} \in \mathbb{R}^d$ (Agencia, Impulso, Relación — vectores de grado 1)

donde $d$ está por determinarse. Se reclama que el mapeo de las propiedades observables de cualquier
entidad coherente a los cuatro casilleros estructurales $\{S, \mathbf{A}, \mathbf{I}, \mathbf{R}\}$ es
estructuralmente único (no existen dos asignaciones inequivalentes que produzcan predicciones
estructuralmente idénticas para la misma entidad) — pero este artículo establece ese reclamo solo al
nivel del *contenedor*, no de las *instancias*, y las dos cosas no deben confundirse (ver la
calificación al final de la Observación 2.1).

*Observación 2.1.* A1 es el axioma fundacional del marco; no se deriva de premisas más simples dentro
de este artículo. Su justificación es el argumento estructural de que $\{S, \mathbf{A}, \mathbf{I},
\mathbf{R}\}$ son los grados de un álgebra geométrica de dimensión mínima compatible con A2 — una
circularidad resuelta por la consistencia mutua de A1 y A2, no por una prueba independiente de A1. El
papel de A1 en esta estructura es análogo al de la selección natural en la teoría darwiniana: un postulado
mínimo que genera el resto.

*Calificación (qué significa "estructuralmente único" aquí, y qué no).* La cláusula de unicidad de A1
se prueba en este artículo solo para el **contenedor**: dado que una UDO tiene un atributo de grado 0
y tres de grado 1, los Lemas 2–4 muestran que el álgebra que los aloja queda forzada a
$\mathrm{Cl}_{3,1}$, de forma única — un argumento de tipo Schur (compatibilidad de representación) que
es precisamente por qué los grados no pueden reordenarse una vez fijados. Este artículo **no** establece
la unicidad al nivel de **instancias**: dada una UDO específica (una partícula, una célula, un mercado),
qué cantidad observable ocupa $S$ frente a $\mathbf{A}$ frente a $\mathbf{I}$ frente a $\mathbf{R}$ es un
problema de asignación sobre el cual el teorema del contenedor guarda silencio. Una condición necesaria
para esa asignación (los candidatos deben compartir la representación del casillero bajo el grupo de
covarianza del dominio) es el mismo argumento de Schur especializado a instancias, y una línea de trabajo
compañera desarrolla criterios de selección suficientes y los prueba contra siete dominios trabajados —
pero ese trabajo está en una etapa de rigor más temprana que los lemas cerrados de este artículo y se
mantiene deliberadamente fuera de aquí (ver §8.3). La palabra "único" en A1 debe leerse como "único al
nivel del contenedor, probado; abierto al nivel de instancia" hasta que ese trabajo compañero madure.
Esto no es un retroceso respecto de A1 — es la misma disciplina que §8.3 aplica en otros lugares: decir
exactamente qué está probado, y no dejar que una palabra fuerte en un axioma implique más de lo que el
teorema entrega.

*Una segunda calificación, previa: existencia, no solo unicidad.* Todo lo anterior concierne a la
*unicidad* de la asignación de casilleros dado que ya existe una cuádrupla SAIR bien-puesta para un
dominio. Una pregunta distinta y más básica es la *existencia*: ¿un dominio dado admite siquiera
$\mathbf A,\mathbf I,\mathbf R$ como vectores de grado 1? **El teorema de este artículo es condicional a
una respuesta afirmativa, y no la provee él mismo.** Esto no es automático: un barrido sistemático de
cinética química y biológica (trabajo compañero, `brainstorming/physics/
veinte_dominios_quimica_biologia.md`) encontró que 13 de 20 dominios probados **no** tienen candidato
vectorial para $\mathbf A,\mathbf I,\mathbf R$ — las variables nativas son escalares (concentraciones,
tasas, números de ocupación) sin embebido natural en $\mathbb R^3$ o un subespacio de grado 1 de
Clifford. Para esos dominios, $\Gamma$ tal como se construye aquí simplemente no aparece; se usa en su
lugar un objeto distinto (una reducción espectral/de Schur de un Jacobiano, fuera del alcance de este
artículo). **Leído correctamente, el Teorema Principal (§4) dice: "si un dominio tiene $\mathbf A,\mathbf
I,\mathbf R$ de grado 1, entonces su álgebra anfitriona queda forzada a $\mathrm{Cl}_{3,1}$" — no "todo
dominio tiene tales atributos."** El teorema del contenedor está probado incondicionalmente como una
pieza de álgebra; su aplicabilidad a un dominio específico no lo está, y nunca debe leerse solo a partir
de este artículo.

Una UDO no es simplemente un sistema con cuatro casilleros etiquetables. Los atributos son intrínsecos
en el sentido operacional: son los generadores del producto geométrico de A2, no etiquetas observacionales
asignadas desde afuera. Un relé de umbral (p.ej., un termostato) tiene cuatro propiedades asignables pero
no satisface ni A2 (su dinámica es una regla de conmutación discontinua, no un producto geométrico) ni A3
(su evolución no es suave). La palabra «intrínseco» en A1 queda anclada por A2 y A3 en conjunto, no
declarada por decreto.

**Axioma A2 (dinámica por producto geométrico).** La dinámica de una UDO está gobernada por el
**producto geométrico** de sus atributos. En un álgebra geométrica $G(d)$ sobre $\mathbb{R}^d$, el
producto geométrico de dos elementos de grado 1, $u, v$, se descompone canónicamente:
$$uv = u \cdot v + u \wedge v$$
en una parte escalar simétrica (grado 0) y una parte bivector antisimétrica (grado 2). Aplicado a los
atributos: el sector **Fuerza** $\Gamma_s$ es el acoplamiento de Gram simétrico del escalar identidad $S$
con los atributos de grado 1 $\{\mathbf{A},\mathbf{I},\mathbf{R}\}$, codificando la estructura métrica
de la unidad. El **Campo** $\mathcal{F} = \mathbf{I} \wedge \mathbf{R} \in \Lambda^2(\mathbb{R}^d)$
(grado 2, antisimétrico) es el sector reactivo. «Fuerza» nombra el sector simétrico de $\Gamma$; $S$ es
de grado 0 y $S\mathbf{A}$ es un vector de grado 1, no un escalar — la estructura simétrica entra a
través de la matriz de Gram, no mediante un producto de grado 0. La separación Fuerza/Campo es forzada
algebraicamente por A2, no es un postulado independiente.

**Definición (embebido SAIR — la construcción de la matriz, nombrada, con el gauge cerrado).** La frase
«acoplamiento de Gram» de arriba nombra una operación sin escribirla; la escribimos una vez, de forma
explícita. Se embeben los atributos vectoriales como las columnas de
$W = [\,\mathbf{A}\mid\mathbf{I}\mid\mathbf{R}\,] \in \mathbb{R}^{4\times3}$ dentro del espacio ambiente
$4$-dimensional que porta una forma bilineal $q$, y se completa $W$ a una base con una dirección escalar
$\mathbf{e}_0$ para $S$: $V = [\,S\mathbf{e}_0\mid W\,]$.

$\mathbf{e}_0$ no es una elección libre. Siempre que la Gram $3\times3$ $W^{\mathsf T}qW$ es no
degenerada (la misma hipótesis de invertibilidad que ya exige el Corolario 4.2), el complemento
$q$-ortogonal de $\mathrm{span}\{\mathbf{A},\mathbf{I},\mathbf{R}\}$ es exactamente unidimensional — un
hecho estándar del álgebra bilineal: para $q$ no degenerada en el $4$-espacio completo,
$\dim W + \dim W^{\perp_q} = 4$, y $W\cap W^{\perp_q}=\{0\}$ precisamente porque $q|_W$ es no
degenerada. **Fijamos $\mathbf{e}_0$ como esta dirección única** (normalizada, con la ambigüedad de
signo residual del mismo tipo inocuo que el gauge de P1). Con esta elección, $\Gamma_s := V^{\mathsf T}qV$
es automáticamente bloque-diagonal:
$$\Gamma_s = \begin{pmatrix}S^2\,q(\mathbf{e}_0,\mathbf{e}_0) & 0\\ 0 & W^{\mathsf T}qW\end{pmatrix},$$
es decir, la **lectura de congruencia** colapsa, por construcción, en la **lectura por-casillero**
$\Gamma_s=\mathrm{diag}\big(q_S(S\mathbf{e}_0),q_A(\mathbf{A}),q_I(\mathbf{I}),q_R(\mathbf{R})\big)$
usada en el trabajo compañero de instanciación — las dos no son alternativas independientes licenciadas
por separado por A2; la lectura por-casillero *es* la lectura de congruencia evaluada en el único gauge
consistente con tratar a $S$ como grado 0 (sin acoplamiento cruzado a los casilleros vectoriales,
compatible con el hecho de incompatibilidad de grado: $S$ y un atributo de grado 1 no pueden emparejarse
bajo un producto que respeta grado). Cualquier otra elección de $\mathbf{e}_0$ da la misma firma por
Sylvester (el Corolario 4.2 de abajo no depende de qué $V$ invertible se use) pero puebla entradas
cruzadas espurias $S$–$\mathbf{A}$, $S$–$\mathbf{I}$, $S$–$\mathbf{R}$ sin contraparte en ningún lugar
donde realmente se usan — de modo que el $\mathbf{e}_0$ ortogonal no es solo *un* gauge válido, es el
canónico, señalado por consistencia con toda construcción explícita de este programa. Verificación
(existencia, unicidad y el colapso bloque-diagonal, 5 ensayos aleatorios):
`models/calcs/brainstorming/papers/weld_clifford/puente_simbolo_gram_sylvester_prueba.py`, parte IV.

**Axioma A3 (evolución continua).** La UDO evoluciona suavemente en tiempo $\tau$ y espacio $\mathbf{x}$,
con velocidad de propagación finita $c > 0$. Tratando $\Gamma(\tau,\mathbf{x})$ como un campo y
expandiendo a segundo orden en $\tau$ y $\mathbf{x}$, compatible con A1 y A2, la ecuación de movimiento
genérica es
$$\ddot\Gamma + \gamma\dot\Gamma - c^2\nabla_{\mathbf{x}}^2\Gamma + \nabla_\Gamma P(\Gamma) = N(\Gamma),$$
donde $\gamma\ge0$ es un parámetro constitutivo de amortiguamiento,
$\nabla_{\mathbf{x}}^2 = \partial_{x_1}^2 + \partial_{x_2}^2 + \partial_{x_3}^2$ es el laplaciano
espacial (propagación a velocidad $c$), y $\nabla_\Gamma P$ es el gradiente del potencial estructural
en el espacio de configuración. Esta es la ecuación de menor orden que acopla inercia ($\ddot\Gamma$),
propagación espacial ($-c^2\nabla_{\mathbf{x}}^2\Gamma$), disipación ($\gamma\dot\Gamma$) y fuerzas
restauradoras ($\nabla_\Gamma P$); no se hace ningún postulado adicional sobre la dinámica más allá de
la suavidad y la velocidad finita.

*Observación 2.2.* El contenido genuino de A2 es la afirmación de que *la estructura es el producto
geométrico*. A3 añade la afirmación de que *la evolución es suave y de segundo orden*: posición y
velocidad son grados de libertad independientes, por lo que una ecuación de primer orden los confundiría.
La separación simétrica/antisimétrica del producto geométrico es un teorema del álgebra geométrica, no
una hipótesis adicional.

*Observación 2.3 (la EOM no jubila a $\Gamma_s,\Gamma_a$).* La ecuación de A3 está escrita para el
$\Gamma$ sin dividir, y de aquí en adelante el artículo trabaja mayormente con $\Gamma$ como una sola
matriz — es fácil leer esto como que la separación Fuerza/Campo de A2 se usó una vez, en §2, y luego se
abandonó. No es así: cada término de la EOM actúa sobre ambos sectores simultáneamente, porque
$\ddot\Gamma=\ddot\Gamma_s+\ddot\Gamma_a$, $\nabla^2_{\mathbf x}\Gamma=\nabla^2_{\mathbf
x}\Gamma_s+\nabla^2_{\mathbf x}\Gamma_a$, y de igual modo para $\gamma\dot\Gamma$, por linealidad de
$\Gamma\mapsto\Gamma_s,\Gamma_a$. El único término que *no* es ciego al sector es el potencial:
$P(\Gamma)$, en el alcance de este artículo (§6, y la Definición 2.1 del trabajo compañero del atlas),
es un funcional de $\Gamma_s$ solamente — el sector Fuerza aporta la fuerza restauradora, y $\Gamma_a$
carece de fuente y de disipación a este orden, evolucionando solo por inercia y propagación. Así que la
descomposición no se pierde; reaparece como una afirmación sobre qué términos de la EOM siente cada
sector. Esto se usa más abajo sin comentario adicional (§6.1–6.2 recuperan Newton y Maxwell como,
respectivamente, los límites solo-$\Gamma_s$ y solo-$\Gamma_a$ de la misma ecuación) y se hace
completamente explícito, con la consecuencia espectral en $\det\Gamma_s=0$, en el trabajo compañero del
atlas.

---

## 3. Cuatro Lemas

### Lema 1 (Clausura — la dimensión queda forzada a $d=3$)

**Lema 1.** *Bajo A1 y A2, la dimensión del espacio de atributos vectoriales es $d = 3$.*

*Prueba (argumento de clausura).* A2 establece que el Campo es la parte de grado 2 del producto
geométrico: $\mathcal{F} = \mathbf{I} \wedge \mathbf{R} \in \Lambda^2(\mathbb{R}^d)$, un bivector de
dimensión $\binom{d}{2} = \tfrac{d(d-1)}{2}$. Para que la UDO sea cerrada — para que $\mathcal{F}$
pueda acoplarse de vuelta al atributo de grado 1 $\mathbf{A}$ sin introducir objetos de rango mayor que
los de A1 — el espacio del Campo y el espacio de atributos deben ser isomorfos como espacios vectoriales:
$$\binom{d}{2} = d \;\Longrightarrow\; \tfrac{d(d-1)}{2} = d \;\Longrightarrow\; d = 3.$$
La única solución no trivial es $d = 3$. Este isomorfismo es la dualidad de Hodge
$\star: \Lambda^2(\mathbb{R}^3) \xrightarrow{\;\sim\;} \mathbb{R}^3$, que mapea
$\mathcal{F} = \mathbf{I} \wedge \mathbf{R}$ al familiar producto vectorial
$\mathbf{I} \times \mathbf{R} \in \mathbb{R}^3$.

*Confirmación por Hurwitz.* Una vez establecido $d=3$ por clausura, el teorema de Eckmann (Eckmann 1943;
Adams 1960) confirma que existe un producto vectorial no degenerado en $\mathbb{R}^3$ — es la parte
imaginaria del producto cuaterniónico ($\mathbb{H}$, dimensión $d+1=4$). Esto es una comprobación de
consistencia, no la fuente de la derivación: Hurwitz verifica que $d=3$ funciona, pero la clausura es lo
que lo fuerza.

*La rama octoniónica ($d=7$) es estructuralmente distinta.* Existe un producto vectorial en
$\mathbb{R}^7$ (Eckmann 1943) como parte imaginaria del producto octoniónico, pero no surge de la
condición de clausura $\binom{d}{2}=d$ (ya que $\binom{7}{2}=21\neq7$). No es el dual de Hodge de un
bivector; es una estructura algebraica genuinamente diferente. Esta rama no se desarrolla en este artículo.
El resto de este artículo trabaja con $d=3$. $\square$

*Corolario 1.1.* «¿Por qué exactamente tres atributos vectoriales?» no es una elección paramétrica
libre — es la respuesta a «¿qué dimensión permite al Campo acoplarse de vuelta a los Agentes sin
escalada de rango?»

### Lema 2 (Clausura del álgebra)

**Lema 2.** *En $d=3$, los tres atributos de grado 1 $\{\mathbf{A}, \mathbf{I}, \mathbf{R}\}$ generan
el álgebra geométrica completa $G(3)$ de dimensión $8 = 2^3$.*

*Prueba.* Tres vectores linealmente independientes en $\mathbb{R}^3$ generan $G(3)$ por definición: los
elementos de base son $\{1, e_1, e_2, e_3, e_1e_2, e_2e_3, e_3e_1, e_1e_2e_3\}$ (grados 0 al 3). $S$
ocupa el grado 0; $\{\mathbf{A}, \mathbf{I}, \mathbf{R}\}$ ocupan el grado 1; los bivectores (grado 2)
y el pseudoescalar (grado 3) son generados por sus productos. No hay un quinto generador de grado 1
disponible en $G(3)$: el subespacio de grado 1 tiene dimensión 3. $\square$

### Lema 3 (El tiempo como cuarta dirección)

**Lema 3.** *Bajo A3, la evolución suave de la UDO requiere una dirección temporal $\partial_\tau$
independiente de las tres direcciones de atributos espaciales de A1. Juntas abarcan un espacio vectorial
$4$-dimensional $V^4$.*

*Prueba.* Por A3, la configuración $\Gamma(\tau,\mathbf{x})$ es suave en el tiempo $\tau$ y el espacio
$\mathbf{x}$. La suavidad implica la existencia de derivadas parciales $\partial_\tau$ y $\nabla$ (el
gradiente espacial a lo largo de las direcciones de atributos). El Lema 2 establece que el espacio de
atributos espaciales es $\mathbb{R}^3$, generado por $\{\mathbf{A}, \mathbf{I}, \mathbf{R}\}$. La
dirección temporal $\partial_\tau$ es independiente de estos tres generadores por tres razones: (i) no
puede expresarse como combinación espacial de $\mathbf{A}, \mathbf{I}, \mathbf{R}$, ya que diferencia
el argumento temporal, no el marco de atributos; (ii) $S$ es de grado 0 (escalar), no una dirección de
grado 1; (iii) promover uno de los atributos espaciales al rol temporal rompería la condición de clausura
$\binom{d}{2}=d$ que fuerza $d=3$ en el Lema 1. Por tanto $\partial_\tau$ es una cuarta dirección
genuinamente independiente.

Juntos, $\{\mathbf{A}, \mathbf{I}, \mathbf{R}, \partial_\tau\}$ generan un espacio vectorial
$4$-dimensional $V^4$. El álgebra de Clifford $\mathrm{Cl}(V^4, q)$ tiene dimensión $2^4=16$; su
representación matricial real fiel más pequeña es $4\times4$ (periodicidad de Bott, una vez fijada la
firma $q$ de $V^4$ por el Lema 4). La UDO tiene un eje temporal porque evoluciona suavemente — no
porque el espacio-tiempo sea postulado. $\square$

**Postulado A3′ (co-localización — nombrado explícitamente, no derivado).** A3 escribe
$\Gamma(\tau,\mathbf{x})$ como un campo sobre coordenadas *externas* $\mathbf{x}$ con un laplaciano
espacial $\nabla_{\mathbf{x}}^2$, mientras que A1/Lema 1 dan un espacio de atributos *interno*
$\mathrm{span}\{\mathbf{A},\mathbf{I},\mathbf{R}\}$. La frase del Lema 3 «las direcciones de atributos
espaciales de A1» identifica a las dos en silencio. Esta identificación no está forzada por A1–A3 tal
como se enunciaron: una UDO podría en principio llevar atributos internos de grado 1 sin que esos
atributos coincidan, como espacio vectorial, con las coordenadas sobre las cuales se propaga. Nombramos
la identificación como un cuarto postulado, ya que la derivación genuinamente lo necesita y antes se
usaba sin declararse:

> **A3′.** *Las direcciones de atributos de grado 1 $\{\mathbf{A},\mathbf{I},\mathbf{R}\}$ se realizan
> como vectores tangentes del mismo espacio físico sobre el cual $\Gamma$ se propaga; es decir, el
> espacio de atributos interno de A1 y el espacio de coordenadas externo de A3 son uno y el mismo
> $\mathbb{R}^3$.*

Esta es la lectura natural siempre que los atributos son vectores espaciales ordinarios (velocidad,
momento angular, un desplazamiento relacional) — objetos que ya transforman como vectores $SO(3)$ bajo
rotaciones del espacio físico que la unidad ocupa, que es justo lo que «grado 1» pretendía capturar en
A1. Deja de ser automática en cuanto un atributo no es literalmente un vector espacial (p.ej., las
normas por-casillero de la Definición en §2, donde $q_S,q_I,q_R$ no necesitan venir en absoluto de la
métrica de coordenadas). A3′ es, por tanto, load-bearing precisamente en la costura que el revisor
identificó en el Lema 3 (§8.3): sin él, el Lema 4 restringe solo el espacio de coordenadas
$\mathbf{x}$, y no dice nada sobre $\{\mathbf{A},\mathbf{I},\mathbf{R}\}$. Con él, la conclusión $(3,1)$
del Lema 4 se transfiere al espacio de atributos mismo, que es lo que el Corolario 4.2 (abajo) requiere
para siquiera ser una pregunta con sentido.

### Lema 4 (Firma Lorentziana a partir del operador de onda)

**Lema 4.** *La firma Lorentziana $(3,1)$ es forzada por el símbolo principal de la EOM (A3), no
postulada.*

*Prueba.* Por A3, la EOM contiene explícitamente el laplaciano espacial $-c^2\nabla_{\mathbf{x}}^2\Gamma$.
La parte principal — los términos de mayor derivada, que gobiernan la propagación — es el operador de
onda $\Box\Gamma = \ddot\Gamma - c^2\nabla_{\mathbf{x}}^2\Gamma$. La isotropía del laplaciano en las
tres direcciones espaciales se sigue directamente de P1: como todos los invariantes físicos de $\Gamma$
son $SO(3)$-invariantes bajo rotaciones de $\{\mathbf{A},\mathbf{I},\mathbf{R}\}$, ninguna dirección
espacial es preferida, y la parte espacial del símbolo principal debe ser $c^2|\mathbf{k}|^2$ (escalar
en $\mathbf{k}$, no un tensor con sesgo direccional). Esto excluye cualquier operador anisotrópico. (Un
operador parabólico como la ecuación del calor $\partial_\tau\Gamma = c^2\nabla_{\mathbf{x}}^2\Gamma$ es
de primer orden en el tiempo y no trata a $\partial_\tau$ como generador independiente en pie de igualdad
con los espaciales; queda excluido.) Tomando el símbolo de Fourier
($\partial_\tau \to i\omega$, $\nabla \to i\mathbf{k}$):
$$\sigma(\Box) = -\omega^2 + c^2|\mathbf{k}|^2 = \eta^{\mu\nu}p_\mu p_\nu, \quad
\eta = \mathrm{diag}(-1, +1, +1, +1)$$
Esta es la forma cuadrática de Minkowski con firma $(3,1)$. El álgebra de Clifford real de esta forma
(Atiyah, Bott y Shapiro 1964; Lounesto 2001) es $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$.

*Unicidad de la representación real.* La clasificación por periodicidad de Bott da $\mathrm{Cl}_{3,1}$
como álgebra matricial *real*. Exigir que $\Gamma$ sea una matriz real (el flujo gradiente
$\dot\Gamma = -\nabla P$ es real; la disipación es un proceso real) fija la firma en $(3,1)$ y excluye
$(1,3)$ (que da $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$, cuaterniónicamente), $(4,0)$ (que da
$\mathrm{Cl}_{4,0} \cong M_2(\mathbb{H})$, también cuaterniónicamente) y todas las demás firmas reales
que no dan $M_4(\mathbb{R})$. La única firma que produce un álgebra matricial $4\times4$ *real* con tres
generadores espaciales y uno temporal es $(3,1)$. $\square$

*Observación 3.1.* El paso «$d=3$ fuerza real $4\times4$» es el puente lógico: exigir tres generadores
espaciales en un álgebra matricial real fuerza exactamente $M_4(\mathbb{R}) = \mathrm{Cl}_{3,1}$. La
firma Lorentziana no es una elección — es lo que queda tras exigir realidad y tres dimensiones espaciales.

*Observación 3.2 (la escalera $\mathrm{Cl}_{3,0}\to\mathrm{Cl}_{3,1}\to\mathrm{Cl}_{4,1}$).* El Lema 3
es el mecanismo general por el cual el álgebra anfitriona de una UoC crece: se añade un nuevo generador
exactamente cuando la condición de suavidad de A3 expone una dirección genuinamente independiente que
los generadores existentes no pueden expresar. La segunda ley de Newton (§6.1) es el piso $d=3$, sin
generador temporal: no necesita $\partial_\tau$ más allá de un parámetro de tiempo escalar ordinario,
así que su anfitrión es $\mathrm{Cl}_{3,0}$. Promover $\partial_\tau$ a un generador independiente de
grado 1 — forzado una vez que la EOM acopla espacio y tiempo simétricamente a través del operador de
onda $\Box$ (Lema 4) — es exactamente el paso que produce $\mathrm{Cl}_{3,1}$, el anfitrión de la
electrodinámica libre (§6.2). Una UoC adicional, explorada fuera de este artículo bajo el nombre
UoC$_\mathrm{st}$ (el espacio-tiempo como unidad dinámica por derecho propio, con $\rho$ como un
verdadero quinto atributo en lugar de una cantidad derivada), expone una *segunda* dirección
independiente más allá de las cuatro de $\mathrm{Cl}_{3,1}$ — una dirección conforme/de escala,
verificada numéricamente que requiere un generador espacial ($e_\rho^2=+1$) para mantener la firma de
Gram Lorentziana, $(3,1)$, en vez de degradarse a $(2,2)$ bajo una elección temporal
($\mathrm{Cl}_{3,2}$). Esto fija el anfitrión a $\mathrm{Cl}_{4,1}$, que contiene a $\mathrm{Cl}_{3,1}$
como la subálgebra par de su graduación de Clifford (§30.3 de la exploración compañera). El patrón a
través de los tres pasos es el mismo: *el componente temporal/de escala nunca se postula — cada nuevo
generador es forzado por una condición de suavidad o de consistencia de firma aplicada al álgebra
anterior.* La verificación numérica completa de la comparación de firma $\mathrm{Cl}_{4,1}$ vs.
$\mathrm{Cl}_{3,2}$ se da en el repositorio de código compañero (§7); esta extensión no forma parte del
teorema cerrado de este artículo y se marca como tal en §8.3.

---

## 4. Teorema Principal

**Teorema ($\Gamma$ es forzada).** *Dados los axiomas A1, A2 y A3, la configuración de cualquier unidad
dinámica operativa es necesariamente*
$$\boxed{\Gamma = \Gamma_s \oplus \Gamma_a \;\in\; M_4(\mathbb{R}) = \mathrm{Cl}_{3,1}}$$
*donde $\Gamma_s = \tfrac{1}{2}(\Gamma + \Gamma^\top)$ (simétrica, 10 entradas independientes — sector
Fuerza) y $\Gamma_a = \tfrac{1}{2}(\Gamma - \Gamma^\top)$ (antisimétrica, 6 entradas independientes —
sector Campo), con:*
- *$\Gamma_s = \mathrm{Gram}(\mathbf{A}, \mathbf{I}, \mathbf{R}; S)$ — la estructura de acoplamiento
  métrico simétrico de los atributos (sector Fuerza; $S$ es la identidad de grado 0, no un generador
  de grado 1)*
- *$\Gamma_a$ = parte magnética ($\mathbf{I}\wedge\mathbf{R}$, bivector espacial, de SAIR) $\oplus$
  parte eléctrica ($\partial_\tau\wedge\nabla$, bivector espacio-temporal, estructura de
  acoplamiento$\leftrightarrow$evolución)*

*Prueba.* El Lema 1 fuerza $d = 3$ por clausura. El Lema 2 establece $G(3)$. El Lema 3 añade el
generador temporal $\partial_\tau$, extendiendo $G(3)$ a un álgebra de 4 generadores. El Lema 4
identifica el álgebra resultante como $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ vía el símbolo del
operador de onda.

*Unicidad de $\Gamma = \Gamma_s \oplus \Gamma_a$.* Una matriz simétrica definida positiva (métrica)
lleva solo Fuerza ($\Gamma_s \succ 0$, sin parte antisimétrica). Una forma simpléctica lleva solo Campo
($\Gamma_a$, sin parte simétrica). El objeto $\Gamma = \Gamma_s \oplus \Gamma_a$ es el **objeto mínimo
único** que lleva Fuerza y Campo simultáneamente — la descomposición única de una matriz real $4\times4$
en partes simétricas y antisimétricas. $\square$

*Observación 4.1.* El teorema no afirma que $\mathrm{Cl}_{3,1}$ sea el álgebra del espacio-tiempo físico
como fondo. Afirma que cualquier unidad dinámica operativa que satisface A1 y A2 tiene un objeto de
configuración que es un elemento de $\mathrm{Cl}_{3,1}$. El espacio-tiempo físico no es una entrada —
es un límite (la rama espacio-temporal del marco; véase §6.2).

---

## 5. Tres Proposiciones de Cierre

Tres elecciones técnicas aparecen en la prueba — la ortonormalidad del marco de atributos, la
identificación del generador temporal y la métrica sobre $M_4(\mathbb{R})$. Cada una está forzada, no
libre.

### Proposición P1 (La ortonormalidad es una redundancia de gauge)

**Proposición P1.** *Los invariantes físicos de $\Gamma$ — su determinante, traza, autovalores y
valores singulares — son independientes de la elección del marco ortonormal para
$\{\mathbf{A}, \mathbf{I}, \mathbf{R}\}$. La ortonormalidad es un gauge representacional, no un
postulado físico.*

*Prueba.* Sea $M \in SO(3)$ la rotación de Gram-Schmidt que mapea cualquier triple linealmente
independiente $\{\mathbf{A}, \mathbf{I}, \mathbf{R}\}$ a un marco ortonormal
$\{\hat{\mathbf{A}}, \hat{\mathbf{I}}, \hat{\mathbf{R}}\}$ que abarca el mismo subespacio. Bajo esta
rotación, $\Gamma \mapsto M\Gamma M^\top$. El espectro de $\Gamma$ (equivalentemente, $\det\Gamma$,
$\mathrm{tr}\,\Gamma$ y todos sus autovalores) es invariante bajo conjugación por cualquier
$M \in SO(3)$. El marco ortonormal fija las entradas matriciales explícitas de $\Gamma_s$ (diagonal en
ese marco), pero no su espectro. $\square$

### Proposición P2 (El generador temporal es el operador de evolución)

**Proposición P2.** *El generador de Clifford temporal $\gamma_0 \in \mathrm{Cl}_{3,1}$ que satisface
$\gamma_0^2 = -\mathbf{1}$ es el único generador de grado 1 asignado a la dirección temporal tal que el
operador diferencial lineal $\mathcal{D} = \gamma^\mu\partial_\mu$ factoriza el operador de onda:
$\mathcal{D}^2 = \Box$.*

*Prueba.* El símbolo del operador de onda $\Box = \partial_\tau^2 - c^2\nabla^2$ es
$\eta^{\mu\nu}p_\mu p_\nu$ con $\eta = \mathrm{diag}(-1,+1,+1,+1)$. Esto define las relaciones de
anticonmutación $\{\gamma_\mu, \gamma_\nu\} = 2\eta_{\mu\nu}$, con $\gamma_0^2 = -\mathbf{1}$ forzado
por $\eta_{00} = -1$. La asignación de $\gamma_0$ a la dirección temporal $\partial_\tau$ es la única
que hace que $(\gamma^\mu\partial_\mu)^2 = \Box$ (la factorización de Dirac). Aquí $\gamma_0$ es un
elemento del álgebra y $\partial_\tau$ es un operador diferencial; P2 no afirma que sean el mismo objeto
— afirma que $\gamma_0$ es el generador algebraico conjugado a $\partial_\tau$ en la factorización de
$\Box$. Verificado numéricamente: existe una representación real $4\times4$ que satisface
$\{\gamma_\mu, \gamma_\nu\}/2 = \eta_{\mu\nu} = \mathrm{diag}(-1,+1,+1,+1)$ con $\gamma_0^2 = -I$,
$\gamma_i^2 = +I$ (residuo $< 10^{-14}$; ver
[`verify_cl31.py`](https://github.com/hmolinab/papers/tree/main/weld_clifford/code/verify_cl31.py)). $\square$

*Nota.* P2 no confunde categorías: $\gamma_0$ es un elemento de $\mathrm{Cl}_{3,1}$; $\partial_\tau$ es
un operador diferencial que actúa sobre funciones $\Gamma(\tau,\mathbf{x})$. Lo que P2 establece es un
emparejamiento canónico entre ambos, mediado por la factorización de Dirac del operador de onda dado
por A3.

### Proposición P3 (Frobenius es la métrica de Clifford canónica)

**Proposición P3.** *La métrica sobre el espacio de configuraciones $\Gamma \in M_4(\mathbb{R}) =
\mathrm{Cl}_{3,1}$ es la norma de Frobenius $\|\Gamma\|^2 = \mathrm{Tr}(\Gamma^\top\Gamma)$, ya
determinada por A2.*

*Prueba.* El producto geométrico de A2 define el producto interno canónico sobre cualquier álgebra de
Clifford:
$$\langle A, B \rangle_{\mathrm{Cl}} := \langle A\tilde{B} \rangle_0$$
la componente de grado 0 (escalar) del producto geométrico de $A$ con el reverso de Clifford $\tilde{B}$.
En la representación real $4\times4$ de $\mathrm{Cl}_{3,1}$, el reverso de Clifford corresponde a la
transposición matricial ($\tilde{B} = B^\top$), dando
$\langle A, B\rangle_{\mathrm{Cl}} = \tfrac{1}{4}\mathrm{Tr}(A^\top B)$, que es el producto interno de
Frobenius salvo la normalización $\tfrac{1}{4}$.

*Unicidad.* $\mathrm{Spin}(3,1)$ actúa sobre $\mathrm{Cl}_{3,1}$ por conjugación adjunta
$g\cdot\Gamma = g\Gamma g^{-1}$. Cualquier métrica física debe ser invariante bajo esta acción. La
descomposición en grados $\Lambda^0 \oplus \Lambda^1 \oplus \Lambda^2 \oplus \Lambda^3 \oplus \Lambda^4$
de $\mathrm{Cl}_{3,1}$ consta de representaciones irreducibles pairwise no isomorfas de
$\mathrm{Spin}(3,1)$. Por el lema de Schur, cualquier forma bilineal $\mathrm{Spin}(3,1)$-invariante es
proporcional a $\mathrm{Tr}(A^\top B)$ en cada bloque de grado, con una constante posiblemente diferente
en cada grado. La restricción de submultiplicatividad — $\|\Gamma\Gamma'\| \leq \|\Gamma\|\|\Gamma'\|$
para todo $\Gamma, \Gamma' \in \mathrm{Cl}_{3,1}$, requerida para que $P(\Gamma) = \|\Gamma\|^2$ sea
compatible con el producto del álgebra — fuerza una escala igual en todos los grados (una escala
diferente por grado violaría la submultiplicatividad para productos de grado mixto). El resultado es
Frobenius, de forma única. $\square$

*Extensión a $\mathrm{Cl}_{4,1}$.* La configuración del espacio-tiempo en el marco GSF vive en
$\mathrm{Cl}_{4,1} \cong M_4(\mathbb{C})$ (periodicidad de Bott: $p-q = 3$). El mismo argumento se
aplica con el reverso de Clifford reemplazado por el conjugado hermítico:
$\langle A, B\rangle = \tfrac{1}{4}\mathrm{Tr}(A^\dagger B)$, dando la norma de Hilbert-Schmidt
$\|\Gamma\|^2 = \mathrm{Tr}(\Gamma^\dagger\Gamma)$, real y no negativa. P3 se mantiene sin modificación.

---

## 6. Dos Límites Físicos

El teorema principal y las proposiciones establecen la estructura algebraica. Dos teorías físicas
aparecen como casos límite, mostrando que el álgebra tiene contenido concreto.

### 6.1 Segunda ley de Newton (sector Fuerza, det > 0)

En el sector operacionalmente activo ($\det\Gamma > 0$, $\Gamma_s \succ 0$), la dinámica dominante
transcurre a lo largo del modo blando de $\Gamma$ — la dirección del valor singular mínimo. Proyectando
la EOM sobre el escalar del modo blando $x$ (valor singular dominante de $\Gamma$ a lo largo de
$\mathbf{A}$):
$$\ddot{x} + \gamma\dot{x} + \partial_x P = F_\text{ext}$$
Esta es la segunda ley de Newton para un oscilador amortiguado: la masa es la inercia del modo blando,
$\gamma$ es el amortiguamiento de la UDO y $P$ es el paisaje de potencial. La ley de Newton no es un
caso especial incorporado al marco — es lo que se obtiene al proyectar la EOM sobre el modo dominante.
**Estado: correspondencia estructural $\langle\mathrm{CE}\rangle$, no una derivación desde primeros
principios.**

### 6.2 Electrodinámica libre (sector Campo, frontera det = 0)

En la frontera $\det\Gamma = 0$, la configuración pierde rango: uno o más valores singulares de $\Gamma$
se aproximan a cero. Cuando $\gamma \to 0$ (límite no disipativo) y la configuración vive en el sector
de grado 2 (bivector) $\Gamma_a$ de $\mathrm{Cl}_{3,1}$, la EOM se reduce a:
$$\Box\Gamma_a = 0 \quad\Rightarrow\quad \Box F_{\mu\nu} = 0$$
que es la ecuación de Maxwell libre en ausencia de fuentes ($\partial^\mu F_{\mu\nu} = 0$), junto con
la identidad de Bianchi $\partial_{[\mu}F_{\nu\rho]} = 0$ (automática de $F = \mathrm{d}A$). El bivector
$F_{\mu\nu}$ es el tensor de Faraday; la identificación de $\Gamma_a$ con el sector de grado 2 de
$\mathrm{Cl}_{3,1}$ hace que el Campo $\mathbf{I}\wedge\mathbf{R}$ corresponda a la parte espacial
(magnética) de $F_{\mu\nu}$, y la parte eléctrica surge del acoplamiento $\partial_\tau\wedge\nabla$.
En el sector de campo libre, la conservación de carga $\partial^\mu J_\mu = 0$ se sigue de la antisimetría de $F$ sin suposiciones
adicionales. **Estado: Maxwell libre $\langle\mathrm{TEO}\rangle[\mathrm{D}]$; ecuación con fuentes
$\langle\mathrm{A}\rangle$ (requiere cerrar el bloque de acoplamiento cruzado).**

*Observación 6.1 (reconciliando dos descomposiciones de $F$).* $\mathbf{I},\mathbf{R}$ aquí son
generadores de grado 1 ordinarios de $V^4$ (Lema 3) — el mismo estatus que $\mathbf{A},\mathbf{I},
\mathbf{R}$ en A1 — y $\mathbf{I}\wedge\mathbf{R}$ es una cuña genuina de dos vectores de grado 1,
exactamente el mecanismo que produce $\mathbf{L}=\mathbf{I}\wedge\mathbf{R}$ en el límite de Newton
(§6.1) o la vorticidad en la correspondencia de Navier–Stokes. $B$ ya es de grado 2 en $\mathbb{R}^3$
(es dual al vector magnético de grado 1 ordinario, es decir, un vector axial), así que identificarlo con
$\mathbf{I}\wedge\mathbf{R}$ no requiere ningún cambio a A1. $E$, en cambio, es de grado 1 en
$\mathbb{R}^3$; solo se vuelve una componente de bivector una vez elevado a $V^4$ mediante cuña con el
generador temporal ($\partial_\tau\wedge\nabla$, no $\mathbf{I}\wedge\mathbf{R}$). Una exploración
compañera (Pieza 4, `pieza4_electromagnetismo.md`) etiqueta las dos mitades covariantes del bivector de
Faraday *ya ensamblado* $F$ como «$I=E$, $R=B$» bajo un criterio basado en trabajo (qué componente hace
trabajo sobre una carga). Ese etiquetado responde una pregunta distinta — cómo dividir $F$ una vez que
existe — y no está en tensión con la derivación aquí, que responde cómo se *construye* la mitad
magnética de $F$ a partir de dos generadores de grado 1. Las dos lecturas comparten nombres pero no
referentes; no deben confundirse.

---

## 7. Verificación Numérica

Los siguientes pasos de la derivación están confirmados numéricamente; los scripts están en
https://github.com/hmolinab/papers/tree/main/weld_clifford/code

| Resultado | Script | Residuo |
|---|---|---|
| $\{\gamma_\mu, \gamma_\nu\}/2 = \eta_{\mu\nu}$ en rep. real $4\times4$ | [`verify_cl31.py`](https://github.com/hmolinab/papers/tree/main/weld_clifford/code/verify_cl31.py) | $< 10^{-14}$ |
| $\gamma_0^2 = -I$, $\gamma_i^2 = +I$ | [`verify_cl31.py`](https://github.com/hmolinab/papers/tree/main/weld_clifford/code/verify_cl31.py) | $< 10^{-14}$ |
| $\langle A, B\rangle_\mathrm{Cl} = \mathrm{Tr}(A^\top B)/4$ en elementos de grado 1 | [`verify_clifford_metric.py`](https://github.com/hmolinab/papers/tree/main/weld_clifford/code/verify_clifford_metric.py) | $< 10^{-14}$ |
| Submultiplicatividad de Frobenius: $\|\Gamma\Gamma'\|_F \leq \|\Gamma\|_F\|\Gamma'\|_F$ (0 violaciones); Pitágoras: $\|\Gamma\|^2 = \|\Gamma_s\|^2 + \|\Gamma_a\|^2$ | [`verify_frobenius.py`](https://github.com/hmolinab/papers/tree/main/weld_clifford/code/verify_frobenius.py) | $0$ violaciones; error $< 10^{-13}$ |
| $\det\Gamma$ como invariante bajo conjugación $SO(3,1)$ | [`verify_det_invariance.py`](https://github.com/hmolinab/papers/tree/main/weld_clifford/code/verify_det_invariance.py) | $< 10^{-12}$ |

---

## 8. Discusión

### 8.1 Qué es nuevo

El programa de álgebra de espacio-tiempo (Hestenes 1966; Doran y Lasenby 2003) toma $\mathrm{Cl}_{3,0}$
o $\mathrm{Cl}_{1,3}$ como el álgebra del espacio físico o el espacio-tiempo, motivado por la geometría
conocida. El presente trabajo invierte esta lógica: $\mathrm{Cl}_{3,1}$ se deriva como la estructura
algebraica forzada de cualquier unidad dinámica que se autodescribe, sin asumir un fondo de
espacio-tiempo. Los pasos clave son: (i) la condición de clausura $\binom{d}{2}=d$ fuerza la dimensión
del espacio de atributos vectoriales (Hurwitz confirma la consistencia); (ii) el operador de onda fija
la firma; (iii) la realidad de $\Gamma$ selecciona $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$ sobre el
álgebra $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$, isomorfa como espacio vectorial pero distinta como
álgebra. El paso (iii) es una selección entre convenciones de firma que una derivación métrica-primero
no enfrenta y que otras rutas de firma emergente (§8.2) no hacen; es específica a la exigencia de que
la configuración y su dinámica disipativa sean reales. Ningún paso es obvio desde la perspectiva de la
física primero.

El antecedente más cercano es la observación (Lounesto 2001, §17) de que el álgebra de Clifford del
símbolo del operador de onda es $\mathrm{Cl}_{3,1}$. Aquí esa observación se convierte en teorema: dentro
de los axiomas A1–A3 es la *única* álgebra de Clifford compatible con una unidad real, que se
autodescribe, en evolución suave.

### 8.1bis Corolario: el resultado de la firma agota las alternativas

El Lema 4 selecciona $(3,1)$. Vale la pena registrar que el mismo argumento, corrido sobre el espacio
completo de símbolos candidatos en vez de solo el que A3 produce, *clasifica* las alternativas en lugar
de meramente excluirlas — lo cual fortalece el teorema sin costo adicional.

**Corolario 4.1 (completitud de los regímenes).** *Sea $q$ el símbolo principal de una EOM de segundo
orden sobre $V^4$, es decir, una forma cuadrática real sobre un espacio $4$-dimensional. Entonces:*
*(i) por la ley de inercia de Sylvester, $q$ cae en exactamente una de $15$ clases de congruencia
indexadas por $(n_+,n_0,n_-)$ con $n_++n_0+n_-=4$; las no degeneradas forman $5$ componentes conexas
del espacio de tales formas, ya que la inercia es un invariante completo y localmente constante;*
*(ii) módulo la convención de signo global $(n_+,\cdot,n_-)\sim(n_-,\cdot,n_+)$, quedan exactamente
tres regímenes — elíptico $(4,0)$, hiperbólico $(3,1)$, ultrahiperbólico $(2,2)$;*
*(iii) de estos, exactamente uno, el Lorentziano $(3,1)$, produce un problema de Cauchy bien puesto. El
caso elíptico está bien puesto como problema de frontera pero describe equilibrio, no evolución; el
caso ultrahiperbólico tiene dos direcciones temporales y está mal puesto en el sentido de Hadamard.*

*Prueba.* (i) es la ley de Sylvester junto con la continuidad de los autovalores: un camino entre formas
de distinta inercia debe pasar por una forma degenerada, así que cada clase es abierta y cerrada en el
estrato no degenerado. (ii) es la identificación de una forma con su negativa. (iii) es la clasificación
estándar de EDP por símbolo principal (Courant y Hilbert 1962, vol. II): todos los autovalores de un
signo dan un operador elíptico; exactamente uno de signo opuesto da un operador hiperbólico con datos de
Cauchy bien puestos; dos o más de cada uno dan un operador ultrahiperbólico, para el cual el problema de
Cauchy está mal puesto. $\square$

Dos consecuencias para la lectura del Lema 4. Primero, la unicidad de $(3,1)$ no es una afirmación sobre
una lista corta de candidatos motivados físicamente: la lista de *todas* las firmas reales sobre $V^4$
es finita, queda agotada arriba, y $(3,1)$ es el único superviviente. Segundo, los casos excluidos
adquieren significado en lugar de simplemente ser descartados — la clase elíptica es el régimen
estático/de equilibrio, y la clase ultrahiperbólica es la patología genuina. Esto importa porque las
clasificaciones basadas en $\det$ no pueden ver la distinción: $\det q>0$ vale tanto para $(4,0)$ como
para $(2,2)$, así que el signo del determinante mezcla un régimen físico con uno patológico, y solo la
inercia completa los separa. Un artículo compañero usa precisamente esta estratificación para organizar
los regímenes dinámicos de $\Gamma$.

*Alcance.* El Corolario 4.1 concierne al símbolo principal — el objeto que fija el tipo de EDP y la
buena postura. No debe confundirse con la inercia de la matriz de Gram $\Gamma_s$ de A2, que es un
objeto distinto construido a partir de los casilleros de atributos. Las dos firmas son, en general,
invariantes independientes de objetos distintos; el Corolario 4.2 establece exactamente cuándo deben
coincidir.

**Corolario 4.2 (cuándo la Gram hereda la firma del símbolo).** *Sea $\eta$ la forma $(3,1)$ del
símbolo (Lema 4, bajo A3′) y sea $\Gamma_s$ construida por la lectura de congruencia de la Definición en
§2 (Axioma A2), $\Gamma_s = V^{\mathsf T}\eta V$ con $V=[S\mathbf{e}_0\mid\mathbf{A}\mid
\mathbf{I}\mid\mathbf{R}]$. Entonces $\mathrm{firma}(\Gamma_s)=\mathrm{firma}(\eta)=(3,1)$
siempre que $V$ sea invertible, sin condición adicional.*

*Prueba.* Esto es exactamente la ley de inercia de Sylvester: la congruencia por una matriz invertible
preserva la firma. $\square$

La condición es exacta. Con $\mathbf e_0$ fijado por el cierre de gauge de §2, la lectura por-casillero
con formas *heterogéneas* $q_S,q_I,q_R\neq\eta$ — usada siempre que los cuatro atributos no se miden
todos bajo la única forma $\eta$, p.ej. $S,\mathbf{I},\mathbf{R}$ llevando normas ordinarias
definidas-positivas sin contenido de Minkowski — no es en absoluto una congruencia de $\eta$ (sigue
siendo una congruencia de *alguna* forma en bloques, a saber $q_S\oplus q_A\oplus q_I\oplus q_R$, pero
no de la única $\eta$ que el Corolario 4.2 exige). El Corolario 4.2 no aplica ahí, y la firma de
$\Gamma_s$ queda libre para variar sobre las cinco clases del Corolario 4.1(i); esto se confirma
numéricamente en el trabajo compañero de instanciación, donde un estado másico (partícula) cae en
$(4,0)$, un estado fotónico cae en la frontera degenerada, y un estado relativista general — donde el
atributo $\mathbf{A}$ genuinamente *es* una cuadrivelocidad de Minkowski, satisfaciendo $\langle
\mathbf{A},\mathbf{A}\rangle_\eta=-c^2$ — cae en $(3,1)$, el caso más cercano a satisfacer la hipótesis
del Corolario 4.2. Verificación:
`models/calcs/brainstorming/papers/weld_clifford/puente_simbolo_gram_sylvester_prueba.py`.

**Observación (sin misterio residual).** La tensión aparente — «el símbolo fuerza $(3,1)$» frente a «la
Gram varía sobre cinco sectores» — se disuelve una vez que las dos construcciones de §2 se distinguen.
No hay inconsistencia oculta: el $(3,1)$ del símbolo es un hecho de fondo fijo sobre el operador
(gobierna si la *evolución del campo* $\Gamma(\tau,\mathbf{x})$ está bien puesta); la firma de la Gram
es un hecho dependiente del estado sobre el *valor* que $\Gamma_s$ toma en un instante (clasifica el
*régimen de ese estado*). Coinciden, por teorema, exactamente en la lectura de congruencia con $V$
invertible; son libres de diferir, también por teorema (Sylvester simplemente no restringe una
construcción que no es de congruencia), bajo la lectura por-casillero. Cuál lectura usa un dominio
físico dado es un hecho de modelado sobre ese dominio, no un hueco en el álgebra.

### 8.2 Relación con los enfoques de firma emergente

La idea de que la firma Lorentziana debería *derivarse* en vez de *postularse* no es nueva, y este
artículo no reclama prioridad sobre ese programa; aporta una ruta específica. Dos comparaciones fijan la
posición de la presente derivación.

Singh (2025) obtiene una firma Lorentziana dentro de una teoría de pre-espacio-tiempo octoniónica
adoptando álgebras de división *split*: la unidad compleja-split $\omega$ con $\omega^2=+1$ da una
magnitud $x^2-y^2$ (Lorentziana) en lugar de $x^2+y^2$ (Euclidiana), y los biocotoniones split entonces
generan una base de firma $(3,3)$ que porta espacio-tiempos Lorentzianos $4$-dimensionales embebidos. La
firma allí es consecuencia de *elegir álgebras split*, una elección motivada por la firma objetivo. La
presente derivación difiere en dos aspectos. Primero, el mecanismo: la firma queda fijada por la
exigencia de que la ecuación de movimiento de segundo orden (A3) admita un problema de Cauchy bien
puesto — un símbolo principal Lorentziano es el único que lo hace (Lema 4; Hadamard) — en vez de por
seleccionar un sistema numérico split. No se asume ningún carácter split; el cambio de signo queda
forzado por la hiperbolicidad de la evolución. Segundo, el álgebra objetivo queda fijada
*específicamente* a $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$ — no a la isomorfa-como-espacio-vectorial
pero distinta-como-álgebra $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$ — por la realidad de $\Gamma$ (la
dinámica disipativa y de gradiente son procesos reales; §8.1, §4). La construcción de Singh vive en
dimensión superior $(3,3)$ con rebanadas Lorentzianas embebidas y no hace esta selección de
realidad-de-la-configuración entre las dos convenciones de firma. Las dos derivaciones son, por tanto,
complementarias: ambas responden «sí» a la pregunta teorema-versus-postulado, por mecanismos
independientes, y la presente es posiblemente la más económica en sus premisas (buena postura de una
evolución real, en vez de un álgebra split elegida).

De forma más amplia, la visión de una firma Lorentziana emergente tiene una larga tradición en la
gravedad análoga e inducida (Sakharov 1967; Barceló, Liberati y Visser 2011; Volovik 2003), donde la
métrica Lorentziana efectiva surge del comportamiento de baja energía de un sustrato no relativista. El
presente resultado es más estrecho y puramente algebraico: no construye una métrica efectiva a partir
de un sustrato, sino que identifica qué álgebra de Clifford real fuerza la estructura de una unidad
dinámica que se autodescribe. Se ofrece como un compañero estructural de esos programas, no como un
reemplazo.

### 8.3 Alcance honesto

Este artículo establece la estructura algebraica. No:
- Prueba la unicidad de la estructura de atributos SAIR con independencia de A1 (ese es el contenido
  de A1 mismo, que tomamos como fundacional en lugar de derivado)
- Cierra la rama $d=7$ (octoniónica) (problema abierto; no desarrollado en este artículo)
- Cierra el siguiente peldaño de la escalera $\mathrm{Cl}_{3,1}\to\mathrm{Cl}_{4,1}$ esbozado en la
  Observación 3.2: la necesidad del generador conforme/de escala está verificada numéricamente en la
  exploración compañera pero aún no derivada de A1–A3 con el mismo rigor que los Lemas 1–4
- Establece la **unicidad** a nivel de instancia de la asignación de casilleros SAIR (calificación de
  la Observación 2.1): qué cantidad observable de una UDO dada ocupa $S$ frente a
  $\mathbf{A},\mathbf{I},\mathbf{R}$ no queda decidido por el teorema del contenedor. Una condición
  necesaria (compatibilidad de representación, Schur) se sigue del mismo argumento que los Lemas 2–4;
  los criterios de selección suficientes son objeto de una línea de trabajo compañera, menos madura
  (siete dominios verificados por retrodicción ciega y rechazo activo de asignaciones incorrectas pero
  compatibles) que se mantiene deliberadamente fuera de este artículo en vez de diluir sus lemas
  cerrados con uno abierto
- Establece, para un dominio dado, la **existencia** de una cuádrupla SAIR en primer lugar (segunda
  calificación de la Observación 2.1): si $\mathbf{A},\mathbf{I},\mathbf{R}$ surgen como vectores de
  grado 1 en absoluto es empírico, no algebraico, y falla en la mayoría de los dominios probados
  (13/20 en un barrido compañero). Esto es lógicamente previo a, e independiente de, la pregunta de
  unicidad de arriba — el teorema del contenedor es condicional a la existencia y no prueba nada sobre
  ella

Dos huecos estructurales fueron identificados en un borrador anterior; ambos quedan ahora nombrados y
con resoluciones precisas (parciales), en lugar de dejarse como admisiones desnudas, ya que un hueco
nombrado que solo se afirma abierto, sin decir exactamente qué lo cerraría, todavía no cumple su función.

**(a) El espacio de atributos y el espacio de coordenadas se identificaron sin argumento — ahora
Postulado A3′.** A1 y el Lema 1 dan un espacio de atributos $\mathbb{R}^3$ *interno* generado por
$\{\mathbf{A},\mathbf{I},\mathbf{R}\}$. A3 trata a $\Gamma(\tau,\mathbf{x})$ como un campo sobre un
espacio de coordenadas *externo* que porta $\nabla_{\mathbf{x}}^2$, y el Lema 4 lee la firma de ese
laplaciano. El paso que identifica los dos espacios queda ahora nombrado explícitamente, inmediatamente
después del Lema 3, como **Postulado A3′**: la resolución no es derivar la identificación de A1–A3 (no
es derivable de ellos; una UDO podría en principio llevar atributos internos que no coincidan con sus
coordenadas de propagación) sino enunciarla como una cuarta premisa independiente, exactamente como la
irreducibilidad de A1 misma se maneja en la Observación 2.1. Este es un fortalecimiento genuino, no un
reetiquetado: el alcance del teorema siempre fue condicional a A3′; el lector ahora puede ver esa
condición y evaluarla, en vez de absorberla en silencio dentro de «las direcciones de atributos
espaciales de A1» en el Lema 3.

**(b) Dos objetos distintos se llamaban ambos «la firma» — ahora Corolario 4.2.** El Lema 4 y el
Corolario 4.1 conciernen a la inercia del *símbolo principal* sobre
$V^4=\mathrm{span}\{\mathbf{A},\mathbf{I},\mathbf{R},\partial_\tau\}$. A2 provee independientemente una
matriz de Gram $\Gamma_s$ de los casilleros $\{S,\mathbf{A},\mathbf{I},\mathbf{R}\}$ (§2, Definición),
que también lleva una inercia. Estas no necesitan coincidir en general — son $4$-espacios distintos, y
la construcción de la Gram admite dos lecturas (§2). El Corolario 4.2 cierra esto con una condición
exacta en vez de un puente afirmado o meramente esperado: la Gram hereda la firma $(3,1)$ del símbolo,
por la ley de inercia de Sylvester, precisamente cuando se construye como una congruencia auténtica
$V^{\mathsf T}\eta V$ con $V$ invertible; bajo la construcción por-casillero alternativa (también
licenciada por A2, y la que se usa siempre que un atributo no lleva estructura de Minkowski propia), no
se reclama ni se necesita tal herencia, y la firma queda libre para variar sobre todas las clases
admisibles — que es exactamente lo que observa un artículo compañero cuando lee regímenes dinámicos a
partir de la Gram. Nada aquí era contradictorio; las dos lecturas de la Definición en §2 simplemente no
se habían distinguido antes.

Los residuos que quedan abiertos tras P1/P2/P3 son los tres axiomas originales A1, A2, A3, junto con
el Postulado A3′ recién nombrado. El hueco (a) se resuelve declarando A3′ como una premisa — su verdad
para un dominio físico dado sigue siendo una pregunta de modelado, no un teorema, y se marca como tal.
El hueco (b) se resuelve por completo: el Corolario 4.2 es un teorema con una hipótesis verificable, no
un problema abierto. El costo de la explicitud: cuatro axiomas en lugar de dos, y un corolario que se
gana su lugar en vez de una promesa por cumplir. La ganancia: ninguna premisa entra en la derivación sin
declararse, y el lugar donde dos «firmas» distintas podían confundirse en silencio ya no puede.

### 8.4 Trabajo relacionado

- Hurwitz (1898): álgebras normadas de división en dimensiones 1, 2, 4, 8.
- Eckmann (1943): productos vectoriales en $\mathbb{R}^n$ solo existen para $n = 1, 3, 7$.
- Atiyah, Bott y Shapiro (1964): módulos de Clifford y periodicidad de Bott.
- Hestenes (1966, 1986): álgebra de espacio-tiempo como lenguaje de la física.
- Doran y Lasenby (2003): álgebra geométrica para físicos (Cambridge).
- Lounesto (2001): álgebras de Clifford y espinores (Cambridge).
- Adams (1960): campos vectoriales en esferas; confirma Hurwitz vía K-teoría.
- Sakharov (1967): gravedad inducida; la métrica como respuesta elástica emergente.
- Barceló, Liberati y Visser (2011): gravedad análoga (Living Rev. Relativity); métricas Lorentzianas
  emergentes a partir de sustratos no relativistas.
- Volovik (2003): *The Universe in a Helium Droplet* (Oxford); relatividad emergente y métrica efectiva
  en líquidos cuánticos.
- Singh (2025): dinámica de trazas, octoniones y unificación; firma Lorentziana desde biocotoniones
  split. arXiv:2501.18139.
- Molina (2024a): el determinante como fuente del término cúbico en flujos gradiente matriciales.
  DOI: 10.5281/zenodo.20752208

---

## 9. Conclusiones

A partir de cuatro axiomas estructurales — estructura de atributos SAIR (A1), producto geométrico (A2),
evolución suave continua (A3), y co-localización del espacio de atributos con las coordenadas de
propagación (A3$'$) — el álgebra de Clifford real $\mathrm{Cl}_{3,1}$ emerge como teorema estructural
más que como postulado geométrico. La cadena de derivación es:

$$\underbrace{\text{SAIR}}_\text{A1} + \underbrace{\text{prod. geom.}}_\text{A2}
\xrightarrow{\binom{d}{2}=d} d=3
\xrightarrow{G(3)} \{\mathbf{A},\mathbf{I},\mathbf{R}\}=\gamma_i
\xrightarrow{\text{A3: suave, }c\text{ finita}} \partial_\tau \perp \mathbb{R}^3
\xrightarrow{\sigma(\Box)=\eta} (3,1)
\xrightarrow{\text{P1/P2/P3}} \Gamma = \Gamma_s\oplus\Gamma_a \in M_4(\mathbb{R})$$

Tres proposiciones cierran los residuos técnicos: la ortonormalidad es un gauge representacional (P1);
$\gamma_0$ es el único generador algebraico conjugado a $\partial_\tau$ en la factorización de Dirac de
$\Box$ — no el operador mismo (P2); Frobenius es la métrica de Clifford canónica forzada por A2 (P3).
Los axiomas irreducibles son A1, A2 y A3. La mecánica clásica (§6.1) y la electrodinámica libre (§6.2)
aparecen como límites estructurales.

El resultado provee una base estructural para el programa de álgebra de espacio-tiempo: no «dado
el espacio de Minkowski, usar $\mathrm{Cl}_{3,1}$», sino «desde la estructura de una unidad dinámica,
$\mathrm{Cl}_{3,1}$ es la representación forzada».

---

## Referencias

Adams, J. F. (1960). Vector fields on spheres. *Annals of Mathematics*, 75(3), 603–632.

Atiyah, M. F., Bott, R. y Shapiro, A. (1964). Clifford modules. *Topology*, 3(S1), 3–38.

Barceló, C., Liberati, S. y Visser, M. (2011). Analogue gravity. *Living Reviews in Relativity*, 14(1), 3.

Doran, C. y Lasenby, A. (2003). *Geometric Algebra for Physicists*. Cambridge University Press.

Eckmann, B. (1943). Stetige Lösungen linearer Gleichungssysteme. *Commentarii Mathematici Helvetici*,
15(1), 318–339.

Hestenes, D. (1966). *Space-Time Algebra*. Gordon and Breach.

Hestenes, D. (1986). A unified language for mathematics and physics. En *Clifford Algebras and their
Applications in Mathematical Physics*. D. Reidel.

Hurwitz, A. (1898). Über die Komposition der quadratischen Formen von beliebig vielen Variabeln.
*Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen*, 309–316.

Lounesto, P. (2001). *Clifford Algebras and Spinors* (2nd ed.). Cambridge University Press.

Molina, H. (2024a). The determinant as an orientation invariant and the source of the cubic term in
equivariant matrix gradient flows. DOI: 10.5281/zenodo.20752208

Molina, H. (2025). *Gamma Space Framework* (manuscrito de trabajo). Disponible en:
https://github.com/hmolinab/gamma-space-framework

Sakharov, A. D. (1967). Vacuum quantum fluctuations in curved space and the theory of gravitation.
*Soviet Physics Doklady*, 12, 1040–1041.

Singh, T. P. (2025). Trace dynamics, octonions, and unification. arXiv:2501.18139.

Volovik, G. E. (2003). *The Universe in a Helium Droplet*. Oxford University Press.
