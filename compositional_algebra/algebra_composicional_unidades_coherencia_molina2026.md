# Un álgebra composicional para configuraciones de Unidades de Coherencia: clausura, balance de entropía, y aditividad de inercia

Henry Molina
Investigador independiente
henrymolina@gmail.com
DOI: pendiente (enviado a Zenodo)

**Nota sobre dependencias.** Este paper presupone el objeto $\Gamma\in M_4(\mathbb R)$ y la Unidad de Coherencia (UoC), y usa el potencial estructural $P(\Gamma,\rho)=\|\Gamma\|_F^2+\mu(\rho)\det\Gamma$ de Ch13 (Part II) sin re-derivarlo; ambos de trabajo previo, todavía no publicado, del mismo programa. El resumen autocontenido de abajo cubre lo que este paper necesita de ese trabajo previo; el lector no necesita consultarlo para seguir el argumento.

**Mínimo autocontenido.** Una Unidad de Coherencia (UoC) es una entidad (física, química, biológica, o social) descrita por una matriz simétrica $\Gamma\in M_4(\mathbb R)$ que codifica sus atributos estructurales como un Gram; $\rho=-\log|\det\Gamma|$ mide qué tan confinada/estructurada está (mayor $\rho$ = más estructura, $\det\Gamma\to0$ = disolución). $P(\Gamma,\rho)$ es un potencial cuyo mínimo caracteriza la configuración de equilibrio de la UoC (Ch13); $\mu(\rho)$ es un acoplamiento que depende del nivel $\rho$, fijado en Ch13 por una condición de auto-consistencia. Este paper toma esos tres objetos como dados y ataca la pregunta de qué pasa cuando **dos o más** UoCs se componen; por qué $P$ tiene esta forma específica es una pregunta de Ch13, no de aquí (§1).

---

Los resultados se etiquetan por registro (**〔DEF〕** definición/postulado · **〔TEO〕** teorema con prueba · **〔CE〕** correspondencia estructural (isomorfismo algebraico con un objeto conocido, no una derivación física) · **〔IF〕** interpretación física) y por estatus (**[D]** demostrado · **[V]** verificado numéricamente · **[A]** asertado (a demostrar) · **[F]** frontera/abierto). Un resultado [D] que dependa de una hipótesis adicional a los axiomas base (A1)-(A4) se marca **[D, condicional a hipótesis nombrada]**, con la hipótesis dicha en el propio enunciado.

---

### Resumen

Doce operaciones composicionales que aparecen, con nombres distintos, en física, química, biología y sistemas sociales (unión, acoplamiento, fusión, fisión, absorción, disolución, entre otras, definidas formalmente en §9ter) se reducen aquí en cinco primitivos (formar el conjunto, acoplar, desacoplar, marginalizar, copiar, relajar) y una sola identidad de álgebra lineal: la fórmula de Schur del determinante de bloques, aplicada al objeto de configuración $\Gamma\in M_4(\mathbb R)$. De esa única identidad se **deriva**, sin un postulado por operación, el balance de entropía completo, una cota exacta de trabajo mínimo (análogo de Jarzynski-Crooks), y una medida domain-agnóstica de cohesión estructural irreducible. La reducción no introduce una operación nueva por dominio; un puñado de primitivos genera las doce. Trabajo posterior en el frente de campos continuos (§5bis) encontró dos primitivos adicionales de uso genuino (Auto-Acoplamiento, reflexivo; Esclavización, hermana de la marginalización) ausentes del catálogo original; su aparición deja intacto el cierre demostrado, pero convierte la completitud de la base primitiva en pregunta abierta, ya no en hecho establecido.

Alrededor de ese núcleo, dos extensiones dentro del cuerpo principal. Removiendo la restricción a matrices definidas positivas, la aditividad de inercia de Haynsworth (1968) extiende el álgebra a cualquier signatura, revelando que la clasificación por signo de determinante usada en todo el paper es la partición más gruesa posible de la inercia de una matriz simétrica, para cualquier dimensión. Un segundo resultado (Teorema 9) muestra que ningún potencial invariante de conjugación puede distinguir estructuralmente sub-sectores que comparten esa fase. Una tercera línea, más incipiente y con hallazgos ya cerrados por separado pero sin ensamblar en una estructura formal única, propone que el álgebra completa es una categoría enriquecida sobre el mismo balance de entropía; se documenta en el Apéndice A como trabajo en curso, no en el cuerpo principal. El paper no reclama derivar física de partículas; sus ejemplos (Coulomb/Lorentz, gas ideal, enlace químico) son correspondencias ilustrativas, pensadas para mostrar la aplicabilidad del álgebra sobre casos ya conocidos.

---

## 1. Alcance y decisiones de scope

Doce operaciones de composición, catalogadas hasta ahora caso por caso en distintos dominios, cierran en cinco primitivos y una sola identidad algebraica (la fórmula de Schur del determinante de bloques) más **dos hechos ya establecidos** en trabajo previo del programa (la extensividad de la co-presencia y la monotonía de Lyapunov del potencial $P$). Ese cierre (Teorema 2, con el balance de entropía completo derivado en §6) es el resultado central del paper. Alrededor de él, dos extensiones estructurales que no eran parte del plan original: la clasificación por signo de determinante empleada a lo largo del paper resulta ser, para cualquier dimensión, la partición **más gruesa posible** de la inercia de una matriz simétrica (Corolario 8.1) (un hecho de geometría algebraica real) y ningún potencial invariante de conjugación puede romper esa clasificación entre sub-sectores que comparten fase (Teorema 9). Una tercera línea, más incipiente, propone que el álgebra completa es una categoría enriquecida sobre el mismo balance de entropía; documentada en el Apéndice A como trabajo en curso, no en el cuerpo principal, precisamente porque su estatus es [A] y este cuerpo se mantiene [D]/[V].

**Ubicación y alcance.** Un resultado de álgebra y sistemas dinámicos, en `math-ph` / `nlin.AO` (Adaptation and Self-Organizing Systems), no física de partículas. Los ejemplos de la §11 (Coulomb/Lorentz, gas ideal, enlace químico) son **correspondencias ilustrativas 〔CE〕** que muestran la aplicabilidad del álgebra a casos ya conocidos.

**Dimensión.** Salvo indicación explícita en contrario (Teoremas 8, 9, y el Corolario 8.1, formulados para $n$ arbitrario), $n=4$ en los Teoremas 1–7 es una elección **específica de la construcción SAIR** ($\Gamma\in M_4(\mathbb R)$), no un resultado general en la dimensión. Donde el argumento sí es dimension-agnóstico (Haynsworth, la tripartición det-signo, el Teorema 9), el enunciado lo dice explícitamente con $n$ libre.

---

## 2. Trabajo relacionado

Este paper se ubica en la intersección de tres literaturas ya establecidas, sin reclamar novedad en ninguna de ellas por separado: la contribución es la síntesis específica (Schur + inercia de Haynsworth + termodinámica composicional) sobre el objeto de configuración $\Gamma$, aplicando herramientas conocidas a un objeto concreto en vez de proponer un método de análisis nuevo.

**Teoría categórica de sistemas dinámicos abiertos.** El programa de Baez y Fong sobre "compositional thermodynamics" (redes de sistemas termodinámicos abiertos compuestos vía operads/categorías monoidales) ataca una pregunta estructuralmente paralela: qué operaciones de composición son admisibles entre sistemas termodinámicos abiertos, y cómo se propaga el balance de entropía a través de ellas. El cuerpo principal de este paper (§4–§10) no pasa por el aparato categórico: deriva la composicionalidad directamente de una identidad de álgebra lineal (Schur) sobre un objeto de configuración concreto. El Apéndice A revisita esta relación con más precisión, no como una analogía de método, sino mostrando que la operación subyacente (el complemento de Schur) coincide exactamente con la regla de composición de su *black-box functor* para redes lineales pasivas.

**Complementos de Schur en modelos gráficos Gaussianos.** La identidad central de este paper (Proposición 1, y la admisibilidad del Teorema 1) es, en su núcleo, el hecho estándar de que el complemento de Schur de una matriz de precisión Gaussiana es exactamente la marginalización de esa distribución; material de manual en la literatura de modelos gráficos (Lauritzen, *Graphical Models*, y su descendencia en inferencia Gaussiana estructurada). Lo que aporta este paper es su aplicación a un objeto de configuración física ($\Gamma$), con una interpretación termodinámica ($\rho=-\log|\det\Gamma|$ como entropía estructural) ausente en el contexto puramente estadístico; la identidad misma es de manual.

**Termodinámica estocástica de sistemas acoplados.** El Teorema 5 ($W_{\min}=\Delta P$) es un análogo directo de las relaciones de Jarzynski (1997) y Crooks (1999): cotas de trabajo mínimo vía una función de Lyapunov/energía libre, generalizadas aquí a la composición estructural de UoCs en vez de a un único sistema termodinámico bajo un protocolo externo. La revisión de Seifert (2012, *Stochastic thermodynamics, fluctuation theorems and molecular machines*) es la referencia estándar de ese terreno. El paralelismo con el Teorema 5 es directo, con una vía de derivación distinta: este paper obtiene la cota desde la monotonía de Lyapunov de $P$, ya establecida en el programa, no desde una teoría de fluctuaciones estocásticas.

Las tres literaturas funcionan aquí como puntos de referencia y contraste, más que como maquinaria importada directamente: la contribución específica es la aplicación conjunta de estas herramientas ya conocidas al objeto $\Gamma$, produciendo el balance composicional cerrado de §6 y la generalización vía Haynsworth de §8.

---

## 3. Introducción: el problema que resuelve este paper

La Unidad de Coherencia (UoC), una entidad física, química, biológica o social descrita por una matriz de configuración $\Gamma\in M_4(\mathbb R)$ cuyo determinante mide qué tan "cerrada"/confinada está su estructura ($\rho=-\log|\det\Gamma|$, la entropía estructural); casi nunca existe aislada: dos átomos se enlazan, dos agentes de mercado se acoplan, una célula se divide, un organismo absorbe a otro. La pregunta que motiva este paper es simple de plantear y, hasta ahora, sin respuesta sistemática dentro del programa: **dadas dos o más UoCs, ¿qué operaciones de composición entre ellas son estructuralmente admisibles, y qué le pasa a la entropía cuando se componen?**

Una construcción caso por caso catalogaría cada operación (unión, fusión, absorción, fisión, disolución) y postularía una regla de balance de entropía para cada una, ajustada al dominio. **Las doce operaciones fenomenológicas que aparecen en física, química, biología y sistemas sociales no son doce reglas independientes**; son composiciones de un puñado de operaciones primitivas (formar el conjunto, acoplar, desacoplar, marginalizar, copiar, relajar), y su balance de entropía se **deriva** de una sola identidad de álgebra lineal (la fórmula de Schur del determinante de bloques) más dos hechos ya establecidos en el programa. No hay una regla nueva por operación; hay una regla, aplicada doce veces.

El resto del paper sigue este orden: §4-§5 establecen la representación conjunta y muestran que las operaciones admisibles cierran en cinco primitivos (Teorema 2); §6-§7 derivan el balance de entropía completo y las cotas de trabajo/espontaneidad; §8-§9 extienden el álgebra más allá del régimen originalmente admisible, revelando dos resultados estructurales sobre qué tan gruesa puede ser, y qué tan ciega es, la clasificación por signo de determinante usada en todo el paper; §10-§11 dan la clasificación completa y tres correspondencias ilustrativas; §12-§13 documentan el proceso de verificación, incluyendo lo que se intentó y no funcionó; §14 cierra. El Apéndice A recoge, por separado, una línea de trabajo en curso (el álgebra como estructura categórica) que todavía no alcanza el estatus [D]/[V] del cuerpo principal.

---

## 4. La representación conjunta y la admisibilidad del acoplamiento

Dos UoCs $A,B$ con configuraciones $\Gamma_A,\Gamma_B\in M_4(\mathbb R)$ se combinan a través de la **matriz conjunta**:

$$\Gamma_{\mathrm{joint}} = \begin{pmatrix}\Gamma_A & C_{AB}\\ C_{AB}^T & \Gamma_B\end{pmatrix}$$

donde $C_{AB}$ es el **bloque de acoplamiento**, el único grado de libertad nuevo que introduce la composición. Toda operación composicional de este paper es una transformación de este objeto.

> **▣ 〔TEO〕 Teorema 1 (Cota de admisibilidad del acoplamiento). [D]** Sean $\Gamma_A,\Gamma_B\succ0$ (sector de fuerza, $\det>0$) con niveles estructurales $\rho_A=-\log\det\Gamma_A$, $\rho_B=-\log\det\Gamma_B$. Un bloque de acoplamiento $C_{AB}$ es **estructuralmente admisible** ($\Gamma_{\mathrm{joint}}\succ0$) si y solo si
> $$\sigma_{\max}\!\left(\Gamma_A^{-1/2}C_{AB}\Gamma_B^{-1/2}\right)<1.$$
> *Prueba.* $\Gamma_{\mathrm{joint}}\succ0 \iff$ complemento de Schur $\Gamma_B-C_{AB}^T\Gamma_A^{-1}C_{AB}\succ0 \iff$ autovalores de $\Gamma_A^{-1/2}C_{AB}\Gamma_B^{-1}C_{AB}^T\Gamma_A^{-1/2}<1$. $\blacksquare$

El umbral $\sigma_{\max}=1$ es también la **frontera de fusión**: en ese punto $\det\Gamma_{\mathrm{joint}}=0$ y las sub-UoCs dejan de ser recuperables por proyección, la misma frontera $\det=0$ que separa los sectores Newtoniano/Maxwell/Relativista de un solo UoC, ya establecida en trabajo previo del programa.[^delta_rho]

[^delta_rho]: **Corolario ($\delta_\rho$), estimado heurístico [A].** La cota se traduce, de forma aproximada, en un umbral de separación de nivel: $\delta_\rho\approx4\ln(1/c_0)$ nats, donde $c_0=\|C_{AB}\|_F$ (el factor $4$ es la dimensión de $\Gamma$, no una constante derivada con rigor; este corolario es una estimación de orden de magnitud, no un teorema; se marca [A] explícitamente por eso, a diferencia de Teorema 1 del que se deriva). **Caveat verificado numéricamente [V]:** la cota basada en norma de Frobenius es exacta para acoplamiento de rango 1, y **conservadora** para acoplamiento de rango completo; $\|C_{AB}\|_F\geq\sigma_{\max}(C_{AB})$ en general, así que un acoplamiento denso puede exceder el umbral de Frobenius y seguir siendo admisible (0/2000 violaciones rango-1; 100% de casos densos que exceden y siguen admisibles; script: `delta_rho_admissibility_bound.py`).

**¿De dónde sale $C_{AB}$? Cierre parcial (jul-11 2026).** El Teorema 1 dice cuánto acoplamiento es
admisible, pero no de dónde sale el valor concreto de $C_{AB}$: una prueba de escritorio directa
mostró que un acoplamiento sin origen físico declarado pasa la cota de admisibilidad exactamente
igual de bien que uno real, siempre que se mantenga bajo $\sigma_{\max}=1$: el teorema filtra
consistencia matemática, no plausibilidad física. Aplicando la EOM de Ch13 al propio
$\Gamma_{\mathrm{joint}}$ se obtiene la identidad **exacta** (no solo a orden lineal, cualquier
tamaño de bloque) $\mathrm{adj}(\Gamma_{\mathrm{joint}})_{AB}=-\mathrm{adj}(S_A)\,C_{AB}\,
\mathrm{adj}(\Gamma_B)$, que cierra un sistema no lineal para $C_{AB}$ mismo: sin forzamiento
externo, el único punto fijo genérico (caso escalar) es $C_{AB}=0$; el acoplamiento decae salvo
que esté sostenido por un forzamiento con origen físico trazable, o el sistema esté exactamente en
un $\mu$ crítico. Para bloques $2\times2$ existen puntos fijos no triviales auto-sostenidos en un
rango amplio de $\mu$, no solo en el punto crítico aislado del caso escalar. Esto da el criterio de
plausibilidad que faltaba, aunque la estabilidad general de esos puntos fijos queda abierta.
(`brainstorming/physics/oq71_derivacion_C_AB_desde_P_gamma.md`,
`brainstorming/physics/oq71_cierre_no_lineal_completo.md`.)

---

## 4bis. El criterio de distinguibilidad

Los axiomas y la clasificación que siguen (§5, (A4); §10) usan "identidad preservada/perdida". Definimos la distinguibilidad aquí, antes de usarla.

**▣ 〔DEF〕 Distinguibilidad.** Dos sub-UoCs $A,B$ son estructuralmente distinguibles dentro de un compuesto $C$ (configuración $\Gamma_C$) si existen proyecciones $\pi_A,\pi_B:V_C\to V_C$ con $\pi_A+\pi_B=\mathrm{Id}$, $\pi_A^2=\pi_A$, $\pi_B^2=\pi_B$, tales que:
- **(contenido estático)** $\|\pi_A\Gamma_C\pi_A^T-\Gamma_A\|_F\leq\epsilon_{AB}$, $\epsilon_{AB}=\|C_{AB}\|_F$ (exacto si $C_{AB}=0$);
- **(localización dinámica)** todo modo propio $v_k$ de $\Gamma_s$ asignado al bloque $i$ tiene razón de participación $\mathrm{PR}(k)=1/\sum_ip_i(k)^2<\tau$, $p_i(k)=\|\pi_iv_k\|^2/\|v_k\|^2$, para algún umbral $\tau\in(1,n)$.

Las dos condiciones miden cosas distintas y ninguna subsume a la otra: la primera es la operativa para Unión/Absorción/Fusión (donde los bloques diagonales sí cambian); la segunda es la única informativa para Acoplamiento/Resonancia, donde el bloque diagonal está fijo por construcción (la primera condición da $\epsilon_{AB}=0$ siempre, trivialmente); el ejemplo mínimo es el batido de dos osciladores acoplados en degeneración exacta: cualquier acoplamiento no nulo mezcla los modos al 50/50 ($\mathrm{PR}\to n$) aunque el bloque diagonal nunca se mueva. Si ninguna proyección así existe, o alguna condición falla, $A$ y $B$ son indistinguibles en $C$. Verificado: $\mathrm{PR}$ es invariante bajo reetiquetado de bloques, consistente con el Teorema 9 (§9) (`part1/07_compositional_operations.md` §7.2).

---

## 5. La base primitiva y el teorema de clausura

**Axiomas (operación composicional admisible).** Un mapa $O$ sobre estados-colección $(N,\{\Gamma_i\},\{C_{ij}\})$ es admisible si:

- **(A1) Acción conjunta:** $O$ actúa sobre $\Gamma_{\mathrm{joint}}$; cada bloque de salida es función de los bloques de entrada.
- **(A2) Clausura en $M_4(\mathbb R)$:** toda salida es un elemento válido $4\times4$ del tipo algebraico correcto (nota: Ch7 usa la etiqueta "$G(3)$" para este axioma, heredada de la notación del álgebra de Clifford $\mathrm{Cl}(3,0)$ de Ch3; un objeto distinto, no usado en este paper; se evita aquí para no confundir).
- **(A3) Sin información externa:** $O$ solo combina, separa, duplica o evoluciona sus operandos; no inyecta configuración externa (única excepción: la elección explícita de sub-estructura en la dirección de fisión, suministrada como dato, no inventada).
- **(A4) Consistencia de dos ejes:** $O$ respeta la clasificación identidad×signo-de-$\Delta\rho$ (§10).

> **▣ 〔TEO〕 Lemma 1 (Unicidad del cierre $\Omega$). [D]** Entre los mapas que reducen la cardinalidad integrando un subespacio bajo (A1)-(A2), el complemento de Schur es el único que preserva la descripción efectiva del bloque retenido. No se requiere ninguna hipótesis sobre $P$.
>
> *Prueba.* $\Gamma_{\mathrm{joint}}$ es una matriz de Gram por construcción (A2): escribiendo los atributos de $A$ y $B$ como las columnas de $V_A,V_B$ en el espacio ambiente, $\Gamma_{\mathrm{joint}}=V^{\mathsf T}V$ con $V=[V_A\mid V_B]$, de modo que el bloque de acoplamiento es $C_{AB}=V_A^{\mathsf T}V_B$, la orientación relativa de los dos conjuntos de atributos. Eliminar $B$ es pasar al cociente por $\operatorname{span}(V_B)$ con la métrica inducida, y la Gram de los atributos retenidos en ese cociente es
> $$(V_A-P_{V_B}V_A)^{\mathsf T}(V_A-P_{V_B}V_A)=\Gamma_A-C_{AB}\Gamma_B^{-1}C_{AB}^{\mathsf T},$$
> con $P_{V_B}=V_B\Gamma_B^{-1}V_B^{\mathsf T}$ el proyector ortogonal sobre $\operatorname{span}(V_B)$: exactamente el complemento de Schur. Equivalentemente, en forma variacional, el complemento de Schur es la minimización parcial de la forma cuadrática que porta la Gram, $\min_{c_B}c^{\mathsf T}\Gamma_{\mathrm{joint}}c=c_A^{\mathsf T}\Omega\,c_A$, es decir el bloque eliminado relajado a su óptimo dado el retenido. Unicidad: el proyector ortogonal sobre un subespacio es el único idempotente autoadjunto sobre él, así que ninguna otra reducción devuelve la Gram del cociente; la proyección ingenua $\Gamma_{kk}$ descarta la retroacción de $C$ y difiere (verificado). $\blacksquare$ Ambas identidades verificadas a precisión de máquina sobre 500 configuraciones Gram aleatorias (`lema1_ruta_geometrica.py`).
>
> *Observación (por qué no la ruta gaussiana).* Leer $\Gamma_{\mathrm{joint}}$ como matriz de precisión de una gaussiana e invocar marginalización gaussiana estándar da el mismo complemento de Schur, pero solo para $P$ cuadrático, y al costo de postular una distribución de probabilidad que el marco no usa en ningún otro lado: en el resto, $\Gamma$ evoluciona bajo un flujo determinista, no como precisión de una distribución. Las dos rutas coinciden porque para formas cuadráticas marginalizar y minimizar concuerdan. Se enuncia la ruta geométrica porque responde la pregunta que esta álgebra sí hace (cuál es la Gram de lo que sobrevive, un hecho estructural, la misma noción que usan $\rho=-\log|\det\Gamma|$, la admisibilidad y la inercia de Haynsworth) y porque no carga ninguna hipótesis sobre $P$.

> **▣ 〔TEO〕 Teorema 2 (Clausura de la base primitiva). [D]** Bajo (A1)-(A4), toda operación composicional admisible factoriza, salvo composición, en cinco primitivos: **JOIN** ($\oplus$, formar el conjunto), **COUPLE/DECOUPLE** (fijar $C_{AB}\neq0/=0$), **$\Omega$** (marginalizar, complemento de Schur), **COPY** ($\Gamma_B^{(0)}\leftarrow\Gamma_A$), **RELAX** (flujo de gradiente a $\arg\min P$).
>
> *Prueba.* Un estado-colección es la tripleta $(N,\{\Gamma_i\},\{C_{ij}\})$: cardinalidad, contenido de bloque y acoplamiento. Por (A1), $O$ actúa únicamente sobre $\Gamma_{\mathrm{joint}}$, así que cualquier cambio que produzca debe ser expresable en términos de estos tres grados de libertad; no hay un cuarto eje disponible. Se muestra que $O$ factoriza a lo largo de ellos, y que cada eje, restringido por (A2)-(A4), admite exactamente los primitivos listados:
>
> **Eje de cardinalidad ($N$).** Por (A3), $O$ no puede inyectar configuración externa; solo puede *aumentar* $N$ copiando un bloque ya existente (**COPY**, la única forma de añadir un grado de libertad sin información nueva) o *disminuirlo* integrando un subespacio. Por el Lemma 1, la única reducción de cardinalidad que preserva la descripción efectiva del bloque retenido es el complemento de Schur (**$\Omega$**). Ningún otro mapa de reducción de cardinalidad satisface (A2) sin descartar información de $C$ que (A4) exige preservar en el balance de $\Delta\rho$.
>
> **Eje de acoplamiento ($C_{ij}$).** Fijado $N$, el único grado de libertad restante entre bloques es si $C_{ij}=0$ o $C_{ij}\neq0$: un valor binario por par de bloques. Imponerlo en una u otra dirección son, por definición, **COUPLE** y **DECOUPLE**; (A2) exige que el resultado siga siendo un $\Gamma_{\mathrm{joint}}$ válido, lo que ambas operaciones satisfacen trivialmente (fijar una submatriz a cero o a un valor admisible no rompe la estructura de bloques).
>
> **Eje de contenido de bloque ($\Gamma_i$).** Con $N$ y $\{C_{ij}\}$ fijos, el único cambio admisible por (A3) (sin inyectar información externa) es mover cada $\Gamma_i$ hacia $\arg\min P$ vía el flujo de gradiente ya establecido en el programa: **RELAX**. Cualquier otro cambio de $\Gamma_i$ requeriría, o bien información externa (excluido por A3), o bien un cambio simultáneo de $N$ o $C_{ij}$, que ya pertenece a los otros dos ejes.
>
> **Formar el conjunto inicial.** $\oplus$ (**JOIN**) es el caso $N\to N+k$ con $C_{ij}=0$ para todo par nuevo: la co-presencia pura, el punto de partida sobre el que actúan los demás primitivos.
>
> Como los tres ejes son independientes (cambiar uno no fuerza un cambio en los otros dos) y cada uno está completamente cubierto por los primitivos anteriores, cualquier $O$ admisible es una composición de estos cinco. $\blacksquare$
>
> **Qué exige y qué no exige el teorema de $P$.** Una versión anterior enunciaba este resultado como condicional a $P$ cuadrático, heredado de probar el Lemma 1 por marginalización gaussiana. Con el Lemma 1 probado geométricamente, ningún eje del argumento de clausura restringe la forma de $P$: el eje de cardinalidad descansa en la estructura Gram de $\Gamma$ (A2), el de acoplamiento en (A2) solo, y el de contenido de bloque solo exige que $P$ admita un flujo de gradiente hacia un mínimo, no que sea cuadrático. En particular el teorema ahora cubre el potencial real del programa, cuyo término $\mu\det\Gamma$ es de grado 4 en las entradas de $\Gamma$ (matriz $4\times4$), no de grado 3. (La palabra "cúbico" pertenece a otro objeto: el coeficiente de $\xi^3$ en la forma normal unidimensional que resulta de proyectar $P$ sobre un modo blando $\xi$, donde el paper hermano sobre el determinante como fuente de ese coeficiente muestra que $D^3\det$, evaluado en el equilibrio, es lineal en $\Gamma_*$ porque $\det$ tiene grado 4.)
>
> **Qué queda fuera del teorema.** La clausura aquí probada es algebraica y cinemática: clasifica qué transformaciones de $\Gamma_{\mathrm{joint}}$ son admisibles, no cómo se comporta el flujo globalmente. Bajo un $P$ no-cuadrático, una perturbación pequeña del potencial puede alterar cualitativamente el retrato de fase (bifurcaciones, nuevos puntos fijos, pérdida de unicidad de $\arg\min P$) sin afectar ninguno de los pasos anteriores, ya que ninguno lee la forma de $P$. Si la *dinámica* construida sobre esta álgebra es estructuralmente estable bajo el $P$ real del programa es una pregunta aparte, de sistemas dinámicos más que de álgebra composicional, y queda fuera de este paper por diseño.

Nueve operaciones fenomenológicas (Unión, Anidamiento, Acoplamiento, Fusión, Absorción, Fisión, Desacoplamiento, Reproducción, Disolución) son composiciones de estos cinco primitivos + identidad, verificado por conteo de parámetros y construcción explícita.

**Límites del teorema de clausura.** La prueba de clausura factoriza por los tres grados de libertad que (A1)-(A2) permiten a un estado-colección (cardinalidad, acoplamiento, contenido de bloque) en vez de enumerar operadores conocidos y descartar el resto por fuerza bruta. Un sexto primitivo tendría que actuar sobre un **cuarto** grado de libertad; por (A1), $O$ actúa únicamente sobre $\Gamma_{\mathrm{joint}}$, así que ese cuarto eje simplemente no existe dentro de la representación conjunta tal como está definida: el conjunto completo se deriva de la estructura del objeto, no se obtiene filtrando candidatos.

Esto tiene un límite que conviene marcar con precisión. Un teorema de universalidad en sentido fuerte (representación tipo Cayley, o libertad del monoide generado) probaría que *ninguna* representación alternativa de "composición de UoCs" puede revelar un cuarto eje. Lo que se prueba aquí es más modesto: dentro de **esta** representación específica ($N$ sub-UoCs, bloques $\Gamma_i$, acoplamientos $C_{ij}$) no hay cuarto eje. Es clausura relativa a una representación fija, y se deja así, marcada, en vez de inflarla a universalidad absoluta.

---

## 5bis. Después del cierre: dos primitivos más encontrados en el frente de trabajo, y una pregunta de completitud genuina que reemplaza la certeza anterior

El Teorema 2 cierra el **catálogo**: las nueve operaciones fenomenológicas conocidas al momento de probarlo factorizan en cinco primitivos. Trabajo posterior, aplicando esta misma álgebra a configuraciones de campo continuas (frontera declarada en §1, fuera de este paper), encontró **dos operaciones más usadas de forma repetida y necesaria** que no estaban en la lista original; su ausencia no rompe el Teorema 2 (que es correcto sobre el catálogo que cerraba), pero sí muestra que "cerrado" y "completo" son afirmaciones distintas, y que la segunda nunca estuvo probada (ya se anotaba como límite en el "¿Cómo se sabe que no hay un sexto primitivo?" de arriba: la prueba cierra frente a los tres ejes de *esta* representación, no frente a cualquier operación futura sobre el mismo objeto).

**▣ 〔DEF〕 Auto-Acoplamiento (Definition 7.19, Ch7).** Una UoC está **auto-acoplada** cuando su propio contenido de configuración reingresa en su término fuente: $\Gamma_\mathrm{ef}=\Gamma+\lambda\,\mathcal E[\Gamma]$, con $\mathcal E[\Gamma]$ un funcional del propio estado de la UoC (p.ej. su contenido energético) y la *misma* constante de acoplamiento $\lambda$ que gobierna su acoplamiento con socios externos. Es Acoplamiento con $A=B$; excluido por la letra de la Definición 7.5 (que exige dos UoCs distintas) pero exigido por consistencia en cuanto el acoplamiento es universal: si todo lo que desplaza $\Gamma_\mathrm{ef}$ acopla, el propio contenido de la UoC no puede quedar exento. *Instancia verificada:* en la extensión continua, la propia energía de gradiente del campo reingresando en su fuente es exactamente lo que produce la auto-interacción de segundo orden correcta (el paso de bootstrap), con el coeficiente fijado por universalidad, no ajustado. Auto-Acoplamiento es la cara composicional de la **reflexividad**; la propiedad que el programa le asigna a $\gamma$; hasta ahora el álgebra no tenía operación reflexiva mientras la EOM sí tenía un término reflexivo. Su desarrollo completo (¿genera la Auto-Acoplamiento iterada el término $\gamma\dot\Gamma$? ¿interactúa con Copia?) queda abierto. [D] la definición y su instancia verificada; [F] su desarrollo completo.

**▣ 〔DEF〕 Esclavización (Definition 7.20, Ch7), hermana de $\Omega$.** Un modo $u$ de una UoC está **esclavizado** a una ranura $s$ cuando la dinámica lo elimina no por marginalización sino por **restricción**: $u=f(s)$, con la dinámica propia de $u$ degenerada o inestable, de modo que la restricción se impone en vez de elegirse. Distinta de $\Omega$: la marginalización integra un grado de libertad hacia afuera (Schur; pierde información; produce entropía, §6), mientras que la esclavización *ata* el modo (sin producción de entropía; el modo sigue presente, expresado a través de $s$). *Instancia verificada:* el modo conforme (de escala) de un campo de configuración es taquiónico cuando es libre y debe esclavizarse a la ranura contextual $\rho$; en la extensión continua esto es una **obligación de estabilidad**. Esta operación ya existía en el programa como mecanismo de *selección* (criterio de covarianza, dependencia funcional/de esclavización); esta definición la promueve de heurística de selección a operación composicional. [D] la definición y su instancia verificada.

**Dos sub-operaciones de Acoplamiento, no primitivos nuevos, pero cuya falta de nombre causó un error concreto.** Toda instancia trabajada de Acoplamiento en este paper comparte un rasgo: $\Gamma_A,\Gamma_B$ se forman por separado a partir de sus propias cuádruplas SAIR *antes* de que $C_{AB}$ entre, y el acoplamiento añade un término de bloque cruzado *después*. Un patrón distinto; encontrado al intentar acoplar directamente los propios campos bivectoriales de dos UoCs, un primer intento que falló y se corrigió derivando desde una energía libre de referencia conocida en vez de asumir el canal de cuña, no encaja en esa plantilla:

- **Acoplamiento-externo** (Definición 7.5, como en §4): $\Gamma_A,\Gamma_B$ computados de forma independiente; $C_{AB}$ es un bloque genuinamente nuevo, ortogonal a ambos bloques diagonales. Es lo que compone toda operación de §§4–11, incluyendo el mecanismo de "pegamento" $n$-ario del Teorema 4 (marginalizar un bloque intermedio induce un término cruzado *externo* entre los sobrevivientes).
- **Acoplamiento-interno** (nuevo, sin cambiar la Definición 7.5, solo nombrando un caso ya usado): el atributo vectorial propio de una sub-UoC se sustituye por una combinación con el vector de la *otra*, **antes** de formar $\Gamma$: $R^A\to R^A-q\,I^B$ (sustitución mínima; la receta de acoplamiento de gauge de la física, aplicada aquí como primitivo composicional en vez de asumida). Expandir $|R^A_\mathrm{ef}|^2$ produce un término cruzado que vive *dentro* de $\Gamma_s^A$ (nunca $\Gamma_a^A$, porque viene de un producto punto, no de una cuña), no hay bloque nuevo fuera-de-diagonal; el acoplamiento es invisible a la estructura de bloques de $\Gamma_\mathrm{joint}$ hasta que las entradas propias de $\Gamma_A$ se expanden. *Instancia verificada:* un parámetro de orden con fase ($R^A=\nabla\theta$) acoplado a un potencial vectorial vía $\nabla\theta\to\nabla\theta-qB$ reproduce exactamente la masa de Meissner/London (mecanismo de Anderson-Higgs), no un acoplamiento cuña-cuña ($\Gamma_a$-$\Gamma_a$) como se conjeturó primero.
- **Absorción-de-gauge** (distinta de Absorción, §11 nota): cuando el Acoplamiento-interno introduce un grado de libertad redundante en $A$ que una transformación compensatoria de $B$ puede eliminar por completo ("comérselo"), fijar esa redundancia colapsa exactamente *un* grado de libertad de $A$ en el propio $\Gamma_s$ de $B$ (típicamente como término de masa), mientras el resto de $A$ (su escalar $S^A$) sobrevive y fija la escala de lo que $B$ ganó. A diferencia de la Absorción del Teorema 8/§10 (donde $B$ se pierde por completo, irreversible), aquí solo se pierde la dirección vectorial redundante, no toda la sub-UoC.

Ninguna de las tres es un primitivo nuevo: ambas sub-operaciones de Acoplamiento reducen a Acoplamiento más una elección de *dónde* entra el término cruzado (antes o después de formar $\Gamma$), y la Absorción-de-gauge añade una reducción $\Omega$ parcial de una sola dirección. Se nombran aquí porque dejarlas sin nombre fue exactamente lo que produjo el error original (asumir que Acoplamiento siempre significa Acoplamiento-externo, y proponer por tanto una cuña $\Gamma_a$-$\Gamma_a$ para un mecanismo que en realidad necesitaba Acoplamiento-interno).

> **Pregunta abierta (completitud de generación, no solo del catálogo).** Este paper prueba que sus operaciones catalogadas se reducen a una base pequeña de primitivos: completitud *del catálogo* (Teorema 2). No prueba que toda transformación de $\Gamma_\mathrm{joint}$ que preserve admisibilidad esté *generada* por los primitivos; completitud *del álgebra*. El teorema que falta: caracterizar el semigrupo generado por {Identidad, Join, Couple (externo/interno), $\Omega$, Slave, Copy, Relax, Self-Couple} dentro del monoide de mapas que preservan admisibilidad, y probar generación o exhibir una transformación admisible fuera de él. Hasta entonces, "el álgebra está completa" es una conjetura que el éxito del catálogo hace plausible, no un hecho establecido; la misma distinción, aplicada a sí misma, que el Corolario 8.1 y el Teorema 9 (§9) hacen entre lo que un invariante grueso puede y no puede ver. [F].

---

## 5ter. Tipo algebraico, y por qué no hay operación de aniquilación

**Tipo algebraico. [D]** Co-presencia $\oplus$ es asociativa y conmutativa: $(\{\mathrm{UoC}\},\oplus,\varnothing)$ es un **monoide conmutativo**. La composición completa, incluyendo el colapso $\Omega$, es **no asociativa**: la fusión falla $(A\circ B)\circ C=A\circ(B\circ C)$ (verificado numéricamente). La estructura precisa es un **magma conmutativo, flexible y power-asociativo**: conmutativo ($A\circ B=B\circ A$), flexible ($(A\circ B)\circ A=A\circ(B\circ A)$) y power-asociativo ($(A\circ A)\circ A=A\circ(A\circ A)$), pero ni asociativo ni de Jordan. Tres consecuencias: **(i)** la power-asociatividad hace bien-definida la auto-iteración (fusión repetida consigo mismo, torres recursivas de nivel) sin ambigüedad de agrupamiento; la no-asociatividad solo muerde al fusionar tres o más UoCs *distintas* en agrupamientos distintos; **(ii)** la no-asociatividad es intrínseca al colapso con pérdida $\Omega$ (el modo relativo marginalizado se pierde de forma dependiente del camino); es el mismo fenómeno que la irreversibilidad $\Delta\rho\geq0$ (§6) y la flecha del tiempo de la composición; JOIN, COUPLE y $\oplus$ (sin colapso) sí asocian; **(iii)** existe un compuesto canónico libre de orden: el colapso $n$-ario simultáneo (marginalizar todos los modos relativos a la vez) es invariante bajo permutación; el compuesto bien-definido de muchas UoCs es el colapso simultáneo, del cual el agrupamiento por pares es una aproximación dependiente del camino. Verificado (`models/calcs/brainstorming/ch7/`, ver §7.2.3 de `part1/07_compositional_operations.md`).

**La aniquilación no es una operación. [D]** Ninguna operación de este catálogo envía contenido a nada ($\Gamma\to0$ con sus atributos destruidos): cada una preserva el conjunto, redistribuye contenido entre niveles ($\Omega$, Fisión), o lo dispersa al nivel siguiente (Disolución); el contenido se conserva siempre. Esto no es una elección de diseño sino consecuencia de dos leyes de conservación ya establecidas: termodinámicamente, los grados de libertad no pueden desaparecer sin dejar rastro (segunda ley; cota de Landauer), así que la Disolución dispersa contenido con entropía creciente en vez de borrarlo; y por conservación de masa-energía (Noether, simetría de traslación temporal), el contenido se transforma, no desaparece; como en la aniquilación partícula-antipartícula, que produce fotones, no nada. La ausencia de una operación de aniquilación es, con esto, una propiedad de consistencia del álgebra.

---

## 6. La identidad generadora y el balance de entropía

Toda la termodinámica de la composición se deriva de una sola identidad:

> **▣ 〔TEO〕 Proposición 1 (Identidad de Schur). [D]** Con $\rho=-\log|\det\Gamma|$ y $\Xi=\Gamma_A^{-1/2}C_{AB}\Gamma_B^{-1/2}$ ($\sigma_i(\Xi)\in[0,1)$ por admisibilidad):
> $$\rho_{AB} = \rho_A+\rho_B+\Delta_{\mathrm{couple}}, \qquad \Delta_{\mathrm{couple}}=-\log\det(I-\Xi^T\Xi)\geq0.$$
> *Prueba:* $\det\Gamma_{\mathrm{joint}}=\det\Gamma_A\det\Gamma_B\det(I-\Xi^T\Xi)$; tomar $-\log$. $\blacksquare$

Junto con la extensividad de la co-presencia ($\rho_{A\oplus B}=\rho_A+\rho_B$, bloque diagonal, $\det=\prod\det\Gamma_i$) y la monotonía de Lyapunov del flujo autónomo ($\dot P\leq0$, ya establecida en el programa), esta identidad **genera** (no postula) el balance de entropía de las doce operaciones:

| Operación | $\Delta\rho$ | Signo | Derivación |
|---|---|---|---|
| Unión | $\Delta_{\mathrm{couple}}$ | $\geq0$ | Schur directo: misma fórmula que Acoplamiento, pero aquí sí describe la dinámica real del conjunto (Unión forma un compuesto genuino) |
| Acoplamiento | $\Delta_{\mathrm{couple}}$ | $\geq0$ | Schur directo: un hecho estático del bloque; ver la precisión más abajo |
| Desacoplamiento (Schur) | $0$ | $=0$ | inverso entrópico exacto |
| Desacoplamiento (SVD) | $\leq0$ | $\leq0$ | minimiza pérdida algebraica, no entrópica |
| Fusión | $\Delta_{\mathrm{couple}}$ | $\geq0$ | idéntico a Acoplamiento |
| Fisión | $-\Delta_{\mathrm{couple}}(B,C')$ | $\leq0$ | inverso algebraico exacto de Fusión |
| Absorción | $\Delta_{\mathrm{couple}}-\rho_B$ | $\pm$ | Schur con $S=B$ |
| Disolución | $\to+\infty$ | $\geq0$ | $\det\Gamma\to0$ |
| Co-presencia $\oplus$ | $0$ | $=0$ | bloque diagonal |
| Copia | $\rho_B$ | $\geq0$ | extensividad de $\oplus$ |
| Reproducción | $\rho_B+\Delta\rho_{\mathrm{relax}}(B)$ | $\geq0$ | Copia + Relajación |
| Relajación | $\int\sigma_{\mathrm{struct}}\,dt=P_i-P_f$ | $\geq0$ | Lyapunov |
| Anidamiento | $0$ | $=0$ | proyección, sin nuevos g.d.l. |

**Todas las entradas son [D]** (Unión añadida jul-11 2026). Ninguna requiere un postulado nuevo por operación: se leen de la misma identidad de Schur más los dos hechos ya citados. Verificado numéricamente sobre 5000–10000 muestras SPD aleatorias por afirmación, cero violaciones (`thm73_cohesion_entropy_bound.py`, `algebra_termodinamica_cierre.py`).

**Precisión sobre la entrada "Acoplamiento" (jul-10 2026).** La fila de Acoplamiento usa la misma
identidad de Schur que Unión; esto describe correctamente $\Delta_{\mathrm{couple}}$ como una
propiedad puramente algebraica del bloque $\Gamma_{\mathrm{joint}}=\begin{pmatrix}\Gamma_A&C_{AB}\\
C_{AB}^T&\Gamma_B\end{pmatrix}$ (una identidad de matrices, cierta independientemente de qué
dinámica se le aplique después). **No implica**, sin embargo, que el Acoplamiento genuino (en el
sentido fenomenológico, "sin formar una UoC compuesta") haga que $\rho_A,\rho_B$ evolucionen según
$\rho_{AB}=\rho_A+\rho_B+\Delta_{\mathrm{couple}}$ bajo una sola EOM compartida: esa lectura
corresponde a Unión (o al límite de acoplamiento fuerte, "Acoplamiento se aproxima al régimen de
unión", ya anotado en la tabla de dos ejes). Para el Acoplamiento propiamente dicho, cada UoC
conserva su propia dinámica, modulada por la otra: la fila de esta tabla describe el costo
entrópico *del bloque conjunto considerado como objeto estático*, útil como cota y como
herramienta analítica, no una afirmación sobre la evolución temporal de cada $\rho_i$ bajo
Acoplamiento. Esta distinción se volvió concreta esta semana al aplicar el álgebra a un problema de
composición física real (tres cuerpos vía Ch7): tratar el Acoplamiento como si resolviera una EOM
conjunta produjo un resultado que dejaba de reproducir la física real (ver la nota de resolución
correspondiente en Ch7 (Definición 7.5, §7.3.3 de `part1/07_compositional_operations.md`).

**Resolución en dos capas, verificada numéricamente (jul-11 2026).** La aparente tensión, si el Acoplamiento tiene o
no una EOM compartida, se resuelve reconociendo dos capas dinámicas coexistentes,
no una pregunta con una sola respuesta. **(i) Capa de estado:** cada UoC conserva su propia
dinámica e identidad, moduladas por la otra; esto nunca se cuestiona. **(ii) Capa de
configuración:** el propio bloque de acoplamiento $C_{AB}$ es un objeto emergente con dinámica
propia, regulada por sus componentes ($\Gamma_A,\Gamma_B,\mu$) y por el contexto (un forzamiento
estructural externo $N_{AB}(t)$): exactamente la EOM que Ch13 postula para cualquier $\Gamma$,
aplicada ahora al bloque conjunto. Un ejemplo trabajado (dos osciladores acoplados por $\kappa(t)$,
`models/calcs/brainstorming/ch7/coupling_dos_capas_prueba.py`) confirma ambos regímenes: con
$N_{AB}$ constante, $\kappa(t)$ relaja al valor fijo $\kappa^*=N_{AB}/(1-\mu/2)$ (error $5\times
10^{-4}$), recuperando exactamente la lectura estándar de un resorte de rigidez fija; con $N_{AB}$
variando más rápido que la relajación propia de $\kappa$, este muestra dinámica genuina, sin
asentarse: el régimen de un enlace químico respondiendo a una reacción en curso, o una sinapsis
plástica. Ninguna lectura es universalmente correcta; cada una es el límite adecuado según la
velocidad relativa del contexto.

**Cohesión irreducible.** Cuando el desacoplamiento redistribuye $C_{AB}$ vía proyección SVD (no vía Schur), un residuo puede quedar sin atribuir a ninguna sub-UoC:

> **▣ 〔TEO〕 Teorema 3 (Cohesión y reversibilidad). [D]** $\mathcal B(A,B)=\|P^\perp_{\mathrm{span_{GS}}(\mathcal E_A\cup\mathcal E_B)}C_{AB}\|_F$ (proyección ortogonal Gram-Schmidt sobre los modos SVD de ambos bloques) satisface: (i) $\mathcal B=0\iff C_{AB}$ recuperable exactamente de $(\Gamma_{A'},\Gamma_{B''})$; (ii) $\Delta\rho_{\mathrm{couple}}\geq\mathcal B^2/\|\Gamma_{AB}\|_F^2\geq0$.
>
> *Prueba (i).* $(\Rightarrow)$ Sea $\mathcal E_A\cup\mathcal E_B$ el conjunto (ortonormalizado vía Gram-Schmidt) de los modos singulares de $\Gamma_A,\Gamma_B$. Si $\mathcal B=0$, la redistribución SVD (proyección de Gram-Schmidt de $C_{AB}$ sobre $\mathrm{span}(\mathcal E_A)$ y $\mathrm{span}(\mathcal E_B)$ por separado) recupera $C_{AB}$ exactamente, ya que $C_{AB}$ vive enteramente en $\mathrm{span_{GS}}(\mathcal E_A\cup\mathcal E_B)$: $\delta\Gamma_A+\delta\Gamma_B=C_{AB}$. Re-acoplar desde $(\Gamma_{A'},\Gamma_{B''})=(\Gamma_A+\delta\Gamma_A,\Gamma_B+\delta\Gamma_B)$ reconstruye $\Gamma_{AB}$ exactamente.
> $(\Leftarrow)$ Contrapositivo: si $\mathcal B>0$, el residuo $C_{AB}-P^\perp_{\mathrm{span_{GS}}}C_{AB}\neq0$ es ortogonal a $\mathrm{span}(\mathcal E_A\cup\mathcal E_B)$ por construcción. Por (A3) (ninguna operación admisible inyecta configuración externa), ese residuo no puede absorberse en $\Gamma_{A'}$ ni en $\Gamma_{B''}$; cualquier reconstrucción $\tilde C$ a partir de $(\Gamma_{A'},\Gamma_{B''})$ vive en $\mathrm{span}(\mathcal E_{A'}\cup\mathcal E_{B''})$, y como las perturbaciones de modo son $O(\|\delta\Gamma\|)$ (Teorema 2), $\|\tilde C-C_{AB}\|_F\geq\mathcal B-O(\|\delta\Gamma\|^2)>0$ para acoplamiento admisible. $\blacksquare$
>
> *Prueba (ii).* De la Proposición 1, $\Delta\rho_{\mathrm{couple}}=-\log\det(I-\Xi^T\Xi)=\sum_i-\log(1-\sigma_i^2)$ donde $\sigma_i=\sigma_i(\Xi)\in[0,1)$ son los valores singulares de $\Xi=\Gamma_A^{-1/2}C_{AB}\Gamma_B^{-1/2}$.
>
> *Primera desigualdad.* $-\log(1-x)\geq x$ para $x\in[0,1)$; sumando sobre los valores singulares: $\Delta\rho_{\mathrm{couple}}\geq\sum_i\sigma_i^2=\|\Xi\|_F^2$.
>
> *Segunda desigualdad, corregida.* $\|\Xi\|_F^2=\|\Gamma_A^{-1/2}C_{AB}\Gamma_B^{-1/2}\|_F^2\geq\|C_{AB}\|_F^2/(\lambda_{\max}(\Gamma_A)\cdot\lambda_{\max}(\Gamma_B))$; la desigualdad estándar de valor singular mínimo de un producto de matrices (no la norma de Frobenius conjunta usada en una versión anterior de esta prueba, que mezclaba incorrectamente norma de operador y norma de Frobenius). Como $\lambda_{\max}(\Gamma_A)\cdot\lambda_{\max}(\Gamma_B)\leq\|\Gamma_A\|_F\|\Gamma_B\|_F\leq\tfrac12(\|\Gamma_A\|_F^2+\|\Gamma_B\|_F^2)\leq\|\Gamma_{AB}\|_F^2$ (la última desigualdad porque $\Gamma_{AB}$ contiene $\Gamma_A,\Gamma_B$ como bloques diagonales, más el acoplamiento), se sigue $\|\Xi\|_F^2\geq\|C_{AB}\|_F^2/\|\Gamma_{AB}\|_F^2$.
>
> *Cierre.* $\mathcal B\leq\|C_{AB}\|_F$ (el residuo de una proyección nunca excede la norma del original), luego $\|C_{AB}\|_F^2\geq\mathcal B^2$. Encadenando: $\Delta\rho_{\mathrm{couple}}\geq\|\Xi\|_F^2\geq\|C_{AB}\|_F^2/\|\Gamma_{AB}\|_F^2\geq\mathcal B^2/\|\Gamma_{AB}\|_F^2\geq0$. $\blacksquare$ Verificado numéricamente sobre 5000 muestras SPD aleatorias, 0 violaciones de la cota (`thm73_cohesion_entropy_bound.py`).

$\mathcal B(A,B)$ es una medida de integración estructural domain-agnóstica que no requiere distribuciones de probabilidad: para enlaces químicos mide no-separabilidad orbital.

---

## 7. Composición en cascada, trabajo, y espontaneidad

> **▣ 〔TEO〕 Teorema 4 (Composición en cascada). [D]** Para tres UoCs acopladas secuencialmente: $\rho_{ABC}=\rho_A+\rho_B+\rho_C+\Delta_{\mathrm{couple}}(A,B)+\Delta_{\mathrm{couple}}(AB,C)$. **Corolario:** esta suma es idéntica bajo cualquier orden de agrupación (verificado, 0 diferencia en 2000 muestras); la entropía *total* producida por acoplar tres UoCs es order-independent, aunque la *estructura residual* específica (qué se pierde en cada colapso) sí depende del orden.

> **▣ 〔TEO〕 Teorema 5 (Cota de trabajo vía Lyapunov). [D]** Para cualquier operación que lleve $P$ de $P_i$ a $P_f>P_i$, el trabajo mínimo externo es $W_{\min}=\Delta P=P_f-P_i$. *Prueba:* $\dot P=-\|\nabla P\|^2_M+\dot W\Rightarrow W=\Delta P+\int\|\nabla P\|^2 dt\geq\Delta P$, análogo GSF de Jarzynski-Crooks.

> **▣ 〔TEO〕 Teorema 6 (Criterio de espontaneidad). [D]** Una operación es espontánea sii $\Delta P\leq0$. $\Delta\rho$ (Prop. 1) y $\Delta P$ (Teo. 5) son **cantidades independientes**: una puede ser $>0$ mientras la otra es $\leq0$, exactamente el perfil de un enlace que forma espontáneamente mientras produce entropía estructural.

**Relación exacta $\rho\leftrightarrow P$.** Usando el potencial explícito de Ch13 ($P=\|\Gamma\|_F^2+\mu(\rho)\det\Gamma$) y el flujo sobreamortiguado ($\dot\Gamma\approx-\frac1{2\gamma}\nabla_\Gamma P$):

> **▣ 〔TEO〕 Teorema 7. [D]** $\dot\rho = \frac{n}{\gamma}+\frac{\mu(\rho)}{2\gamma}\det\Gamma\,\|\Gamma^{-1}\|_F^2$ ($n=4$), vía la fórmula de Jacobi $\nabla_\Gamma\det\Gamma=\det\Gamma\cdot\Gamma^{-T}$.

Verificado por diferencias finitas (error $<10^{-8}$, `rho_P_exact_relation.py`). El resultado: **$\rho$ y $P$ son monedas de entropía distintas**; el coeficiente de variación de su razón sobre muestras aleatorias es $\approx1.45$, no cero. No hay una identidad $\rho\propto P$ escondida; hay dos leyes de conservación complementarias sobre el mismo flujo.

El Teorema 7 **demuestra** que ninguna identidad lineal ata $\rho$ y $P$ para este flujo, con la misma solidez que cualquier otro resultado [D] del paper; la no-proporcionalidad está probada, no pendiente de un principio unificador que falte encontrar. $\rho$ (vía Schur, cinemático) y $P$ (vía Lyapunov, dinámico) miden aspectos genuinamente distintos del mismo flujo, exactamente como energía y entropía en termodinámica clásica: dos leyes acopladas a través de la energía libre, cada una con su propia dinámica.

---

## 8. Más allá del régimen admisible: aditividad de inercia (Haynsworth)

Los Teoremas 1–6 restringen la composición al sector de fuerza: $\Gamma_A,\Gamma_B\succ0$. Esta sección remueve esa restricción con una herramienta clásica de 1968.

> **▣ 〔TEO〕 Teorema 8 (Aditividad de inercia de Haynsworth). [D]** Para $\Gamma_{\mathrm{joint}}=\begin{pmatrix}\Gamma_A & C_{AB}\\ C_{AB}^T & \Gamma_B\end{pmatrix}$ con $\Gamma_A$ simétrica **invertible** (cualquier signatura, no restringida a $\succ0$):
> $$\mathrm{In}(\Gamma_{\mathrm{joint}}) = \mathrm{In}(\Gamma_A) + \mathrm{In}(S_A), \qquad S_A=\Gamma_B-C_{AB}^T\Gamma_A^{-1}C_{AB}$$
> donde $\mathrm{In}(M)=(n_+,n_-,n_0)$ es la inercia (conteo de autovalores positivos/negativos/nulos). *Prueba:* la congruencia $\begin{pmatrix}I&0\\-C_{AB}^T\Gamma_A^{-1}&I\end{pmatrix}\Gamma_{\mathrm{joint}}\begin{pmatrix}I&-\Gamma_A^{-1}C_{AB}\\0&I\end{pmatrix}=\mathrm{diag}(\Gamma_A,S_A)$ bloque-diagonaliza $\Gamma_{\mathrm{joint}}$; por la ley de inercia de Sylvester, matrices congruentes comparten inercia, y la inercia es aditiva sobre una suma directa. $\blacksquare$ Verificado (2000 muestras binarias + 3000 en cascada de 3 cuerpos, 0 violaciones; `haynsworth_inertia_cascade.py`).

**El Teorema 1 es el caso especial** $\mathrm{In}(\Gamma_A)=\mathrm{In}(\Gamma_B)=(n,0,0)$: la única suma posible es $(2n,0,0)$, exactamente por qué la conjetura ingenua de signos mixtos en cascada (§12, ítem 3) murió *dentro* del régimen SPD. Relajar esa restricción es lo que reabre la pregunta.

### 8bis. $\Omega$ regularizada en el sector de masa nula ($\det\Gamma_B=0$), jul-11 2026

El Teorema 8 exige $\Gamma_A$ invertible pero no restringe la signatura, sin embargo, la
marginalización misma ($\Omega$, complemento de Schur) exige $\Gamma_B$ invertible, un requisito
que la teoría física de fondo hace fallar exactamente en uno de sus tres sectores propios: el
sector de masa nula ($\det\Gamma_B=0$). Absorber o fusionar un sub-UoC que vive ahí era, hasta
ahora, una división por cero sin resolver.

> **▣ 〔TEO〕 Teorema 8bis ($\Omega$ regularizada). [D]** Sea $\Omega_B:=\lim_{\varepsilon\to0^+}
> [\Gamma_A-C_{AB}(\Gamma_B+\varepsilon I)^{-1}C_{AB}^T]$. Este límite **existe (es finito) si y
> solo si** $C_{AB}$ se anula sobre $\ker(\Gamma_B)$ (condición de Albert: $C_{AB}q=0\ \forall
> q\in\ker(\Gamma_B)$), en cuyo caso coincide **exactamente** con la fórmula de Moore–Penrose
> $\Gamma_A-C_{AB}\Gamma_B^+C_{AB}^T$. Si la condición falla, el límite diverge **exactamente como
> $1/\varepsilon$**. *Prueba (una línea):* diagonalizando $\Gamma_B=Q\,\mathrm{diag}(\lambda_1,
> \ldots,\lambda_{n-1},0)\,Q^T$ y $C'=C_{AB}Q$, $C_{AB}(\Gamma_B+\varepsilon I)^{-1}C_{AB}^T=
> \sum_{i<n}\frac{c_i'(c_i')^T}{\lambda_i+\varepsilon}+\frac{c_n'(c_n')^T}{\varepsilon}$; el último
> término diverge salvo que $c_n'=0$, exactamente la condición de Albert. $\blacksquare$ Verificado
> numéricamente (tasa de divergencia exacta $1/\varepsilon$, razón consecutiva $10.00\pm0.03$ por
> década).

**Lectura física.** La divergencia es genuina, no un artefacto: acoplar con componente finita y no
ortogonal a un modo sin rigidez estructural (masa nula) cuesta energía estructural infinita; el
análogo composicional de excitar resonantemente un oscilador sin amortiguamiento en su propia
frecuencia. La condición de Albert es exactamente la afirmación de que un fotón se absorbe por su
energía/polarización, nunca empujando contra su propia dirección de propagación sin masa.

**El balance de entropía se generaliza sin maquinaria nueva.** $\rho_C=\rho_A+\Delta_{\mathrm{int}}$
se mantiene exacto (verificado a $<10^{-15}$) sustituyendo únicamente $\Gamma_B^{-1}\to\Gamma_B^+$
en $\Delta_{\mathrm{int}}=-\log|\det(I-\Gamma_A^{-1}C_{AB}\Gamma_B^+C_{AB}^T)|$; la cota de
admisibilidad $\Delta_{\mathrm{int}}\geq0$ es exactamente la misma del Teorema 1
($\lambda_{\max}<1$), no una cota nueva. Una identidad complementaria,
$\mathrm{pdet}(\Gamma_{\mathrm{joint}})=\mathrm{pdet}(\Gamma_B)\det(\Gamma_C)$ y
$\mathrm{rank}(\Gamma_{\mathrm{joint}})=\mathrm{rank}(\Gamma_A)+\mathrm{rank}(\Gamma_B)$
(pseudo-determinante/rango, exacta bajo la condición de Albert), muestra que **el modo sin masa de
$\Gamma_B$ sobrevive intacto** como modo nulo exacto del compuesto; nunca se absorbe, solo se
absorben los grados de libertad masivos del sub-UoC. El caso doblemente singular ($\Gamma_A$
también en $\det=0$) se cierra igual bajo la condición doble de Albert, con ambos modos sin masa
sobreviviendo sin mezclarse. (`brainstorming/physics/omega_regularizado_sector_masa_nula.md`,
`brainstorming/physics/delta_int_generalizado_sector_masa_nula.md`,
`brainstorming/physics/caso_doblemente_singular.md`.)

> **▣ 〔TEO〕 Corolario 8.1 (La tripartición det-signo es la clasificación más gruesa posible de la inercia, para cualquier $n$). [D]** $\mathrm{sign}(\det\Gamma_s)\in\{+,0,-\}$ divide $\mathrm{Sym}(n,\mathbb R)$ en exactamente dos regiones **abiertas y genéricas** ($n_-$ par / $n_-$ impar) separadas por la hipersuperficie **de codimensión 1, no genérica** $n_0\geq1$. Cierto para cualquier dimensión $n$; hecho clásico de geometría algebraica real ($\{\det=0\}$ es una variedad algebraica de codimensión 1), no una conjetura numérica ni específico de $n=4$ ni del GSF.

Este es el enunciado más agudo del paper sobre la clasificación por signo de determinante usada en los Teoremas 1–7: la tripartición no es un corte arbitrario de tres; es la partición *forzada*, la más gruesa posible, de la inercia en fases genéricas más separatriz, independiente de la dimensión. Es más gruesa que la firma completa $(n_+,n_-,n_0)$, que para $n=4$ admite hasta 15 clases distintas.

**Precisión (jul-11 2026); esta "pregunta abierta" no es una pregunta bien planteada del álgebra.**
Preguntar si la tripartición por signo "esconde" la estructura fina de 15 clases confunde el
álgebra con lo que corre sobre ella: cualquier invariante grueso es, por construcción, ciego a lo
que descarta; la aritmética que suma dinero es ajena a si se cuenta en billetes o monedas. Esa
ceguera no es un hueco a cerrar; es lo que hace del invariante un invariante. El Teorema 9 (§9)
confirma esto desde el otro lado: ningún potencial invariante de conjugación puede recuperar esa
estructura fina al nivel de la geometría local (Hessiano); la capa estática/cinemática que este
álgebra captura es, demostrablemente, incapaz de seleccionarla. Si existe estructura fina
dinámicamente relevante, vive en la **topología del flujo de gradiente de $P$** (cuencas,
separatrices, clasificación Morse-Smale); una pregunta legítima, pero de la dinámica, no de esta
álgebra composicional.

---

## 9. El compañero dinámico: ningún sub-sector recibe privilegio algebraico

El Corolario 8.1 es una afirmación **estática/cinemática**: clasifica qué formas puede tomar $\Gamma_s$. Una pregunta natural sigue de inmediato: dado un objeto compuesto de varios bloques que comparten la misma fase, ¿alguna dinámica razonable distingue el papel de un bloque del de otro; o la ceguera del Corolario 8.1 se hereda intacta por la dinámica construida encima? Esta sección responde: para una clase amplia y natural de potenciales, se hereda exactamente. Descubierto atacando una composición concreta de tres sectores (notas exploratorias del autor, no publicadas) y registrado aquí en forma general porque el argumento no usa nada específico de esa construcción.

> **▣ 〔TEO〕 Teorema 9 (Ningún sub-sector privilegiado bajo potenciales invariantes de conjugación). [D]** Sea $\mathcal M$ un espacio de matrices ($\mathrm{Sym}(n,\mathbb R)$ o $M_n(\mathbb R)$ general) y $G$ un grupo actuando sobre $\mathcal M$ dejando $P:\mathcal M\to\mathbb R$ invariante: conjugación $P(S\Gamma S^T)=P(\Gamma)$, $S\in O(n)$, si $\mathcal M=\mathrm{Sym}(n,\mathbb R)$; o la acción de dos lados $P(U\Gamma V)=P(\Gamma)$, $(U,V)\in O(n)\times O(n)$, $\det(U)\det(V)=1$, si $\mathcal M=M_n(\mathbb R)$ general. Tanto $\|\Gamma\|_F^2$ como $\det\Gamma$ son invariantes bajo su acción respectiva, así que cualquier $P$ construido de ellos, en particular $P(\Gamma)=\|\Gamma\|_F^2+\mu\det\Gamma$, cumple la hipótesis. Sea $\Gamma^\ast\in\mathcal M$ un punto crítico de $P$. Entonces:
>
> **(a)** El espacio tangente a la $G$-órbita de $\Gamma^\ast$ yace enteramente en el núcleo del Hessiano de $P$ en $\Gamma^\ast$. *Prueba:* la invarianza implica $\nabla P(g\cdot\Gamma^\ast)=0$ para todo $g\in G$ (toda la órbita es crítica, no solo el punto). Derivando esta identidad a lo largo de una curva $g(t)\in G$: $H(\Gamma^\ast)\cdot v=0$ para $v$=tangente de la órbita. $\blacksquare$ Este paso no requiere estructura de bloques; es el hecho general tipo Goldstone para cualquier punto crítico de cualquier $P$ invariante.
>
> **(b)** Si además $\Gamma^\ast=\mathrm{blockdiag}(\Gamma_1,\dots,\Gamma_k)$, el generador de rotación interna de **cualquier** bloque $\Gamma_i$ es un caso particular de (a).
>
> **(c) Corolario, sin sub-sector privilegiado.** Por (b), la libertad gauge interna de cada bloque tiene exactamente el mismo carácter algebraico para todo $i$; $P$ no puede distinguir estructuralmente un bloque de otro. Si los bloques se etiquetan por rol físico, ninguna etiqueta recibe trato especial de la geometría local de $P$.

**Verificación, tres instancias independientes:**

| $n$ | Objeto | $\mathcal M$ / grupo $G$ | Dim. órbita esperada | Verificado |
|---|---|---|---|---|
| 4 | $\Gamma$ (punto fijo Lorentziano, general) | $M_4(\mathbb R)$, $O(4)\times O(4)$ | $12-\mathrm{estab.}=6$ | 6 modos cero exactos |
| 3 | $G_3$ (composición abstracta de 3 sectores) | $\mathrm{Sym}(3,\mathbb R)$, $O(3)$ | $\dim SO(3)-\dim(O(2)\times O(1))=2$ | 2 modos cero exactos |
| 6 | $\Gamma_{\mathrm{joint}}=\mathrm{blockdiag}(\Gamma_1,\Gamma_2,\Gamma_3)$, simétrico | $\mathrm{Sym}(6,\mathbb R)$, $O(6)$ | $\dim O(6)-\dim(O(3)\times O(3))=9$ | 9 de 15 modos cero (rango exacto) |

El caso $n=6$ confirma (c) directamente: la rotación interna de cada uno de los tres bloques se alinea al **100% exacto** con el subespacio de modos cero, idéntica para los tres; ningún bloque se distingue.

**Alcance.** El Teorema 9 es un resultado negativo estructural para una clase específica y natural de potenciales, no afirma que ninguna dinámica pueda distinguir sectores, solo que esta clase amplia y simétrica no puede. Romper la conclusión requiere un ingrediente explícitamente *no* invariante bajo $G$ (candidatos: una tasa de disipación no-escalar, distinta por sector; una estructura de referencia externa; un término relacional inherentemente direccional, no simétrico entre sectores). Extender la reducción de acoplamiento débil usada en la verificación $n=6$ a acoplamiento fuerte es tarea separada, no resuelta aquí; con tres bloques (no dos) el acoplamiento genera un término de tercer orden genuino (triangular) ausente con solo dos bloques, conectando con el efecto "puramente tridimensional" ya registrado (ítem 3, §12). Ninguna de las dos rutas se ataca en este paper.

**Dos candidatos concretos ya se probaron y fallaron.** En notas exploratorias del autor, no publicadas, se atacó directamente si (a) pesos distintos por sector en el potencial, o (b) la estructura no-asociativa del álgebra de Jordan octoniónica $J_3(\mathbb O)$ (el marco natural para una composición simétrica de tres sectores) rompen la conclusión del Teorema 9 de forma *forzada*, sin ingrediente externo. **Ninguno de los dos lo logra.** (a) Levanta curvatura del Hessiano en un punto crítico específico, pero verificado vía el teorema de Noether asociado a la simetría de conjugación, la carga conservada sobrevive intacta: la ruptura observada es un efecto indirecto, no una violación de la invarianza. (b) $J_3(\mathbb O)$ preserva la simetría de permutación $S_3$ completa pese a la no-asociatividad octoniónica (consistente con que la forma cúbica de Freudenthal es parte del grupo de automorfismos $F_4$). Hasta donde se ha explorado, el ingrediente que rompería la conclusión tiene que ser genuinamente externo a $\Gamma$, no una propiedad intrínseca de ningún álgebra candidata probada.

Este teorema es el gemelo dinámico del Corolario 8.1: ese corolario muestra que la clasificación *estática* de formas es tan gruesa como algebraicamente posible; el Teorema 9 muestra que una clase amplia y natural de *dinámicas* construidas sobre esa clasificación hereda la misma ceguera entre sub-sectores de la misma fase.

---

## 9bis. Invariancia del bivector bajo eliminación de un compañero simétrico

Descubierto poniendo el álgebra a prueba fuera de los dominios habituales de este paper: mapeando datos físicos tabulados reales (electronegatividad, energía de disociación de enlace) de un átomo de hidrógeno y uno de oxígeno a objetos SAIR→Γ, y componiéndolos vía Unión+Ω para ver si el álgebra distingue el radical OH de H₂O (`brainstorming/physics/uoc_st_toroide/h2o_prueba_fuego_sair_gamma.md`).

> **▣ 〔TEO〕 Teorema 10 (Invariancia del bivector). [D]** Sean $\Gamma_A,\Gamma_B\in M_4(\mathbb R)$, $\Gamma_A=\Gamma_s^A+\Gamma_a^A$ (descomposición simétrica+antisimétrica), y $C_{AB}$ **cualquier** bloque de acoplamiento (sin restricción de estructura). Si $\Gamma_a^B=0$ (es decir, $\Gamma_B$ es simétrica) entonces la marginalización de Ω (complemento de Schur) de $B$ deja la parte antisimétrica de la configuración efectiva de $A$ exactamente inalterada:
> $$\Gamma_a\!\left(\Gamma_A - C_{AB}\,\Gamma_B^{-1}\,C_{AB}^T\right) = \Gamma_a^A$$

*Prueba.* $\Gamma_B^{-1}$ es simétrica siempre que $\Gamma_B$ lo sea. Para cualquier matriz $C$ y cualquier $M$ simétrica, $(CMC^T)^T=CM^TC^T=CMC^T$; así que el término de corrección $C_{AB}\Gamma_B^{-1}C_{AB}^T$ es simétrico sin importar $C_{AB}$. Restar una matriz simétrica de $\Gamma_A$ solo altera $\Gamma_s^A$; $\Gamma_a^A$ queda intacto. $\blacksquare$

**El recíproco, ahora derivado (cierre ago-6 2026); ver Teorema 11 más abajo.** Cuando $\Gamma_a^B\neq0$, el término de corrección genéricamente **no** es simétrico, y $\Gamma_a^A$ genéricamente cambia; incluso cuando $A$ partió con $\Gamma_a^A=0$ (un bivector nulo puede ser genuinamente creado, no solo preservado o destruido). Verificado numéricamente sobre 2000 muestras aleatorias de $(\Gamma_A,\Gamma_B,C_{AB})$ admisibles con $\Gamma_a^A=0$ inicial: eliminar un bloque sin bivector deja los bivectores de los sobrevivientes congelados a precisión de máquina ($<10^{-15}$) bajo acople completamente general (no restringido); eliminar un bloque con bivector propio inyecta un bivector genuino y creciente en un compañero que partió en exactamente cero. Esta subsección se limitaba, hasta esta ronda de cierre, a reportar esa creación de bivector como un hecho **verificado, no derivado**; el Teorema 11 identifica el mecanismo exacto que lo produce.

**Alcance.** Es un hecho estructural sobre la eliminación Ω/Schur, independiente de cualquier interpretación de dominio; vale para cualquier $(\Gamma_A,\Gamma_B,C_{AB})$ admisible que satisfaga la definición-positiva del Teorema 1 (o su generalización de Haynsworth, Teorema 8, para otras signaturas). Precisa, con una prueba en vez de una observación, el hallazgo informal anterior de que "$\Gamma_a$ nunca mezcla" bajo acoples restringidos (solo R-R): ese hallazgo no era un hecho sobre la restricción, sino un caso particular de este teorema, ya que los ejemplos restringidos eliminaban por casualidad un objeto sin contenido de bivector en las direcciones relevantes. El teorema **no** dice que Ω nunca afecta el canal simétrico; $\det$ y $\rho$ genéricamente sí cambian (§7 de este paper); solo la parte antisimétrica del objeto que **sobrevive** está protegida, y solo cuando el objeto **eliminado** no aporta parte antisimétrica.

Este teorema es el compañero estructural de los Teoremas 8–9: donde el Teorema 8 clasifica la inercia bajo colapso y el Teorema 9 muestra que la dinámica simétrica no distingue sub-sectores, el Teorema 10 identifica una tercera invariante (protegida algebraicamente, no dinámicamente) del proceso de colapso mismo.

---

## 9bis2. El mecanismo exacto de creación de bivector: descomposición recíproca/no-recíproca

**Grieta cerrada en esta ronda (ago-6 2026).** El Teorema 10 dejaba su recíproco como un hecho solo verificado: que eliminar un compañero *con* bivector inyecta bivector genuino en el sobreviviente, sin decir *por qué* ni *cuánto*. `part1/07_compositional_operations.md` §7.3.3 ya tenía, desde jul-26 2026, el teorema que cierra exactamente esa pregunta, no estaba incorporado a este paper. Se incorpora aquí, sin cambios de enunciado, y se propaga la actualización a §10, §13 y Apéndice B.

Toda la maquinaria de acoplamiento usada hasta aquí (Teoremas 1, 2, 7, 8) asume $\Gamma_{\mathrm{joint}}$ simétrica; $C_{BA}=C_{AB}^T$, acoplamiento **recíproco**. Esa suposición es la norma en este paper (enlaces químicos, resortes acoplados, fuerza de Coulomb), pero no universal: arrastre de Stokes sobre una partícula diluida en un fluido, por ejemplo, empuja al fluido sin recibir back-reacción apreciable; ambas direcciones son no-nulas (satisface la Definición 7.5 literalmente) pero no son recíprocas en magnitud.

> **▣ 〔TEO〕 Teorema 11 (Descomposición recíproca/no-recíproca de la configuración conjunta). [D]** Para $\Gamma_{\mathrm{joint}}=\begin{pmatrix}K_A&C_{AB}\\C_{BA}&K_B\end{pmatrix}$ con $K_A,K_B,C_{AB},C_{BA}$ **arbitrarios** (sin simetría, sin asumir $C_{BA}=C_{AB}^T$ en ningún punto), defínase $C_{\mathrm{eff}}=(C_{AB}+C_{BA}^T)/2$ (la parte recíproca/Hamiltoniana del acoplamiento) y $D_{\mathrm{eff}}=(C_{AB}-C_{BA}^T)/2$ (el exceso no-recíproco). Entonces, exactamente:
> $$\Gamma_s(\Gamma_{\mathrm{joint}})=\begin{pmatrix}\Gamma_s^A&C_{\mathrm{eff}}\\C_{\mathrm{eff}}^T&\Gamma_s^B\end{pmatrix},\qquad\Gamma_a(\Gamma_{\mathrm{joint}})=\begin{pmatrix}\Gamma_a^A&D_{\mathrm{eff}}\\-D_{\mathrm{eff}}^T&\Gamma_a^B\end{pmatrix}$$
>
> *Prueba.* Inmediato de $\Gamma_{\mathrm{joint}}^T=\begin{pmatrix}K_A^T&C_{BA}^T\\C_{AB}^T&K_B^T\end{pmatrix}$ y $\Gamma_s=(\Gamma_{\mathrm{joint}}+\Gamma_{\mathrm{joint}}^T)/2$, $\Gamma_a=(\Gamma_{\mathrm{joint}}-\Gamma_{\mathrm{joint}}^T)/2$ aplicado por bloques, sin complemento de Schur, sin positividad, sin reciprocidad en ningún paso. $\blacksquare$ Verificado: `models/sair/tests/test_state_system.py` (`test_reciprocity_theorem_gamma_s_*`, `test_reciprocity_theorem_gamma_a_*`); **formalizado en Lean 4, sin `sorry`** (`lean/CompositionalAlgebra/Theorem11.lean`, verificado con `#print axioms`; solo depende de los axiomas estándar de mathlib).

**Consecuencia; el mecanismo que faltaba.** Los Teoremas 1/8 (admisibilidad, Haynsworth) se aplican *sin modificación* a $\Gamma_s(\Gamma_{\mathrm{joint}})$, usando $C_{\mathrm{eff}}$ en vez del acoplamiento crudo; la maquinaria clásica nunca necesitó generalizarse, solo identificar el canal correcto. **El corolario que cierra el Teorema 10:** dos bloques puramente simétricos ($\Gamma_a^A=\Gamma_a^B=0$, pozos de potencial genuinos) acoplados de forma **no-recíproca** generan un $\Gamma_a(\Gamma_{\mathrm{joint}})=\begin{pmatrix}0&D_{\mathrm{eff}}\\-D_{\mathrm{eff}}^T&0\end{pmatrix}\neq0$; la no-reciprocidad por sí sola es una **fuente** de estructura rotacional/giroscópica que ningún subsistema poseía. Esto da una derivación (no solo una instancia verificada) del recíproco que el Teorema 10 dejaba abierto: $D_{\mathrm{eff}}$ **es** el mecanismo de inyección, identificado aquí al nivel de la configuración conjunta, antes de cualquier eliminación.

**Una segunda forma cerrada, incondicional incluso tras la eliminación.** $\det(\Gamma_{\mathrm{joint}})=\det(K_A)\cdot\det(\Omega)$, $\Omega=K_B-C_{BA}K_A^{-1}C_{AB}$, es la identidad clásica del determinante LU por bloques; exige solo $K_A$ invertible, nunca simetría ni reciprocidad, y por eso sobrevive intacta a la eliminación Ω. Es lo que sostiene el balance de entropía de §6 ($\rho=-\log|\det\Gamma|$) incluso fuera del régimen recíproco.

**Componente antisimétrica tras la eliminación.** La descomposición limpia del Teorema 11 no se propaga a través de Ω: $\Gamma_a(\Omega)$ no es, en general, una función simple de $D_{\mathrm{eff}}$ solo (verificado numéricamente; $K_A^{-1}$ entrelaza genuinamente los canales recíproco y no-recíproco durante la eliminación, porque la inversión de una matriz no-simétrica no preserva la descomposición simétrica/antisimétrica de lo que multiplica). Esto marca *exactamente* dónde el Teorema 8 (una afirmación sobre Ω, no sobre $\Gamma_{\mathrm{joint}}$) deja de generalizar: no en la composición (el Teorema 11 es exacto ahí), específicamente en la eliminación. Para ese régimen la composición lineal caso-por-caso da la respuesta, que provee `models/sair/core/state_system.py` (`StateSystem`), no una forma cerrada. Verificado: `models/calcs/brainstorming/ds/algebra_bloques_no_simetricos/03_teorema_reciprocidad.py`.

Este teorema es también el que fija, con precisión, un límite de alcance de la Definición 7.5 (Acoplamiento) que este paper no había marcado: esa definición exige solo que ambas direcciones del acoplamiento sean no-nulas, pero la maquinaria de Schur que sostiene los Teoremas 1/2/7/8 exige la condición **más fuerte** de reciprocidad en magnitud ($C_{BA}=C_{AB}^T$) en el momento en que cualquiera de los bloques propios deja de ser simétrico o el acoplamiento físico es genuinamente unidireccional. Un acoplamiento no-recíproco (tipo baño forzando a un subsistema, más que dos subsistemas modulándose mutuamente) no está todavía en el catálogo de primitivos (§5); si admite una forma cerrada al estilo Teorema 1/8, o solo la composición lineal caso-por-caso, queda abierto, no se ataca en este paper.

---

## 9ter. Las nueve operaciones catalogadas: definiciones formales

Las secciones anteriores prueban resultados *sobre* las doce operaciones citadas en el Resumen sin haberlas definido todavía dentro de este paper; se apoyaban en el nombre y en su fila de la tabla de entropía (§6). Esta sección los define, en forma compacta y usando la distinguibilidad de §4bis y los primitivos de §5, las nueve operaciones nombradas de las que las doce derivan (las tres restantes (Copia, Co-presencia, Relajación) son primitivos, ya definidos en §5). Versión completa, con ejemplos por dominio y las variantes de Acoplamiento externo/interno, en `part1/07_compositional_operations.md` §§7.3–7.8.

**▣ 〔DEF〕 Unión.** $U=A\cup B$ con $\Gamma_U=\Gamma_\mathrm{joint}$ (§4), $A,B$ distinguibles en $U$. Reversible: separable si $C_{AB}\to0$. Requiere $\rho$-proximidad ($|\rho_A-\rho_B|\leq\delta_\rho$, Corolario del Teorema 1); nivel del compuesto $\rho_U=\max(\rho_A,\rho_B)$. Ejemplo: dos átomos antes de enlazar; una coalición temporal.

**▣ 〔DEF〕 Anidamiento.** $B$ está anidada en $A$ ($B\triangleleft A$) si $V_B\subsetneq V_A$ es un subespacio estable bajo $\Gamma_A$ ($\Gamma_AV_B\subseteq V_B$) y $\Gamma_B=\Gamma_A|_{V_B}$; asimétrica ($B\triangleleft A\not\Rightarrow A\triangleleft B$), y no es sinónimo de "estar contenido": exige que $A$ module *activamente* la dinámica de $B$ (una cáscara de huevo no anida al huevo; es un límite pasivo, no un anfitrión estructural). Ejemplo: el sitio activo dentro de una enzima; una galaxia anidada en el espacio-tiempo.

**▣ 〔DEF〕 Acoplamiento.** $A\rightleftharpoons B$ si ejercen modulación epistemológica mutua ($\Gamma_E^{A\to B}\neq0$, $\Gamma_E^{B\to A}\neq0$) sin formar un compuesto: cada uno conserva su propio $\Gamma,\rho,\xi^*$, modulados por el otro. Es un estado persistente, no un evento. Distinto de Unión: en Unión se resuelve un único $\Gamma_\mathrm{joint}$; en Acoplamiento hay dos capas coexistentes; la capa de estado (cada UoC conserva su dinámica, nunca en duda) y la capa de configuración (el propio bloque $C_{AB}$ tiene dinámica emergente propia, gobernada por la EOM de §4 aplicada al bloque). Ejemplo: una relación interpersonal sostenida; dos osciladores acoplados.

**▣ 〔DEF〕 Fusión.** $F$ tal que $\{S,A,I,R\}_F$ son variables nuevas (no sumas de las de $A,B$), $\Gamma_F$ sin bloque recuperable; $A,B$ indistinguibles en $F$, dejan de existir por separado. Irreversible en general. Ejemplo: fecundación (dos gametos → un cigoto).

**▣ 〔DEF〕 Absorción.** $A\leftarrow B$: $A$ persiste modificado, $\Gamma_{A'}=\Gamma_A-C_{AB}\Gamma_B^{-1}C_{AB}^\top$ (el complemento de Schur; la forma explícita del mapa de modificación, antes sin especificar); $B$ pierde identidad. Asimétrica: $A\leftarrow B\not\cong B\leftarrow A$. Ejemplo: endosimbiosis mitocondrial.

**▣ 〔DEF〕 Fisión.** Separación de $C$ en $\{A,B,\ldots\}$, exhaustiva ($V_A\oplus V_B\oplus\cdots=V_C$), con $\Gamma_i=\pi_i\Gamma_C\pi_i^T$ por restricción y los bloques cruzados descartados. Para $P$ cuadrático, $\|\Gamma_C\|_F^2=P(\Gamma_A)+P(\Gamma_B)+2\|\pi_A\Gamma_C\pi_B^T\|_F^2\geq P(\Gamma_A)+P(\Gamma_B)$: la energía libre no aumenta bajo fisión; teorema, no conjetura, en ese régimen (subaditividad conjeturada para $P$ no cuadrático). Ejemplo: división celular.

**▣ 〔DEF〕 Desacoplamiento.** $C_{AB}\to0$ con redistribución de la energía de acoplamiento hacia $\Gamma_{A'},\Gamma_{B''}$, no deja los bloques intactos; la regla exacta es la proyección modal multi-modo vía SVD (`part1/07_compositional_operations.md`, Definiciones 7.9a–f), y el residuo no atribuible a ninguno de los dos es la cohesión irreducible $\mathcal B(A,B)$ del Teorema 3 (§6). Ejemplo: ruptura de un enlace de van der Waals ($\mathcal B=0$, exacto) vs. covalente ($\mathcal B=\|C_{AB}\|_F$, irreducible).

**▣ 〔DEF〕 Reproducción.** $A$ genera $B$ con $\Gamma_B^{(0)}\approx\Gamma_A$ (o $\Gamma_A(\xi^*_A)$); $A$ persiste (posiblemente modificado); $B$ evoluciona después de forma independiente; distinta de Copia (aquí $B$ no queda atado a seguir siendo copia) y de Fisión (aquí $A$ persiste, no se consume en la separación). Ejemplo: división celular con herencia imperfecta (mutación).

**▣ 〔DEF〕 Disolución.** $A$ se disuelve cuando, sin forzamiento externo ($F_\mathrm{ext}\to0$), el flujo de gradiente lleva $\Gamma_A$ al mínimo global de $P$, perdiendo su atractor local. Es dispersión, no aniquilación (§5ter): terminal y no generativa; a diferencia de la Fisión, no produce sub-UoCs identificables nuevas. Ejemplo: muerte de un organismo; la estructura mantenida se relaja al cesar el forzamiento; los componentes se dispersan, no desaparecen.

---

## 10. Clasificación estructural (dos ejes, tres valores cada uno)

La clasificación original (identidad preservada/perdida × reversible/irreversible) sub-representaba el álgebra: la Fisión tiene $\Delta\rho\leq0$, un tercer signo no contemplado por la dicotomía binaria. La versión completa:

| | $\Delta\rho<0$ | $\Delta\rho=0$ | $\Delta\rho>0$ |
|---|---|---|---|
| **Identidad preservada** | Desacoplamiento (SVD, $\mathcal B>0$) | Co-presencia; Desacoplamiento (Schur); Anidamiento | Unión; Acoplamiento |
| **Identidad perdida** | Absorción ($\Delta_{\mathrm{couple}}<\rho_B$) | Absorción (frontera, no genérico) | Fusión; Absorción; Disolución |
| **Generativa (cardinalidad cambia)** | Fisión | (excluida) | Reproducción; Copia |

Dos celdas están vacías, y ambas son **predicciones falsables genéricas** (no exclusiones de frontera de medida cero): identidad-perdida×$\Delta\rho=0$ solo ocurre en el punto exacto $\Delta_{\mathrm{couple}}=\rho_B$ de Absorción; generativa×$\Delta\rho=0$ requiere $\rho_B\to0$ (copia sin estructura, degenerada).

**Tabla de invariantes.** La clasificación anterior organiza las operaciones por su efecto sobre identidad y entropía; la siguiente tabla las organiza por qué cantidades algebraicas preservan; una lectura complementaria, más cercana a cómo se leería este álgebra en el lenguaje estándar de teoría de invariantes.

| Operación | Rango | Firma/inercia | $\det$ | Espectro | $\|\cdot\|_F$ | $\mathcal B$ |
|---|---|---|---|---|---|---|
| Co-presencia $\oplus$ | preservado (suma directa) | preservada por bloque | multiplicativo | unión de espectros | $\|\Gamma_A\|_F^2+\|\Gamma_B\|_F^2$ | n/a ($C=0$) |
| Acoplamiento/Unión | preservado | preservada si admisible (Teo. 1) | crece ($\times\det(I-\Xi^T\Xi)^{-1}$, Prop. 1) | mezclado, no preservado | crece | define $\mathcal B$ |
| Desacoplamiento (Schur) | preservado | preservada | inverso exacto del acoplamiento | recuperado exactamente | recuperada exactamente | $\mathcal B=0$ por construcción |
| Desacoplamiento (SVD) | preservado | preservada | aproximado | aproximado | aproximada | $\mathcal B\geq0$, mide la falla |
| Fusión/Absorción | reducido (colapso $\Omega$) | la de $S_A$ (Haynsworth, Teo. 8) | el del complemento de Schur | el de $S_A$, no el de $\Gamma_{AB}$ | no preservada | no aplica tras colapso |
| Copia | duplicado | duplicada | duplicado | duplicado | duplicada | n/a |
| Relajación (RELAX) | preservado genéricamente | puede cambiar cerca de $\det=0$ (Teo. 8/Cor. 8.1) | $\to\arg\min P$ | fluye a lo largo del gradiente | decrece monótonamente ($P$, no $\|\cdot\|_F$ necesariamente) | n/a |

La fila más informativa es Fusión/Absorción: el Teorema 8 (Haynsworth) es exactamente la afirmación de que la **inercia**, no el rango ni el determinante por sí solo, es la cantidad que se preserva de forma aditiva bajo colapso, generalizando lo que el Teorema 1 ya mostraba en el caso restringido a $\Gamma_A,\Gamma_B\succ0$.

---

## 11. Correspondencias ilustrativas 〔CE〕

Estos tres ejemplos muestran que el álgebra es *aplicable*, no que deriva física nueva desde cero. Cada uno usa exclusivamente la maquinaria de §§4–10, sin postulados adicionales.

### 11.1 Fuerza de Coulomb y Lorentz desde el morfismo de Acoplamiento 〔CE〕 [D]

**Γ del caso (SAIR):** dos UoCs cargadas $A,B$ con bloque de acoplamiento $C_{12}=q\,A_\mu\otimes u_\nu$ (producto exterior entre potencial y cuadrivelocidad).

**Descomposición:** $\Gamma_s(C_{12})\to$ fuerza conservativa (Coulomb), $\Gamma_a(C_{12})\to$ fuerza reactiva (magnética/Lorentz). Verificado numéricamente a precisión de máquina: caso Coulomb puro ($v=0$) da $\|\Gamma_s\|=1$, $\|\Gamma_a\|=0$; caso magnético da la fuerza de Lorentz completa $f=q(E+v\times B)$; el observable $\mathcal C(C_{12})$ (coherencia, Ch5) transita de $0$ (Coulomb, bloque simétrico) a $1$ (Josephson, bloque antisimétrico); una firma limpia del tipo de interacción.

### 11.2 Independencia estadística vía co-presencia $\oplus$ 〔CE〕 [D]

> **▣ 〔CE〕** $Z_{AB}=Z_A\cdot Z_B \iff \Gamma_{AB}=\Gamma_A\oplus\Gamma_B$, con
> $Z_\mathrm{Gauss}(\Gamma)=(\det\Gamma)^{-1/2}$ (Lema 7.1, Ch7; $\Gamma_\mathrm{joint}$ leída
> como matriz de precisión Gaussiana) y $\rho=2\log Z_\mathrm{Gauss}$, **exacto, sin postular
> $\beta=\rho$** (corrección jul-11/12 2026: la versión anterior de esta fila usaba
> $Z(\rho)=\mathrm{tr}(e^{-\rho\Gamma})$, que sí exige $\beta=\rho$; un postulado refutado por 6+
> rutas independientes en otro lugar del programa, ver `insight_t3_status.md`; esa construcción
> nunca hizo falta aquí). *Prueba:* bloque diagonal $\Rightarrow\det$ factoriza
> $\Rightarrow Z_\mathrm{Gauss}$ factoriza; el recíproco se sigue de que $\det\Gamma$ determina el
> volumen Gaussiano conjunto.

El gas ideal de $N$ partículas es $\Gamma_N=\Gamma_1^{\oplus N}$, $Z_N=Z_1^N$; el resultado estándar, ahora como co-presencia iterada. La frontera de fusión ($\det\Gamma_{\mathrm{joint}}\to0$) es exactamente la condición termodinámica de formación de un estado ligado.

### 11.3 El espectro del enlace químico vía cohesión $\mathcal B$ 〔CE〕 [D]

Van der Waals ($\mathcal B=0$, decoupling exacto) → iónico ($0<\mathcal B<\|C_{AB}\|_F$, residuo parcial) → covalente ($\mathcal B=\|C_{AB}\|_F$, irreducible) es la lectura directa del Teorema 3 sobre un continuo de bloques de acoplamiento, sin ningún parámetro nuevo.

**Esta es una correspondencia de forma, no validada con datos.** $\mathcal B$ nunca se evaluó aquí sobre datos reales de átomos tabulados; la progresión vdW→iónico→covalente es una analogía cualitativa sobre la *forma* del espectro de $\mathcal B/\|C_{AB}\|_F\in[0,1]$, no un ajuste a moléculas concretas. §11.4, que sí usa datos reales para una pregunta distinta (Teorema 10), encontró que reproducir comportamiento químico real desde constantes tabuladas es sensible al mapeo SAIR→Γ y no funcionó a parámetros físicamente realistas sin una normalización estrecha y no principiada. Las dos preguntas son distintas ($\mathcal B$ clasifica la descomponibilidad del propio bloque de acoplamiento; el Teorema 10 concierne si Ω puede alterar el bivector de un compañero) y no están en conflicto, pero el estatus [D] de esta subsección debe leerse como "derivado dado el bloque de acoplamiento", no como "validado contra química real".

### 11.4 OH vs. H₂O: el Teorema 10 en un ejemplo concreto, y sus límites 〔CE〕 [D]/[V]

**Γ del caso (SAIR), con datos tabulados reales, no ilustrativos:** $\rho_H=2.20$, $\rho_O=3.44$ (electronegatividad de Pauling); $\Gamma_a^H=0$ (H es $1s^1$, $l=0$, sin momento angular); $\Gamma_a^O=$ dos rotaciones en planos ortogonales (O es $2p^4$, regla de Hund: 2 electrones desapareados); $q_{HO}=D_{OH}/D_{HH}=463/436\approx1.062$ (energías de enlace de tablas de termoquímica). Cada enlace O–H empalma el electrón de H con el plano de momento angular de O que ese enlace satura.

**Aplicación directa del Teorema 10:** dado que $\Gamma_a^H=0$, el teorema **prohíbe, por razones puramente estructurales**, que el carácter orbital/bivector de O cambie al enlazarse con hidrógenos, sin importar cómo se modele el acoplamiento. Verificado exactamente: el residuo antisimétrico de O queda congelado a $<5\times10^{-16}$ para OH (1 enlace) y H₂O (2 enlaces), a cualquier intensidad de acople.

**Lo que el teorema no garantiza; y donde el ejemplo revela el límite real del programa:** el canal simétrico ($\det$) sí distingue OH de H₂O cualitativamente (a intensidad de acople $\lambda=2.0$, OH cruza a $\det<0$ mientras H₂O permanece justo positivo), pero **solo al doble de la energía de enlace física real**; a $\lambda=1$ (el acople físico real) ninguno de los dos cruza. Un diagnóstico en reversa (`brainstorming/physics/uoc_st_toroide/h2o_reversa_algebra_vs_sair.md`), fijando el álgebra y variando solo el mapeo SAIR, encontró: (i) la ventana de éxito es angosta ($\sim10\%$ relativo) y las normalizaciones más naturales para $q_{HO}$ (energías de enlace típicas H-H, C-H, N-H) caen todas fuera de ella; (ii) cambiar $\rho$ de electronegatividad a energía de ionización (donde H y O son casi idénticos) mata el cruce de H₂O por completo; (iii) incluso con $\rho$ idénticos para H y O (sin ninguna asimetría física real) el álgebra **ya** produce una transición cualitativa; evidencia de que la composición misma tiene la capacidad estructural necesaria.

**Interpretación.** El fallo en reproducir la estabilidad de H₂O a escala física real es predominantemente un problema del **mapeo SAIR** (no hay todavía un principio que fije de forma no arbitraria las unidades y escala de $\rho,q$ para un dominio nuevo como la química), no de la **composición algebraica** (Unión+Ω), que es la misma maquinaria ya verificada en los Teoremas 1–9 sin modificación alguna.

### 11.5 Clausura operacional (autopoiesis): hasta dónde llega la base de cinco primitivos 〔DEF〕[D]

Sea $\Phi=\textsf{RELAX}\circ\Omega\circ\textsf{COUPLE}\circ\textsf{JOIN}\circ\textsf{COPY}$ un **ciclo de producción**: una UoC copia una plantilla de su propia configuración ($\textsf{COPY}$), la reintegra con su propio estado en decaimiento ($\textsf{JOIN}+\textsf{COUPLE}+\Omega$), y mantiene el resultado contra el desgaste ($\textsf{RELAX}$). Una UoC es **operacionalmente cerrada** (autopoiética) si su configuración es un punto fijo de su propio ciclo de producción: $\Phi(\Gamma^\ast)=\Gamma^\ast$.

Tres precisiones fijan su estatus. **(i)** No es un primitivo nuevo; $\Phi$ se construye enteramente con los cinco primitivos ya cerrados en el Teorema 2; la clausura operacional es un punto fijo del álgebra existente (verificado: como $\Omega$ es homogénea de grado 1, el multiplicador del ciclo es exacto y la clausura es el punto marginal entre proliferación y disolución; `models/calcs/brainstorming/ch7/autopoiesis_punto_fijo.py`). **(ii)** Por el segundo principio de esta álgebra ($\Delta\rho\geq0$, §6), cada colapso $\Omega$ sube la entropía estructural, así que la clausura no puede ser un equilibrio pasivo; es un estado estacionario disipativo que exige trabajo estructural continuo, igual que la persistencia de un solo UoC bajo forzamiento externo. **(iii)** La condición de punto fijo por sí sola está ajustada finamente (multiplicador exactamente uno); la versión robusta (la condición sostenida dentro de una banda de viabilidad por regulación homeostática) es la forma viva de la clausura, y queda fuera del alcance puramente algebraico de este paper.

Este resultado es el cierre natural de la base de cinco primitivos: con $\Omega$ dando el colapso sistema→individuo y $\Phi$ dando el punto fijo auto-regenerativo, la aritmética de composición alcanza a expresar no solo cómo se construye una estructura, sino cómo puede sostenerse a sí misma; el umbral algebraico, no todavía dinámico, donde la composición se vuelve organización persistente. Desarrollo completo (dinámica de la banda de viabilidad, regulación homeostática): `part1/07_compositional_operations.md` §7.8.3.

---

## 12. Historial de verificación y conjeturas descartadas

Esta sección documenta el proceso de verificación, incluyendo lo que se descartó.

1. **Numeración duplicada (grave, corregida).** Las Definiciones 7.10–7.15 de la versión-libro colisionaban con seis definiciones preexistentes de igual número; renombradas a un esquema sin colisión antes de esta redacción.
2. **Conflación de dos monedas de entropía (corregida).** Una versión anterior citaba el Teorema 5 ($\Delta P$) para justificar afirmaciones sobre $\Delta\rho$ (Prop. 1); dos cantidades que §7 (Teorema 6) demuestra son independientes. Corregido: cada afirmación de balance en este paper cita explícitamente cuál de las dos monedas usa, sin mezclarlas.
3. **Conjetura de signos mixtos en cascada; muerta en su forma simple, generalizada vía Haynsworth. [D]+[V]** Se investigó si los determinantes anidados de una cascada de tres cuerpos (Teo. 4) podrían tomar signos independientes (+/0/−). **Resultado dentro del régimen admisible (Teo. 1): los complementos de Schur de una matriz definida positiva son siempre definidos positivos** (hecho estándar de álgebra lineal); los tres determinantes anidados son siempre $(+,+,+)$; el único cruce a signo negativo coincide con la frontera $\sigma_{\max}=1$ ya conocida. Verificado: 3000 muestras, 0 excepciones (`schur_cascade_signs_check.py`). **Este resultado negativo llevó al Teorema 8 (§8):** la restricción SPD es exactamente lo que fuerza $(+,+,+)$; removerla da la ley general de Haynsworth (1968), que compone la inercia *aditivamente* para cualquier signatura de entrada, no una nueva conjetura numérica sino un teorema clásico, verificado aquí en el contexto composicional (2000+3000 muestras, 0 violaciones). El resultado revela que la tripartición det-signo es la clasificación más gruesa posible de la inercia (dos fases genéricas + una frontera delgada), pero deja abierta una pregunta puramente matemática sobre si el flujo dinámico de $P$ selecciona estructura más fina dentro de esa clasificación gruesa.
4. **Omisión sin explicar en la clasificación de dos ejes (corregida).** Fisión y Reproducción no encajaban en la dicotomía binaria original; generalizada a tres valores por eje (§10), con las dos celdas vacías re-verificadas como exclusiones genéricas consistentes entre sí.
5. **La pregunta abierta del ítem 3, atacada; respuesta parcial vía el Teorema 9 (§9). [D]+[V]** El ítem 3 dejó abierto si el flujo dinámico de $P$ selecciona estructura más fina dentro de la clasificación gruesa de Haynsworth. Atacado desde un ángulo específico: ¿puede un potencial invariante de conjugación (la clase a la que pertenece $P(\Gamma)=\|\Gamma\|_F^2+\mu\det\Gamma$) distinguir sub-sectores que comparten fase? **Resultado: no, nunca, para esta clase de potenciales** (Teorema 9, verificado en $n=3,4,6$). Esto no cierra la pregunta del ítem 3; la sharpens: cualquier selección dinámica de estructura fina requeriría romper explícitamente la invarianza de conjugación, un ingrediente que no está en $P$ tal como se usa en este paper.
6. **Composición aplicada a un caso químico real (H₂O), ver §9bis y §11.4. [D]+[V]/negativo.** Se usó el álgebra para reproducir un hecho químico concreto (H₂O estable, OH inestable) con datos tabulados reales (electronegatividad, energía de enlace). El intento directo **falló** a parámetros físicamente realistas (§11.4), pero sacó a la luz el Teorema 10 (§9bis), un hecho estructural sobre la eliminación Ω que no se había buscado. Diagnóstico (`h2o_reversa_algebra_vs_sair.md`): el fallo es del mapeo SAIR→Γ (unidades/normalización sin principio físico que las fije), no de la composición algebraica; la misma maquinaria (Unión+Ω) que da los Teoremas 1–9 sin cambios.

---

## 13. Estatus de los resultados

| Resultado | Registro | Estatus |
|---|---|---|
| Cota de admisibilidad (Teo. 1) | 〔TEO〕 | [D] |
| Clausura de la base primitiva (Teo. 2) | 〔TEO〕 | [D]: incondicional en $P$ desde la prueba geométrica del Lemma 1 (§5) |
| Identidad de Schur (Prop. 1) | 〔TEO〕 | [D] |
| Balance de entropía, 12 operaciones | 〔TEO〕 | [D] + [V] (todas verificadas numéricamente) |
| Cohesión y reversibilidad (Teo. 3) | 〔TEO〕 | [D] + [V] |
| Cascada, trabajo, espontaneidad (Teos. 4–6) | 〔TEO〕 | [D] + [V] |
| Relación exacta $\rho\leftrightarrow P$ (Teo. 7) | 〔TEO〕 | [D] + [V] |
| Aditividad de inercia de Haynsworth (Teo. 8, §8) | 〔TEO〕 | [D] + [V]: clásico (1968), aplicado aquí al caso composicional |
| Sin sub-sector privilegiado bajo potenciales invariantes (Teo. 9, §9) | 〔TEO〕 | [D] + [V] ($n=3,4,6$): negativo estructural, alcance explícito |
| Tripartición det-sign = clasificación más gruesa de inercia, cualquier $n$ | 〔TEO〕 | [D]: hecho de geometría algebraica real |
| Conjetura ingenua de signos mixtos en cascada | | **descartada [V negativo]**, ver Teo. 8 |
| Estructura fina de inercia (15 clases, $n=4$) seleccionada dinámicamente por $P$ | | **[F] pregunta matemática abierta, no atacada** |
| Coulomb/Lorentz, gas ideal, enlace químico vía $\mathcal B$ (§11.1–11.3) | 〔CE〕 | [D]: correspondencia de forma, no validada con datos reales |
| Invariancia del bivector bajo Ω-eliminación de un compañero simétrico (Teo. 10, §9bis) | 〔TEO〕 | [D]: converso ahora **derivado**, no solo verificado (ver Teo. 11) |
| Descomposición recíproca/no-recíproca de $\Gamma_{\mathrm{joint}}$ (Teo. 11, §9bis2) | 〔TEO〕 | [D] + [V]: formalizado en Lean 4 sin `sorry`; cierra el converso del Teo. 10 |
| OH vs. H₂O, aplicación concreta del Teo. 10 con datos reales (§11.4) | 〔CE〕 | [D] (teorema) + **negativo** (canal simétrico no reproduce estabilidad a escala real; fallo trazado al mapeo SAIR) |
| Auto-Acoplamiento (Def. 7.19, §5bis) | 〔DEF〕 | [D] la definición + instancia verificada; [F] su desarrollo completo (relación con $\gamma\dot\Gamma$, con Copia) |
| Esclavización (Def. 7.20, §5bis) | 〔DEF〕 | [D] la definición + instancia verificada |
| Acoplamiento-externo/interno y absorción-de-gauge (§5bis) | 〔DEF〕 | [D]: no son primitivos nuevos, son nombres para usos ya presentes en Acoplamiento |
| Completitud de generación de la base primitiva (§5bis) | | **[F] pregunta abierta, distinta de la completitud del catálogo (Teo. 2), no atacada** |
| Distinguibilidad (proyecciones + razón de participación) (§4bis) | 〔DEF〕 | [D] |
| Las nueve operaciones catalogadas, definidas formalmente (§9ter) | 〔DEF〕 | [D]: cierra la deuda de §5–§10, que las usaba sin definirlas en este paper |
| Tipo algebraico (magma conmutativo, flexible, power-asociativo) (§5ter) | 〔TEO〕 | [D] + [V] |
| Ausencia de operación de aniquilación (§5ter) | 〔TEO〕 | [D]: consecuencia de conservación (termo + Noether), no una elección de diseño |
| Clausura operacional / autopoiesis (§11.5) | 〔DEF〕 | [D] el punto fijo algebraico; [F] su forma viva/regulada (fuera de alcance) |

**Fronteras nombradas:** (i) el álgebra es exacta para cualquier $P$ (Lemma 1, §5), pero la *dinámica* construida encima bajo $P$ no-cuadrático (estabilidad estructural del flujo, bifurcaciones) no se aborda aquí; (ii) la relación exacta entre las dos monedas de entropía queda como dos leyes complementarias, no una identidad; (iii) capa cinética (tasas, barreras, catálisis) fuera de alcance; el álgebra es cinemática, no dinámica de velocidades; (iv) la completitud de generación de la base primitiva (§5bis) queda abierta, distinta de la completitud del catálogo ya cerrada por el Teorema 2. El álgebra como estructura categórica (Apéndice A) es una quinta frontera, tratada aparte por su estatus [A].

---

## 14. Discusión y cierre

La promesa de la introducción (§3) era que las doce operaciones composicionales fenomenológicas se reducirían a un puñado de primitivos y una sola identidad de balance de entropía. Esa promesa se cumple sin excepciones marcadas [A] en el cuerpo principal: la clausura (Teorema 2), el balance completo (§6), y las cotas de trabajo/espontaneidad (§7) son todas [D]+[V]. Las dos extensiones más allá del régimen originalmente admisible (Haynsworth, §8; el negativo estructural del Teorema 9, §9) no eran parte del plan original; surgieron de investigar por qué una conjetura ingenua sobre signos en cascada moría (§12, ítem 3), y terminaron revelando algo más interesante que la conjetura misma: la clasificación por signo de determinante, usada en todo este programa desde el principio, es la partición más gruesa posible de la inercia, y ningún potencial invariante de conjugación puede romperla dinámicamente entre sub-sectores que comparten fase. Ninguno de los dos resultados estaba anticipado; ambos son, en retrospectiva, consecuencias directas de tomarse en serio qué es exactamente $\Gamma_s$ como objeto algebraico.

**Problemas abiertos.** Cuatro fronteras nombradas (§13) marcan dónde termina lo demostrado: la dinámica del flujo bajo $P$ no-cuadrático (el álgebra en sí es incondicional), la relación entre las dos monedas de entropía, la capa cinética completa, y la completitud de *generación* de la base primitiva (§5bis); distinta de la completitud del catálogo que el Teorema 2 sí cierra: dos primitivos encontrados en el frente de campos continuos (Auto-Acoplamiento, Esclavización) después de probar ese teorema muestran que la lista de primitivos pudo no estar completa desde el inicio, y no hay todavía un argumento que descarte un séptimo. A estas se suma la pregunta que cierra el Teorema 9; qué ingrediente, explícitamente no invariante bajo conjugación, sería necesario para romper la ceguera entre sub-sectores; que este paper deja sin atacar por diseño: es una pregunta de física concreta (qué es ese ingrediente en un sistema real), no de álgebra composicional en abstracto, y pertenece al siguiente nivel del programa, no a este paper. La línea categórica del Apéndice A es una sexta frontera, ya con avance real pero sin cerrar.

Un paper posterior extiende la maquinaria composicional a sistemas continuos; fluidos y campos, donde $\Gamma$ deja de ser una matriz finita y la composición se vuelve una operación sobre campos acoplados en el espacio. La pregunta central se mantiene idéntica en espíritu: ¿qué operaciones son admisibles, y cómo se balancea la entropía cuando se componen?; solo que ahora sobre un espacio de configuraciones de dimensión infinita. Si el álgebra de este paper es, como se argumenta aquí, una consecuencia de la estructura de bloques y la identidad de Schur más que de la dimensión finita específica de $\Gamma$, debería sobrevivir ese paso, pero eso, como todo lo demás en este programa, se dice para verificarse, no para asumirse. Dos rutas adicionales quedan señaladas: (i) terminar de formalizar el puente categórico del Apéndice A; en particular, la ley de cociclo de la 2-celda $\Delta_2$ y el ensamblaje en los axiomas estándar de una 2-categoría laxa; (ii) investigar si el resto de la firma fina de inercia (más allá de la tripartición por signo, §8); por ejemplo, si el flujo de gradiente de $P$ estabiliza preferentemente firmas específicas como $(2,2,0)$ frente a $(3,1,0)$ en $n=4$; tiene contenido dinámico, la pregunta que el Corolario 8.1 deja explícitamente abierta.

---

## Apéndice A. Trabajo en curso: el álgebra como multicategoría enriquecida sobre $\Delta\rho$ [A]

*Esta sección se mantiene fuera del cuerpo principal (§1–§14) porque su estatus es [A] en conjunto, no [D]/[V]; se documenta aquí en vez de omitirse, pero no forma parte de lo que este paper certifica como cerrado.*

Construir un instrumento interactivo con ejemplos trabajados para los cinco primitivos (§5) reveló algo ausente tanto de los tratamientos categóricos estándar de composición (Baez-Fong, Span/Cospan, PROPs, operads) como de la termodinámica clásica de procesos: una **cinemática explícita**. Mover un parámetro físico continuo no salta entre operaciones discretas; fluye continuamente de Unión a Acoplamiento a Fusión, con $\Delta\rho$ variando suavemente todo el tiempo. Las categorías ordinarias (enriquecidas sobre Conjuntos) no tienen forma nativa de portar esa cinemática; sus morfismos son flechas sin magnitud.

**El encaje.** Lawvere (1973) mostró que un espacio métrico $(X,d)$ es una categoría enriquecida sobre $([0,\infty],+,\geq)$: el "hom" entre dos puntos es el número $d(x,y)$, no un conjunto de flechas, y la composición categórica es la desigualdad triangular. La Proposición 1 de este paper ($\rho_{AB}=\rho_A+\rho_B+\Delta_{\mathrm{couple}}$, $\Delta_{\mathrm{couple}}\geq0$) ya es exactamente ese ingrediente; aditividad de un costo no-negativo bajo composición.

*Nota de numeración: los resultados de esta sección no se etiquetan "Teorema 12, 13..."; a diferencia de los Teoremas 1–11 del cuerpo principal (todos [D]), este apéndice permanece [A] en conjunto, así que sus piezas individuales quedan sin promover a la numeración formal hasta que la estructura completa se cierre.*

**▣ 〔DEF〕 Multicategoría entrópica $\mathcal U$.** Objetos: UoCs, $\Gamma\in M_4(\mathbb R)$. Morfismo $n$-ario $(A_1,\dots,A_n)\to B$: colapso simultáneo admisible, donde $B$ es el complemento de Schur de un input retenido tras eliminar los $n-1$ restantes como un solo bloque conjunto. Peso: $w(A_1,\dots,A_n\to B):=\rho(B)-\rho(A_{\mathrm{retenido}})$; generaliza $\Delta_{\mathrm{couple}}$ directamente para $n=2$.

**▣ 〔TEO〕 No-negatividad del peso. [D]** Para $\Gamma_{\mathrm{joint}}$ definida-positiva, $w\geq0$. *Prueba.* Partiendo $\Gamma_{\mathrm{joint}}$ en dos bloques (el retenido y el bloque conjunto de los $n-1$ eliminados (con sus acoplamientos mutuos)) la desigualdad de Fischer (generalización de Hadamard a bloques, válida para toda matriz PD) da $\det\Gamma_{\mathrm{joint}}\leq\det(\text{bloque eliminado})\cdot\det(A_{\mathrm{retenido}})$, i.e. $\rho_{\mathrm{joint}}\geq\rho(\text{bloque eliminado})+\rho(A_{\mathrm{retenido}})$. La identidad de Schur da $\rho(B)=\rho_{\mathrm{joint}}-\rho(\text{bloque eliminado})$ exactamente. Combinando: $\rho(B)\geq\rho(A_{\mathrm{retenido}})$. $\blacksquare$ Verificado en 2995 configuraciones aleatorias confirmadas PD ($n\in[2,5]$), cero violaciones (`models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/correccion_peso_n_ario.py`). **La definida-positividad de $\Gamma_{\mathrm{joint}}$ es hipótesis necesaria**; una versión anterior de esta definición sumaba la entropía de los $n$ inputs (no solo del retenido) y reclamaba no-negatividad "por Hadamard generalizado"; esa fórmula da $w<0$ en ~3% de configuraciones PD para $n\geq3$, corregida antes de escribir esta sección.

**La no-asociatividad de Fusión es la desigualdad triangular estricta, no un defecto.** Dos secuencias de composición binaria que llegan a los mismos objetos finales son dos factorizaciones distintas del mismo morfismo $n$-ario, y el enriquecimiento de Lawvere solo garantiza $w(\text{directo})\leq w(\text{vía intermedio})$, no igualdad; exactamente donde $\Omega$ actúa irreversiblemente; desaparece donde la composición es reversible (Unión, Acoplamiento sin colapso, Desacoplamiento por Schur).

**Dos piezas adicionales, verificadas pero no ensambladas en una estructura formal única.** (i) **Ley de unidad [D]:** $\mathrm{id}_A$ es el caso degenerado $n=1$ de la misma maquinaria ($w=0$ exacto), y sustituirlo en cualquier posición de un morfismo mayor deja objeto y peso total sin cambio; verificado en 6 configuraciones independientes, exacto a precisión de máquina.

(ii) **RELAX no conmuta con $\Omega$, con una 2-celda de corrección de forma cerrada [D].** Relajar dos inputs por separado bajo su propio potencial antes de colapsar difiere genuinamente de colapsar primero y relajar el resultado. Esa brecha no es un fracaso genérico: escala exactamente como $O(\|C\|^2)$ (ajuste log-log, exponente $2.0014\pm0.0006$ en 10 configuraciones aleatorias, `ley_intercambio_2categoria.py`); la firma de una **2-categoría laxa** (objeto categórico establecido), no una categoría estricta. Más aún, esa 2-celda de corrección tiene **forma cerrada, verificada exacta**: escribiendo $C=\varepsilon\tilde C$, el complemento de Schur es exactamente cuadrático en $C$, y a orden líder

$$\Delta_2(A,B,C,t) = J_B(t)\!\left[\tilde C^T A^{-1}\tilde C\right] - \tilde C^T A_t^{-1}\tilde C,$$

donde $J_B(t)$ es la derivada direccional del flujo de RELAX en $B$; la discrepancia entre evaluar la corrección de acoplamiento en el bloque ya relajado versus empujar la corrección original a través de la linealización del flujo. Verificado: error relativo $0.0000$ entre esta fórmula y la diferencia numérica real en 8 configuraciones independientes (`forma_cerrada_2celda.py`). RELAX es esa 2-celda: una deformación continua *dentro* de una forma combinatoria fija, gobernada por el gradiente de $P$, con los colapsos $n$-arios como 1-morfismos. Solo faltan las leyes de coherencia de orden superior de la estructura laxa completa; eso permanece [A].

Finalmente, la operación subyacente de Schur coincide, verificada en dos topologías de circuito contra dos métodos independientes (transformación estrella-triángulo cerrada, análisis nodal de Kirchhoff), con la regla de composición del *black-box functor* de Baez-Fong para redes lineales pasivas (su "reducción de Kron"); $\mathcal U$ parece ser un levantamiento enriquecido genuino de ese marco categórico, no solo adyacente a él.

**Estado.** [A] en conjunto; cada pieza individual (no-negatividad del peso, ley de unidad, no-conmute de RELAX con su escalado cuadrático y forma cerrada, el cociclo del Jacobiano que rige su coherencia temporal, coincidencia con Baez-Fong) verificada por separado, con la 2-celda de corrección $\Delta_2$ siendo el hallazgo más cercano a una propiedad genuinamente nueva de este álgebra, no una aplicación de matemática ya conocida. Pendiente: la ley de cociclo de $\Delta_2$ en sí (cómo se acumula sobre relajación partida) todavía no está formulada con precisión (un intento inicial resultó ser una comparación mal planteada, no una verificación) y el ensamblaje final en los axiomas estándar de una 2-categoría laxa de la literatura categórica. Desarrollado en extenso en `brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere.md`.

---

## Apéndice B. Verificación numérica

Todos los resultados load-bearing del cuerpo principal (§1–§14) y del Apéndice A están verificados en:
- `models/calcs/brainstorming/ch7/thm73_cohesion_entropy_bound.py`
- `models/calcs/brainstorming/ch7/algebra_termodinamica_cierre.py`
- `models/calcs/brainstorming/ch7/delta_rho_admissibility_bound.py`
- `models/calcs/brainstorming/ch10/rho_P_exact_relation.py`
- `models/calcs/brainstorming/uoc_st/schur_cascade_signs_check.py` (resultado negativo, §12.3)
- `models/calcs/brainstorming/uoc_st/haynsworth_inertia_cascade.py` (Teorema 8, §8)
- `models/sair/tests/test_state_system.py` (Teorema 11, §9bis2; `test_reciprocity_theorem_gamma_s_*`/`_gamma_a_*`)
- `models/calcs/brainstorming/ds/algebra_bloques_no_simetricos/03_teorema_reciprocidad.py` (Teorema 11, no-supervivencia de la descomposición bajo Ω, §9bis2)
- `lean/CompositionalAlgebra/Theorem11.lean` (Teorema 11, formalización Lean 4 sin `sorry`, incluido con este paper)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/correccion_peso_n_ario.py` (no-negatividad del peso, Apéndice A)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/ley_unidad_prueba.py` (ley de unidad, Apéndice A)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/relax_vs_colapso.py` (no-conmute de RELAX, Apéndice A)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/ley_intercambio_2categoria.py` (escalado $O(\|C\|^2)$ de la brecha de intercambio, Apéndice A)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/forma_cerrada_2celda.py` (forma cerrada de la 2-celda de corrección $\Delta_2$, Apéndice A)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/coherencia_orden_superior.py` (cociclo del Jacobiano, Apéndice A)
- `models/calcs/brainstorming/papers/draf_algebra_uoc/multicategoria_lawvere/funtor_baez_fong.py` (funtor Baez-Fong/reducción de Kron, Apéndice A)

## Referencias

Este paper se apoya en trabajo previo, todavía no publicado, del mismo programa de investigación
(el objeto $\Gamma$ y la Unidad de Coherencia; el potencial estructural $P(\Gamma,\rho)$ de Ch13)
, resumido de forma autocontenida al inicio de este documento, sin exigir al lector consultar
ninguna fuente externa. Sin entradas citables con DOI todavía; se agregarán aquí cuando ese
trabajo se publique.
- Capítulo 7 y Capítulo 10 del manuscrito GSF (Part I), de donde este paper extrae y re-deriva el material en forma autocontenida.
