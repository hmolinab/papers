# Documento compañero — Extensión inercial (Bogdanov–Takens) y fenomenología del caos

*Compañero de "El determinante como invariante anisótropo y fuente del término cúbico…" (`paper_es.md`).
**Estatus:** direcciones **exploradas numéricamente**, NO teoremas. Se separa del paper principal a propósito,
para que el núcleo probado (Teoremas 1–2, Lema 1) no quede mezclado con material conjetural. Marcado
[arg]=argumento de reducción, [num]=evidencia numérica, [conj]=conjetura abierta.*

---

## 1. Motivación: por qué hace falta salir del gradiente

Por el **Lema 1** del paper principal, ningún flujo metric-gradiente admite bifurcación oscilatoria: su
linealización tiene espectro real. Toda dinámica con ritmo (Hopf, Bogdanov–Takens, Shilnikov) exige **romper la
forma gradiente**. Hay dos vías: (a) levantar el sistema a la dinámica **inercial** de segundo orden
\(\ddot\Gamma+\gamma\dot\Gamma+\nabla P=0\) (cuya linealización compañera es no-normal aunque el campo siga
siendo mecánico); (b) un **sector reactivo genuinamente no-gradiente** (la parte antisimétrica \(\Gamma_a\)).
Este documento recorre ambas, sin reclamar teoremas.

## 2. Bogdanov–Takens en el levantamiento inercial [arg]

En el flujo gradiente puro, BT está **obstruido**: \(-H_*\) es simétrico, luego diagonalizable, y un autovalor
doble cero tendría multiplicidad geométrica 2 en vez de un bloque de Jordan. Liberar el bloque de Jordan exige
agrandar el espacio de fases. En la ecuación de segundo orden, la linealización compañera en el modo blando es
\(\big(\begin{smallmatrix}0&1\\-a_1&-\gamma\end{smallmatrix}\big)\), con autovalores \(\{0,-\gamma\}\) que en
\(\gamma=0\) **colapsan a un doble cero con bloque de Jordan**. La reducción planar es
\(\ddot\xi+\gamma(\xi)\dot\xi+(a_1+c\,\xi^2)=0\), \(c=\tfrac12 a_3\). Con amortiguamiento dependiente del estado
\(\gamma(\xi)=\gamma_0+\gamma_1\xi\), del punto BT emanan las curvas de saddle-node (= el pliegue del Teorema 1),
de Hopf y de homoclínica (Bogdanov 1975; Takens 1974).

**Estatus [arg, abierto].** Es un argumento de reducción y forma normal que exhibe el mecanismo del bloque de
Jordan y la ecuación BT reducida planar; **NO** una verificación BT completa. Las dos condiciones de no
degeneración de Kuznetsov (\(a_{20},b_{11}\neq0\) y la regularidad del mapa de parámetros) las exhibe la ecuación
reducida; el cómputo algebraico explícito de los coeficientes en \(16+16\) dimensiones es analíticamente
prohibitivo. **El BT no degenerado completo en el flujo ambiente queda abierto al nivel de un certificado de
coeficientes.**

## 3. Fenomenología del caos: saddle-focus y Shilnikov [num, conj]

Acoplando la inercia con la parte antisimétrica (no-gradiente), la no-linealidad cúbica inducida por el
determinante produce un equilibrio **saddle-focus** y, con él, la posibilidad de caos de Shilnikov. El **modelo
de juguete** integrado (no derivado del flujo completo) es el jerk cuadrático tipo Sprott
$$\dddot\xi+a\,\ddot\xi-(\dot\xi)^2+\xi=0,\qquad a=2.017,$$
donde el término \((\dot\xi)^2\) se **interpreta** (no se deriva) como imagen reducida del arrastre cuadrático del
cofactor. Integrándolo (RK4): atractor caótico con \(\lambda\approx0.055\) (coincide con Sprott) y una
homoclínica de periodo logarítmicamente divergente.

**Conjetura 1 [conj].** *En la extensión inercial acoplada con \(\Gamma_a\), la no-linealidad cúbica del
determinante basta para una conexión homoclínica a un saddle-focus que satisface la condición de Shilnikov
(\(|\lambda_{\mathrm{real}}|>|\operatorname{Re}\lambda_{\mathrm{compl}}|\); Shilnikov 1965), y con ella un
atractor caótico. La reducción exacta \(16{+}16\to\) jerk y el despliegue analítico de esta bifurcación global
quedan abiertos.*

**Honestidad.** El jerk de Sprott es un sistema caótico **conocido, insertado a mano**; la conexión con el
cofactor es una **interpretación**, no una derivación. Por eso esto vive aquí y no en el paper principal.

## 4. Verificación numérica (de este documento)

| # | objeto | resultado | script |
|---|--------|-----------|--------|
| A | Teorema 3 (BT) reducido | bloque de Jordan; curva de Hopf; ciclo límite | `code/pieza1_bogdanov_takens.py` |
| B | obstrucción de energía | \(\gamma\ge0\Rightarrow E\) Lyapunov \(\Rightarrow\) relaja; damping activo \(\Rightarrow\) ciclo (2 modos) | `code/pieza1_caos_EOM_2modos.py` |
| C | homoclínica + caos (juguete) | \(T=0.738(-\ln\Delta)+2.08\), \(R^2=1.0\); \(\lambda\approx0.055\) | `code/pieza1_homoclinica_caos.py` |

## 5. Qué haría falta para que esto suba a teorema

(i) La reducción **exacta** del flujo inercial de \(16+16\) dimensiones a la ecuación de jerk reactiva (hoy:
modelo de juguete ilustrativo). (ii) El **certificado explícito** de los coeficientes BT de Kuznetsov en el flujo
ambiente. (iii) El despliegue completo del escenario Shilnikov–Hopf en el sector no-gradiente. Mientras tanto,
estos resultados son **dirección de investigación**, valiosos como mapa, no como cierre.

---

*Referencias: Bogdanov (1975), Takens (1974), Shilnikov (1965), Sprott (1997) — ver `paper_es.md`.*
