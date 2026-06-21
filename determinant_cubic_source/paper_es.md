# El determinante como fuente del término cúbico: reducción a formas normales en un flujo gradiente matricial

**Henry Molina**
Investigador independiente
hmolinab@unal.edu.co
DOI: 10.5281/zenodo.20752208

*Manuscrito autónomo en el lenguaje de los sistemas dinámicos; no requiere ningún marco externo.
Versión en español (la versión de envío en inglés está en `paper_en.md`). Los scripts de verificación
reproducibles, uno por enunciado numérico (§7), están en `code/`.*

---

## Resumen

Consideramos el flujo gradiente \(\dot\Gamma=-\nabla P(\Gamma;\mu)\) sobre las matrices reales
\(4\times4\), con el potencial \(P(\Gamma)=\|\Gamma\|^2+\mu\det\Gamma+\beta\|\Gamma\|^4\) (más un
sextico regularizador opcional), y su versión amortiguada de segundo orden
\(\ddot\Gamma+\gamma\dot\Gamma+\nabla P=0\). Cerca de una degeneración del Hessiano —un modo blando
simple— la reducción de variedad central conduce a las formas normales locales de la teoría de
bifurcaciones. El coeficiente cúbico de la forma reducida proviene del determinante a través de su
matriz de cofactores, la única no-linealidad anisótropa del campo; es su única fuente cuando el modo
blando es ortogonal a \(\Gamma_*\). Clasificamos los centros organizadores accesibles: pliegue y
tridente en codimensión 1, la cúspide en el sector gradiente y Bogdanov–Takens en codimensión 2,
cuya existencia está topológicamente obstruida en el límite gradiente y exige levantar el sistema al
flujo inercial de segundo orden. Un lema de no-Hopf precisa la dicotomía y la hace invariante
metric-gradiente: mientras gobierna el sector simétrico (disipativo) solo hay bifurcaciones
estacionarias, y todo régimen oscilatorio está condicionado por el sector reactivo antisimétrico.
La homoclínica cierra el retrato de Bogdanov–Takens, y la parte no-gradiente del campo,
responsable de la rotación, sostiene numéricamente un régimen de caos de tipo Shilnikov. Los
resultados analíticos se complementan con simulaciones que verifican los escalamientos críticos: la
ley de Kramers, una continuación pseudo-arclength a través del pliegue, la ley \(3/2\) de la cúspide
y el exponente de Lyapunov del régimen caótico.

**Palabras clave:** flujo gradiente matricial, reducción de variedad central, formas normales,
matriz de cofactores, cúspide, Bogdanov–Takens, caos de Shilnikov.

---

## 1. Introducción

La teoría de bifurcaciones organiza los cambios cualitativos de un sistema dinámico en torno a un
catálogo de formas normales: el pliegue \(\dot\xi=\lambda-\xi^2\), el tridente
\(\dot\xi=\lambda\xi-\xi^3\), la cúspide, Hopf, Bogdanov–Takens (Guckenheimer–Holmes 1983;
Kuznetsov 2004). Analizamos el papel geométrico del determinante en la selección de la forma normal
para flujos gradiente con variable matricial, cuando el Hessiano se degenera en un modo blando.

Bajo las hipótesis (H1)–(H4), el determinante genera el término cúbico de la reducción local. Su gradiente es la matriz
de cofactores \(\mathrm C(\Gamma)=\operatorname{cof}(\Gamma)\), multilineal en las entradas y
anisótropa, mientras que los términos de norma \(\|\Gamma\|^{2k}\) son isótropos. Al proyectar sobre
la variedad central de un modo blando, esa anisotropía sobrevive como el coeficiente cúbico de la
forma normal, y persiste incluso cuando los términos de norma se anulan, esto es, cuando el modo
blando es ortogonal a \(\Gamma_*\).

Probamos un teorema de reducción en codimensión 1 con coeficientes explícitos (§3–§4); clasificamos
los dos centros organizadores de codimensión 2, cúspide y Bogdanov–Takens, y mostramos que esta
última exige la dinámica de segundo orden (§5); analizamos la pérdida de la estructura gradiente y su
relación con el caos (§6); y respaldamos cada resultado con verificación numérica reproducible (§7).

---

## 2. El sistema

Sea \(V=M_4(\mathbb R)\cong\mathbb R^{16}\) con el producto interno de Frobenius
\(\langle X,Y\rangle=\operatorname{tr}(X^\top Y)\). Tomamos
$$
P(\Gamma;\mu,J)=\|\Gamma\|^2+\mu\det\Gamma+\beta\|\Gamma\|^4+b_6\|\Gamma\|^6-\langle J,\Gamma\rangle,
\qquad \beta\ge0,\ b_6\ge0,
$$
donde \(\mu\in\mathbb R\) es el parámetro de control y \(J\in M_4(\mathbb R)\) un campo externo. El
sextico \(b_6\) no interviene en los enunciados locales; su papel es global. Aunque \(\beta\ge0\) ya
acota \(P\) a orden más bajo, la **corrección de esclavizamiento** del cuártico reducido (Teorema 1.4)
puede volver el coeficiente efectivo \(a_4^{\mathrm{eff}}\) **negativo** (tridente subcrítico), a lo
largo del cual la reducción a la variedad central escaparía a infinito; el séxtico \(b_6>0\) es lo que
**estabiliza globalmente esas ramas subcríticas** cuando el esclavizamiento voltea el signo del
cuártico. El potencial sin campo (\(J=0\)) depende únicamente de \(\|\Gamma\|^2\) y \(\det\Gamma\),
ambos invariantes bajo la acción ortogonal bilateral \(\Gamma\mapsto U\Gamma V^\top\) con
\(U,V\in O(4)\) (la misma de la descomposición en valores singulares que reaparece en §4). Esta alta
isotropía hace que sus degeneraciones aparezcan en familias y no de forma aislada. Un campo \(J\)
genérico la rompe y sitúa el equilibrio en una configuración donde el modo blando de la bifurcación
es simple (hipótesis H2): el término lineal \(\langle J,\Gamma\rangle\) intersecta transversalmente
las órbitas de \(O(4)\times O(4)\) (transversalidad de Thom), levantando la degeneración que la
simetría continua imponía y dejando un único autovalor cero. Como \(J\) entra de forma lineal,
desplaza el equilibrio pero no altera el Hessiano. El flujo gradiente es
$$
\dot\Gamma=-\nabla P,\qquad \nabla P=2\Gamma+\mu\,\mathrm C(\Gamma)+\big(4\beta\|\Gamma\|^2+6b_6\|\Gamma\|^4\big)\Gamma,
$$
con \(\mathrm C(\Gamma)=\operatorname{cof}(\Gamma)=\partial\det\Gamma/\partial\Gamma\). El Hessiano
\(H(\Gamma)=D^2P\) es simétrico por tratarse de un campo gradiente. Consideramos también la versión
amortiguada de segundo orden
$$
\ddot\Gamma+\gamma\dot\Gamma+\nabla P=0,\qquad \gamma\in\mathbb R,
$$
cuyo límite sobreamortiguado \(\gamma\to\infty\) recupera el flujo gradiente. El sistema es
determinista; solo para sondear las cuencas de atracción y las tasas de escape (§7) recurrimos de
forma auxiliar a la extensión estocástica de Langevin \(\dot\Gamma=-\nabla P+\sqrt{2D}\,\eta(t)\), con
\(\eta\) ruido blanco matricial y \(D>0\).

**Observación 2.1 (alcance).** Las partes 1 y 2 del Teorema 1 son la reducción de variedad central /
Lyapunov–Schmidt para cualquier \(P\) real-analítico bajo (H1)–(H2), y no dependen de la forma
concreta de \(P\); solo la identificación del coeficiente cúbico (§3, punto 3) y del cuártico efectivo
usan el potencial particular. La construcción requiere un producto interno definido positivo —el de
Frobenius— que acota \(P\) por abajo y fija la estructura gradiente, y es independiente de cualquier
reinterpretación métrica posterior de las entradas de \(\Gamma\). Un muestreo de Monte Carlo sobre los
coeficientes \((\beta,b_6)\) y el campo \(J\) confirma que el modo blando simple y la contribución del
determinante persisten, lo que indica estabilidad estructural de la reducción de codimensión 1.

---

## 3. Resultado principal (codimensión 1)

Suponemos en el punto \((\Gamma_*,\mu_*)\) las hipótesis siguientes:

- (H1) \(\nabla P(\Gamma_*,\mu_*)=0\);
- (H2) \(H_*=H(\Gamma_*)\) tiene un autovalor cero simple, con autovector unitario \(V\), y el resto
  del espectro acotado lejos de cero;
- (H3) transversalidad: \(\tau:=\langle V,\mathrm C(\Gamma_*)\rangle\neq0\), de modo que el control
  \(\mu\) mueve el modo blando;
- (H4) no degeneración: \(a_3:=D^3P(\Gamma_*)[V,V,V]\neq0\); o bien una involución \(\mathbb Z_2\)
  fuerza \(a_3=0\) y entonces \(a_4^{\mathrm{eff}}\neq0\).

**Teorema 1 (reducción \(\Gamma\to\xi\)).** *Bajo (H1)–(H2) existe en un entorno de
\((\Gamma_*,\mu_*)\) una variedad central unidimensional, única y suave,
\(\Gamma=\Gamma_*+\xi V+h(\xi,\mu)\) con \(h\in V^\perp\) y \(h=O(\xi^2,\xi\tilde\mu)\), sobre la cual
el flujo es gradiente, \(\dot\xi=-\partial_\xi\Phi(\xi,\mu)\). Si además se cumplen (H3)–(H4):*

1. *si \(a_3:=D^3P(\Gamma_*)[V,V,V]\neq0\), la forma reducida es el pliegue
   \(\dot\xi=\alpha-\tfrac12 a_3\xi^2\), con \(\alpha=-\tau(\mu-\mu_*)\) y \(\tau=\langle V,\mathrm C(\Gamma_*)\rangle\);*
2. *si una involución \(\mathbb Z_2\) fuerza \(a_3=0\), la forma reducida es el tridente
   \(\dot\xi=-a_2'\xi-\tfrac16 a_4^{\mathrm{eff}}\xi^3\);*
3. *\(a_3=\mu_*\,D^3\!\det(\Gamma_*)[V,V,V]+24\beta\langle\Gamma_*,V\rangle\); dentro del espacio de
   invariantes del potencial (1), el primer término es la única fuente del cúbico cuando
   \(V\perp\Gamma_*\) (un invariante de grado tres como \(\operatorname{tr}\Gamma^3\), ausente en (1),
   también contribuiría);*
4. *\(a_4^{\mathrm{eff}}=D^4P[V^{\otimes4}]-3\,\langle D^3P[V,V],(H_*|_{V^\perp})^{-1}D^3P[V,V]\rangle\),
   cuyo signo depende del espectro de \(H_*|_{V^\perp}\) (definido positivo en la rama estable,
   indefinido en una silla).*

En el sector simétrico, \(a_4^{\mathrm{eff}}\) cambia de signo en \(\mu=16\beta\), línea que separa el
régimen de un único equilibrio del de tres (Figura 1).

![**Figura 1.** Bifurcaciones de codimensión 1: pliegue \(\dot\xi=\alpha-\xi^2\) y tridente
\(\dot\xi=\lambda\xi-\xi^3\). En azul las ramas estables, en rojo discontinuo las inestables. El
término cúbico proviene de \(\det\Gamma\).](figs/fig1_codim1.png)

---

## 4. Demostración (Lyapunov–Schmidt)

La reducción es la de Lyapunov–Schmidt para campos gradiente (Carr 1981; Golubitsky–Schaeffer 1985).
Escribimos \(\Gamma=\Gamma_*+\xi V+W\) con \(W\in V^\perp\) y \(\mu=\mu_*+\nu\), y sea \(Q\) la
proyección ortogonal sobre \(V^\perp=\operatorname{ran}H_*\). La ecuación \(\nabla P=0\) se separa en
sus componentes en \(V^\perp\) y en \(V\).

La componente en \(V^\perp\), \(Q\nabla P=0\), se resuelve por el teorema de la función implícita
—\(H_*|_{V^\perp}\) es invertible por (H2)— y despeja la variedad de esclavizamiento \(W=h(\xi,\mu)\),
con \(h(0,\mu_*)=0\), \(\partial_\xi h(0,\mu_*)=0\) y \(\partial_\xi^2 h(0)=-(H_*|_{V^\perp})^{-1}\,Q\,D^3P(\Gamma_*)[V,V]\)
al derivar dos veces. Sustituyendo \(h\) en la componente restante se obtiene la ecuación de
bifurcación \(g(\xi,\mu)=\langle V,\nabla P\rangle\), que por ser el campo gradiente coincide con
\(\partial_\xi\Phi\), \(\Phi=P|_{\text{var.\ central}}\); el flujo reducido \(\dot\xi=-g\) hereda la
estructura gradiente. Escribiendo \(a_k=\partial_\xi^k\Phi(0,\mu_*)\):

- \(\partial_\nu a_1|_0=\langle V,\partial_\mu\nabla P\rangle=\langle V,\mathrm C(\Gamma_*)\rangle=\tau\)
  (el segundo sumando \(\langle V,H_*\partial_\mu h\rangle\) se anula porque \(H_*\partial_\mu h\perp V\));
- \(a_2(\mu_*)=\langle V,H_*V\rangle=0\) (modo blando);
- \(a_3=\langle V,D^3P[V,V]\rangle=D^3P(\Gamma_*)[V,V,V]\); el término de esclavizamiento
  \(\langle V,H_*\partial_\xi^2 h\rangle\) se anula por ser \(\perp V\), de modo que el cúbico no
  recibe corrección.

Para identificar \(a_3\) se descompone \(D^3P\) por términos. El término \(\|\Gamma\|^2\) es cuadrático
y no contribuye. Para la norma cuártica, con \(\|V\|=1\),
\(D^3(\|\Gamma\|^4)[V,V,V]=24\,\langle\Gamma_*,V\rangle\). Para el determinante, que en \(4\times4\) es
de grado \(4\), \(D^3\det\) es lineal y \(D^3(\mu\det\Gamma)[V,V,V]=\mu_*\,D^3\!\det(\Gamma_*)[V,V,V]\).
Sumando,
\[
a_3=\mu_*\,D^3\!\det(\Gamma_*)[V,V,V]+24\beta\,\langle\Gamma_*,V\rangle,
\]
que es el punto 3. El primer término es genéricamente no nulo aun cuando \(\langle\Gamma_*,V\rangle=0\):
ahí la norma calla y, dentro de los invariantes de (1), el determinante es la única fuente del cúbico.
Esto tiene una lectura geométrica directa en términos de los valores singulares de \(\Gamma\). El
determinante es su producto, \(\det\Gamma=\prod_i\sigma_i\) (salvo signo), mientras que la norma es la
suma de cuadrados, \(\|\Gamma\|^2=\sum_i\sigma_i^2\). El producto acopla los cuatro valores singulares
de forma irreducible y aporta la parte anisótropa del cúbico; la suma es isótropa y solo contribuye a
través de \(\langle\Gamma_*,V\rangle\).
El cuártico efectivo se obtiene de derivar \(g\) una vez más y sustituir \(\partial_\xi^2 h\), lo que
da el punto 4; el signo de la corrección queda fijado por la definitud de \(H_*|_{V^\perp}\). La clasificación
pliegue/tridente se sigue entonces de las condiciones de Sotomayor (Sotomayor 1973; Kuznetsov 2004):
con \(a_1(\mu_*)=a_2(\mu_*)=0\) y \(a_3\neq0\) se obtiene el pliegue \(\dot\xi=\alpha-\tfrac12 a_3\xi^2\);
si una simetría \(\mathbb Z_2\) anula \(a_3\) (y \(\langle\Gamma_*,V\rangle\)), el primer término no
trivial es el cuártico y se obtiene el tridente. \(\square\)

*(Detalle completo en el documento técnico `teorema_gamma_xi.md`, §2.)*

---

## 5. Centros organizadores de codimensión 2

**Teorema 2 (cúspide, \(A_3\)).** *Un punto con \(a_2=a_3=0\) y \(a_4^{\mathrm{eff}}\neq0\) es una
cúspide, el despliegue universal del tridente (Thom 1975; Golubitsky–Schaeffer 1985). Su existencia
aquí no es un mero «\(a_3\) cambia de signo»: \(a_3(\mu,s)\) es continuo y, como las contribuciones
del determinante y de la norma compiten, cambia de signo en la hoja de parámetros, así que por el
teorema del valor intermedio se anula sobre una curva; el segundo mando \(s\) fija \(a_2=0\) en un
punto de esa curva; allí se verifica \(a_4^{\mathrm{eff}}\neq0\) y la transversalidad
(\(\partial(a_1,a_2)/\partial(\mu,s)\) no singular) — luego una \(A_3\) versal genuina. Las cuatro
condiciones se certifican numéricamente (§7), donde la ventana de tres equilibrios se mide con anchura
\(\propto(-a_2)^{3/2}\)* (Figura 2).

![**Figura 2.** La cúspide \(A_3\) en el plano de despliegue \((a_1,a_2)\). Dentro de la cuña
semicúbica \(4a_2^3+27a_1^2\le0\) hay tres equilibrios; fuera, uno. El recuadro muestra la ley
\(3/2\).](figs/fig2_cuspide.png)

**Lema 1 (sin Hopf en el flujo (metric-)gradiente).** *El Jacobiano de \(\dot\Gamma=-\nabla P\) en un
equilibrio es \(-H_*\), con \(H_*=D^2P\) simétrico; su espectro es real, así que ningún par complejo
puede cruzar el eje imaginario y no ocurre bifurcación de Hopf. Esto persiste para el flujo
metric-gradiente \(\dot\Gamma=-G^{-1}\nabla P\) con cualquier \(G\succ0\) simétrico —**incluso una
métrica Riemanniana dependiente del estado \(G(\Gamma)\)**, pues en el equilibrio \(\nabla P=0\) el
término con la derivada de la métrica se anula y la linealización es exactamente
\(-G(\Gamma_*)^{-1}H_*\), semejante a la simétrica \(-G(\Gamma_*)^{-1/2}H_*G(\Gamma_*)^{-1/2}\), luego
real. En consecuencia,
mientras \(G\) es definida positiva el modo blando solo admite bifurcaciones estacionarias; una
inestabilidad oscilatoria (Hopf) exige romper la forma gradiente —ya sea \(G\) perdiendo su
positividad, o un término reactivo genuinamente no-gradiente, aquí el sector antisimétrico
\(\Gamma_a\).*

**Teorema 3 (Bogdanov–Takens).** *En el flujo gradiente esta bifurcación está obstruida (Lema 1): el
Jacobiano \(-H_*\) es simétrico, luego diagonalizable, y un autovalor doble cero tendría multiplicidad
geométrica 2 en lugar de un bloque de Jordan. Liberar el bloque de Jordan exige agrandar el espacio
de fases más allá de la dinámica gradiente de primer orden; dentro de la fenomenología disipativa que
estudiamos, esto se consigue levantando el sistema a la ecuación de segundo orden (inercial), cuya
linealización compañera es no-normal aunque el campo subyacente siga siendo mecánico. Allí la
linealización
\(\big(\begin{smallmatrix}0&I\\-H_*&-\gamma I\end{smallmatrix}\big)\) tiene, en el modo blando,
autovalores \(\{0,-\gamma\}\), que en \(\gamma=0\) colapsan a un doble cero con bloque de Jordan. La reducción es \(\ddot\xi+\gamma(\xi)\dot\xi+(a_1+c\,\xi^2)=0\) con \(c=\tfrac12 a_3\); con un
amortiguamiento dependiente del estado \(\gamma(\xi)=\gamma_0+\gamma_1\xi\), del punto BT emanan, en
la ecuación reducida, las curvas de saddle-node (el pliegue), de Hopf (\(\gamma_0=-\gamma_1\xi_*\)) y
de homoclínica (Bogdanov 1975; Takens 1974).*

*Estatus del Teorema 3.* Es un **argumento de reducción y forma normal** que establece el mecanismo
del bloque de Jordan y la ecuación BT reducida planar, **no aún** una verificación BT completa: las dos
condiciones de no degeneración de Kuznetsov (los coeficientes cuadráticos \(a_{20},b_{11}\neq0\) de la
forma normal planar y la regularidad del mapa de parámetros) las exhibe la ecuación reducida y, si
bien la teoría de variedad central garantiza su persistencia en el flujo completo una vez la reducción
es exacta, el cómputo algebraico explícito de los coeficientes en 32 dimensiones resulta
analíticamente prohibitivo —de ahí nuestro foco en la ecuación reducida planar. El BT no degenerado
completo en el flujo ambiente queda abierto al nivel de un certificado explícito de coeficientes.

La rama de saddle-node de Bogdanov–Takens coincide con el pliegue del Teorema 1, de manera que ambos
centros de codimensión 2 son degeneraciones del mismo modo blando. El punto BT marca la frontera entre
el régimen sobreamortiguado —gradiente, con pliegue y cúspide— y el oscilatorio (Figura 3).

**Observación (clasificación espectral).** *El Lema 1 organiza el catálogo por el espectro de la
degeneración. Un autovalor real simple que cruza cero da una bifurcación **estacionaria** —pliegue,
tridente o cúspide, con el cúbico originado por el determinante (Teoremas 1–2). Un régimen
**oscilatorio** —Hopf, Bogdanov–Takens, Shilnikov— exige un par complejo cruzando el eje, lo cual por
el Lema 1 es imposible mientras gobierna en solitario el sector simétrico (disipativo) y reclama el
sector no-gradiente \(\Gamma_a\) (§6). El tipo de bifurcación se lee, pues, del espectro crítico: real
\(\Rightarrow\) estacionaria; complejo \(\Rightarrow\) oscilatoria, con \(\Gamma_a\) como compuerta.*

![**Figura 3.** Despliegue de Bogdanov–Takens en \((\mu-\mu_f,\gamma_0)\): del punto BT emanan la
curva de saddle-node (el pliegue), la de Hopf y la homoclínica; el ciclo límite vive entre la de Hopf
y la homoclínica.](figs/fig3_bogdanov_takens.png)

---

## 6. Extensión no-gradiente y fenomenología del caos

**Proposición 4 (obstrucción de energía).** *La ecuación de segundo orden con \(\gamma\ge0\) uniforme
admite \(E=\tfrac12\|\dot\Gamma\|^2+P\) como función de Lyapunov, ya que
\(\dot E=-\gamma\|\dot\Gamma\|^2\le0\); toda trayectoria relaja a un equilibrio, de modo que el sistema
gradiente disipativo no admite caos sostenido.*

El caos no puede emerger, por tanto, de la mera disipación de los grados de libertad acoplados: exige
una inyección de energía (\(\gamma_{\mathrm{ef}}\le0\) en alguna región) emparejada con la asimetría
del sector reactivo \(\Gamma_a\), que rompe la simetría del Hessiano e introduce la rotación
(\(\operatorname{Im}\lambda\neq0\)). Esa parte antisimétrica, no-gradiente, aporta además la tercera
dimensión que Poincaré–Bendixson exige. Acoplándola con un amortiguamiento activo, la no-linealidad
cúbica inducida por el
determinante produce una **ecuación de jerk con un equilibrio de tipo saddle-focus**. El modelo de
juguete explícito que se integró para la Figura 4 es el jerk cuadrático (tipo Sprott)
$$\dddot\xi+a\,\ddot\xi-(\dot\xi)^2+\xi=0,\qquad a=2.017,$$
equivalente al sistema de primer orden \(\dot x=y,\ \dot y=z,\ \dot z=-a\,z+y^2-x\); el término
cuadrático \((\dot\xi)^2\) puede leerse como la imagen reducida de la no-linealidad del cofactor del
determinante (físicamente, un arrastre no lineal proporcional al cuadrado de la velocidad que frena el
escape y permite que el atractor se pliegue sobre sí mismo).
Integrándola (RK4) se observa un atractor caótico con exponente de Lyapunov positivo
(\(\lambda\approx0.055\), coincidente con el valor de Sprott) y un ciclo límite que termina en una
homoclínica de periodo logarítmicamente divergente (Figura 4). La reducción del flujo de segundo orden
en \(16+16\) dimensiones a esta ecuación de jerk específica no se demuestra aquí; el modelo de juguete
se exhibe como la ecuación tras la Figura 4, y la reducción \(16{+}16\to\) jerk se enuncia como conjetura.

**Conjetura 1.** *En la extensión inercial acoplada con la parte antisimétrica del campo, la
no-linealidad cúbica inducida por el determinante basta para producir una conexión homoclínica a un
equilibrio saddle-focus que satisface la condición de Shilnikov
(\(|\lambda_{\mathrm{real}}|>|\operatorname{Re}\lambda_{\mathrm{compl}}|\); Shilnikov 1965), y con ella
un atractor caótico. El despliegue analítico de esta bifurcación global queda abierto.*

![**Figura 4.** (a) Atractor caótico de tipo Shilnikov (saddle-focus) de la ecuación de jerk
cuadrática. (b) Dependencia sensible: la separación de dos trayectorias crece como \(e^{\lambda t}\)
con \(\lambda\approx0.055\).](figs/fig4_caos.png)

---

## 7. Verificación numérica

Cada enunciado se acompaña de un script autónomo en Python (NumPy/SciPy) que lo verifica de forma
reproducible. Los puntos de degeneración se localizan resolviendo simultáneamente \(\nabla P=0\) y la
condición de modo blando \(\lambda_{\min}(H)=0\); los coeficientes de la forma normal se extraen por
ajuste polinómico de \(P\) restringido a las direcciones relevantes; los exponentes de Lyapunov se
calculan por el método de Benettin (Benettin et al. 1980); las tasas de escape se contrastan con la
ley de Kramers (Hänggi et al. 1990); y las ramas de equilibrios se siguen por continuación
pseudo-arclength (Doedel 1981). La tabla resume objeto, resultado y script.

| # | objeto | resultado | script |
|---|--------|-----------|--------|
| 1 | pliegue/tridente como objetos invariantes; Var\(\sim1/k\); Monte Carlo \(10^3\) | tridente crítico \(k_2=0\); \(k\cdot\)Var\(\approx\)const; clasificación de \(10^3\) matrices al 100% | `code/pieza1_bifurcaciones_rigor.py` |
| 2 | reducción exacta (rayo invariante) | \(\nabla P\parallel\Gamma\); \(P_{\mathrm{red}}\) tridente; umbral \(\mu=16\beta\) | `code/pieza1_reduccion_normal_forms.py` |
| 3 | variedad central genérica | \(B=2\sum g_i^2/\omega_i-b\); flujo completo = reducida (no la ingenua) | `code/pieza1_centro_manifold_generico.py` |
| 4 | Kramers + continuación | \(\ln\langle\tau\rangle=0.904\,\Delta U/D+1.78\), \(R^2=0.989\); pliegue trazado a \(\mu\approx2.04\) | `code/pieza1_kramers_continuacion.py` |
| 5 | Teorema 1 en 16-dim | cero simple; \(\tau=-12.84\); \(a_3=5.09\) (det \(-11.67\)); saddle-node real | `code/pieza1_teorema_4x4.py` |
| 6 | Teorema 2 (cúspide) | \(a_2,a_3\sim10^{-11}\); Jacobiano versal \(=1.30\); ley \(3/2\): \(\propto(-a_2)^{1.503}\), \(R^2=1.0\) | `code/pieza1_cuspide_codim2.py` |
| 7 | Teorema 3 (BT) | bloque de Jordan; curva de Hopf; ciclo límite | `code/pieza1_bogdanov_takens.py` |
| 8 | homoclínica + caos | \(T=0.738(-\ln\Delta)+2.08\), \(R^2=1.0\); Lyapunov \(\lambda\approx0.055\) (Sprott) | `code/pieza1_homoclinica_caos.py` |
| 9 | obstrucción de energía + caos desde la EOM | \(\gamma\ge0\Rightarrow E\) Lyapunov \(\Rightarrow\) relaja; damping activo \(\Rightarrow\) ciclo límite (2 modos) | `code/pieza1_caos_EOM_2modos.py` |
| 10 | robustez / estabilidad estructural | variando \((a,\beta,b_6,J)\): 40/40 conservan modo blando simple, pliegue y contribución del det | `code/pieza1_robustez_teorema.py` |

---

## 8. Discusión

El contenido central es que, cuando la no-linealidad dominante de un flujo gradiente matricial es el
determinante, la geometría de la matriz —a través de su cofactor— determina el tipo de bifurcación
del modo blando. La sucesión pliegue → cúspide → Bogdanov–Takens → caos se recorre degenerando un
único modo y añadiendo en cada paso una estructura: el determinante aporta el cúbico que distingue
pliegue de tridente; el amortiguamiento \(\gamma\) aporta el segundo parámetro de Bogdanov–Takens al
pasar a segundo orden; y la parte no-gradiente aporta la rotación que abre la puerta al caos. El
determinante interviene como el invariante que genera el cúbico, no como un indicador de estabilidad:
la estabilidad lineal la fija el espectro del Hessiano simétrico, mientras que \(\det\Gamma\) codifica
orientación y rango. (Nota de alcance: no se afirma que este Lagrangiano sea *universal* ni privilegiado; es un potencial **general**, uno de una clase amplia para la que el determinante genera el cúbico —Obs. 2.1—. La palabra «universal» se usa aquí solo en el sentido técnico de *despliegue universal* de las formas normales. El determinante genera el cúbico **dentro de esta clase de potenciales**, no como afirmación sobre flujos matriciales arbitrarios.)

Estos resultados están en **niveles distintos**, y no se presentan como un solo teorema: el pliegue, el tridente y la cúspide (Teoremas 1–2) son resultados de forma normal del flujo gradiente; el Bogdanov–Takens (Teorema 3) es un argumento a nivel de la reducción que exige el levantamiento inercial; y el caos (Conjetura 1) es numérico. La cadena pliegue → cúspide → BT → caos es un hilo organizador a través de la codimensión y el orden, no un único objeto.

**Exponente crítico medible.** Más allá de la topología, el determinante fija un número *medible*: la ventana de tres equilibrios de la cúspide escala como \((-a_2)^{3/2}\), la ley \(3/2\) universal de la catástrofe \(A_3\). Los exponentes críticos son independientes del marco y accesibles en laboratorio, así que esto convierte el papel del determinante de un enunciado topológico en una **herramienta empírica**.

**Dónde aparecen estos flujos.** Los flujos gradiente matriciales reales de este tipo surgen en física aplicada: el flujo del \(Q\)-tensor de Landau–de Gennes en cristales líquidos nemáticos, los tensores de deformación/strain continuos, y los paisajes de pérdida de pequeñas redes neuronales son todos flujos gradiente sobre matrices (simétricas o generales) donde una no-linealidad guiada por un determinante o invariante gobierna el modo blando — escenarios naturales para poner a prueba la dicotomía pliegue/cúspide. En el entrenamiento adversarial (GANs) la simetría gradiente se rompe de forma nativa por la estructura min-max, excitando precisamente los modos oscilatorios que el Lema 1 atribuye a \(\Gamma_a\) — una instancia discreta de la transición de dinámica estacionaria a rotacional.

**Lectura termodinámica del Lema 1.** El lema sin Hopf es, bajo la geometría, un enunciado termodinámico: la disipación estricta está *topológicamente obstruida* de producir oscilación sostenida o ciclos límite. Es el correlato topológico de por qué los sistemas en equilibrio termodinámico no pueden albergar dinámica compleja autosostenida — el ritmo exige el sector reactivo, no-gradiente.

Quedan abiertas tres líneas. Primero, la reducción rigurosa del flujo de segundo orden en \(16+16\)
dimensiones a la ecuación de jerk reactiva; el modelo del sector no-gradiente en §6 es ilustrativo y
no una reducción exacta. Segundo, el despliegue completo del escenario caótico —cascadas, conexión
Shilnikov–Hopf— en el sector no-gradiente. Tercero, la extensión a \(M_n(\mathbb R)\) con \(n>4\),
donde \(\det\) tiene grado \(n\) y aporta no-linealidades de orden superior.

---

## Referencias

1. J. Carr, *Applications of Centre Manifold Theory*, Applied Mathematical Sciences 35, Springer, 1981.
2. J. Guckenheimer, P. Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields*, Applied Mathematical Sciences 42, Springer, 1983.
3. Yu. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3.ª ed., Applied Mathematical Sciences 112, Springer, 2004.
4. M. Golubitsky, D. G. Schaeffer, *Singularities and Groups in Bifurcation Theory*, vol. I, Applied Mathematical Sciences 51, Springer, 1985.
5. J. Sotomayor, *Generic bifurcations of dynamical systems*, en *Dynamical Systems* (M. M. Peixoto, ed.), Academic Press, 1973, pp. 561–582.
6. R. I. Bogdanov, *Versal deformations of a singular point of a vector field on the plane in the case of zero eigenvalues*, Selecta Math. Soviet. 1 (1981) 389–421 (orig. 1975).
7. F. Takens, *Forced oscillations and bifurcations*, Comm. Math. Inst. Rijksuniversiteit Utrecht 3 (1974) 1–59.
8. R. Thom, *Structural Stability and Morphogenesis*, W. A. Benjamin, 1975.
9. L. P. Shilnikov, *A case of the existence of a countable number of periodic motions*, Soviet Math. Dokl. 6 (1965) 163–166.
10. P. Hänggi, P. Talkner, M. Borkovec, *Reaction-rate theory: fifty years after Kramers*, Rev. Mod. Phys. 62 (1990) 251–341.
11. J. C. Sprott, *Simplest dissipative chaotic flow*, Phys. Lett. A 228 (1997) 271–274.
12. E. J. Doedel, *AUTO: a program for the automatic bifurcation analysis of autonomous systems*, Congr. Numer. 30 (1981) 265–284.
13. G. Benettin, L. Galgani, A. Giorgilli, J.-M. Strelcyn, *Lyapunov characteristic exponents for smooth dynamical systems; a method for computing all of them*, Meccanica 15 (1980) 9–30.
