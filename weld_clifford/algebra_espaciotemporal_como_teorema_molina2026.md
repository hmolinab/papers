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

Derivamos el álgebra de Clifford real $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ a partir de tres axiomas
estructurales sobre cualquier unidad dinámica operativa (UDO). A1 (SAIR): la unidad queda descrita por
cuatro atributos intrínsecos — un escalar $S$ y tres vectores $\mathbf{A}, \mathbf{I}, \mathbf{R}$ en
$\mathbb{R}^d$. A2 (producto geométrico): la estructura está gobernada por el producto geométrico de esos
atributos, cuya parte de grado 2, $\mathbf{I}\wedge\mathbf{R}$, es el bivector Campo. A3 (evolución
continua): la UDO evoluciona suavemente en tiempo y espacio a velocidad de propagación finita. A partir
de estos tres axiomas — sin postular una métrica de espacio-tiempo ni una geometría de fondo — derivamos:
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

Mostramos que la respuesta es afirmativa, bajo tres axiomas mínimos: A1 (estructura de atributos), A2
(producto geométrico) y A3 (evolución suave a velocidad finita). La derivación no requiere el
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

**Plan.** §2 enuncia los tres axiomas. §3 deriva los cuatro lemas. §4 enuncia y prueba el teorema
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

donde $d$ está por determinarse. El mapeo de las propiedades observables de cualquier entidad coherente
a los cuatro casilleros estructurales $\{S, \mathbf{A}, \mathbf{I}, \mathbf{R}\}$ es estructuralmente
único (no existen dos asignaciones inequivalentes que produzcan predicciones estructuralmente idénticas
para la misma entidad).

*Observación 2.1.* A1 es el axioma fundacional del marco; no se deriva de premisas más simples dentro
de este artículo. Su justificación es el argumento estructural de que $\{S, \mathbf{A}, \mathbf{I},
\mathbf{R}\}$ son los grados de un álgebra geométrica de dimensión mínima compatible con A2 — una
circularidad resuelta por la consistencia mutua de A1 y A2, no por una prueba independiente de A1. El
papel de A1 en esta estructura es análogo al de la selección natural en la teoría darwiniana: un postulado
mínimo que genera el resto.

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
$\mathbb{R}^7$ (Eckmann 1943) como parte imaginaria del producto octoniómico, pero no surge de la
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
la firma. Ningún paso es obvio desde la perspectiva de la física primero.

El antecedente más cercano es la observación (Lounesto 2001, §17) de que el álgebra de Clifford del
símbolo del operador de onda es $\mathrm{Cl}_{3,1}$. Aquí esa observación se convierte en teorema: es
la *única* álgebra de Clifford compatible con A1 y A2.

### 8.2 Alcance honesto

Este artículo establece la estructura algebraica. No:
- Prueba la unicidad de la estructura de atributos SAIR con independencia de A1 (ese es el contenido
  de A1 mismo, que tomamos como fundacional en lugar de derivado)
- Cierra la rama $d=7$ (octoniónica) (problema abierto; no desarrollado en este artículo)

Los residuos que quedan abiertos tras P1/P2/P3 son exactamente A1, A2 y A3 — los tres axiomas. Todo lo
demás en la derivación es un teorema. El costo de la explicitud: tres axiomas en lugar de dos. La
ganancia: ninguna premisa entra en la derivación sin declararse.

### 8.3 Trabajo relacionado

- Hurwitz (1898): álgebras normadas de división en dimensiones 1, 2, 4, 8.
- Eckmann (1943): productos vectoriales en $\mathbb{R}^n$ solo existen para $n = 1, 3, 7$.
- Atiyah, Bott y Shapiro (1964): módulos de Clifford y periodicidad de Bott.
- Hestenes (1966, 1986): álgebra de espacio-tiempo como lenguaje de la física.
- Doran y Lasenby (2003): álgebra geométrica para físicos (Cambridge).
- Lounesto (2001): álgebras de Clifford y espinores (Cambridge).
- Adams (1960): campos vectoriales en esferas; confirma Hurwitz vía K-teoría.
- Molina (2024a): el determinante como fuente del término cúbico en flujos gradiente matriciales.
  DOI: 10.5281/zenodo.20752208

---

## 9. Conclusiones

A partir de tres axiomas estructurales — estructura de atributos SAIR (A1), producto geométrico (A2) y
evolución suave continua (A3) — el álgebra de Clifford real $\mathrm{Cl}_{3,1}$ emerge como teorema
estructural más que como postulado geométrico. La cadena de derivación es:

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
