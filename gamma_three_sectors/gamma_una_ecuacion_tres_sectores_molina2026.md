---
title: "Γ: una ecuación de movimiento, tres sectores"
subtitle: "Correspondencias estructurales con Newton, Navier-Stokes, Maxwell y Schrödinger"
author: "Henry Molina · Investigador independiente, Bogotá, Colombia · henrymolina@gmail.com"
date: "Julio 2026"
---

DOI: 10.5281/zenodo.21496578  

*Manuscrito autocontenido más allá del teorema algebraico del paper compañero (Molina 2026,
"Spacetime Algebra as a Theorem"), que este artículo reutiliza sin re-derivar. Las verificaciones
numéricas citadas a lo largo del texto están en `code/` (ver Anexo B) y en
`models/calcs/brainstorming/` para los cálculos exploratorios adicionales.*

**Convención de notación.** Cada afirmación va marcada con dos etiquetas independientes. La
primera nombra el **registro**: 〔DEF〕 definición, 〔TEO〕 teorema o lema, 〔CE〕 correspondencia
estructural (isomorfismo o relabeling algebraico con un objeto físico conocido, no un teorema
físico nuevo), 〔IF〕 hallazgo/hipótesis en investigación, 〔A〕 afirmación aún no cerrada. La
segunda, entre corchetes, nombra el **grado de certeza**: [D] demostrado analíticamente, [V]
verificado numéricamente (sin demostración analítica cerrada), [A] abierto/no resuelto, [F]
frontera fuera del alcance de este paper. Por ejemplo, 〔TEO〕[D] es un teorema con demostración
completa; 〔CE〕[V] es una correspondencia estructural confirmada por verificación numérica, no
por una prueba analítica de que la correspondencia sea exacta en general.

# Resumen

Este paper hace tres cosas en un solo argumento. Primero, deriva —no postula— por qué la
configuración de cualquier unidad dinámica operativa (UDO) vive en $M_4(\mathbb{R})$
dados dos axiomas mínimos (la ontología SAIR y el producto geométrico como ley de acoplamiento)
más un criterio de minimalidad hecho explícito: el teorema de Hurwitz/Eckmann fuerza la dimensión, el álgebra de Clifford
$\mathrm{Cl}_{3,1}$ queda fijada por la firma del símbolo de la ecuación de movimiento, y la
norma de Frobenius emerge como la única métrica compatible con esa estructura. Segundo, muestra
que la matriz de acoplamiento $\Gamma$, sometida a la dinámica de gradiente de un potencial
$P(\Gamma,\rho)$, se organiza en tres sectores separados por una sola condición topológica
—$\mathrm{sign}(\det\Gamma)$— y que el cruce de esa frontera es una bifurcación matemáticamente
rigurosa (teorema $\Gamma\to\xi$), no una observación cualitativa. Tercero, recorre el atlas de
recuperaciones dinámicas resultante: Newton, Navier-Stokes, Maxwell libre y Schrödinger libre
como correspondencias estructurales cerradas y verificadas; y, para el régimen linealizado de
Einstein en gauge armónico, separamos con cuidado un hecho de relatividad general estándar
—$\nabla^2\Phi=4\pi G\rho$ atravesado sin ajustar ningún factor por la maquinaria propia del
programa— de la restricción **condicional** que es específica de GSF: *si* la correspondencia
$\Gamma_s\sim\bar h_{\mu\nu}$ se sostiene, el coeficiente de acoplamiento a materia queda
forzado, no es ajustable. Para el régimen no lineal (ecuaciones de
Einstein completas) reportamos el estado real del programa: dos ingredientes cerrados de la ruta
termodinámica de Jacobson, un tercero acotado con precisión pero abierto, y un hallazgo positivo
reciente sobre el sector de masa (construcción tipo dRGT con métrica de referencia $f=\eta$) que
reproduce Fierz-Pauli exacto a orden cuadrático. El criterio de éxito de este paper no es la
predicción de física nueva: es que un solo objeto algebraico, con una sola ecuación de
movimiento, organiza correctamente cuatro siglos de física bajo condiciones precisas y
verificables — con las fronteras nombradas donde el programa aún no cierra.

---

# 1. Fundamento — por qué $\Gamma \in M_4(\mathbb{R})$

## 1.1 Los dos axiomas

**〔DEF〕 A1 (SAIR — ontología).** Cualquier unidad dinámica se caracteriza por cuatro atributos
intrínsecos: **S** (escalar, grado 0 — *qué es*, esencia) y **A, I, R** (vectores, grado 1 —
*qué puede*, potencia; *qué hace*, acto; *contexto*, relación). Esta es una descomposición
mínima postulada, no derivada de una física previa — es aristotélica en espíritu, y se lee en
tercera persona (domain-neutral), no como fenomenología psicológica.

**〔DEF〕 A2 (producto geométrico — fuerza/campo).** La dinámica de una UDO está gobernada por el
**producto geométrico** de sus atributos. En el álgebra geométrica $G(3)$, el producto de dos
elementos de grado 1 se descompone canónicamente en una parte simétrica de grado 0 y una
antisimétrica de grado 2: $uv = u\cdot v + u\wedge v$. Aplicado a SAIR, esto da **Fuerza**
$F=S\cdot A$ (simétrica) y **Campo** $\mathcal{F}=I\wedge R$ (antisimétrica, dual de Hodge del
producto cruz $I\times R$). Esta descomposición fuerza/campo no es un postulado adicional — es
consecuencia algebraica automática de A2 en $G(3)$. El único postulado genuino de A2 es: *la
dinámica usa el producto geométrico*.

**〔IF〕 Criterio de UDO genuina — la hipótesis falsable del programa.** A1+A2 fijan qué es *el
contenedor* algebraico; no garantizan que un sistema dado lo llene. La hipótesis de trabajo de todo
el programa, hecha explícita aquí para que sea falsable, es más fuerte que "existe un candidato
vectorial": **una UDO/UoC se caracteriza por los cuatro atributos SAIR de forma intrínseca, con
Fuerza y Campo inherentes, y con una cinemática y una dinámica caracterizables** — es decir, si
$S,A,I,R$ existen genuinamente (no como relabeling de una variable cualquiera) y $F,\mathcal F$ son
inherentes al sistema (no impuestos), entonces el sistema exhibe la cinemática/dinámica que la EOM
de §4 predice para su sector. El contraejemplo que falsificaría esto no es un dominio *sin*
candidato vectorial (eso simplemente dice que el contenedor no aplica ahí, ver §8.1) — es un
dominio *con* SAIR y F/E genuinamente detectables que, sin embargo, no siga la cinemática/dinámica
característica de su sector. Ningún caso así se ha encontrado hasta ahora en los dominios resueltos
(§3, §5); no se ha buscado sistemáticamente uno tampoco — queda como criterio de falsación
explícito, no como resultado.

Todo lo que sigue en esta sección es una cadena de cuatro lemas — cada uno una consecuencia
forzada de A1+A2, no una elección adicional.

## 1.2 Lema 1 (dimensión) — Hurwitz fuerza dim 3

〔TEO〕[D]. Por A2, el Campo es $\mathcal F=I\wedge R\in\Lambda^2(\mathbb R^d)$, un bivector de
dimensión $\binom{d}{2}$ — todavía no un producto cruz: eso hay que ganarlo. Para que la UDO sea
**cerrada** (que $\mathcal F$ pueda acoplar de vuelta con el atributo de grado 1 $A$ sin introducir
un objeto de rango mayor que los de A1), el espacio del Campo y el espacio de atributos deben ser
isomorfos como espacios vectoriales: $\binom{d}{2}=d\Rightarrow d(d-1)=2d\Rightarrow d=3$ (la única
solución no trivial). Ese isomorfismo *es* la dualidad de Hodge $\star:\Lambda^2(\mathbb R^3)
\xrightarrow{\sim}\mathbb R^3$, que convierte $\mathcal F=I\wedge R$ en el producto cruz
$I\times R$ — la identificación "Campo = producto cruz" es la **conclusión** de la clausura, no su
punto de partida. Solo entonces entra Hurwitz, como confirmación de consistencia: por el teorema de
Eckmann/Hurwitz, un producto cruz vectorial ($V\times V\to V$, bilineal, antisimétrico, con
$|u\times v|^2=|u|^2|v|^2-(u\cdot v)^2$) existe únicamente en dimensión 1, 3 o 7 —equivalente a
la existencia de un álgebra normada de división de dimensión $n+1$: $\mathbb{R},\mathbb{C},
\mathbb{H},\mathbb{O}$—, y verifica que $d=3$ efectivamente admite uno no degenerado; Hurwitz no
es la fuente de la derivación, la clausura lo es (Hurwitz por sí solo tampoco descartaría $d=1$ ni
$d=7$, que la clausura sí descarta). La dimensión 1 es degenerada (el producto cruz se anula); la
dimensión 2 da un escalar, no un vector. Quedan exactamente dos ramas no triviales:

- **Dim 3 (rama $\mathbb{H}$):** producto cruz único $\Rightarrow$ $A,I,R$ = base ortonormal de
  $\mathbb{R}^3$. La rama espacio-temporal — donde vive toda la física de este paper.
- **Dim 7 (rama $\mathbb{O}$):** producto cruz octoniónico $\Rightarrow$ una realización interna/
  atemporal, candidata a estructura de color/generaciones (frontera abierta, fuera de alcance
  aquí).

*Por qué exactamente tres atributos vectoriales* se reduce a la clausura $\binom{d}{2}=d$, no a
Hurwitz — Hurwitz confirma que $d=3$ funciona, la clausura es lo que lo fuerza. No es una elección.

## 1.3 Lema 2 (álgebra) — $A,I,R$ generan $\mathrm{Cl}_{3,0}=G(3)$

〔TEO〕[D]. En dimensión 3, los tres vectores de grado 1 (linealmente independientes) generan la
totalidad del álgebra geométrica $G(3)$: $8=2^3$ dimensiones — grado 0 = $S$, grado 1 = $A,I,R$,
grado 2 = los bivectores (Campo, vía dual de Hodge), grado 3 = pseudoescalar. Ningún quinto
generador de grado 1 hace falta.

## 1.4 Lema 3 (tiempo) — la dinámica añade una cuarta dirección

〔TEO〕[D]. La ecuación de movimiento (§4) es de segundo orden; su parte principal es el operador
de onda $\Box\Gamma=\ddot\Gamma-c^2\nabla^2\Gamma$. La cuarta dirección (temporal) es
$\gamma_0=\partial_\tau$ —la evolución misma de la UDO—, no un quinto atributo. El rango de
$\{A,I,R\}$ es exactamente 3; $S$ es de grado 0 (escalar, no vector); promover cualquiera de
$A,I,R$ a una cuarta dirección independiente rompería la simetría y mal-categorizaría el
atributo. La cuarta dirección tiene que venir de fuera del conjunto de atributos, y la dinámica
—que el marco ya posee— la provee.

## 1.5 Lema 4 (firma) — Lorentz se lee, no se postula

〔TEO〕[D]. El símbolo de $\Box$ bajo transformada de Fourier ($\partial_\tau\to i\omega$,
$\nabla\to ik$) es $-\omega^2+c^2|k|^2$ — exactamente la forma cuadrática de Minkowski, firma
$(3,1)$. La firma Lorentziana **no se postula: se lee** de la ecuación de movimiento. El álgebra
de Clifford real de esa firma es $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$: verificado que la
representación real $4\times4$ satisface $\{\gamma_\mu,\gamma_\nu\}=2\eta_{\mu\nu}$ con
$\gamma_0^2=-1$ forzado por realidad y $\gamma_i^2=+1$.

## 1.6 Teorema (Γ) — la configuración está forzada

**〔TEO〕[D] Teorema.** *Dados A1 y A2, la configuración de una UDO es forzosamente*
$$\boxed{\;\Gamma \;=\; \Gamma_s \oplus \Gamma_a \;\in\; M_4(\mathbb{R}) \;=\; \mathrm{Cl}_{3,1}\;}$$
*donde $\Gamma_s=\mathrm{Gram}(S,A,I,R)$ (sector Fuerza, simétrico, 10 componentes) es el único
mapa canónico desde el álgebra, y $\Gamma_a$ (sector Campo, antisimétrico, 6 componentes) se
descompone en magnético ($I\wedge R$, espacio-espacio) y eléctrico ($\partial_\tau\wedge\nabla$,
espacio-tiempo).*

**Por qué $\Gamma$ y no otra cosa.** Una métrica (forma simétrica) carga solo la Fuerza; una
forma simpléctica (antisimétrica) carga solo el Campo. $\Gamma=\Gamma_s\oplus\Gamma_a$ es el
único objeto **mínimo** que carga ambos simultáneamente. La estructura real $4\times4$
($\mathrm{Cl}_{3,1}$) queda forzada por: dimensión 3 (Lema 1) + tiempo como evolución (Lema 3) +
realidad (Lema 4).

*Precisión honesta sobre "mínimo".* La palabra "mínimo" en el párrafo anterior es un criterio
adicional, no una consecuencia de A1+A2 por sí solos: A1+A2 hacen fértil y coherente cargar
Fuerza y Campo en un solo objeto, pero no excluyen formalmente un objeto *más grande* que también
lo haga (por ejemplo, con estructura redundante). "Forzado" en este teorema significa *forzado
dado el criterio de minimalidad*, no forzado de forma absoluta e independiente de ese criterio —
minimalidad no es lo mismo que necesidad lógica. Este es el único punto de la cadena donde un
criterio estético/de economía (y no solo álgebra) entra en juego; se nombra aquí explícitamente
en vez de dejarlo implícito en la palabra "único".

**Proposición (Frobenius, [D]).** La métrica en el espacio de configuraciones es la norma de
Frobenius, $\langle A,B\rangle=\tfrac14\mathrm{Tr}(A^\top B)$ — el producto interno canónico de
Clifford ($\langle A\tilde B\rangle_0$, componente escalar del producto geométrico con el
reverso). Por el lema de Schur aplicado a la acción de $\mathrm{Spin}(3,1)$ sobre la
descomposición por grados, cualquier forma bilineal $\mathrm{Spin}(3,1)$-invariante es
proporcional a esta traza en cada bloque de grado; la condición de submultiplicatividad iguala
las constantes entre bloques. Frobenius no es una elección posterior a la construcción de
$\Gamma$ — está determinada por A2.

Los dos axiomas remanentes (A1: SAIR es la descomposición mínima de cualquier descripción
dinámica; A2: la dinámica usa el producto geométrico) son el fundamento genuino de la cadena —
no se derivan de nada más profundo, y no deberían. Con ellos, todo lo demás —dimensión, álgebra,
tiempo, firma, métrica, y la propia existencia de $\Gamma$— es teorema, no postulado.

---

# 2. Dinámica de los sectores — el cruce $\det\Gamma=0$ es una bifurcación

## 2.1 El potencial y sus invariantes

**〔DEF〕.** La dinámica de $\Gamma$ está gobernada por un potencial que depende de exactamente
dos invariantes:
$$P(\Gamma,\rho) = \|\Gamma\|_F^2 + \mu(\rho)\det\Gamma + \beta\|\Gamma\|_F^4, \qquad \beta\geq|\mu|/16$$
La cota $\beta\geq|\mu|/16$ (AM-GM) no es una elección: es la condición para que $P$ esté
acotado por debajo en presencia de un $\mu\det\Gamma$ de cualquier signo.

**〔TEO〕[D] (fórmula exacta de la curvatura).** Para $\Gamma_0=\mathrm{diag}(\lambda_1,\ldots,
\lambda_4)$ y una fluctuación antisimétrica en la dirección $(i,j)$ (entradas $(i,j)$ y $(j,i)$,
resto cero), la curvatura normalizada del potencial en esa dirección es *exactamente*
$$m_{\rm eff}^2 = 2 + \mu\frac{\det\Gamma_0}{\lambda_i\lambda_j} + 4\beta\|\Gamma_0\|_F^2$$
*Demostración.* Con $E^{ij}$ el generador antisimétrico unitario de esa dirección
($\|E^{ij}\|_F^2=2$) y $\Gamma(\varepsilon)=\Gamma_0+\varepsilon E^{ij}$: $\|\Gamma(\varepsilon)
\|_F^2=\|\Gamma_0\|_F^2+2\varepsilon^2$ (el término lineal se anula, $\Gamma_0$ diagonal y
$E^{ij}$ fuera de diagonal); el determinante, restringido al bloque $2\times2$ perturbado,
es $\det\Gamma(\varepsilon)=(\lambda_i\lambda_j+\varepsilon^2)\prod_{k\neq i,j}\lambda_k=
\det\Gamma_0(1+\varepsilon^2/\lambda_i\lambda_j)$ (cálculo directo del bloque, no una fórmula
citada); y $\beta\|\Gamma(\varepsilon)\|_F^4=\beta(\|\Gamma_0\|_F^2+2\varepsilon^2)^2$. Sumando
las tres contribuciones de segundo orden en $\varepsilon$ y dividiendo por $\|E^{ij}\|_F^2=2$ da
la fórmula. Verificada simbólicamente sin aproximar
(`models/calcs/brainstorming/papers/draft_atlas/verificacion_cota_amgm.py`). $\blacksquare$

**Hallazgo honesto: la cota $\beta\geq|\mu|/16\Rightarrow m_{\rm eff}^2\geq2$ para *todo*
$\Gamma_0$ diagonal, tal como se enunciaba en el material previo del programa, es FALSA.**
Contraejemplo explícito, verificado simbólicamente (mismo script): con $\lambda_i=\lambda_j=
\delta\to0$ (el par perturbado) y $\lambda_k=\lambda_l=t$ (el otro par, fijo), $\det\Gamma_0/
(\lambda_i\lambda_j)\to t^2$ mientras $\|\Gamma_0\|_F^2\to2t^2$ — ambos términos escalan igual
con $t$, y para $\mu<0$ con $\beta=|\mu|/16$ (el caso límite de la cota), $m_{\rm eff}^2\to
2+t^2\mu/2\to-\infty$ cuando $t\to\infty$. El paso que falla en la demostración original
(no reproducida aquí por ser incorrecta) es acotar $\|\Gamma_0\|_F^2$ como si siempre controlara
el cociente $\det\Gamma_0/(\lambda_i\lambda_j)=\lambda_k\lambda_l$ relevante — pero
$\|\Gamma_0\|_F^2$ puede crecer proporcionalmente a $\lambda_k\lambda_l$ sin que la cota
$\beta\geq|\mu|/16$ (una razón fija, sin escala) alcance a compensarlo.

**Lo que sí se verificó:** esta configuración contraejemplo **no es un equilibrio genuino**
($\nabla P=0$) para ningún $\beta\geq0$ admisible — resolviendo $\nabla P=0$ exactamente en el
límite $\delta\to0$ se obtiene $\beta=-1/4$, fuera del dominio físico.

**〔TEO〕[D] (versión restringida a equilibrios — CERRADA, jul-08 2026).** *Para $\beta\geq|\mu|/16$,
el único equilibrio de $\nabla P=0$ con $\Gamma_0$ diagonal y $\det\Gamma_0\neq0$ es $\Gamma_0=0$
— es decir, no hay ningún equilibrio no trivial en ninguno de los dos sectores ($\det>0$ o
$\det<0$).*

*Demostración.* Para cualquier equilibrio con todo $\lambda_i\neq0$, la identidad
$$\lambda_i\cdot\partial_{\lambda_i}P - \lambda_j\cdot\partial_{\lambda_j}P = 2(\lambda_i^2-\lambda_j^2)(2\beta\|\Gamma_0\|_F^2+1)$$
(verificada por expansión directa, no una fórmula citada) se anula en el equilibrio. El segundo
factor, $2\beta\|\Gamma_0\|_F^2+1$, es **siempre positivo** para $\beta\geq0$ (suma de un término
no negativo más 1) — nunca puede anularse. Por tanto $\lambda_i^2=\lambda_j^2$ para todo $i,j$:
**todo equilibrio no trivial tiene los cuatro $|\lambda_i|$ iguales** a un valor común $t>0$, sin
excepción — no hay equilibrios "completamente asimétricos" que buscar. Quedan solo dos familias,
por la paridad del número de signos negativos entre los cuatro $\lambda_i=\pm t$:

- **Número par de signos negativos** ($\det\Gamma_0=+t^4$): la ecuación de equilibrio da
  $t^2=-2/(\mu+16\beta)$, que requiere $\mu+16\beta<0$. Pero $\beta\geq|\mu|/16\Rightarrow16\beta
  \geq|\mu|\geq-\mu\Rightarrow\mu+16\beta\geq0$ — **contradicción**, sin solución real.
- **Número impar de signos negativos** ($\det\Gamma_0=-t^4$): la ecuación da $t^2=2/(\mu-16\beta)$,
  que requiere $\mu>16\beta$. Pero $\beta\geq|\mu|/16\Rightarrow16\beta\geq|\mu|\geq\mu\Rightarrow
  \mu\leq16\beta$ — **contradicción**, sin solución real.

Ninguna de las dos familias (que agotan todos los patrones de signo posibles, salvo permutación)
tiene solución real cuando $\beta\geq|\mu|/16$. $\blacksquare$ Verificado con sympy, sin
aproximar (`models/calcs/brainstorming/papers/draft_atlas/cota_amgm_restringida_equilibrios.py`).

**Lo que esto significa, con honestidad completa.** La afirmación original de Theorem 3.1
("$P$ es estable en todos los sectores, incluyendo $\det\Gamma<0$") resulta **vacuamente cierta**
en el sentido más fuerte posible: para $\beta\geq|\mu|/16$ **no hay ningún equilibrio viviendo en
$\det\Gamma\neq0$** — ni en $\det>0$ ni en $\det<0$ — así que no hay nada que "desestabilizar". La
dinámica oscilatoria observada en el sector $\det<0$ (§2.2) no puede entenderse, en este régimen,
como oscilación *alrededor de un equilibrio estático* — debe ser genuinamente transitoria/dinámica
desde el inicio, o vivir en la región complementaria $\beta<|\mu|/16$ (donde sí existen los
equilibrios no triviales — incluyendo $\Gamma_\ast(\sigma)$ de §2.3, que requiere $\mu>16\beta$, o
su análogo con signo opuesto). Esto no requiere ni invoca termodinámica de no-equilibrio: es un
resultado completo dentro del flujo gradiente puro — simplemente aclara *dónde* viven los
equilibrios no triviales (fuera de esta región), no que dejen de ser equilibrios genuinos.

## 2.2 Los sectores, contados por la firma — teorema de completitud

〔TEO〕[D]. Un primer conteo, puramente topológico, es este: $\det:M_4(\mathbb{R})\to\mathbb{R}$ es
continua, su conjunto de ceros es codimensión 1, y el complemento tiene exactamente dos componentes
conexas abiertas; sumando la frontera, tres sectores. **Ese conteo es correcto para
$M_4(\mathbb{R})$ pero no es el clasificador que la física necesita**, y conviene decir por qué
antes de usarlo.

El tipo de la ecuación de movimiento —y con él la buena postura— lo determina la **parte simétrica**
$\Gamma_s$, no el signo de $\det\Gamma$. Y sobre $\mathrm{Sym}(4,\mathbb{R})$ el invariante correcto
es la **inercia** $(n_+,n_0,n_-)$, que por la ley de Sylvester es un invariante *completo* de
congruencia y, por continuidad de los autovalores, *localmente constante*. Se sigue:

> **Teorema (completitud de sectores).**
> **(i)** *(Sylvester)* La inercia particiona $\mathrm{Sym}(4,\mathbb{R})$ en exactamente **15**
> clases —finito y exhaustivo por construcción—; el subconjunto no degenerado
> $\mathrm{Sym}^*(4,\mathbb{R})$ tiene **cinco** componentes conexas, una por clase:
> $(4,0)$, $(3,1)$, $(2,2)$, $(1,3)$, $(0,4)$.
> **(ii)** Módulo la convención de signo global $(n_+,\cdot,n_-)\sim(n_-,\cdot,n_+)$ quedan **tres**
> regímenes: elíptico, hiperbólico y ultrahiperbólico.
> **(iii)** *(Hadamard)* De los tres, **exactamente uno** —el Lorentziano $(3,1)$— sustenta un
> problema de Cauchy bien puesto. Las clases degeneradas ($n_0\ge1$, $\det\Gamma_s=0$) forman la
> frontera de codimensión $\ge1$ entre ellas.

| Firma de $\Gamma_s$ | $\det\Gamma_s$ | Tipo de EDP | Régimen |
|---|:---:|---|---|
| $(4,0)$ *(y su espejo $(0,4)$)* | $>0$ | elíptico | equilibrio clásico: Newton, Stokes, Landau–Ginzburg |
| $n_0\ge1$ | $=0$ | degenerado (frontera) | onda sin masa, fotón, criticidad |
| $(3,1)$ *(y su espejo $(1,3)$)* | $<0$ | **hiperbólico bien puesto** | evolución relativista, $\Gamma_a$ activo, tipo Hopf |
| $(2,2)$ | $>0$ | ultrahiperbólico | **excluido**: dos direcciones temporales, Cauchy mal puesto |

**Por qué el signo de $\det$ no basta.** Como $\det\Gamma_s=(-1)^{n_-}\prod|\lambda_i|$, el signo
solo registra la *paridad* de $n_-$: alterna $+,-,+,-,+$ a lo largo de los cinco estratos. Por eso
$\det>0$ es la **unión** de $(4,0)$, $(2,2)$ y $(0,4)$ —mete en la misma casilla el equilibrio
clásico y el caso ultrahiperbólico patológico— y $\det<0$ la unión de $(3,1)$ y $(1,3)$. El signo de
$\det$ no separa las componentes: las mezcla. Es la sombra más gruesa de la inercia (Corolario 8.1
de Paper C), útil como coordenada pero insuficiente como clasificador.

Más aún, $(4,0)$ y $(2,2)$ **no son adyacentes**: pasar de una a otra exige que *dos* autovalores
crucen cero, uno a la vez, de modo que todo camino atraviesa primero el estrato Lorentziano $(3,1)$.
La región patológica está separada de la clásica *por* la región relativista — estructura que el eje
$\det$ pliega y `fig_atlas_map.png` ahora despliega sobre el eje $n_-$.

*Verificado numéricamente* (`models/calcs/brainstorming/papers/draft_atlas/completitud_sectores_sylvester_hadamard_prueba.py`):
enumeración exhaustiva de las 15 clases; 20 000 matrices simétricas aleatorias, ninguna firma fuera
de la enumeración; y la imposibilidad de conectar $(4,0)$ con $(2,2)$ sin cruzar una degeneración
(el segmento recto y 100 caminos aleatorios con waypoint, todos cruzan).

**Estatus.** La parte (iii) —la unicidad de $(3,1)$ por buena postura— es el Lema 4 del paper
compañero sobre $\mathrm{Cl}_{3,1}$ (Molina 2026); este teorema la enmarca mostrando que además
*agota* las alternativas y les asigna significado físico. Lo que permanece 〔A〕 no es la
clasificación —cerrada, dado el $4$— sino la **completitud física**: que la física clásica se agote
en un único $\Gamma_s$ de $4\times4$, lo cual descansa en los Lemas 1–3 (dimensión), no en el conteo
de sectores.

## 2.3 El cruce como bifurcación — teorema $\Gamma\to\xi$

Lo anterior describe *dónde* viven los tres sectores. Lo que sigue establece que *cruzar* la
frontera $\det\Gamma=0$ no es una observación cualitativa post-hoc: es una bifurcación en el
sentido riguroso de la teoría de sistemas dinámicos, con formas normales explícitas.

**〔TEO〕[D] (reducción $\Gamma\to\xi$, codimensión 1, flujo gradiente).** Sea
$(\Gamma_\ast,\mu_\ast)$ un equilibrio de $\dot\Gamma=-\nabla P$ con un modo blando **simple**
(autovalor 0 simple del Hessiano $H_\ast$, resto del espectro acotado lejos de cero) y
transversalidad ($\tau=\langle V,\mathrm{adj}(\Gamma_\ast)^\top\rangle\neq0$, $V$ el autovector
del modo blando). *Por qué el modo simple no es un supuesto gratuito*: el potencial desnudo
($J=0$) depende solo de $\|\Gamma\|^2$ y $\det\Gamma$, invariantes bajo la acción ortogonal
bilateral $\Gamma\mapsto U\Gamma V^\top$ — es isótropo bajo $O(4)\times O(4)$, y sus
degeneraciones propias son por tanto *no genéricas* (la simetría continua produce clusters de
modos blandos). Un campo externo genérico $J$ (que entra linealmente, sin alterar el Hessiano)
rompe esa isotropía y hace simple el modo blando — es la formalización del forzamiento, no un
truco numérico. Bajo esa condición, existe, en un entorno, una variedad central 1-dimensional
$\Gamma=\Gamma_\ast+\xi V+h(\xi,\mu)$ sobre la cual la dinámica sigue siendo gradiente,
$\dot\xi=-\partial_\xi\Phi(\xi,\mu)$, reduciéndose a las formas normales estándar de
bifurcación:

- **Genérico** ($a_3\neq0$): pliegue (saddle-node), $\dot\xi=\alpha-c\xi^2$.
- **$\mathbb{Z}_2$-simétrico** ($a_3=0$): tridente (pitchfork), $\dot\xi=-a_2'\xi-\tfrac16
  a_4^{\rm eff}\xi^3$.

**El determinante es la fuente estructural del cúbico**: $a_3=\mu_\ast D^3\!\det(\Gamma_\ast)
[V^{\otimes3}]+24\beta\langle\Gamma_\ast,V\rangle+\cdots$, con el término del determinante como
única fuente cuando el modo blando es transverso a $\Gamma_\ast$. *La geometría de $\Gamma$ —su
determinante— fija el tipo de bifurcación, no el tamaño de $\Gamma$ (su norma).*

**〔TEO〕[V] (la línea AM-GM es la bifurcación).** Sobre el rayo simétrico $\det<0$,
$\Gamma_\ast(\sigma)=\sigma\,\mathrm{diag}(1,1,1,-1)$ (subespacio invariante exacto), el cuártico
efectivo reducido es $(16\beta-\mu)$; su cambio de signo —el pitchfork— ocurre exactamente en
$\mu=16\beta$, el mismo valor crítico que aparecía en la cota de Hessiano de §2.1 (ahí, sin
embargo, encontramos que la cota general no es demostrable como se pensaba — ver el hallazgo
honesto de §2.1; este resultado sobre el rayo invariante específico es independiente y sí está
verificado con equilibrios genuinos) y marca el cambio de orientación $\det>0\to\det<0$. La
coincidencia numérica entre ambos —el valor $\mu=16\beta$ apareciendo en dos cálculos distintos—
sigue siendo intrigante, pero ya no puede presentarse como "tres fenómenos convergiendo sin
parámetro libre" hasta que se resuelva el estatus de la cota de Hessiano general. Verificado
numéricamente, para el rayo invariante (`pieza1_teorema_4x4.py`,
`pieza1_reduccion_normal_forms.py`): modo blando simple (brecha 0.027), $a_3=5.09$ con
contribución estructural del determinante ($-11.67$), saddle-node entre equilibrios genuinos de
$\nabla P=0$.

**Alcance honesto.** La cúspide (codimensión 2, mismo flujo gradiente) y Bogdanov-Takens
(codimensión 2, requiere el fibrado tangente $(\Gamma,\dot\Gamma)$, no es corolario del teorema
anterior) están cerradas con certificado numérico, no con la misma demostración estándar. La
homoclínica y el caos del sector reactivo $\Gamma_a$ —donde vive el régimen activo/vital,
$\gamma_{\rm eff}\leq0$— son programa con reducción-modelo, no teorema cerrado: la reducción
rigurosa del espacio 16+16-dimensional al jerk reactivo, y la condición de Shilnikov global,
quedan como frontera 〔F〕 explícita.

---

# 3. Cinemática — la lectura SAIR por dominio

## 3.1 Diccionario por dominio

Cada dominio físico es el mismo objeto $\Gamma$, leído desde las variables observables propias
de esa física:

| Dominio | S | A | I | R | $\Gamma_a$ |
|---|---|---|---|---|---|
| Newton/Kepler | masa $m$ | aceleración $\mathbf a=\ddot{\mathbf x}$ (grado 1) | impulso $\mathbf p=m\mathbf v$ (grado 1) | posición $\mathbf r$ (grado 1) | $\mathbf L=\mathbf I\wedge\mathbf R=\mathbf p\wedge\mathbf r$ (derivado) |
| Navier-Stokes | presión $p$ | vel. fluido $\mathbf u$ (grado 1, con ambigüedad honesta — ver documento) | $\mathbf u$ | $\nabla$ | vorticidad $=I\wedge R=\nabla\times\mathbf u$ (identidad estándar, verificada simbólicamente) |
| Mec. estadística | $Z(\rho)$ | energías $\lambda_i(\Gamma_s)$ | fluctuación $\sigma^2$ | temperatura $1/\rho$ | $\sim0$ equilibrio |
| Maxwell libre | carga $\rho_q=0$ | corriente $\mathbf J$ (grado 1) | $\mathbf A_\mathrm{vec}$ (potencial vectorial) | $\nabla$ | $\mathbf B=I\wedge R=\nabla\times\mathbf A_\mathrm{vec}$ (misma identidad que NS); parte eléctrica $=\partial_\tau\wedge\nabla$ (mecanismo distinto) |
| Schrödinger | carga/masa $q$ | impulso $\mathbf p=m\mathbf v$ (grado 1) | impulso $\mathbf p$ (grado 1, $=$Newton corregido) | posición $\mathbf r$ (grado 1, $=$Newton) | $\mathbf L=\mathbf I\wedge\mathbf R$ (derivado); $E_n\cdot\hat I$ como invariante derivado, $\hat I=e_1e_2e_3$ |
| Firma Lorentz | energía en reposo $mc^2$ | 4-velocidad $u^\mu$ (grado 1) | impulso $p^\mu$ (grado 1) | 4-posición $x^\mu$ (grado 1) | $F_{\mu\nu}$, $\star^2=-1$ (los 4 ya eran grado 1 — este renglón no tenía el error) |
| Hopf/reactivo | tasa de crecimiento | capacidad reactiva | ⚠ discrepancia de dimensión (2D vs 3D), no resuelto | ⚠ ídem | $\omega_H$: la reducción a la forma normal vive en 2D, no encaja directo en el marco 3D de SAIR — ver `correccion_grado_I_R_todos_dominios.md` |

**Corrección fundacional (jul-11 2026), avance de esta ronda — ver
`brainstorming/physics/correccion_grado_I_R_todos_dominios.md`.** HM señaló que $I,R$ deben ser
**ambos grado 1** (vectores), con el Campo $\mathcal F=I\wedge R$ como bivector **derivado** — no
$I$=bivector y $R$=pseudoescalar directamente, como tenían las filas anteriores (excepto Firma
Lorentz, que ya estaba correcta). Corregido y verificado para Newton, Schrödinger (hereda Newton),
Navier-Stokes y Maxwell (estos dos últimos vía la identidad estándar $\mathrm{rot}=\nabla\wedge(\cdot)$,
con $R=\nabla$ jugando el mismo rol formal que $\partial_\tau$ en la parte eléctrica de Paper B).
Hopf/reactivo queda con una discrepancia estructural genuina (dimensión 2D de la forma normal vs.
3D exigido por SAIR), no resuelta por conveniencia. H₂O es el siguiente paso.

**Corrección (jul-11 2026).** La fila de Newton/Kepler se corrigió para coincidir con
`brainstorming/unification/release/pieza1_anexo_newton.md` §1.1, el mapeo ya revisado y usado en
el problema de tres cuerpos: $A$ debe ser la aceleración, no la velocidad (condición formal C5 —
$A$ debe ser invariante bajo boost galileano, y $\mathbf v\to\mathbf v+\mathbf v_0$ mientras
$\mathbf a=g(\mathbf r)$ no cambia), y $R$ ocupa el slot de pseudoescalar (grado 3, 1 dimensión),
no un vector — aquí, la energía específica orbital, no la posición.

**Tercera corrección (jul-11 2026) — Schrödinger.** La fila decía "masa $m$ / $\nabla\psi/\psi$ /
$\hbar\omega$ / $|\psi\rangle$", una correspondencia de forma sin rigor. `pieza3_sector_cuantico.md`
§1 ya prueba un **Teorema de la asignación cuántica**: bajo condiciones C1–C5 en $\mathrm{Cl}_{3,0}$
restringido a $\det=0$, la asignación $S=q$, $A=\mathbf p$, $I=\mathbf L=\mathbf r\wedge\mathbf p$,
$R=E_n\cdot I$ (el pseudoescalar $I=e_1e_2e_3$, $I^2=-1$, es la "$i$" de Schrödinger sin postularse)
es la **única** que las satisface — el mismo SAIR de Newton, en el sector $\det=0$. Corregido.

**Segunda corrección (jul-11 2026) — Navier-Stokes.** La fila también se corrigió para coincidir
con `brainstorming/ds/gamma_a_transporte_navier_stokes.md` (estudios 01–05, [D]): la asignación de
slots **no es fenomenológica, está forzada por covarianza rotacional** — cada observable ocupa el
grado de Clifford de su rango tensorial, verificado que los rotores preservan grado. Presión
(escalar) → grado 0 ($S$); velocidad (vector) → grado 1 ($A$); **vorticidad → grado 2 ($I=\Gamma_a$,
el mismo sector que ya se lista en la columna $\Gamma_a$, ahora consistente con $I$ en vez de
aparecer duplicada informalmente)**; helicidad $\mathbf u\cdot\boldsymbol\omega$ (pseudoescalar) →
grado 3 ($R$). La fila anterior (densidad/vel./vorticidad/deformación) no reflejaba esta derivación
— la deformación $\nabla\mathbf u$ no es un slot SAIR sino el tensor completo del que $A$ (vector) e
$I$ (vorticidad) se extraen por descomposición simétrica/antisimétrica. Además, la ecuación de
Navier-Stokes misma (incluyendo el término de autoadvección $(\mathbf u\cdot\nabla)\mathbf u$) está
**derivada, no postulada**: la covarianza galileana fuerza $\partial_t\to D/Dt=\partial_t+(\mathbf
u\cdot\nabla)$ (verificado simbólicamente que solo $D/Dt$, no $\partial_t$ solo, es invariante de
forma bajo boost). Euler emerge como el límite conservativo $\gamma\to0$. El único residuo abierto
es la asignación de slots matriz→vector (A-1), compartida con Stokes y con el weld
Clifford→$M_4(\mathbb R)$ general — un hueco fundacional, no específico de fluidos.

**Dos lecturas de SAIR, no en competencia.** El axioma fundacional A1 (§1.1) lee $A,I,R$ como los
**tres generadores abstractos de grado 1** que fuerzan $G(3)$ (Lema 1/2: por qué $d=3$, sin
comprometerse aún con qué variable física ocupa cada dirección). La tabla de este dominio lee
$A,I,R$ ya **instanciados** en un dominio físico concreto — y ahí $I$ y $R$ pueden aparecer en
grados más altos (bivector, pseudoescalar) porque lo que se tabula es el contenido físico que
llena cada slot de la construcción de $\Gamma$ (Gram/wedge de A1), no los tres generadores
crudos de grado 1 de la derivación abstracta. Son dos niveles de descripción del mismo objeto, no
dos mapeos alternativos — pero conviene no leer esta tabla como si extendiera A1 literalmente
grado por grado.

**Lectura práctica.** Para construir $\Gamma$ de un sistema dado: identificar $S$ (variable
escalar de estado), $A$ (capacidad de acción), $I$ (impulso o ciclo propio), $R$ (acoplamiento al
entorno). Su producto geométrico —no cualquier matriz $4\times4$ arbitraria— es el $\Gamma$ del
atlas.

## 3.2 Relaciones de dispersión por sector

〔CE〕. Linealizando $\Gamma(t,x)=\Gamma_0+\delta\Gamma\,e^{i(kx-\omega t)}$ alrededor de un
equilibrio, la tripartición de sectores da tres ramas de dispersión distintas:

| Sector | Dispersión $\omega(k)$ | Régimen no-relativista |
|---|---|---|
| $\det\Gamma>0$ | $\omega^2=c^2k^2+m_{\rm eff}^2$ | $\omega\approx m_{\rm eff}+c^2k^2/2m_{\rm eff}$ (Newton) |
| $\det\Gamma=0$ | $\omega=ck$ | — (sin masa por construcción) |
| $\det\Gamma<0$ (activo) | $\omega=\pm\omega_{\rm Hopf}(k)$ | oscilación sin crecimiento |

El análisis espectral completo (fotografía estática vs. película del propagador completo por
sector, con las figuras correspondientes) se presenta en el Anexo D.

---

# 4. La ecuación de movimiento

**〔DEF〕.**
$$\boxed{\ddot\Gamma + \gamma\dot\Gamma - c^2\nabla^2\Gamma + \nabla_\Gamma P(\Gamma,\rho) = N(t)}$$
$$\nabla_\Gamma P = \underbrace{2\Gamma}_{\text{elástico}} + \underbrace{\mu(\rho)\,\mathrm{adj}(\Gamma)^\top}_{\text{conoce el sector}} + \underbrace{4\beta\|\Gamma\|_F^2\Gamma}_{\text{amarra la norma}}$$

El término $\mu\,\mathrm{adj}(\Gamma)^\top=\mu\det(\Gamma)\Gamma^{-1}$ es el que conoce el
sector: se anula en $\det\Gamma=0$ (linealizando exactamente la EOM ahí), estabiliza en
$\det\Gamma>0$, y es el motor de la dinámica reactiva en $\det\Gamma<0$ con $\mu<0$. Es el mismo
Lagrangiano para todos los casos que siguen — cero parámetros nuevos por dominio.

---

# 5. Recuperaciones dinámicas

Cada caso sigue el protocolo de cinco pasos: (1) definir el $\Gamma$ del caso; (2) análisis
espectral (modo crítico, signo de $\det$); (3) traer la EOM sin re-derivarla; (4) reducir
proyectando sobre el modo del paso 2; (5) clasificar y nombrar la frontera.

*Nota de registro:* siguiendo la guía de estilo del programa, las identificaciones "esto **es**
Newton/Maxwell/Schrödinger" son correspondencias estructurales 〔CE〕 —isomorfismo o relabeling
algebraico con un objeto físico conocido—, no teoremas físicos nuevos. El aporte verificable es
el mapeo desde SAIR/$\Gamma$; la reducción algebraica interna (proyección, linealización) sí es
matemática de teorema y se marca aparte donde corresponde.

## 5.1 Newton (〔CE〕[D], $\det\Gamma>0$)

*En el sector $\det\Gamma>0$ con $\Gamma_s\succ0$ y $\|\Gamma_a\|\ll\lambda_{\min}(\Gamma_s)$
(condición de carga — Observación: no se sigue solo de $\det\Gamma>0$), la proyección de
Lyapunov-Schmidt sobre el modo blando $\xi$ da*
$$m_{\rm eff}\ddot\xi = F_{\rm eff} - \partial_\xi V_{\rm eff} - \gamma m_{\rm eff}\dot\xi$$
*que en el límite $\gamma\to0$ tiene la forma de la segunda ley de Newton.* La proyección misma
es 〔TEO〕[D] (Lyapunov-Schmidt, Papers A/B); la identificación con Newton es la correspondencia.
Verificado numéricamente por sector (`calc1_newton_limit.py`): $a_1>0$ estable en $\det\Gamma>0$,
$a_1\to0$ en la frontera, $a_1<0$ señalando que el modo diagonal deja de ser el modo blando
correcto en $\det\Gamma<0$.

## 5.2 Navier-Stokes (〔CE〕[D], $\det\Gamma>0$)

$\Gamma_s$ corresponde a la tasa de deformación (strain rate); $\Gamma_a$, a la vorticidad.
Dispersión $\lambda\sim k^2$ (difusión), con la amplificación no-modal del operador linealizado
$\mathcal{A}=\begin{psmallmatrix}0&I\\-\mathcal{L}_{\bar\Gamma}&-\gamma I\end{psmallmatrix}$
(genéricamente no normal) dando $G_{\max}\sim\mathrm{Re}^2$ — consistente al orden de magnitud
con $\mathrm{Re}_c^{\rm obs}=2040$ de Poiseuille en tubería (PR-22).

## 5.3 Maxwell libre (〔CE〕[D], $\det\Gamma=0$)

Con $\det\Gamma\to0$: $\mathrm{adj}(\Gamma)\to0$ y la EOM se linealiza exactamente —este paso es
〔TEO〕[D], álgebra directa. Con $\Gamma_a=F_{\mu\nu}$ (bivector de grado 2) y $\gamma\to0$, la EOM
linealizada tiene la forma
$$\partial_\mu F^{\mu\nu}=0, \qquad dF=0$$
que corresponde a Maxwell libre y a la identidad de Bianchi. La identidad de Bianchi sale de la
antisimetría de $\Gamma_a$ ($d^2=0$), no de una simetría de gauge postulada. La masa del fotón
$m_\gamma=0$ es automática: $\det\Gamma=0$ fuerza el modo nulo.

## 5.4 Schrödinger (〔CE〕[D]+[V] para partícula libre, $\det\Gamma=0$)

**Estado real, corregido.** Este caso tuvo una cita histórica incorrecta ("verificado a
$\sim10^{-10}$" sin script de respaldo), ya corregida. La cadena verificada: $\det\Gamma\to0^+$
linealiza la EOM $\Rightarrow$ Klein-Gordon, $(\Box+m^2)\Gamma=0$ con $m^2=1$ (unidades naturales)
$\Rightarrow$ en el límite no-relativista ($\Gamma=e^{-imt}\Psi$, $|\partial_t\Psi|\ll m|\Psi|$),
$i\partial_t\Psi=-\nabla^2\Psi/2m$. La complexificación correcta es la proyección estándar de
frecuencia positiva de un campo de Klein-Gordon real —**no** $\Psi=\Gamma_s+i\Gamma_a$, que falla
por incompatibilidad dimensional ($\mathrm{Sym}(4)$ es 10-dim, $\mathrm{Antisym}(4)$ es 6-dim).
Verificado con tres pasos independientes (Euler-Lagrange simbólico, dispersión Klein-Gordon
numérica, reducción wavepacket-a-envolvente con error decreciente en $dk/m$):
`schrodinger_from_gsf_eom_verificacion.py`.

**Frontera nombrada, honesta.** El caso con potencial externo $V(x)$ general —acoplando
$V(x)$ como masa efectiva posición-dependiente, $m^2\to m^2+2mV$— tiene la reducción analítica
correcta (verificada para el oscilador armónico), pero la verificación numérica independiente no
cerró: un error residual no diagnosticado en el tiempo disponible. Queda 〔A〕, no 〔D〕.

**§5.4bis — por qué la frontera es oscilatoria: el espectro, no el campo.** El teorema de
completitud (§2.2) clasificó $\Gamma_s$ por su inercia — correcto para el tipo de EDP, pero
puramente real: Sylvester solo habla de autovalores de una matriz simétrica. Falta la mitad
imaginaria, y es ahí donde vive la razón estructural de que la frontera $\det\Gamma_s=0$ sea
justamente donde aparece Schrödinger. **Aclaración de alcance, para no reabrir un resultado ya
cerrado:** esto NO revive $\Psi=\Gamma_s+i\Gamma_a$ (§5.4 lo descartó correctamente, por
incompatibilidad dimensional $10\neq6$). El objeto nuevo es el **espectro** de
$\Gamma=\Gamma_s+\Gamma_a$, no una recombinación del campo. $\Gamma_a=\mathbf I\wedge\mathbf R$ es
antisimétrica real, luego su espectro es **puramente imaginario** ($\pm i\lambda$) por construcción
algebraica —ningún cálculo lo necesita, es una propiedad de toda matriz antisimétrica real—. 〔V〕
al barrer $\Gamma_s(t)$ a través de $\det\Gamma_s=0$ con $\Gamma_a$ fija, la fracción de espectro
imaginario de $\Gamma$ completo crece según el modo que se anula deja de aportar peso real, y en el
límite puro $\Gamma_s\to0$ el espectro es imaginario puro garantizado. Un espectro imaginario puro
es la forma normal de una evolución $e^{\pm i\omega t}$ —oscilación de fase con amplitud
conservada—, la estructura formal que Schrödinger exige. 〔IF〕 es la razón espectral de que la
frontera sea oscilatoria: no porque "Maxwell/fotón sea per se cuántico", sino porque en la frontera
el sector Fuerza deja de aportar autovalores reales y el sector Campo —siempre imaginario puro— pasa
a dominar. No deriva Born ni $|\psi|^2$ (sigue 〔F〕); es el mecanismo espectral preciso, ahora
explícito. Verificado:
`models/calcs/brainstorming/papers/draft_atlas/frontera_det0_espectro_imaginario_prueba.py`.

---

# 6. Einstein linealizado — una restricción condicional, no un teorema de GSF

*Nota de registro, antes de empezar.* La identidad de esta sección combina dos cosas de
naturaleza distinta, y separarlas es el punto central de esta versión del texto (corregido tras
revisión): (a) un hecho de **relatividad general estándar**, conocido, que no se re-descubre
aquí; (b) una correspondencia **específica de GSF** ($\Gamma_s\sim\bar h_{\mu\nu}$) que el propio
§6.3 admite que no está garantizada para un $\Gamma_s$ arbitrario. Marcar la combinación de
ambas como 〔TEO〕 sin distinguirlas —como hacía una versión anterior de este texto— sobre-reclama:
un teorema construido sobre una correspondencia no cerrada es, en el mejor de los casos, un
resultado **condicional**, no un teorema limpio. Lo que sigue separa explícitamente ambas partes.

## 6.1 El vacío en gauge armónico: hecho de GR (citado) + verificación de consistencia de GSF

**Hecho establecido (GR estándar, no nuevo aquí).** Definiendo $\bar h_{\mu\nu}=h_{\mu\nu}
-\tfrac12\eta_{\mu\nu}h$ (traza revertida) e imponiendo el gauge armónico/de Lorenz
$\partial^\mu\bar h_{\mu\nu}=0$, el tensor de Einstein linealizado se reduce, en cualquier
tratamiento estándar de gravedad linealizada, a
$$G_{\mu\nu}^{(1)} = -\tfrac12\Box\bar h_{\mu\nu}$$
— la ecuación de onda simple, sin términos cruzados. Esto es un hecho de relatividad general de
libro de texto; no es una contribución de este programa.

**〔V〕 Lo específico de GSF: verificación de consistencia, no descubrimiento.** Se confirmó que la
maquinaria simbólica propia del programa reproduce esta identidad con precisión racional exacta
(30/30 comparaciones no triviales en gauge armónico impuesto exactamente,
`einstein_gauge_armonico_verificacion.py`). El valor de esto es metodológico —confirma que las
herramientas de cálculo del programa no tienen errores en un caso donde la respuesta ya se
conoce— no un teorema nuevo.

**〔CE〕, condicional, el punto real.** La forma $\Box\bar h_{\mu\nu}=$fuente es *exactamente* la
que ya produce el término de Frobenius de GSF, sin modificar el Lagrangiano — *si* se acepta la
correspondencia $\Gamma_s\sim\bar h_{\mu\nu}$ y *si* la configuración satisface el gauge armónico.
Ninguna de las dos condiciones está demostrada para un $\Gamma_s$ genérico (§6.3). Esta sección
establece una **consistencia condicional**, no una derivación.

## 6.2 Fuente de materia: la normalización de Newton como restricción, no como predicción lista para testear

**Hecho establecido + verificación de consistencia.** Acoplando $T_{\mu\nu}=\mathrm{diag}
(\rho,0,0,0)$ (polvo estático) a la identidad de §6.1 vía $G_{\mu\nu}=8\pi G\,T_{\mu\nu}$ (la
ecuación de Einstein, definición de $G$), resolviendo Poisson para una fuente puntual y
revirtiendo la traza (con sympy, no a mano, para evitar un error de signo ya cometido una vez en
este mismo cálculo), se recupera exactamente el límite newtoniano estándar:
$$\Phi = -\frac{GM}{r}, \qquad \nabla^2\Phi = 4\pi G\rho$$
sin ajustar ningún factor (`einstein_newton_normalizacion_verificacion.py`). Esto tampoco es un
resultado nuevo de física —es el límite newtoniano de GR, bien conocido—; lo verificable aquí es
que la cadena de cálculo propia del programa no introduce ningún factor espurio al atravesarla.

**〔CE〕, condicional — la restricción real.** *Si* la correspondencia $\Gamma_s\sim\bar
h_{\mu\nu}$ se sostiene (no demostrada en general, §6.3) y *si* GSF acopla materia a su propia
EOM de campo, el coeficiente que reproduce Newton correctamente está **forzado**:
$J=-16\pi G\,T_{\mu\nu}$, no un parámetro ajustable. Esta es la forma correcta de presentar el
resultado: no "GSF predice $J=-16\pi G\,T_{\mu\nu}$" sin más, sino "*si* el programa cierra los
huecos de §6.3, el coeficiente queda forzado a este valor, y ningún otro sería consistente con
Newton" — una restricción estructural falsable en el sentido fuerte (si el programa cerrara y el
coeficiente que emergiera fuera otro, la identificación completa fallaría), pero condicional,
no una predicción lista para verificación empírica hoy.

## 6.3 Fronteras honestas de esta identificación

Tres huecos, nombrados con precisión, no ocultos:

1. **Alcanzabilidad dinámica del gauge.** La divergencia $D_\nu=\partial^\mu h_{\mu\nu}$ satisface
   una ecuación de onda homogénea con masa (preservación temporal: sí, $D_\nu=0$ es consistente),
   pero no se ha identificado una simetría de gauge propia de GSF que garantice, para *cualquier*
   $\Gamma_s$, la existencia de una transformación que lleve a satisfacer la condición. Es una
   identificación parcial, no universal — hasta §6.4.
2. **El sector cinético de GSF (Frobenius) no admite ninguna simetría de este tipo**, para
   ningún generador, verificado explícitamente (ni siquiera como derivada total de la acción).
3. El término "$+\Gamma_s$" de la EOM (masa Klein-Gordon) no cancela limpiamente con
   $(\mu/2)\mathrm{adj}(\Gamma)^\top$ para ningún $\mu$ único — el coeficiente de masa efectivo se
   parte entre componentes puras y mixtas de forma incompatible.

## 6.4 La reparación identificada — Einstein-Hilbert genuino + masa tipo dRGT

Los tres huecos de §6.3 resultaron ser la **misma pregunta**: la libertad de gauge que en GR
garantiza simultáneamente (a) alcanzar el gauge armónico y (b) la sintonización de Fierz-Pauli
sin fantasma, es una sola simetría (difeomorfismo linealizado). Dos hallazgos cierran esto a
orden cuadrático:

**〔CE〕 Sector cinético.** Adoptar $\mathcal{L}_{\rm coord}=\sqrt{-\det\Gamma_s}\,R(\Gamma_s)$
—la acción de Einstein-Hilbert genuina, en vez de $\mathrm{Tr}(\partial\Gamma_s^\top\partial
\Gamma_s)$— resuelve el problema por definición: es invariante de difeomorfismos por ser
literalmente la acción EH, sin necesitar sintonizar ningún coeficiente.

**〔CE〕[V] Sector de masa.** Con $\mathcal{K}=I-\sqrt{\Gamma_s^{-1}\eta}$ (construcción tipo
dRGT, $f=\eta$ resuelto perturbativamente, verificado con sympy), la identidad algebraica
$V=\beta_2\,e_2(\mathcal{K})=h_{\mu\nu}h^{\mu\nu}-h^2$ (el término de masa de Fierz-Pauli) se
confirma exactamente —residuo cero en instancia independiente (`f_como_eta_verificacion.py`)—, y
esta construcción es consistente con $\mu\det(\Gamma)$ (que ya da $\Lambda=\mathrm{adj}(\Gamma)$,
sin interferencia en fondo ni orden lineal): $\beta_2=4\mu$ corresponde a gravitón sin masa (GR
ordinaria), consistente con la propia calibración de GSF ($\mu(\rho_{GR})=2$). La identidad
algebraica en sí ($V=e_2(\mathcal{K})\equiv$ Fierz-Pauli) es 〔TEO〕[V]; su lectura como "el sector
de masa de la gravedad de GSF" es la correspondencia.

**Pendientes reales, no cerrados:** (i) verificación solo a orden cuadrático — el enunciado
genuino de ausencia de fantasma de Boulware-Deser es no lineal, requiere el análisis
ADM/hamiltoniano completo (dRGT 2010, Hassan-Rosen 2011), fuera de alcance de este trabajo; (ii)
un candidato de referencia derivado de $\Gamma_a$ ($f=-\Gamma_a^2$) fue descartado por firma
euclidiana (hecho algebraico general); (iii) $f=\eta+\kappa\Gamma_a^2$ sobrevive el chequeo de
firma pero desplaza el punto de equilibrio, requiriendo rehacer el análisis de tadpole.

---

# 7. Einstein completo — el estado real del programa

Dado que la ruta de acción cuadrática general no cerró (§6), se ataca el régimen no lineal por la
ruta termodinámica de Jacobson (1995): las ecuaciones de Einstein completas emergen de la
relación de Clausius $\delta Q=T\,dS$ aplicada a horizontes de Rindler locales, usando la
ecuación de Raychaudhuri exacta —sin linealizar nada.

## 7.1 Ingrediente cerrado — el tensor energía-momento

**〔TEO〕[V].** Construido vía Noether desde el Lagrangiano de campo de GSF, se verificó de forma
exacta (no citada): (i) **conservación**, $\partial_\mu T^\mu_{\ \nu}=\sum_{ij}(\partial_\nu
\Gamma_{ij})\cdot\mathrm{EL}_{ij}$, identidad algebraica que se anula automáticamente sobre
soluciones de la EOM; (ii) **simetría**, $T_{\mu\nu}=T_{\nu\mu}$ off-shell —más fuerte de lo que
Jacobson necesita, sin requerir la mejora de Belinfante-Rosenfeld
(`einstein_completo_tensor_energia_momento.py`).

## 7.2 Ingrediente cerrado — la derivación completa

**〔CE〕.** Se ejecutó la derivación paso a paso que la literatura del programa enunciaba pero
nunca mostraba: Raychaudhuri exacta $\to$ integración de área $\to$ flujo de calor (con el
$T_{ab}$ de §7.1) $\to$ Clausius $\to$ emparejamiento de coeficientes para todo $k^a$ nulo $\to$
Bianchi fija la constante de integración, llegando explícitamente a
$$R_{ab}-\tfrac12Rg_{ab}+\Lambda g_{ab}=8\pi G\,T_{ab}$$
sin linealizar en ningún paso (`jacobson_raychaudhuri_clausius_derivacion.md`).

## 7.3 Ingrediente abierto — el funcional de área local (Assumption 36.A)

**〔F〕, acotado con precisión.** El argumento necesita $S_{\rm local}(p)=k_BA_{\rm local}(p)/
4\ell_P^2$ en cada punto, vía un funcional de área covariante $A_{\rm local}:M\to\mathbb{R}_{>0}$
—independiente de qué observador acelerado se elija. Se descartó el candidato ingenuo
$\det(\Gamma(p))$ con evidencia concreta ($\sqrt{-g}$ es una densidad, no un escalar; verificado
con un contraejemplo explícito, la 2-esfera en dos sistemas de coordenadas). Se verificó (contra
dos casos exactos, $S^2$ y $S^3$) que un escalar genuino de curvatura, $R(\Gamma_s)$, vía la
fórmula de esfera geodésica de radio propio fijo, sí resuelve la observador-dependencia; y se
extendió al caso Lorentziano (diamante causal, derivado desde cero). Hallazgo estructural: "$\rho$
local de Planck" y "$\rho_{\rm spacetime}$ global cosmológico" (ya postulado en el programa) son
dos regímenes relacionados pero genuinamente distintos, sin una fórmula única que los unifique
todavía.

## 7.4 Auto-auditoría del programa Einstein

| Ingrediente | Estado |
|---|:---:|
| $\Lambda=\mathrm{adj}(\Gamma)$ (álgebra pura) | [D] |
| $T_{ab}$ conservado y simétrico | [D]+[V] |
| Derivación Raychaudhuri+Clausius completa | [CE], no linealizada |
| Sector cinético (Einstein-Hilbert genuino) | [CE] |
| Sector de masa (Fierz-Pauli vía $e_2(\mathcal{K})$, $f=\eta$) | [V], orden cuadrático |
| Funcional de área local (Assumption 36.A) | [F], acotado con precisión |
| Ausencia de fantasma a todos los órdenes | [F], fuera de alcance |

---

# 8. Discusión

## 8.1 Qué está probado y qué no

Este paper no reclama haber derivado las ecuaciones de Einstein completas, ni una teoría del
todo. Reclama: (a) que $\Gamma\in M_4(\mathbb{R})$ es forzado dados dos axiomas mínimos **y** un
criterio de minimalidad hecho explícito (§1.6) —no una elección arbitraria, pero tampoco una
necesidad lógica absoluta independiente de ese criterio—; (b) que el cruce $\det\Gamma=0$ es una
bifurcación matemática rigurosa, no una observación; (c) que cuatro leyes físicas maestras son
correspondencias estructurales verificables de una sola EOM; (d) que el régimen de Einstein
linealizado da una restricción cuantitativa exacta, **condicional** a una correspondencia
($\Gamma_s\sim\bar h_{\mu\nu}$) y unos huecos de gauge nombrados con precisión —no una predicción
lista para testear hoy, y no una promesa vaga tampoco—; y (e) que el programa entero es falsable en
el sentido preciso del criterio de UDO genuina (§1.1): un dominio con SAIR y F/E intrínsecos que no
siguiera su cinemática/dinámica característica lo refutaría — ningún caso así ha aparecido, pero
tampoco se ha buscado exhaustivamente.

## 8.2 Lo que el atlas no resuelve todavía

| Frontera | Estado | Nota |
|---|:---:|---|
| Masas del Modelo Estándar | [F] | requiere extensión octoniónica de $\mathrm{Cl}(3,1)$ |
| Ecuaciones de Einstein completas, todos los órdenes | [F] | análisis ADM pendiente |
| Schrödinger con potencial externo general | [A] | reducción analítica correcta, verificación numérica sin cerrar |
| Alcanzabilidad dinámica del gauge armónico en GSF | [F] | requiere simetría de gauge propia, no identificada |
| Número de generaciones (3) | [F] | geometría de $J_3(\mathbb{O})$ |
| Cota de Hessiano AM-GM (Theorem 3.1 original) | [A] refutado, [D] versión corregida | contraejemplo para $\Gamma_0$ arbitrario (§2.1); **cerrado**: para $\beta\geq|\mu|/16$ no hay equilibrio no trivial en ningún sector, resultado más fuerte que el original |

---

# 9. Conclusión

Cuatro siglos de física —Newton, Maxwell, Schrödinger, Einstein— no son cuatro teorías esperando
unificación. Este paper muestra que son cuatro vecindarios de un territorio con mapa: un solo
objeto algebraico ($\Gamma\in M_4(\mathbb{R})$, forzado por dos axiomas), una sola ecuación de
movimiento, y una sola condición topológica ($\det\Gamma=0$) que separa los regímenes. El
resultado de mayor precisión numérica —la normalización de Newton desde Einstein linealizado en
gauge armónico— combina un hecho de GR estándar (no nuevo) con una restricción condicional
específica de GSF: *si* la correspondencia $\Gamma_s\sim\bar h_{\mu\nu}$ se sostiene, el
coeficiente de acoplamiento a materia queda forzado, no ajustable — una restricción estructural
fuerte, pero condicional a huecos nombrados, no una predicción cerrada. El programa de Einstein
completo tiene, hoy, dos ingredientes cerrados, uno acotado con precisión, y un hallazgo positivo
reciente sobre el sector de masa que reordena por completo qué queda por hacer. El criterio de
éxito de este trabajo no es predicción de física nueva —es que la correspondencia estructural se
sostiene, con las fronteras nombradas donde no cierra, y sin sobre-reclamar donde la
correspondencia sigue siendo condicional.

---

# Referencias

Courant, R. and Hilbert, D. (1962). *Methods of Mathematical Physics*, Vol. II. Wiley.

de Rham, C., Gabadadze, G., and Tolley, A. J. (2010). Resummation of massive gravity. *Physical
Review Letters*, 106, 231101.

Hassan, S. F. and Rosen, R. A. (2011). Resolving the ghost problem in nonlinear massive gravity.
*Physical Review Letters*, 108, 041101.

Jacobson, T. (1995). Thermodynamics of spacetime: the Einstein equation of state. *Physical
Review Letters*, 75, 1260–1263.

Molina, H. (2024a). The determinant as an orientation invariant and the source of the cubic term
in equivariant matrix gradient flows. DOI: 10.5281/zenodo.20752208

Molina, H. (2026). Spacetime algebra as a theorem: deriving Cl(3,1) from the structure of a
dynamical unit. DOI: 10.5281/zenodo.21184515

---

\appendix

# Anexo A — La ecuación de movimiento explícita

$$\ddot{\Gamma} + \gamma\dot{\Gamma} - c^2\nabla^2\Gamma
  + \underbrace{2\Gamma}_{\text{elástico}}
  + \underbrace{\mu\,\mathrm{adj}(\Gamma)}_{\text{conoce el sector}}
  + \underbrace{4\beta\|\Gamma\|_F^2\Gamma}_{\text{amarra la norma}} = N(t)$$

# Anexo B — Scripts de cálculo

Copias de verificación incluidas en `code/` junto a este paper (fuente original en
`models/calcs/brainstorming/`, dentro del repositorio del programa):

```
code/
  calc1_newton_limit.py                          -> fig_calc1_newton_reduction
  calc2_dispersion_relations.py                  -> fig_calc2_dispersion
  calc2b_antisymmetric_hessian.py                -> fig_calc2b_antisymm_hessian
  calc3_coherence_responsiveness.py              -> fig_calc3_coherence_observables
  calc4_spectral_film.py                         -> fig_calc4_spectral_film
  calc_coulomb_couple.py                         -> fig_coulomb_couple
  verificacion_cota_amgm.py                      -> cota AM-GM, contraejemplo (§2.1)
  cota_amgm_restringida_equilibrios.py           -> cota AM-GM, versión restringida a equilibrios (§2.1)
  completitud_sectores_sylvester_hadamard_prueba.py -> teorema de completitud de sectores (§2.2)
  frontera_det0_espectro_imaginario_prueba.py    -> espectro imaginario en la frontera (§5.4bis)
  atlas_sectores_desde_sair_prueba.py            -> validación de sectores desde datos SAIR (§3)
  puente_simbolo_gram_sylvester_prueba.py        -> puente símbolo-Gram, compartido con el paper compañero
  schrodinger_from_gsf_eom_verificacion.py       -> reducción a Schrödinger (§5.4)
  einstein_gauge_armonico_verificacion.py        -> consistencia en gauge armónico (§6.1)
  einstein_newton_normalizacion_verificacion.py  -> normalización de Newton desde Einstein (§6.2)
  einstein_completo_tensor_energia_momento.py    -> T_ab conservado y simétrico (§7.1)
  f_como_eta_verificacion.py                     -> sector de masa, f=η (§6.4)
  conexion_potencial_completo_lambda_masa.py     -> Λ=adj(Γ) y conexión con el sector de masa
```

Requisitos: `numpy`, `sympy`. No hace falta scipy.

# Anexo C — Ejemplo ilustrativo: Coulomb y Lorentz vía la operación de Acoplamiento (Paper C)

**Nota de estatus (bajado de "resultado" a ejemplo ilustrativo tras revisión).** Lo que sigue
**no** es una recuperación general en el sentido de §5 — es un ejemplo numérico concreto, sobre
configuraciones de campo específicas, con un bloque de acoplamiento postulado ad hoc. Se incluye
por su valor pedagógico (conecta el vocabulario SAIR con Coulomb/Lorentz, casos muy reconocibles),
no como evidencia adicional de la tesis central del paper.

**Anclaje correcto.** La operación relevante de composición entre dos UDO es la de **Acoplamiento**
de Paper C (`paper_c_algebra_composicional.md`): dadas $\Gamma_A,\Gamma_B$, el acoplamiento
produce $\rho_{AB}=\rho_A+\rho_B+\Delta_{\rm couple}$ con $\Delta_{\rm couple}=-\log\det(I-\Xi^\top
\Xi)\geq0$ ($\Xi$ los valores singulares normalizados del bloque cruzado $C_{AB}$) — un
morfismo $n$-ario bien definido dentro de la multicategoría entrópica de Paper C, no una
construcción de Ch7. El ejemplo que sigue usa una UDO-partícula y una UDO-campo EM acopladas por
un bloque cruzado $C_{AB}$, en el mismo espíritu categórico de Paper C, pero **no** instancia el
formalismo completo de $\Delta_{\rm couple}$ (Schur complement) — es una simplificación con un
ansatz de acoplamiento específico, elegido para reproducir Coulomb/Lorentz, no derivado de la
fórmula general de Paper C.

**〔IF〕, con un ansatz explícito.** Se **postula** (no se deriva) el bloque de acoplamiento
$$C_{\mu\nu} = q\,A_\mu\,u_\nu$$
(producto exterior del 4-potencial y la 4-velocidad) — la forma de acoplamiento mínimo estándar,
análoga al acoplamiento mínimo de teoría de gauge. Descomponiendo por el teorema Force-Field,
$\Gamma_s(C)=(C+C^\top)/2$, $\Gamma_a(C)=(C-C^\top)/2$:

| Caso | Configuración | Resultado |
|---|---|---|
| Estático ($v=0$) | solo $\Gamma_s(C)\neq0$ | fuerza de Coulomb, $q\mathbf E$ |
| Magnético puro ($v\neq0$, solo $B$) | solo $\Gamma_a(C)\neq0$ | fuerza de Lorentz magnética, $q(\mathbf v\times\mathbf B)$ |
| General | $\Gamma_s+\Gamma_a$ | Lorentz completa, $q(\mathbf E+\mathbf v\times\mathbf B)$ |

Verificado numéricamente (`calc_coulomb_couple.py`): la fuerza calculada desde $f^\mu=qF^{\mu\nu}
u_\nu$ coincide exactamente con las tres configuraciones esperadas. El observable de coherencia
$C$ del **bloque de acoplamiento** (no del campo $F_{\mu\nu}$, que es siempre $C=1$) transiciona
de $0$ (Coulomb, conservativo) a $1$ (magnético/Josephson, reactivo) de forma continua bajo
interpolación — la transición electrostática→radiación es una transición de $C(C_{12})$.

**Frontera:** este es un acoplamiento inter-UDO (partícula—campo), distinto del $F=S\cdot A$
intra-UDO de §1.2, que es el propagador libre. Conectar formalmente esta construcción con el
$\Delta_{\rm couple}$ de Paper C (en vez del ansatz $C_{\mu\nu}=qA_\mu u_\nu$ elegido a mano), y
la generalización a Coulomb/Lorentz como recuperación *dentro* de un solo $\Gamma$ (sin acoplar
dos UDO), quedan abiertas.
Adicionalmente, los casos magnético y general del script usan potenciales vectoriales
$A_\mu$ explícitamente marcados como "simplificados" en el propio código fuente —no derivados
sistemáticamente del campo $F_{\mu\nu}$ dado, sino elegidos ad hoc para reproducir el resultado
esperado. El caso estático (Coulomb puro) sí usa el potencial correcto y completo. Los tres casos
son verificaciones numéricas de consistencia sobre configuraciones de campo específicas, no una
derivación general de $A_\mu$ a partir de $F_{\mu\nu}$ arbitrario.

**Nota de coherencia (jul-11 2026).** Ch7 (`part1/07_compositional_operations.md`, §7.3.3)
distingue ahora explícitamente dos capas dinámicas coexistentes en cualquier Acoplamiento: (i) la
capa de estado — cada UDO conserva su propia dinámica, identidad y ecuación de movimiento,
modulada por el acoplamiento; (ii) la capa de configuración — el propio bloque de acoplamiento
$C_{AB}$ (aquí, $C_{\mu\nu}=qA_\mu u_\nu$) es un objeto con dinámica propia, regulada por sus
componentes y el contexto externo. La fórmula $\Delta_{\rm couple}$ usada arriba es exacta como
hecho algebraico estático sobre el bloque conjunto en cualquiera de las dos lecturas; una
afirmación sobre cómo evoluciona *en el tiempo* el acoplamiento partícula-campo en sí (más allá
del ansatz fijo $qA_\mu u_\nu$ usado aquí) pertenece a la capa (ii) y no se desarrolla en este
anexo — ver Ch7 §7.11 (OQ7.1) para la derivación general de esa dinámica cuando aplica.

# Anexo D — Análisis espectral: fotografía y película

Las tres ramas de dispersión (§3.2) se complementan aquí con el análisis dinámico completo: la
evolución temporal del propagador por sector (la "película"), contrastada con la configuración
estática de $\Gamma$ en un instante dado (la "fotografía").

- **Figura D.1** (`fig_calc2_dispersion.png`): las tres ramas $\omega(k)$ superpuestas; mapa de
  calor de velocidad de grupo $v_g=c^2k/\omega$ sobre $(k,\det\Gamma)$ — el atlas visible en un
  solo plano.
- **Figura D.2** (`fig_calc2b_antisymm_hessian.png`): curvatura $m_{\rm eff}^2$ por modo y sector
  para los casos de prueba originales del programa — *nota:* tras la revisión de §2.1, esta
  figura ilustra instancias particulares, no una cota general demostrada; reinterpretar en esos
  términos.
- **Figura D.3** (`fig_calc3_coherence_observables.png`): $C(t)$ y $R(t)=\dot C/\gamma$ para los
  tres sectores — el sector $\det\Gamma<0$ tiene el $|R|_{\max}$ más alto, consistente con
  dinámica tipo Hopf.
- **Figura D.4** (`fig_calc4_spectral_film.png`): trayectorias de autovalores en $\mathbb C$
  (arriba) y retrato de fase $(\det\Gamma,C)$ (abajo) — la película completa, no solo el
  instante.

**Lectura operacional:** de cualquier trayectoria $\Gamma(t)$, calcular dos escalares
—$\det\Gamma(t)$ y $C(t)$— y leer el régimen, sin ajuste de parámetros y sin conocimiento previo
de qué física gobierna el sistema.

---

*Programa Gamma Space Framework. Julio 2026.*
*henrymolina@gmail.com*
