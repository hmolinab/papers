# El determinante como invariante anisótropo y fuente del término cúbico en flujos gradiente matriciales equivariantes

**Henry Molina**
Investigador independiente — Bogotá, Colombia
hmolinab@unal.edu.co
DOI: 10.5281/zenodo.20752208 (v2)

*Manuscrito autónomo en el lenguaje de los sistemas dinámicos; no requiere ningún marco externo.
Versión en español (la de envío en inglés está en `paper_en.md`). Los scripts de verificación
reproducibles, uno por enunciado numérico (§8), están en `code/`. El material sobre la extensión inercial
(Bogdanov–Takens) y la fenomenología del caos se trata en el documento compañero `outlook_inercial_caos.md`.*

---

## Resumen

Consideramos el flujo gradiente \(\dot\Gamma=-\nabla P(\Gamma;\mu,J)\) sobre las matrices reales
\(4\times4\), donde \(P\) es **invariante bajo la acción ortogonal bilateral** \(\Gamma\mapsto U\Gamma V^\top\)
(\(U,V\in O(4)\), \(\det U\det V=1\)) salvo un término lineal \(-\langle J,\Gamma\rangle\) que rompe la
simetría. El anillo de invariantes polinómicos de esa acción está generado por las **funciones simétricas de
los valores singulares** y por el **determinante**; en particular `tr(Γ³)` —el candidato ingenuo a cúbico—
**no es invariante y queda excluido por la simetría**. Cerca de una degeneración del Hessiano (un modo blando
simple, aislado por el rompimiento de simetría de \(J\) en el sentido de la teoría de bifurcaciones
imperfectas), la reducción de variedad central produce las formas normales locales, y el **coeficiente cúbico
proviene del determinante** a través de su matriz de cofactores —el invariante anisótropo de menor grado—,
que es su **única fuente** sobre el estrato \(V\perp\Gamma_*\). Probamos la reducción de codimensión 1
(pliegue y, sobre estratos con isotropía \(\mathbb Z_2\), tridente) con coeficientes explícitos, y la cúspide
\(A_3\) en codimensión 2. Un **lema sin Hopf** —el resultado más general del trabajo— muestra que ningún flujo
metric-gradiente (con cualquier métrica \(G\succ0\), incluso dependiente del estado) admite bifurcación
oscilatoria: el espectro de la degeneración es real, de modo que toda inestabilidad oscilatoria exige romper la
forma gradiente. Situamos el resultado como una **instancia de un principio general** —el invariante anisótropo
de menor grado de la simetría es la fuente del cúbico—, cuya contraparte para tensores simétricos (el flujo del
\(Q\)-tensor de Landau–de Gennes, con simetría de conjugación \(O(3)\)) es `tr(Q³)`. Cada enunciado se verifica
con simulaciones reproducibles, incluyendo el escalamiento \(3/2\) de la cúspide.

**Palabras clave:** bifurcación equivariante, flujo gradiente matricial, reducción de variedad central, formas
normales, matriz de cofactores, invariante anisótropo, lema sin Hopf, cúspide.

---

## 1. Introducción

La teoría de bifurcaciones organiza los cambios cualitativos de un sistema dinámico alrededor de un catálogo de
formas normales (Guckenheimer–Holmes 1983; Kuznetsov 2004). Cuando el campo posee una **simetría**, la teoría
equivariante (Golubitsky–Schaeffer–Stewart 1988) dicta qué bifurcaciones son genéricas, cómo aparecen las
degeneraciones en familias (órbitas del grupo) y qué invariantes pueden figurar en la forma normal. Este
trabajo analiza, para un flujo gradiente con **variable matricial** y simetría ortogonal **bilateral**, el
**origen del término cúbico** de la bifurcación de modo blando, y muestra que está fijado por la estructura de
invariantes de la simetría.

El principio organizador es simple: **el invariante anisótropo de menor grado del grupo de simetría es la
fuente del cúbico de la forma normal reducida.** Para la acción bilateral \(O(4)\times O(4)\) sobre matrices
generales, ese invariante es el **determinante**; para la acción de conjugación \(O(n)\) sobre tensores
simétricos (e.g. el \(Q\)-tensor nemático), es `tr(Q³)` (§7). El determinante es así el representante natural de
un mecanismo más amplio, no una elección particular del potencial.

Contribuciones: (i) el **reencuadre equivariante** que excluye `tr(Γ³)` por simetría y singulariza al
determinante (§2); (ii) el **teorema de reducción** de codimensión 1 con coeficientes explícitos, identificando
el determinante como fuente del cúbico (§3–§4); (iii) la **cúspide** \(A_3\) de codimensión 2 (§5); (iv) el
**lema sin Hopf** metric-gradiente y su lectura termodinámica (§6); (v) el **principio general** y su instancia
en el \(Q\)-tensor de Landau–de Gennes (§7); (vi) **verificación numérica reproducible** (§8). La extensión
inercial (Bogdanov–Takens) y el caos se tratan, como direcciones numéricamente exploradas y no como teoremas,
en el documento compañero.

---

## 2. El sistema y su simetría

Sea \(V=M_4(\mathbb R)\cong\mathbb R^{16}\) con el producto interno de Frobenius
\(\langle X,Y\rangle=\operatorname{tr}(X^\top Y)\). Consideramos
$$
P(\Gamma;\mu,J)=\|\Gamma\|^2+\mu\det\Gamma+\beta\|\Gamma\|^4+\beta'\operatorname{tr}\!\big((\Gamma^\top\Gamma)^2\big)+b_6\|\Gamma\|^6-\langle J,\Gamma\rangle,
$$
con \(\beta,\beta',b_6\ge0\), parámetro de control \(\mu\in\mathbb R\) y campo externo \(J\in M_4(\mathbb R)\).

**Simetría bilateral.** Para \(J=0\), \(P\) es invariante bajo la acción
\(\Gamma\mapsto U\Gamma V^\top\) del grupo
$$
G=\{(U,V)\in O(4)\times O(4):\ \det U\det V=1\},
$$
ya que \(\|U\Gamma V^\top\|^2=\|\Gamma\|^2\) y \(\det(U\Gamma V^\top)=\det U\det V\det\Gamma=\det\Gamma\). Esta es
la simetría de la descomposición en valores singulares (SVD).

**El anillo de invariantes (la clave del origen del cúbico).** Los invariantes polinómicos de \(G\) son
funciones de los valores singulares \(\sigma_i\ge0\) de \(\Gamma\): están generados por las sumas de potencias
\(p_k(\Gamma)=\operatorname{tr}\!\big((\Gamma^\top\Gamma)^k\big)=\sum_i\sigma_i^{2k}\) (todas de grado par) y por
el determinante \(\det\Gamma=\pm\prod_i\sigma_i\) (de grado \(4\)), con \(\det^2=\prod_i\sigma_i^2\) ya expresable
en los \(p_k\). En consecuencia:

> **El determinante es el único generador invariante de grado impar-en-orientación / anisótropo de bajo grado.**
> El candidato ingenuo a cúbico, \(\operatorname{tr}(\Gamma^3)=\sum_i\lambda_i^3\) (suma de potencias de los
> *autovalores*), **no es función de los valores singulares y por tanto no es \(G\)-invariante**: queda
> **excluido por la simetría bilateral**. (Solo bajo la subsimetría de conjugación \(U=V\) sería invariante; ese
> es el caso del \(Q\)-tensor, §7.)

Así, el potencial \(P\) **no es una elección particular**: a orden cuártico es el potencial \(G\)-invariante
general (los términos \(p_1=\|\Gamma\|^2\), \(p_1^2=\|\Gamma\|^4\), \(p_2=\operatorname{tr}((\Gamma^\top\Gamma)^2)\)
y \(\det\), más el séxtico regularizador \(b_6\)). El término \(\mu\det\Gamma\) es el único capaz de aportar
anisotropía al cúbico; los demás son **isótropos** en el sentido preciso de §3 (su contribución cúbica es una
contracción con \(\Gamma_*\), que se anula sobre el estrato \(V\perp\Gamma_*\)).

**El campo \(J\) y la bifurcación imperfecta.** \(J\) rompe \(G\). Genéricamente lo rompe por completo: el
término lineal \(-\langle J,\Gamma\rangle\) intersecta transversalmente las órbitas de \(G\) (transversalidad de
Thom), levanta la degeneración que la simetría continua imponía —por la cual las degeneraciones aparecerían en
familias y no aisladas— y deja un **único autovalor cero** del Hessiano (un modo blando simple, H2). Esto es la
**teoría de bifurcaciones imperfectas / despliegue por rompimiento de simetría** (Golubitsky–Schaeffer 1985).
Como \(J\) entra linealmente, desplaza el equilibrio pero **no altera el Hessiano**. Si en cambio \(J\) preserva
un subgrupo de isotropía \(\mathbb Z_2\subset G\) (campo en un estrato simétrico), el modo blando hereda esa
isotropía y la bifurcación genérica es el **tridente** (§3.2): los tridentes viven sobre los estratos
simétricos, como es estándar en bifurcación equivariante.

El flujo gradiente es
$$
\dot\Gamma=-\nabla P,\qquad \nabla P=2\Gamma+\mu\,\mathrm C(\Gamma)+\big(4\beta\|\Gamma\|^2+\dots\big)\Gamma,\quad
\mathrm C(\Gamma)=\operatorname{cof}(\Gamma)=\partial\det\Gamma/\partial\Gamma,
$$
con Hessiano \(H(\Gamma)=D^2P\) simétrico. Consideramos también la versión amortiguada de segundo orden
\(\ddot\Gamma+\gamma\dot\Gamma+\nabla P=0\), cuyo límite sobreamortiguado \(\gamma\to\infty\) recupera el flujo
gradiente; solo para sondear cuencas y tasas de escape (§8) usamos la extensión de Langevin
\(\dot\Gamma=-\nabla P+\sqrt{2D}\,\eta\).

**Observación 2.1 (alcance y dimensión).** Las partes 1–2 del Teorema 1 son la reducción de variedad central /
Lyapunov–Schmidt para cualquier \(P\) real-analítico \(G\)-invariante bajo (H1)–(H2); solo la identificación del
coeficiente cúbico usa la estructura del anillo de invariantes. Presentamos \(n=4\) por concreción y porque allí
\(\det\) tiene grado \(4\) y \(D^3\det\) es **lineal**; el mecanismo se extiende a \(M_n(\mathbb R)\) con la acción
bilateral \(O(n)\times O(n)\), donde \(\det\) tiene grado \(n\) y aporta no-linealidades de orden \(n-3\) (§9).
Un muestreo de Monte Carlo sobre \((\beta,\beta',b_6,J)\) confirma la persistencia del modo blando simple y de la
contribución del determinante (estabilidad estructural; §8, fila 10).

---

## 3. Resultado principal (codimensión 1)

En \((\Gamma_*,\mu_*)\) suponemos: **(H1)** \(\nabla P=0\); **(H2)** \(H_*=H(\Gamma_*)\) tiene un autovalor cero
simple, con autovector unitario \(V\), y el resto del espectro acotado lejos de cero; **(H3)** transversalidad
\(\tau:=\langle V,\mathrm C(\Gamma_*)\rangle\neq0\) (el control \(\mu\) mueve el modo blando); **(H4)** no
degeneración \(a_3:=D^3P(\Gamma_*)[V,V,V]\neq0\), salvo sobre estratos con isotropía \(\mathbb Z_2\) (entonces
\(a_3=0\) y \(a_4^{\mathrm{eff}}\neq0\)).

**Teorema 1 (reducción \(\Gamma\to\xi\)).** *Bajo (H1)–(H2) existe en un entorno de \((\Gamma_*,\mu_*)\) una
variedad central unidimensional, única y suave, \(\Gamma=\Gamma_*+\xi V+h(\xi,\mu)\) con \(h\in V^\perp\),
\(h=O(\xi^2,\xi\tilde\mu)\), sobre la cual el flujo es gradiente \(\dot\xi=-\partial_\xi\Phi(\xi,\mu)\). Si además
(H3)–(H4):*

1. *(genérico) si \(a_3\neq0\): **pliegue** \(\dot\xi=\alpha-\tfrac12 a_3\xi^2\), con \(\alpha=-\tau(\mu-\mu_*)\);*
2. *(estrato \(\mathbb Z_2\)) si la isotropía fuerza \(a_3=0\): **tridente** \(\dot\xi=-a_2'\xi-\tfrac16 a_4^{\mathrm{eff}}\xi^3\);*
3. ***fuente del cúbico:*** \(a_3=\mu_*\,D^3\!\det(\Gamma_*)[V,V,V]+\big(\text{contribuciones de }p_1^2,p_2\big)\),
   *donde las contribuciones de las invariantes de norma son contracciones con \(\Gamma_*\) (e.g.
   \(24\beta\langle\Gamma_*,V\rangle\)) y **se anulan sobre el estrato \(V\perp\Gamma_*\)**. Allí el determinante
   es la **única fuente** del cúbico. Por la simetría bilateral (§2), `tr(Γ³)` no figura.*
4. *\(a_4^{\mathrm{eff}}=D^4P[V^{\otimes4}]-3\,\langle D^3P[V,V],(H_*|_{V^\perp})^{-1}D^3P[V,V]\rangle\) (corrección
   de esclavizamiento); su signo lo fija el espectro de \(H_*|_{V^\perp}\).*

En el sector simétrico, \(a_4^{\mathrm{eff}}\) cambia de signo en \(\mu=16\beta\), línea que separa el régimen de
un equilibrio del de tres (Figura 1).

![**Figura 1.** Bifurcaciones de codim 1: pliegue y tridente. Azul: ramas estables; rojo discontinuo:
inestables. El cúbico proviene de \(\det\Gamma\).](figs/fig1_codim1.png)

---

## 4. Demostración (Lyapunov–Schmidt)

Reducción de Lyapunov–Schmidt para campos gradiente (Carr 1981; Golubitsky–Schaeffer 1985). Con
\(\Gamma=\Gamma_*+\xi V+W\), \(W\in V^\perp\), \(\mu=\mu_*+\nu\), y \(Q\) la proyección sobre
\(V^\perp=\operatorname{ran}H_*\): la componente \(Q\nabla P=0\) se resuelve por la función implícita
(\(H_*|_{V^\perp}\) invertible) y da el esclavizamiento \(W=h(\xi,\mu)\), con \(\partial_\xi h(0,\mu_*)=0\) y
\(\partial_\xi^2 h(0)=-(H_*|_{V^\perp})^{-1}Q\,D^3P(\Gamma_*)[V,V]\). Sustituyendo, la ecuación de bifurcación
\(g=\langle V,\nabla P\rangle=\partial_\xi\Phi\) (gradiente). Con \(a_k=\partial_\xi^k\Phi(0,\mu_*)\):
\(\partial_\nu a_1|_0=\langle V,\mathrm C(\Gamma_*)\rangle=\tau\); \(a_2(\mu_*)=\langle V,H_*V\rangle=0\);
\(a_3=\langle V,D^3P[V,V]\rangle\) (el esclavizamiento no corrige el cúbico, por ser \(\perp V\)).

Descomponiendo \(D^3P\) por invariantes: \(\|\Gamma\|^2\) (cuadrático) no contribuye;
\(D^3(\|\Gamma\|^4)[V,V,V]=24\langle\Gamma_*,V\rangle\) (contracción con \(\Gamma_*\), isótropa); análogamente
\(p_2=\operatorname{tr}((\Gamma^\top\Gamma)^2)\) contribuye una contracción con tensores construidos de
\(\Gamma_*\), también \(\propto\) proyecciones sobre \(\Gamma_*\); y, para \(\det\) (grado \(4\), \(D^3\det\)
lineal), \(D^3(\mu\det)[V,V,V]=\mu_*\,D^3\!\det(\Gamma_*)[V,V,V]\). Por tanto el cúbico es la suma del término del
determinante más términos de norma \(\propto\langle\Gamma_*,\cdot\rangle\). **Sobre el estrato \(V\perp\Gamma_*\)
las contribuciones de norma se anulan y solo sobrevive el determinante.**

Lectura geométrica: \(\det\Gamma=\prod_i\sigma_i\) (producto) acopla los cuatro valores singulares de forma
irreducible —la parte anisótropa del cúbico—, mientras la norma \(\|\Gamma\|^2=\sum_i\sigma_i^2\) (suma) es
isótropa y solo entra por \(\langle\Gamma_*,V\rangle\). La clasificación pliegue/tridente se sigue de las
condiciones de Sotomayor (1973). \(\square\)

*(Cómputo explícito completo en el Material Suplementario `code/` y el apéndice técnico.)*

---

## 5. Cúspide de codimensión 2

**Teorema 2 (cúspide \(A_3\)).** *Un punto con \(a_2=a_3=0\) y \(a_4^{\mathrm{eff}}\neq0\) es una cúspide, el
despliegue universal del tridente (Thom 1975). \(a_3(\mu,s)\) es continuo y, como las contribuciones del
determinante y de la norma compiten, cambia de signo: por el teorema del valor intermedio se anula sobre una
curva; el segundo control \(s\) fija \(a_2=0\) en un punto de esa curva; allí \(a_4^{\mathrm{eff}}\neq0\) y la
transversalidad \(\partial(a_1,a_2)/\partial(\mu,s)\) es no singular —una \(A_3\) versal genuina. Las cuatro
condiciones se certifican numéricamente (§8); la ventana de tres equilibrios escala como
\((-a_2)^{3/2}\)* (Figura 2).

![**Figura 2.** La cúspide \(A_3\) en \((a_1,a_2)\): dentro de \(4a_2^3+27a_1^2\le0\), tres equilibrios; fuera,
uno. Recuadro: ley \(3/2\).](figs/fig2_cuspide.png)

---

## 6. El lema sin Hopf (resultado central)

**Lema 1 (sin Hopf en el flujo metric-gradiente).** *El Jacobiano de \(\dot\Gamma=-G^{-1}\nabla P\) en un
equilibrio es, para cualquier métrica \(G\succ0\) simétrica —**incluida una métrica Riemanniana dependiente del
estado \(G(\Gamma)\)**, pues en \(\nabla P=0\) el término con la derivada de la métrica se anula—, semejante a la
matriz simétrica \(-G_*^{-1/2}H_*G_*^{-1/2}\); su espectro es **real**. Por tanto ningún par complejo cruza el
eje imaginario y **no ocurre bifurcación de Hopf**: mientras la dinámica es metric-gradiente, el modo blando solo
admite bifurcaciones **estacionarias** (pliegue, tridente, cúspide). Una inestabilidad oscilatoria exige romper
la forma gradiente —que \(G\) pierda positividad, o un término reactivo genuinamente no-gradiente.*

**Observación (clasificación espectral).** El Lema 1 organiza el catálogo por el espectro de la degeneración:
autovalor real que cruza cero \(\Rightarrow\) bifurcación estacionaria, con cúbico del determinante (Teoremas
1–2); par complejo \(\Rightarrow\) régimen oscilatorio (Hopf, etc.), imposible en el sector gradiente. El tipo se
lee del espectro crítico: real \(\Rightarrow\) estacionaria; complejo \(\Rightarrow\) oscilatoria.

**Lectura termodinámica.** El lema es, bajo la geometría, un enunciado termodinámico: la disipación estricta
(flujo gradiente con métrica positiva) está *topológicamente obstruida* de producir oscilación sostenida. Es el
correlato topológico de por qué un sistema en relajación monótona no alberga dinámica compleja autosostenida —el
ritmo exige un sector no-gradiente.

Este lema es el resultado **más general** del trabajo: no depende del potencial particular ni de la dimensión, y
fija qué bifurcaciones son accesibles a un flujo gradiente matricial.

---

## 7. Un principio general y la instancia del \(Q\)-tensor

El mecanismo de §3 es una instancia de un principio:

> **En un flujo gradiente con grupo de simetría \(K\), el invariante anisótropo \(K\)-invariante de menor grado
> es la fuente del término cúbico de la forma normal del modo blando.**

Para la acción **bilateral** \(K=O(n)\times O(n)\) sobre matrices generales, ese invariante es el **determinante**
(este trabajo). Para la acción de **conjugación** \(K=O(n)\) sobre **tensores simétricos** —el flujo del
\(Q\)-tensor de Landau–de Gennes de cristales líquidos nemáticos, \(\dot Q=-\partial F/\partial Q\) con
\(F=\tfrac a2\operatorname{tr}Q^2-\tfrac b3\operatorname{tr}Q^3+\tfrac c4(\operatorname{tr}Q^2)^2\)—, la simetría
de conjugación **sí** admite `tr(Q³)` como invariante, y es precisamente `tr(Q³)` la que aporta el cúbico que
distingue la transición isótropo–nemática de primer orden. Así, el mismo principio selecciona invariantes
distintos según la simetría: **\(\det\) para la simetría bilateral, `tr(Q³)` para la conjugación**. El resultado
de este trabajo es la instancia bilateral, hasta ahora no aislada, de un patrón que la fenomenología de
Landau–de Gennes ya encarna en el caso de conjugación. Esto conecta el enunciado con un sistema físico estándar y
ofrece un escenario natural de prueba (los \(Q\)-tensores y los strain tensors continuos son flujos gradiente
matriciales reales).

---

## 8. Verificación numérica

Cada enunciado se acompaña de un script autónomo (NumPy/SciPy) reproducible. Las degeneraciones se localizan
resolviendo \(\nabla P=0\) y \(\lambda_{\min}(H)=0\); los coeficientes de forma normal por ajuste polinómico; los
exponentes de Lyapunov por Benettin (1980); las tasas de escape por Kramers (Hänggi et al. 1990); las ramas por
continuación pseudo-arclength (Doedel 1981).

| # | objeto | resultado | script |
|---|--------|-----------|--------|
| 1 | pliegue/tridente invariantes; Var\(\sim1/k\); Monte Carlo \(10^3\) | tridente crítico \(k_2=0\); clasificación 100% | `code/pieza1_bifurcaciones_rigor.py` |
| 2 | reducción exacta (rayo invariante) | \(\nabla P\parallel\Gamma\); umbral \(\mu=16\beta\) | `code/pieza1_reduccion_normal_forms.py` |
| 3 | variedad central genérica | flujo completo = reducida (no la ingenua) | `code/pieza1_centro_manifold_generico.py` |
| 4 | Kramers + continuación | \(\ln\langle\tau\rangle=0.904\,\Delta U/D+1.78\), \(R^2=0.989\); pliegue a \(\mu\approx2.04\) | `code/pieza1_kramers_continuacion.py` |
| 5 | **Teorema 1 en 16-dim** | cero simple; \(\tau=-12.84\); \(a_3=5.09\) (det \(-11.67\)); saddle-node real | `code/pieza1_teorema_4x4.py` |
| 6 | Teorema 2 (cúspide) | \(a_2,a_3\sim10^{-11}\); versal \(=1.30\); ley \(3/2\): \(\propto(-a_2)^{1.503}\), \(R^2=1.0\) | `code/pieza1_cuspide_codim2.py` |
| 7 | Lema 1 / exclusión de `tr Γ³` | espectro real en metric-gradiente; `tr Γ³` no \(G\)-invariante | `code/pieza1_no_hopf_invariantes.py` |
| 8 | robustez / estabilidad estructural | \((\beta,\beta',b_6,J)\): 40/40 conservan modo blando, pliegue y contribución del det | `code/pieza1_robustez_teorema.py` |

*(El estudio numérico del régimen inercial/caótico está en el documento compañero.)*

---

## 9. Discusión

El contenido central: cuando la no-linealidad de un flujo gradiente matricial **equivariante** está fijada por la
simetría, el invariante anisótropo de menor grado —para la simetría bilateral, el **determinante**— determina el
tipo de bifurcación del modo blando, vía su cofactor. La exclusión de `tr(Γ³)` por la simetría bilateral es lo
que vuelve el resultado **estructural y no una elección del potencial**: \(P\) es el potencial \(G\)-invariante
general a su orden. El determinante interviene como el **invariante que genera el cúbico**, no como indicador de
estabilidad (esa la fija el espectro del Hessiano simétrico). El **Lema 1** delimita el alcance: el sector
gradiente solo produce bifurcaciones estacionarias.

**Sobre el exponente \(3/2\).** La ventana de tres equilibrios de la cúspide escala como \((-a_2)^{3/2}\). Esta
es la ley **universal de la catástrofe \(A_3\)** —la comparte *cualquier* cúspide— y por sí sola **no valida el
mecanismo del determinante**; lo que valida es que el organizador *es* una cúspide \(A_3\) genuina. El número
medible es la firma de la **clase** de bifurcación, no del invariante que la origina.

**Dónde aparecen estos flujos.** Flujos gradiente matriciales reales surgen en el \(Q\)-tensor de Landau–de
Gennes (§7), los strain tensors continuos y los paisajes de pérdida de redes pequeñas, donde una no-linealidad
invariante gobierna el modo blando —escenarios para poner a prueba la dicotomía pliegue/cúspide. En el
entrenamiento adversarial (GANs) la simetría gradiente se rompe nativamente, excitando los modos oscilatorios que
el Lema 1 atribuye al sector no-gradiente —una instancia discreta de la transición estacionario\(\to\)rotacional.

**Nota de alcance.** No se afirma que este Lagrangiano sea *privilegiado*: es el potencial \(G\)-invariante
general a orden cuártico. «Universal» se usa solo en el sentido técnico de *despliegue universal* de las formas
normales. El determinante genera el cúbico **dentro de la clase de potenciales con la simetría bilateral**, no
para flujos matriciales arbitrarios.

**Direcciones (en el documento compañero).** (i) La extensión inercial de segundo orden, donde el bloque de
Jordan de Bogdanov–Takens se libera (obstruido en el límite gradiente por el Lema 1) y cuyo certificado completo
de coeficientes en \(16+16\) dimensiones queda abierto; (ii) la fenomenología del caos (saddle-focus,
Shilnikov) del sector no-gradiente, explorada numéricamente sobre un modelo de juguete y enunciada como
conjetura; (iii) la extensión a \(M_n(\mathbb R)\), \(n>4\).

---

## Referencias

1. J. Carr, *Applications of Centre Manifold Theory*, Springer AMS 35, 1981.
2. J. Guckenheimer, P. Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields*, Springer AMS 42, 1983.
3. Yu. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3.ª ed., Springer AMS 112, 2004.
4. M. Golubitsky, D. G. Schaeffer, *Singularities and Groups in Bifurcation Theory*, vol. I, Springer AMS 51, 1985.
5. M. Golubitsky, I. Stewart, D. G. Schaeffer, *Singularities and Groups in Bifurcation Theory*, vol. II, Springer AMS 69, 1988.
6. J. Sotomayor, *Generic bifurcations of dynamical systems*, en *Dynamical Systems* (M. M. Peixoto, ed.), Academic Press, 1973, 561–582.
7. R. Thom, *Structural Stability and Morphogenesis*, W. A. Benjamin, 1975.
8. P. G. de Gennes, J. Prost, *The Physics of Liquid Crystals*, 2.ª ed., Oxford, 1993.
9. N. J. Mottram, C. J. P. Newton, *Introduction to Q-tensor theory*, arXiv:1409.3542, 2014.
10. P. Hänggi, P. Talkner, M. Borkovec, *Reaction-rate theory: fifty years after Kramers*, Rev. Mod. Phys. 62 (1990) 251–341.
11. E. J. Doedel, *AUTO: a program for the automatic bifurcation analysis of autonomous systems*, Congr. Numer. 30 (1981) 265–284.
12. G. Benettin et al., *Lyapunov characteristic exponents for smooth dynamical systems*, Meccanica 15 (1980) 9–30.
