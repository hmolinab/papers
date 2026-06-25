# El determinante como invariante de orientación y fuente del término cúbico en flujos gradiente matriciales equivariantes

Henry Molina
Investigador independiente, Bogotá, Colombia
hmolinab@unal.edu.co
DOI: 10.5281/zenodo.20752208 (v3)

Manuscrito autónomo en el lenguaje de los sistemas dinámicos; no requiere ningún marco externo. Versión en
español; la de envío en inglés está en `paper_en.md`. Los scripts de verificación reproducibles, uno por
enunciado numérico (§8), están en `code/`. La extensión inercial (Bogdanov–Takens) y la fenomenología del
caos se tratan, como direcciones numéricamente exploradas y no como teoremas, en el documento compañero
`outlook_inercial_caos.md`.

---

## Resumen

Consideramos el flujo gradiente $\dot\Gamma=-\nabla P(\Gamma;\mu,J)$ sobre las matrices reales $4\times4$, con
$P=\|\Gamma\|^2+\mu\det\Gamma+\beta\|\Gamma\|^4+b_6\|\Gamma\|^6-\langle J,\Gamma\rangle$, y su versión amortiguada
de segundo orden. El potencial sin campo es invariante bajo la acción ortogonal bilateral
$\Gamma\mapsto U\Gamma V^\top$ ($U,V\in O(4)$, $\det U\det V=1$). El anillo de invariantes de esa acción está
generado por las funciones simétricas de los valores singulares y por el determinante; este último es el único
generador sensible a la orientación, y el candidato ingenuo a invariante cúbico, $\operatorname{tr}\Gamma^3$, no
es invariante de esta simetría. Cerca de una degeneración del Hessiano —un modo blando simple, aislado por el
término lineal $J$ en el sentido de la bifurcación imperfecta— la reducción de variedad central da las formas
normales locales, y el coeficiente cúbico recibe del determinante, vía su matriz de cofactores, su única
contribución sensible a la orientación; dentro del potencial considerado, es su única fuente sobre el estrato
$V\perp\Gamma_*$. Probamos la reducción de codimensión 1 (pliegue y, sobre estratos con isotropía $\mathbb Z_2$,
tridente) con coeficientes explícitos, y la cúspide $A_3$ de codimensión 2. Un lema sin Hopf muestra que ningún
flujo metric-gradiente, con cualquier métrica definida positiva, admite bifurcación oscilatoria: el espectro de
la degeneración es real. El mismo mecanismo, bajo la simetría de conjugación $O(n)$ de los tensores simétricos,
selecciona $\operatorname{tr}Q^3$, como en la energía de Landau–de Gennes del $Q$-tensor nemático. Cada enunciado
se acompaña de verificación numérica reproducible.

Palabras clave: bifurcación equivariante, flujo gradiente matricial, reducción de variedad central, formas
normales, matriz de cofactores, invariante de orientación, lema sin Hopf, cúspide.

---

## 1. Introducción

La teoría de bifurcaciones organiza los cambios cualitativos de un sistema dinámico alrededor de un catálogo de
formas normales (Guckenheimer y Holmes 1983; Kuznetsov 2004). Cuando el campo tiene una simetría, la teoría
equivariante (Golubitsky, Stewart y Schaeffer 1988) determina qué bifurcaciones son genéricas, por qué las
degeneraciones aparecen en familias y qué invariantes pueden figurar en la forma normal. Estudiamos, para un
flujo gradiente con variable matricial y simetría ortogonal bilateral, el origen del término cúbico de la
bifurcación de modo blando.

El contenido es que la estructura del anillo de invariantes de la simetría fija ese término. El determinante es
el único generador del anillo bilateral que no es función del tensor $\Gamma^\top\Gamma$, es decir, el único
sensible a la orientación; al proyectar sobre la variedad central, aporta la parte de orientación del cúbico.
El invariante de tercer grado en autovalores, $\operatorname{tr}\Gamma^3$, no pertenece al anillo bilateral.
La misma lógica, para la simetría de conjugación de los tensores simétricos, selecciona $\operatorname{tr}Q^3$:
es el cúbico de la teoría de Landau–de Gennes (§7). El resultado de este trabajo es la instancia bilateral de
ese patrón.

Probamos la reducción de codimensión 1 con coeficientes explícitos (§3–§4), clasificamos la cúspide de
codimensión 2 (§5), establecemos un lema sin Hopf que delimita el alcance del sector gradiente (§6), situamos el
mecanismo junto a su contraparte de conjugación (§7) y verificamos cada resultado numéricamente (§8).

---

## 2. El sistema y su simetría

Sea $V=M_4(\mathbb R)\cong\mathbb R^{16}$ con el producto interno de Frobenius
$\langle X,Y\rangle=\operatorname{tr}(X^\top Y)$. Tomamos
$$
P(\Gamma;\mu,J)=\|\Gamma\|^2+\mu\det\Gamma+\beta\|\Gamma\|^4+b_6\|\Gamma\|^6-\langle J,\Gamma\rangle,\qquad \beta,b_6\ge0,
$$
con parámetro de control $\mu$ y campo externo $J\in M_4(\mathbb R)$. El séxtico $b_6$ no interviene en los
enunciados locales; estabiliza globalmente las ramas subcríticas cuando la corrección de esclavizamiento
(Teorema 1.4) vuelve negativo el cuártico efectivo.

Para $J=0$, $P$ es invariante bajo $\Gamma\mapsto U\Gamma V^\top$ del grupo
$G=\{(U,V)\in O(4)\times O(4):\det U\det V=1\}$, pues $\|U\Gamma V^\top\|^2=\|\Gamma\|^2$ y
$\det(U\Gamma V^\top)=\det\Gamma$. Es la simetría de la descomposición en valores singulares.

Los invariantes polinómicos de $G$ son funciones de los valores singulares $\sigma_i$ de $\Gamma$: están
generados por las sumas de potencias $p_k=\operatorname{tr}((\Gamma^\top\Gamma)^k)=\sum_i\sigma_i^{2k}$, todas de
grado par y funciones de $\Gamma^\top\Gamma$, y por el determinante $\det\Gamma=\pm\prod_i\sigma_i$, con
$\det^2$ ya expresable en los $p_k$. El determinante es así el único generador que no es función de
$\Gamma^\top\Gamma$; es el invariante sensible a la orientación. El candidato ingenuo a cúbico,
$\operatorname{tr}\Gamma^3=\sum_i\lambda_i^3$ (potencias de los autovalores), no es función de los valores
singulares y por tanto no es $G$-invariante; queda fuera del anillo bilateral. Solo bajo la subsimetría de
conjugación $U=V$ sería invariante, que es el caso de los tensores simétricos (§7).

La simetría continua haría que las degeneraciones aparecieran en órbitas de $G$ y no aisladas. El término lineal
$-\langle J,\Gamma\rangle$ rompe $G$. Genéricamente lo rompe por completo: intersecta transversalmente las
órbitas de $G$ (transversalidad de Thom), levanta la degeneración y deja un único autovalor cero del Hessiano
(hipótesis H2). Es la teoría de bifurcaciones imperfectas (Golubitsky y Schaeffer 1985). Como $J$ entra
linealmente, desplaza el equilibrio sin alterar el Hessiano. Si $J$ preserva un subgrupo de isotropía
$\mathbb Z_2\subset G$ (campo en un estrato simétrico), el modo blando hereda esa isotropía y la bifurcación
genérica es el tridente (§3); los tridentes viven sobre los estratos simétricos, como es estándar en bifurcación
equivariante.

El flujo gradiente es
$$
\dot\Gamma=-\nabla P,\qquad \nabla P=2\Gamma+\mu\,\mathrm C(\Gamma)+\big(4\beta\|\Gamma\|^2+6b_6\|\Gamma\|^4\big)\Gamma,
$$
con $\mathrm C(\Gamma)=\operatorname{cof}(\Gamma)=\partial\det\Gamma/\partial\Gamma$. El Hessiano $H(\Gamma)=D^2P$
es simétrico. Consideramos también la versión amortiguada de segundo orden $\ddot\Gamma+\gamma\dot\Gamma+\nabla
P=0$, cuyo límite $\gamma\to\infty$ recupera el flujo gradiente; solo para sondear cuencas y tasas de escape
(§8) usamos la extensión de Langevin $\dot\Gamma=-\nabla P+\sqrt{2D}\,\eta$.

Observación 2.1 (alcance y dimensión). Las partes 1–2 del Teorema 1 son la reducción de variedad central /
Lyapunov–Schmidt para cualquier $P$ real-analítico bajo (H1)–(H2); solo la identificación del coeficiente cúbico
usa la forma de $P$. La construcción requiere un producto interno definido positivo (el de Frobenius), que acota
$P$ por abajo y fija la estructura gradiente. Presentamos $n=4$ por concreción y porque allí $\det$ tiene grado
$4$ y $D^3\det$ es lineal; el mecanismo se extiende a $M_n(\mathbb R)$ con la acción bilateral $O(n)\times O(n)$,
donde $\det$ tiene grado $n$. Un muestreo de Monte Carlo sobre $(\beta,b_6,J)$ confirma la persistencia del modo
blando simple y de la contribución del determinante (§8).

Observación 2.2 (otros invariantes de cuarto grado). El anillo bilateral contiene un segundo invariante de
grado cuatro además de $\det$ y $\|\Gamma\|^4=p_1^2$: a saber $p_2=\operatorname{tr}((\Gamma^\top\Gamma)^2)$. Su
contribución cúbica es $D^3p_2[V,V,V]=24\langle\Gamma_*,V(V^\top V)\rangle$, que no es función de
$\langle\Gamma_*,V\rangle$ y por tanto, a diferencia de la de $\|\Gamma\|^4$, no se anula en general sobre
$V\perp\Gamma_*$. No incluimos $p_2$ en $P$: trabajamos con el potencial de arriba, donde sobre $V\perp\Gamma_*$
el determinante es la única fuente del cúbico. La afirmación que sobrevive con $p_2$ presente es más débil pero
intrínseca: el determinante es la única contribución sensible a la orientación del cúbico, pues $p_2$, por ser
función de $\Gamma^\top\Gamma$, es ciega a la orientación.

---

## 3. Resultado principal (codimensión 1)

En $(\Gamma_*,\mu_*)$ suponemos: (H1) $\nabla P=0$; (H2) $H_*=H(\Gamma_*)$ tiene un autovalor cero simple, con
autovector unitario $V$, y el resto del espectro acotado lejos de cero; (H3) transversalidad
$\tau:=\langle V,\mathrm C(\Gamma_*)\rangle\neq0$; (H4) no degeneración $a_3:=D^3P(\Gamma_*)[V,V,V]\neq0$, salvo
sobre estratos con isotropía $\mathbb Z_2$, donde $a_3=0$ y $a_4^{\mathrm{eff}}\neq0$.

Teorema 1 (reducción $\Gamma\to\xi$). Bajo (H1)–(H2) existe en un entorno de $(\Gamma_*,\mu_*)$ una variedad
central unidimensional, única y suave, $\Gamma=\Gamma_*+\xi V+h(\xi,\mu)$ con $h\in V^\perp$,
$h=O(\xi^2,\xi\tilde\mu)$, sobre la cual el flujo es gradiente, $\dot\xi=-\partial_\xi\Phi(\xi,\mu)$. Si además
(H3)–(H4):

1. si $a_3\neq0$, la forma reducida es el pliegue $\dot\xi=\alpha-\tfrac12 a_3\xi^2$, con
   $\alpha=-\tau(\mu-\mu_*)$;
2. si una isotropía $\mathbb Z_2$ fuerza $a_3=0$, la forma reducida es el tridente
   $\dot\xi=-a_2'\xi-\tfrac16 a_4^{\mathrm{eff}}\xi^3$;
3. $a_3=\mu_*\,D^3\!\det(\Gamma_*)[V,V,V]+24\beta\langle\Gamma_*,V\rangle$; el segundo término se anula sobre el
   estrato $V\perp\Gamma_*$, donde el determinante es la única fuente del cúbico dentro de $P$. La contribución
   del determinante es, además, la única sensible a la orientación (Obs. 2.2);
4. $a_4^{\mathrm{eff}}=D^4P[V^{\otimes4}]-3\,\langle D^3P[V,V],(H_*|_{V^\perp})^{-1}D^3P[V,V]\rangle$; su signo lo
   fija el espectro de $H_*|_{V^\perp}$.

En el sector simétrico, $a_4^{\mathrm{eff}}$ cambia de signo en $\mu=16\beta$, línea que separa el régimen de un
equilibrio del de tres (Figura 1).

![Figura 1. Bifurcaciones de codimensión 1: pliegue y tridente. En azul las ramas estables, en rojo discontinuo
las inestables. El término cúbico proviene de $\det\Gamma$.](figs/fig1_codim1.png)

---

## 4. Demostración (Lyapunov–Schmidt)

Es la reducción de Lyapunov–Schmidt para campos gradiente (Carr 1981; Golubitsky y Schaeffer 1985). Con
$\Gamma=\Gamma_*+\xi V+W$, $W\in V^\perp$, $\mu=\mu_*+\nu$, y $Q$ la proyección sobre
$V^\perp=\operatorname{ran}H_*$, la componente $Q\nabla P=0$ se resuelve por la función implícita
($H_*|_{V^\perp}$ invertible por H2) y despeja el esclavizamiento $W=h(\xi,\mu)$, con $\partial_\xi h(0,\mu_*)=0$
y $\partial_\xi^2 h(0)=-(H_*|_{V^\perp})^{-1}Q\,D^3P(\Gamma_*)[V,V]$. Sustituyendo, la ecuación de bifurcación
$g=\langle V,\nabla P\rangle$ coincide, por ser el campo gradiente, con $\partial_\xi\Phi$. Con
$a_k=\partial_\xi^k\Phi(0,\mu_*)$: $\partial_\nu a_1|_0=\langle V,\mathrm C(\Gamma_*)\rangle=\tau$;
$a_2(\mu_*)=\langle V,H_*V\rangle=0$; $a_3=\langle V,D^3P[V,V]\rangle$, sin corrección del esclavizamiento por ser
$\perp V$.

Descomponemos $D^3P$ por términos. El de $\|\Gamma\|^2$ es cuadrático y no contribuye. Para la norma cuártica,
$D^3(\|\Gamma\|^4)[V,V,V]=24\langle\Gamma_*,V\rangle$. Para el determinante, de grado $4$, $D^3\det$ es lineal y
$D^3(\mu\det)[V,V,V]=\mu_*\,D^3\!\det(\Gamma_*)[V,V,V]$. Sumando se obtiene el punto 3. Sobre $V\perp\Gamma_*$ el
término de norma se anula y solo sobrevive el del determinante.

La lectura geométrica es directa en los valores singulares: $\det\Gamma=\prod_i\sigma_i$ acopla los cuatro de
forma irreducible y aporta la parte sensible a la orientación; $\|\Gamma\|^2=\sum_i\sigma_i^2$ es función de
$\Gamma^\top\Gamma$ y solo entra por $\langle\Gamma_*,V\rangle$. El cuártico efectivo se obtiene de derivar $g$
una vez más; su signo lo fija la definitud de $H_*|_{V^\perp}$. La clasificación pliegue/tridente sigue de las
condiciones de Sotomayor (1973): con $a_1(\mu_*)=a_2(\mu_*)=0$ y $a_3\neq0$ se obtiene el pliegue; si una
$\mathbb Z_2$ anula $a_3$, el primer término no trivial es el cuártico y se obtiene el tridente. $\square$

El cómputo simbólico completo está en el Material Suplementario (`code/`) y en el documento técnico
`teorema_gamma_xi.md`, §2.

---

## 5. Cúspide de codimensión 2

Teorema 2 (cúspide $A_3$). Un punto con $a_2=a_3=0$ y $a_4^{\mathrm{eff}}\neq0$ es una cúspide, el despliegue
universal del tridente (Thom 1975). Como las contribuciones del determinante y de la norma compiten, $a_3(\mu,s)$
cambia de signo y, por el teorema del valor intermedio, se anula sobre una curva; el segundo control $s$ fija
$a_2=0$ en un punto de esa curva, donde $a_4^{\mathrm{eff}}\neq0$ y la transversalidad
$\partial(a_1,a_2)/\partial(\mu,s)$ es no singular, de modo que la $A_3$ es versal. Las cuatro condiciones se
certifican numéricamente (§8); la ventana de tres equilibrios escala como $(-a_2)^{3/2}$ (Figura 2).

![Figura 2. La cúspide $A_3$ en el plano de despliegue $(a_1,a_2)$. Dentro de la cuña $4a_2^3+27a_1^2\le0$ hay
tres equilibrios; fuera, uno. El recuadro muestra la ley $3/2$.](figs/fig2_cuspide.png)

---

## 6. Un lema sin Hopf

Lema 1 (sin Hopf en el flujo metric-gradiente). En un equilibrio, el Jacobiano de $\dot\Gamma=-G^{-1}\nabla P$,
para cualquier métrica $G\succ0$ simétrica, incluida una métrica Riemanniana dependiente del estado $G(\Gamma)$
(en $\nabla P=0$ el término con la derivada de la métrica se anula), es semejante a la matriz simétrica
$-G_*^{-1/2}H_*G_*^{-1/2}$, luego tiene espectro real. Ningún par complejo cruza el eje imaginario y no ocurre
bifurcación de Hopf: mientras la dinámica es metric-gradiente, el modo blando solo admite bifurcaciones
estacionarias (pliegue, tridente, cúspide). Una inestabilidad oscilatoria exige romper la forma gradiente: que
$G$ pierda positividad, o un término reactivo no-gradiente.

El lema organiza el catálogo por el espectro de la degeneración. Un autovalor real que cruza cero da una
bifurcación estacionaria, con cúbico originado por el determinante (Teoremas 1–2). Un régimen oscilatorio exige
un par complejo cruzando el eje, imposible en el sector gradiente. El tipo se lee del espectro crítico.

El lema admite una lectura termodinámica: la disipación estricta, como flujo gradiente con métrica positiva,
está obstruida de producir oscilación sostenida o ciclos límite. Es el correlato dinámico de por qué un sistema
en relajación monótona no alberga ritmo autosostenido. A diferencia de los Teoremas 1–2, el lema no depende del
potencial particular ni de la dimensión.

---

## 7. La contraparte de conjugación: el $Q$-tensor

El mecanismo de §3 tiene una contraparte bajo otra simetría. Para la acción de conjugación $Q\mapsto RQR^\top$,
$R\in O(n)$, sobre los tensores simétricos, el invariante $\operatorname{tr}Q^3$ sí es invariante (es función de
los autovalores, que la conjugación preserva). En la energía de Landau–de Gennes de los cristales líquidos
nemáticos,
$$
F(Q)=\tfrac a2\operatorname{tr}Q^2-\tfrac b3\operatorname{tr}Q^3+\tfrac c4(\operatorname{tr}Q^2)^2,
$$
es $\operatorname{tr}Q^3$ el término que aporta el cúbico responsable de la transición isótropo–nemática de
primer orden (de Gennes y Prost 1993; Mottram y Newton 2014). Así, según la simetría, el invariante de menor
grado que rompe la isotropía cambia: el determinante para la acción bilateral, $\operatorname{tr}Q^3$ para la
conjugación. El resultado de este trabajo es la instancia bilateral; la de conjugación es física conocida. No
afirmamos un teorema general que abarque ambas; la observación es que el cúbico de la forma normal lo provee, en
cada caso, el invariante anisótropo de menor grado admitido por la simetría, y conviene verificarla caso por
caso. Los $Q$-tensores y los tensores de deformación continuos son flujos gradiente matriciales reales y
ofrecen un escenario de prueba.

---

## 8. Verificación numérica

Cada enunciado se acompaña de un script autónomo (NumPy/SciPy) reproducible. Las degeneraciones se localizan
resolviendo $\nabla P=0$ y $\lambda_{\min}(H)=0$; los coeficientes de forma normal por ajuste polinómico; los
exponentes de Lyapunov por Benettin (1980); las tasas de escape por Kramers (Hänggi et al. 1990); las ramas de
equilibrios por continuación pseudo-arclength (Doedel 1981).

| # | objeto | resultado | script |
|---|--------|-----------|--------|
| 1 | pliegue/tridente como objetos invariantes; Var$\sim1/k$; Monte Carlo $10^3$ | tridente crítico $k_2=0$; clasificación 100% | `code/pieza1_bifurcaciones_rigor.py` |
| 2 | reducción exacta (rayo invariante) | $\nabla P\parallel\Gamma$; umbral $\mu=16\beta$ | `code/pieza1_reduccion_normal_forms.py` |
| 3 | variedad central genérica | flujo completo $=$ reducida (no la ingenua) | `code/pieza1_centro_manifold_generico.py` |
| 4 | Kramers $+$ continuación | $\ln\langle\tau\rangle=0.904\,\Delta U/D+1.78$, $R^2=0.989$; pliegue a $\mu\approx2.04$ | `code/pieza1_kramers_continuacion.py` |
| 5 | Teorema 1 en 16-dim | cero simple; $\tau=-12.84$; $a_3=5.09$ (det $-11.67$); saddle-node real | `code/pieza1_teorema_4x4.py` |
| 6 | Teorema 2 (cúspide) | $a_2,a_3\sim10^{-11}$; versal $=1.30$; ley $3/2$: $\propto(-a_2)^{1.503}$, $R^2=1.0$ | `code/pieza1_cuspide_codim2.py` |
| 7 | invariantes: $\operatorname{tr}\Gamma^3$ fuera del anillo bilateral; Lema 1 | $\operatorname{tr}\Gamma^3$ no $G$-invariante; espectro real en metric-gradiente | `code/pieza1_no_hopf_invariantes.py` |
| 8 | robustez / estabilidad estructural | $(\beta,b_6,J)$: 40/40 conservan modo blando, pliegue y contribución del det | `code/pieza1_robustez_teorema.py` |

El estudio numérico del régimen inercial y caótico está en el documento compañero.

---

## 9. Discusión

Cuando la no-linealidad de un flujo gradiente matricial con simetría bilateral está fijada por esa simetría, el
invariante sensible a la orientación, el determinante, determina el tipo de bifurcación del modo blando vía su
cofactor. Que $\operatorname{tr}\Gamma^3$ quede fuera del anillo bilateral es lo que distingue al determinante
sin recurrir a una elección del potencial: $P$ usa los generadores admitidos de menor grado. El determinante
interviene como el invariante que genera la parte de orientación del cúbico, no como indicador de estabilidad;
esa la fija el espectro del Hessiano simétrico. El Lema 1 delimita el alcance del sector gradiente.

Sobre el exponente $3/2$. La ventana de tres equilibrios de la cúspide escala como $(-a_2)^{3/2}$. Es la ley
universal de la catástrofe $A_3$, que comparte cualquier cúspide, y por sí sola no valida el mecanismo del
determinante; lo que valida es que el organizador es una cúspide genuina. El número medible es la firma de la
clase de bifurcación, no del invariante que la origina.

Dónde aparecen estos flujos. Flujos gradiente matriciales reales surgen en el $Q$-tensor de Landau–de Gennes
(§7), los tensores de deformación continuos y los paisajes de pérdida de redes pequeñas, donde una no-linealidad
invariante gobierna el modo blando. En el entrenamiento adversarial (GANs) la simetría gradiente se rompe de
forma nativa por la estructura min-max, excitando los modos oscilatorios que el Lema 1 atribuye al sector
no-gradiente.

Nota de alcance. No se afirma que este Lagrangiano sea privilegiado: es uno de la clase con simetría bilateral,
construido con los generadores admitidos de menor grado. La palabra «universal» se usa solo en el sentido
técnico de despliegue universal de las formas normales. El determinante genera la parte de orientación del
cúbico dentro de esta clase, no como afirmación sobre flujos matriciales arbitrarios.

Direcciones, tratadas en el documento compañero como exploración y no como teoremas: la extensión inercial de
segundo orden, donde el bloque de Jordan de Bogdanov–Takens se libera (obstruido en el límite gradiente por el
Lema 1), con su certificado de coeficientes en $16+16$ dimensiones abierto; la fenomenología del caos
(saddle-focus, Shilnikov) del sector no-gradiente; y la extensión a $M_n(\mathbb R)$, $n>4$.

---

## Referencias

1. J. Carr, *Applications of Centre Manifold Theory*, Springer AMS 35, 1981.
2. J. Guckenheimer y P. Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields*, Springer AMS 42, 1983.
3. Yu. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3.ª ed., Springer AMS 112, 2004.
4. M. Golubitsky y D. G. Schaeffer, *Singularities and Groups in Bifurcation Theory*, vol. I, Springer AMS 51, 1985.
5. M. Golubitsky, I. Stewart y D. G. Schaeffer, *Singularities and Groups in Bifurcation Theory*, vol. II, Springer AMS 69, 1988.
6. J. Sotomayor, *Generic bifurcations of dynamical systems*, en *Dynamical Systems* (M. M. Peixoto, ed.), Academic Press, 1973, 561–582.
7. R. Thom, *Structural Stability and Morphogenesis*, W. A. Benjamin, 1975.
8. P. G. de Gennes y J. Prost, *The Physics of Liquid Crystals*, 2.ª ed., Oxford, 1993.
9. N. J. Mottram y C. J. P. Newton, *Introduction to Q-tensor theory*, arXiv:1409.3542, 2014.
10. P. Hänggi, P. Talkner y M. Borkovec, *Reaction-rate theory: fifty years after Kramers*, Rev. Mod. Phys. 62 (1990) 251–341.
11. E. J. Doedel, *AUTO: a program for the automatic bifurcation analysis of autonomous systems*, Congr. Numer. 30 (1981) 265–284.
12. G. Benettin, L. Galgani, A. Giorgilli y J.-M. Strelcyn, *Lyapunov characteristic exponents for smooth dynamical systems*, Meccanica 15 (1980) 9–30.
