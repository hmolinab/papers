# Guía de estudio + cuaderno en limpio — Γ: la viscosidad como amortiguación estructural

*Compañero de `gamma_viscosidad_amortiguacion_estructural_molina2026.md`. Nivel: estudiante de
pregrado con cálculo vectorial, ecuaciones diferenciales básicas, y mecánica de fluidos
introductoria (Cauchy, Navier-Stokes, número de Reynolds). No hace falta haber leído los papers
compañeros (weld Clifford, atlas de sectores) en detalle — este cuaderno reconstruye lo mínimo
necesario de cada uno cuando aparece. Cada sección re-deriva la matemática paso a paso, no solo
cita el resultado: si el paper dice "verificado numéricamente", aquí se muestra, cuando es
razonable, el cálculo cerrado detrás.*

---

# Parte I — Guía de estudio

## Pregunta central

El paper hace una apuesta concreta: que γ, el único parámetro de la ecuación de movimiento de GSF
sin significado físico fijado de antemano, **es** la viscosidad cinemática cuando esa ecuación se
instancia en el dominio de fluidos — no "se parece a", sino que la identidad ν=c²/γ reproduce datos
reales sin ajustar nada. Para creer eso hace falta seguir tres piezas, en este orden:

1. **¿Por qué esta asignación concreta de S,A,I,R y no otra?** (Parte II, §1 — el protocolo de
   selección, no una elección de conveniencia.)
2. **¿Por qué la ecuación de Stokes/Navier-Stokes sale de la EOM general de GSF, y no se postula
   aparte?** (Parte II, §2 — un límite singular con teoremas de convergencia citables, más una
   derivación de covarianza galileana que vale la pena hacer a mano.)
3. **¿Qué evidencia hay de que γ=ν funciona, más allá de la consistencia algebraica?** (Parte II,
   §3-4, datos tabulados; y Parte II §6, el resultado de mayor interés aplicado: la transición
   subcrítica en tubería, con una derivación cerrada del escalamiento Re² que el paper solo cita
   como verificado numéricamente.)

## Prerrequisitos mínimos (reconstruidos aquí, no asumidos)

- **Qué es Γ.** Basta saber que Γ es una matriz real 4×4 que se parte en dos piezas,
  Γ=Γ_s+Γ_a: Γ_s es simétrica (10 componentes independientes) y se llama el sector **Fuerza**;
  Γ_a es antisimétrica (6 componentes) y se llama el sector **Campo**. Esta partición no es una
  elección: es lo que le pasa automáticamente a cualquier producto de dos vectores en álgebra
  geométrica, $uv=u\cdot v+u\wedge v$ — la parte simétrica es el producto punto (un escalar), la
  antisimétrica es el producto cuña (un bivector). El paper del weld deriva, a partir de dos
  axiomas mínimos, que Γ tiene que vivir exactamente en $M_4(\mathbb R)$ — este cuaderno no
  repite esa derivación, la usa como dada.
- **Qué es SAIR.** Cuatro "roles" abstractos que cualquier sistema dinámico llena con variables
  físicas concretas: S (escalar, "qué es"), A (vector, "qué haría sin restricciones"), I (vector,
  "qué hace dado el entorno"), R (vector, "cuál es el contexto/restricción"). La Fuerza es
  $F=S\cdot A$; el Campo es $\mathcal F=I\wedge R$ (un bivector, dual de un producto cruz en
  $\mathbb R^3$).
- **La ecuación de movimiento (EOM), citada sin re-derivar aquí:**
  $$\ddot\Gamma+\gamma\dot\Gamma-c^2\nabla^2\Gamma+\nabla_\Gamma P(\Gamma,\rho)=N(t).$$
  Es literalmente la ecuación de un oscilador amortiguado y forzado, pero para una matriz en vez
  de un número: $\ddot\Gamma$ es inercia, $\gamma\dot\Gamma$ es fricción, $-c^2\nabla^2\Gamma$ es
  un término de onda/difusión espacial, $\nabla_\Gamma P$ es la fuerza restauradora de un
  potencial, y $N(t)$ es ruido/forzaje externo.
- Cauchy y Navier-Stokes de un curso estándar de mecánica de fluidos: la ecuación de momento
  $\rho\,D\mathbf u/Dt=\nabla\cdot\boldsymbol\sigma+\mathbf f$, y su forma newtoniana
  $\rho\,D\mathbf u/Dt=-\nabla p+\mu\nabla^2\mathbf u+\mathbf f$.

## Mapa lógico

```
EOM general de GSF (citada del weld/atlas)
        |
        v
  §1: diccionario SAIR en fluidos           <- protocolo de seleccion (Gram-fuerza + trabajo)
  S=rho, A=Du/Dt, I=u, R=nabla              <- NO es la escalera vieja (S=rho,A=u,I=omega,R=h)
        |                                       esa violaba el axioma A1 (I,R deben ser grado 1)
        v
  §2.1: 3 limites con nombre fisico  ->  Stokes (lineal, sin adveccion)
  (friccion alta / amplitud chica / escala corta)
        |
        v
  §2.2: covarianza galileana  ->  Navier-Stokes completo (con adveccion)
        |
        v
  §3: nu = c^2(rho)/gamma        <- la operacionalizacion central del paper
        |
        v
  §4: datos sin ajustar      §6: transicion subcritica en tuberia
  (24 ordenes de magnitud,    (G_max ~ Re^2, origen exacto en el sector Gamma_a,
   gamma proporcional a rho)   no en el gradiente del potencial)
```

Igual que en los otros cuadernos del programa: **§1-2 son álgebra/cinemática** (qué variable física
llena cada slot, qué ecuación sale de ahí), **§3-6 son verificación/dinámica** (¿coincide con datos
reales?, ¿qué predice el mecanismo?). No conviene mezclarlas al leer.

---

# Parte II — El cuaderno en limpio

## §1. El diccionario SAIR en fluidos, paso a paso

### 1.0 Por qué esto no es arbitrario: el protocolo de selección

Antes de asignar nada, hay una regla que limita las opciones: por el Axioma A1 del weld, **A, I, R
tienen que ser los tres vectores de grado 1** (en $\mathbb R^3$: flechas ordinarias, no bivectores
ni pseudoescalares). Eso ya descarta, de entrada, cualquier asignación donde I o R sean cosas como
"vorticidad" o "helicidad" (que son de grado 2 o 3). Dentro de los candidatos de grado 1 que
sobran, dos mecanismos deciden cuál va en cada slot:

- **Mecanismo (a), Gram-fuerza.** $\Gamma_s=S\cdot A$ tiene que reproducir, sin ajustar nada, una
  ley de fuerza ya conocida e independiente.
- **Mecanismo (b), trabajo/potencia.** Entre dos candidatos de grado 1 que sobreviven (a), el que
  hace $I\cdot A\neq0$ de forma genérica (no accidental) va a $I$; el que se anula por una
  **identidad geométrica pura** (no por una restricción particular del flujo) va a $R$.

### 1.1 Aplicando el mecanismo (a): por qué A es la aceleración material, no la velocidad

La ecuación de Cauchy (balance de momento de cualquier medio continuo) es
$$\rho\,\frac{D\mathbf u}{Dt}=\nabla\cdot\boldsymbol\sigma+\mathbf f.$$
El lado izquierdo, $\rho\,D\mathbf u/Dt$, es "densidad por aceleración" — la parte inercial de la
fuerza. Si probamos $S=\rho$ y $A=D\mathbf u/Dt$:
$$\Gamma_s=S\cdot A=\rho\,\frac{D\mathbf u}{Dt},$$
que es **exactamente** el lado izquierdo de Cauchy. Ningún otro par $(S,A)$ de grado compatible lo
logra sin reajustar unidades o introducir un factor extra — en particular, $A=\mathbf u$ (la
velocidad misma, la elección más obvia a primera vista) **no** funciona: $\rho\mathbf u$ no es una
fuerza ni tiene sus unidades, es un flujo de masa. Esto es el mismo patrón que en Newton, donde
$A$ es la aceleración $\ddot{\mathbf x}$ y no la velocidad $\dot{\mathbf x}$ — la razón formal es
la misma en ambos casos: bajo un boost galileano $\mathbf v\to\mathbf v+\mathbf v_0$, la velocidad
cambia, pero la aceleración de un flujo dado por una ley $\mathbf a=g(\mathbf r)$ no cambia. $A$
tiene que ser lo invariante.

### 1.2 Aplicando el mecanismo (b): por qué I es la velocidad, calculado explícitamente

Con $A=D\mathbf u/Dt$ ya fijado, quedan dos candidatos de grado 1 para $I$ y $R$: la velocidad
$\mathbf u$ y el gradiente $\nabla$ (tratado como generador vectorial formal). El criterio de
trabajo pregunta: ¿cuál de los dos, puesto en el slot $I$, da $I\cdot A\neq0$ de forma genérica?

**Cálculo para $I=\mathbf u$:**
$$\mathbf u\cdot\frac{D\mathbf u}{Dt}=\mathbf u\cdot\left(\frac{\partial\mathbf u}{\partial t}+(\mathbf u\cdot\nabla)\mathbf u\right).$$
Usa la identidad de cálculo vectorial $\mathbf u\cdot\partial_t\mathbf u=\tfrac12\partial_t|\mathbf u|^2$
(la regla del producto aplicada a $\mathbf u\cdot\mathbf u$) y análogamente para el término
convectivo: $\mathbf u\cdot(\mathbf u\cdot\nabla)\mathbf u=\tfrac12(\mathbf u\cdot\nabla)|\mathbf u|^2$.
Sumando,
$$\mathbf u\cdot\frac{D\mathbf u}{Dt}=\frac12\frac{\partial|\mathbf u|^2}{\partial t}+\frac12(\mathbf u\cdot\nabla)|\mathbf u|^2=\frac{D}{Dt}\left(\frac{|\mathbf u|^2}{2}\right).$$
Esto **no es cero en general** — es exactamente la tasa de cambio de la energía cinética
específica. Pasa el criterio (b): es genérico, no accidental, y tiene significado físico preciso.

**¿Por qué no $R=\nabla p$ (el gradiente de presión)?** Es la elección "obvia" para lo que
completa la ecuación, pero falla el criterio de trabajo de una forma sutil que vale la pena
entender: $\mathbf u\cdot\nabla p$ **no se anula por una identidad geométrica**, solo se reduce a
una divergencia pura ($\nabla\cdot(p\mathbf u)-p\nabla\cdot\mathbf u$) bajo la restricción
*adicional* de incompresibilidad ($\nabla\cdot\mathbf u=0$). Eso es una propiedad del flujo, no del
álgebra — no cuenta como el tipo de anulación limpia que el criterio (b) pide para $R$.

**El candidato que sí se anula por identidad pura: el vector de Lamb $\mathbf u\times\boldsymbol\omega$.**
El producto triple escalar con un vector repetido es idénticamente cero:
$$\mathbf u\cdot(\mathbf u\times\boldsymbol\omega)=0\quad\text{siempre},$$
porque $\mathbf a\cdot(\mathbf a\times\mathbf b)=\det[\mathbf a,\mathbf a,\mathbf b]=0$ (un
determinante con dos filas iguales es cero — es álgebra lineal pura, no física). Este es
exactamente el mismo mecanismo por el que el campo magnético no hace trabajo sobre una carga en
electromagnetismo ($q\mathbf v\cdot(\mathbf v\times\mathbf B)=0$). Pero $\boldsymbol\omega$
(vorticidad) es de **grado 2** — no puede ocupar $R$ directamente (violaría A1). El vector de
grado 1 que *genera* $\boldsymbol\omega$ por cuña con $\mathbf u$ es $\nabla$ mismo:
$$\boldsymbol\omega=\nabla\times\mathbf u=\mathbf u\wedge\nabla\quad(\text{via dualidad de Hodge}).$$
Por eso $R=\nabla$, no $\nabla p$: el candidato correcto es el generador formal, no la presión.

### 1.3 La tabla resultante, y qué es derivado vs. asignado

| Rol SAIR | Variable | Grado | Por qué |
|:---:|---|:---:|---|
| S | densidad $\rho$ | 0 | fija junto con A por mecanismo (a) |
| A | aceleración material $D\mathbf u/Dt$ | 1 | $S\cdot A$=lado izquierdo de Cauchy, exacto |
| I | velocidad $\mathbf u$ | 1 | $I\cdot A=D(|\mathbf u|^2/2)/Dt$, genérico ≠0 |
| R | $\nabla$ (generador formal) | 1 | genera $\Gamma_a$ por cuña con $I$, sin hacer trabajo |

El Campo **no se asigna, se deriva**:
$$\Gamma_a=I\wedge R=\mathbf u\wedge\nabla=\nabla\times\mathbf u=\boldsymbol\omega.$$
La vorticidad es literalmente la parte antisimétrica del tensor de deformación $\partial_j u_i$
— no un cuarto grado que alguien eligió, sino lo que sale automáticamente de tener $I$ y $R$ ya
fijados. La helicidad $h=\mathbf u\cdot\boldsymbol\omega$, si aparece en algún cálculo, es el
invariante pseudoescalar de $\Gamma_a$ (análogo a $\mathbf E\cdot\mathbf B$ en electromagnetismo),
nunca un slot SAIR propio.

**Dónde queda la presión.** No ocupa ningún grado — es el multiplicador de Lagrange de la
restricción $\nabla\cdot\mathbf u=0$ (descomposición de Leray-Hodge: cualquier campo vectorial se
separa en una parte libre de divergencia y un gradiente puro; la presión es precisamente el
gradiente que hay que restar para mantener $\mathbf u$ incompresible). Entra como forzaje
termodinámico del entorno, no como grado de libertad interno de Γ.

### 1.4 La identidad de Lamb, completa

La descomposición que separa la parte de gradiente (presión) de la parte irreducible (vorticidad)
usa esta identidad de cálculo vectorial, que vale la pena tener a mano:
$$(\mathbf u\cdot\nabla)\mathbf u=\nabla\!\left(\frac{|\mathbf u|^2}{2}\right)-\mathbf u\times\boldsymbol\omega.$$
*Derivación rápida (notación índice, convención de suma):* $[(\mathbf u\cdot\nabla)\mathbf u]_i=
u_j\partial_j u_i$. Usa $u_j\partial_j u_i=u_j\partial_i u_j-u_j(\partial_i u_j-\partial_j u_i)=
\partial_i(\tfrac12 u_ju_j)-u_j\epsilon_{ijk}\omega_k\cdot(\text{signo})$, que tras acomodar
signos con el tensor de Levi-Civita da exactamente $\partial_i(|\mathbf u|^2/2)-(\mathbf
u\times\boldsymbol\omega)_i$. Este es el paso algebraico que separa, dentro del término de
advección, lo que va a la presión de lo que vive en $\Gamma_a$.

---

## §2. De la EOM general a Stokes y Navier-Stokes

### 2.1 Los tres límites, explicados uno por uno

La EOM completa es de segundo orden en el tiempo y tiene un término no lineal
($\mathrm{adj}(\Gamma)$, que aparece en la fuerza del potencial). Stokes, en cambio, es de
**primer orden** y **lineal**. Para pasar de una a la otra hacen falta tres límites, cada uno con
un nombre físico preciso:

1. **Fricción alta** ($\varepsilon=1/(\gamma T)\to0$, con $T$ una escala de tiempo característica
   del sistema). Intuición: si la fricción $\gamma$ es muy grande comparada con la escala de
   tiempo de interés, el término de inercia $\ddot\Gamma$ se vuelve despreciable frente a
   $\gamma\dot\Gamma$ — la ecuación efectivamente "pierde memoria" de la aceleración y pasa a
   primer orden. Este es exactamente el límite de **Smoluchowski-Kramers** de la dinámica de
   Langevin de alta fricción (un resultado estándar de procesos estocásticos, Nelson 1967), no
   una aproximación ad hoc de este paper.
2. **Amplitud pequeña** ($|\mathbf v|\sim\varepsilon\to0$). El término no lineal
   $\mathrm{adj}(\Gamma)$ escala como el cuadrado de la amplitud de la perturbación, así que para
   perturbaciones pequeñas se vuelve subdominante frente a los términos lineales.
3. **Escala corta** ($L\ll c$, equivalente a número de Mach bajo). El término de "masa
   estructural" (el que le da a Γ una longitud de pantalla $\ell=c$) se vuelve despreciable frente
   al término difusivo $c^2\nabla^2\Gamma$ cuando la escala espacial de interés es mucho menor que
   $c$. Es el límite incompresible estándar de mecánica de fluidos (Mach bajo), con teoremas de
   convergencia publicados (Schochet 2010; Lions-Masmoudi 1998).

Cada uno de estos tres es un teorema de convergencia **ya publicado en su propio dominio** —
el aporte de este paper no es demostrarlos de nuevo, es identificar que los tres, aplicados
simultáneamente a la EOM de GSF, dan exactamente Stokes:
$$\boxed{\partial_t v_i=\nu_{\mathrm{kin}}\nabla^2 v_i-\frac1\rho\partial_i p,\qquad\nabla\cdot\mathbf v=0,\qquad\nu_{\mathrm{kin}}=\frac{c^2(\rho)}\gamma.}$$

**Lo que está probado y lo que no.** La forma del límite y su existencia están demostradas
(cada eslabón es un teorema citable). Lo que falta es la constante explícita $C$ de la cota
$\|\Gamma-u\|\le C\cdot\max(\varepsilon,\mathrm{Ma},L/c)$ en el formalismo matricial específico de
Γ — adaptar esa cota desde los papers originales (que hablan de campos escalares/vectoriales, no
de una matriz $4\times4$) queda como trabajo pendiente, nombrado así en el propio paper.

### 2.2 De Stokes a Navier-Stokes: la covarianza galileana, derivada a mano

Esta es la pieza de álgebra que el paper resume en una frase ("verificado simbólicamente") y que
vale la pena hacer completa, porque es el tipo de cálculo que un estudiante debería poder repetir
solo.

**La pregunta.** Bajo un cambio de marco de referencia con velocidad constante $\mathbf V$ (un
boost galileano), $\mathbf x'=\mathbf x-\mathbf V t$, $t'=t$: ¿qué forma de derivada temporal es
invariante?

**El cálculo.** Un campo $f$ tiene dos descripciones, $f(\mathbf x,t)$ en el marco original y
$f'(\mathbf x',t')$ en el marco que se mueve con $\mathbf V$, relacionadas por
$f'(\mathbf x',t')=f(\mathbf x,t)$ con $\mathbf x=\mathbf x'+\mathbf Vt'$ (mismo punto físico,
descrito en las dos coordenadas). Deriva respecto a $t'$ manteniendo $\mathbf x'$ fija, usando la
regla de la cadena:
$$\left.\frac{\partial f'}{\partial t'}\right|_{\mathbf x'}=\left.\frac{\partial f}{\partial t}\right|_{\mathbf x}\cdot\underbrace{\frac{\partial t}{\partial t'}}_{=1}+\nabla_{\mathbf x}f\cdot\underbrace{\left.\frac{\partial\mathbf x}{\partial t'}\right|_{\mathbf x'}}_{=\mathbf V}=\partial_tf+\mathbf V\cdot\nabla f.$$
Es decir: **la derivada parcial temporal sola no es invariante** — al cambiar de marco, adquiere un
término extra $\mathbf V\cdot\nabla f$ que depende de la velocidad relativa entre los marcos. Un
término $\partial_t(\cdot)$ suelto en una ecuación de campo no puede ser, por sí solo, la forma
correcta de una ley física que debe verse igual en todo marco inercial.

**La reparación.** La velocidad del fluido se transforma como cualquier velocidad bajo un boost
galileano: $\mathbf u'=\mathbf u-\mathbf V$ (la velocidad medida en el marco que se mueve con
$\mathbf V$ es menor en $\mathbf V$). Ahora arma la derivada material en el marco primado y
sustituye:
$$\frac{D'f'}{Dt'}=\partial_{t'}f'+(\mathbf u'\cdot\nabla')f'=(\partial_tf+\mathbf V\cdot\nabla f)+\big[(\mathbf u-\mathbf V)\cdot\nabla f\big]=\partial_tf+(\mathbf u\cdot\nabla)f=\frac{Df}{Dt}.$$
Los términos en $\mathbf V$ se cancelan exactamente. **$D/Dt=\partial_t+(\mathbf u\cdot\nabla)$ es
la única combinación de primer orden que es invariante de forma bajo un boost galileano** — no es
un ingrediente que Navier-Stokes añade por fuera, es lo que la covarianza exige que aparezca en
cualquier dinámica de continuo, incluida la instancia fluida de la EOM de GSF.

**Conclusión de la sección.** Sustituyendo $\partial_t\to D/Dt$ en los slots de flujo ya fijados en
§1, y usando la identidad de Lamb de §1.4 para separar la parte de gradiente (presión) de la parte
irreducible ($\Gamma_a$), se recupera exactamente
$$\partial_t\mathbf u+(\mathbf u\cdot\nabla)\mathbf u=\nu\nabla^2\mathbf u-\frac1\rho\nabla p+\mathbf f,\qquad\nabla\cdot\mathbf u=0.$$
Navier-Stokes completo, con el término de advección incluido, sale del mismo postulado de
asignación de grados que Stokes — sin ningún parámetro ni postulado adicional. La única frontera
que queda abierta aquí es puramente algebraica (el weld Clifford→$M_4(\mathbb R)$), no específica
de fluidos.

---

## §3. La operacionalización de γ

La identidad central del paper:
$$\nu_{\mathrm{kin}}=\frac{c^2(\rho)}{\gamma}\quad\Longleftrightarrow\quad\gamma=\frac{c^2(\rho)}{\nu_{\mathrm{kin}}}.$$
Con esto, el número de Reynolds (adimensional, $\mathrm{Re}=vL/\nu$) se reescribe en términos del
parámetro estructural de la EOM:
$$\mathrm{Re}=\frac{vL}{\nu_{\mathrm{kin}}}=\frac{vL\,\gamma}{c^2(\rho)}.$$
Léelo así: **$\mathrm{Re}$ es, salvo el factor geométrico $vL$, el inverso de $\gamma$** —
amortiguación alta (γ grande) es viscosidad alta es Stokes (Re bajo); amortiguación baja es
inviscido/Euler (Re alto). Este es el puente conceptual que conecta §2 (la reducción a Stokes) con
§6 (qué pasa cuando Re no es bajo, y el flujo empieza a transicionar).

**La frontera nombrada aquí, y que conviene no perder de vista en las secciones siguientes:** la
rigidez de campo $c^2(\rho)$ viene de una ley de escala del programa GSF más amplio, no
establecida en los papers compañeros citados — se usa como **hipótesis de entrada**. A las
densidades de cualquier fluido terrestre, esa ley predice $c^2$ efectivamente constante, lo cual
es lo que permite que §4 convierta razones de $\gamma$ en razones puras de viscosidad tabulada
(ver más abajo por qué eso es válido incluso sin conocer el valor absoluto de $c^2$).

---

## §4. Los datos, y por qué "sin ajustar nada" es una afirmación verificable

### 4.1 Por qué las razones de viscosidad no necesitan conocer $c^2$

Si $c^2$ es (aproximadamente) la misma constante para dos fluidos $A,B$ a densidades terrestres,
entonces
$$\frac{\gamma_A}{\gamma_B}=\frac{c^2/\nu_A}{c^2/\nu_B}=\frac{\nu_B}{\nu_A}.$$
El $c^2$ se cancela — la razón de amortiguaciones estructurales es, exactamente, la razón inversa
de viscosidades cinemáticas tabuladas. Esto es lo que permite comparar mercurio con manto
terrestre (24 órdenes de magnitud de diferencia) sin necesitar el valor absoluto de $c^2$ ni de
$\gamma$: **es una predicción sobre razones, verificable con datos de ingeniería estándar, sin
ningún parámetro libre nuevo** — el único supuesto es que ambos fluidos comparten la misma
densidad estructural $\rho$ (un supuesto explícito, nombrado en el paper, no verificado
independientemente).

*Nota de honestidad aritmética.* El resumen del paper dice "veinticuatro" órdenes de magnitud, no
veinticinco — es una corrección de una versión anterior, verificada por script
(`code/verificacion_razones_viscosidad.py`): el rango real es 24.4, y el manto terrestre en
particular reproduce con ~11% de diferencia (es un valor de orden de magnitud citado en la
literatura, no una medición de precisión), mientras el resto de la tabla reproduce con <1%.

### 4.2 γ∝ρ: por qué 0.1% en cinco décadas es un resultado fuerte

Para el aire, la viscosidad cinemática obedece $\nu\propto1/\rho$ (dato experimental estándar,
válido en régimen continuo) sobre presiones de $10^{-3}$ a $10$ atm — cinco órdenes de magnitud de
densidad. Combinando esto con $c^2$ aproximadamente constante en ese rango (la misma saturación de
§3):
$$\gamma=\frac{c^2}{\nu}\propto\frac{1}{1/\rho}=\rho.$$
La proporcionalidad $\gamma\propto\rho$ no se ajusta — **se deriva** de combinar dos hechos ya
establecidos independientemente ($\nu\propto1/\rho$ del aire, y $c^2$ constante a esas densidades).
Que la predicción resultante coincida a 0.1% con la medición es la confirmación más fuerte del
paper de la relación estructural entre γ y la densidad.

### 4.3 La calibración absoluta es condicional, y hay que leerla así

Todo lo anterior son *razones*. Para pasar a un valor absoluto de γ hace falta una hipótesis
adicional, no una medición: que $c^2(\rho_{\mathrm{agua}})\approx c^2_{\mathrm{luz}}$. Bajo esa
hipótesis, $\gamma_{\mathrm{agua}}\approx9\times10^{22}\,\mathrm s^{-1}$, con un tiempo de
relajación estructural de orden $10^{-23}\,\mathrm s$ — un número que el paper marca
explícitamente como predicción condicional, no medición, precisamente porque descansa en una
hipótesis teórica no verificada. Vale la pena que el estudiante note la diferencia de estatus
entre esta sección (condicional) y las dos anteriores (verificadas contra datos tabulados).

---

## §5. La identidad acústica-electromagnética, en una frase

En el límite sin vorticidad y sin fuentes ($\Gamma_a=0$), la EOM se reduce a la ecuación de onda
sin masa $\Box\varphi=0$ para el potencial de velocidad — el mismo mecanismo estructural que da el
fotón libre en el paper compañero de electromagnetismo. La analogía acústica-electromagnética
clásica (Bergmann 1946), ya conocida y usada en cloaking acústico, se relee aquí como una
consecuencia estructural: ambos fenómenos son instancias del mismo sector $\det=0$ (γ≈0, régimen
de onda) del mismo objeto algebraico, no una analogía formal entre dos ecuaciones parecidas.

---

## §6. La transición subcrítica en tubería: derivación completa del escalamiento Re²

Esta es la sección de mayor interés aplicado del paper, y la que más vale la pena reconstruir a
mano — el paper cita "verificado numéricamente: pendiente log-log de 2.000" sin mostrar de dónde
sale ese 2. Aquí sí se muestra.

### 6.1 Qué es un operador no normal, y por qué importa

Reteniendo el término de segundo orden que la reducción a Stokes descarta (§2.1, límite de
fricción alta), la EOM linealizada alrededor de un estado base da un sistema de primer orden en
$\mathbf Y=(\delta\Gamma,\dot{\delta\Gamma})$:
$$\dot{\mathbf Y}=\mathcal A\mathbf Y,\qquad\mathcal A=\begin{pmatrix}0&I\\-\mathcal L_{\bar\Gamma}&-\gamma I\end{pmatrix}.$$
**Un operador $\mathcal A$ es normal** si conmuta con su propio adjunto, $\mathcal A\mathcal
A^\top=\mathcal A^\top\mathcal A$. Una matriz simétrica o antisimétrica real siempre es normal;
una matriz genérica no. La propiedad importante: **si $\mathcal A$ es normal, sus autovalores
determinan todo el comportamiento de $\|e^{\mathcal At}\|$** (crece o decae monótonamente, sin
sorpresas). **Si $\mathcal A$ NO es normal, puede haber amplificación transitoria enorme** —
$\|e^{\mathcal At}\|$ puede crecer mucho antes de decaer, incluso si todos los autovalores tienen
parte real negativa (estable a largo plazo). Este es exactamente el mecanismo detrás de la
transición subcrítica: el flujo en tubería es linealmente estable (ningún autovalor cruza a
inestable) pero perturbaciones pequeñas se amplifican transitoriamente lo suficiente como para
disparar no-linealidades y turbulencia — el mecanismo de "estabilidad hidrodinámica sin
autovalores" de Trefethen et al. (1993).

### 6.2 El resultado en tres pasos, cada uno con su porqué

**Paso 1 — diagonal prohíbe el crecimiento.** Si $\Gamma$ (y por tanto $\mathcal L_{\bar\Gamma}$)
es puramente diagonal, $\mathcal A$ es simétrica por bloques de una forma que la hace normal:
no hay acoplamiento fuera de la diagonal, así que $G_{\max}=1$ para todo Re — ninguna
amplificación transitoria es posible. El mecanismo lift-up necesita, por definición,
acoplamiento entre componentes distintas (una componente "alimenta" a otra), que no puede vivir
en la diagonal.

**Paso 2 — el gradiente del potencial no puede darlo (no-go demostrado, no observado).** Este es
el paso más bonito del argumento. El Hessiano de cualquier potencial $P(\Gamma)$ es simétrico,
porque las derivadas parciales mixtas conmutan (teorema de Schwarz/Clairaut):
$$\frac{\partial^2P}{\partial\Gamma_{ij}\partial\Gamma_{kl}}=\frac{\partial^2P}{\partial\Gamma_{kl}\partial\Gamma_{ij}}.$$
Simétrico $\Rightarrow$ normal $\Rightarrow$ diagonalizable con autovalores reales $\Rightarrow$
**ningún crecimiento transitorio posible por construcción**, sea cual sea la forma detallada de
$P$. Este resultado descarta, de una vez, que **cualquier** perturbación no simétrica de la EOM
*desnuda* de Γ (sin el término convectivo) alcance el escalamiento Re²: verificado numéricamente
que un acoplamiento no normal genérico (construido a mano, sin la estructura lift-up específica)
da solo $G_{\max}\sim\mathrm{Re}^1$, no $\mathrm{Re}^2$ — la no-normalidad genérica es necesaria
pero no suficiente.

**Paso 3 — el término convectivo sí lo da, y no es un ingrediente ajeno.** El acoplamiento lift-up
correcto sale, exactamente, de linealizar el término convectivo $(\mathbf u\cdot\nabla)\mathbf u$
alrededor de un perfil de cizalla base $U(y)$: la parte $(\mathbf u'\cdot\nabla)\mathbf U$ acopla
la componente normal $u_y'$ dentro de la ecuación de $u_x'$ con coeficiente $S=\partial_yU(y)$ (la
cizalla del flujo base). Esto **no** es un ingrediente añadido para este resultado: es exactamente
el mismo término que §2.2 ya mostró que la covarianza galileana obliga a incluir. El acoplamiento
resultante es $u_y'\to u_x'$ pero no al revés — genuinamente fuera de la diagonal, vive en
$\Gamma_a$, no en el gradiente.

### 6.3 El cálculo cerrado: de dónde sale exactamente Re²

Aquí está la derivación completa que el paper resume con "verificado numéricamente". El operador
lift-up mínimo, de primer orden, con daño $1/\mathrm{Re}$ en ambas componentes y acoplamiento de
cizalla $c$:
$$\mathcal A=\begin{pmatrix}-1/\mathrm{Re}&0\\c&-\chi/\mathrm{Re}\end{pmatrix}.$$

**Caso $\chi=1$ (defectivo, bloque de Jordan).** Escribe $\mathcal A=-\tfrac1{\mathrm{Re}}I+cE$ con
$E=\begin{pmatrix}0&0\\1&0\end{pmatrix}$. Como $E^2=0$ (nilpotente), la exponencial de matriz trunca
exacta: $e^{ctE}=I+ctE$. Entonces
$$e^{\mathcal At}=e^{-t/\mathrm{Re}}\begin{pmatrix}1&0\\ct&1\end{pmatrix}.$$
El valor singular más grande de esta matriz, para $ct\gg1$, es aproximadamente $|ct|$ (la entrada
que crece). Así que $\|e^{\mathcal At}\|\approx c\,t\,e^{-t/\mathrm{Re}}$. Maximiza sobre $t$:
$$\frac{d}{dt}\left(c\,t\,e^{-t/\mathrm{Re}}\right)=c\,e^{-t/\mathrm{Re}}\left(1-\frac{t}{\mathrm{Re}}\right)=0\quad\Longrightarrow\quad t^*=\mathrm{Re}.$$
En $t=t^*$: $\|e^{\mathcal At^*}\|\approx c\,\mathrm{Re}\,e^{-1}=c\,\mathrm{Re}/e$. Por tanto
$$G_{\max}=\|e^{\mathcal At^*}\|^2\approx\frac{c^2\,\mathrm{Re}^2}{e^2}.$$
**Ahí está el Re² — sale de maximizar $t\,e^{-t/\mathrm{Re}}$, un cálculo de una variable, cálculo
1.** El máximo ocurre en $t^*=\mathrm{Re}$ (el tiempo característico de decaimiento) precisamente
porque ahí el crecimiento lineal en $t$ todavía no ha sido vencido por el decaimiento exponencial.

**Caso $\chi=2$ (no defectivo, el modelo de Gustavsson).** Resolviendo la EDO componente a
componente ($y_1(t)=e^{-t/\mathrm{Re}}$, y sustituyendo en la ecuación de $y_2$):
$$y_2(t)=c\int_0^te^{-2(t-s)/\mathrm{Re}}e^{-s/\mathrm{Re}}\,ds=c\,\mathrm{Re}\left(e^{-t/\mathrm{Re}}-e^{-2t/\mathrm{Re}}\right).$$
Con $s=t/\mathrm{Re}$, maximiza $f(s)=e^{-s}-e^{-2s}$: $f'(s)=-e^{-s}+2e^{-2s}=0\Rightarrow
e^{s}=2\Rightarrow s^*=\ln2$. En $s^*$: $f(s^*)=\tfrac12-\tfrac14=\tfrac14$. Entonces
$$y_2^{\max}=\frac{c\,\mathrm{Re}}4\quad\Longrightarrow\quad G_{\max}\approx\left(\frac{c\,\mathrm{Re}}4\right)^2=\frac{c^2\,\mathrm{Re}^2}{16}.$$

**En ambos casos, $G_{\max}\propto\mathrm{Re}^2$ exacto, con una constante puramente geométrica**
($e^2$ o $16$, según la estructura del bloque) que no depende de Re — esto es lo que el paper
llama "el prefactor geométrico fijado desde el álgebra del operador", y por qué el ajuste
log-log da pendiente 2.000: la potencia 2 no es un ajuste, sale de maximizar $t\,e^{-t/\mathrm{Re}}$
o $e^{-t/\mathrm{Re}}-e^{-2t/\mathrm{Re}}$, cuyo máximo escala linealmente con Re en ambos casos, y
se eleva al cuadrado al pasar de norma a $G=\|\cdot\|^2$.

### 6.4 Qué se puede afirmar, y qué no

**Formulación precisa (para no sobre-reclamar).** El escalamiento Re² no sale de la EOM desnuda de
Γ con cualquier perturbación no simétrica (descartado en el Paso 2). Sale de la instancia fluida
completa — Navier-Stokes con su término convectivo (§2.2) — linealizada alrededor de un perfil de
cizalla base. Ese perfil $U(y)$ sigue siendo un dato externo, el mismo que exige toda la teoría
estándar de estabilidad hidrodinámica (Orr-Sommerfeld/Squire) — no es específico de este marco.

### 6.5 Comparación con el Re crítico observado

Con una constante geométrica $C\approx50$ y una amplitud umbral $A_0\approx10^{-7}$ (tomadas de
Hof et al. 2003, no derivadas), la cadena predice $\mathrm{Re}_c\approx2200$, en acuerdo razonable
con el $\mathrm{Re}_c\approx2040$ observado. Hay que separar con precisión:
- **Estructural, derivado:** que el escalamiento es Re² y no otra potencia; que requiere
  estrictamente $\Gamma_a$ activo; que la cizalla no puede venir del sector de gradiente.
- **Dependiente de literatura:** el valor numérico exacto de $\mathrm{Re}_c$, que necesita $C$ y
  $A_0$ medidos experimentalmente, no derivados de la EOM.

Un segundo régimen de la misma ecuación explica la diferencia cualitativa tubería/canal: el canal
transita por un mecanismo modal (Tollmien-Schlichting, $\mathrm{Re}_c\approx5772$); la tubería,
donde ese modo es linealmente estable para todo Re, transita por el mecanismo no modal de
crecimiento transitorio en $\mathrm{Re}_c\approx2040$. Mismo objeto Γ, misma ecuación — lo que
distingue los regímenes es la geometría, no un parámetro distinto del fluido.

---

## Figuras y scripts reutilizables de `code/`

- `pieza2_transient_growth.py` — reproduce exactamente los cálculos cerrados de §6.3 (Partes A-B),
  el no-go del gradiente (Parte E), y la derivación de la cizalla desde el término convectivo
  (Parte F). Es el script que vale la pena correr en paralelo con esta sección.
- `verificacion_razones_viscosidad.py` — reproduce la tabla de §4.1 desde los valores de ν citados;
  confirma los ~24.4 órdenes de magnitud y el 11% de diferencia del manto terrestre.
- `caso_iron_bridge_united_pipeline.py` — caso de ingeniería real (oleoducto de lechada, United
  Pipeline Systems) que aplica el mecanismo de §6 con la librería `models/sair/`, incluyendo la
  distinción entre el Re_c hidrodinámico de esta sección y el "Re crítico" empírico de depósito de
  sólidos de la práctica de diseño de lechadas — dos cosas distintas, ver advertencia en el script.

---

# Parte III — Checklist de preguntas abiertas

Para cada una, intenta responderla sin mirar la sección referida — si no puedes, es un hueco real
en tu comprensión, no del paper.

1. **§1.** ¿Por qué $A=D\mathbf u/Dt$ y no $A=\mathbf u$? Da la razón formal (invariancia bajo
   boost), no solo "porque coincide con Cauchy". → §1.1.
2. **§1.** ¿Por qué $R=\nabla p$ falla el criterio de trabajo, si intuitivamente "presión" parece
   el candidato correcto para completar la ecuación? → §1.2.
3. **§2.2.** Deriva tú mismo, sin mirar, por qué $\partial_t$ solo no es invariante de forma bajo
   un boost galileano, y por qué $D/Dt$ sí lo es. → §2.2.
4. **§6.** ¿Por qué un Hessiano nunca puede producir el mecanismo lift-up, sea cual sea la forma
   detallada del potencial $P$? → §6.2, Paso 2.
5. **§6.3.** Repite la maximización de $t\,e^{-t/\mathrm{Re}}$ (caso $\chi=1$) sin ver la
   respuesta. ¿En qué $t^*$ ocurre el máximo, y por qué ese valor tiene sentido físico (pista:
   compáralo con el tiempo de decaimiento $1/\mathrm{Re}$)?
6. **§4.3.** ¿Qué widget de la cadena de razonamiento distingue la calibración absoluta de γ (§4.3)
   de las razones de viscosidad (§4.1)? ¿Por qué una es condicional y la otra no?
7. **Fuera de este cuaderno, pregunta abierta real:** la constante $C$ explícita del teorema de
   convergencia a Stokes (§2.1) no está adaptada al formalismo matricial de Γ. ¿Qué tendría que
   pasar para cerrarla? (No hay respuesta en el paper — es investigación futura nombrada.)

---

# Parte IV — Tabla de estatus única

| # | Resultado | Estatus | Nota |
|---|---|:---:|---|
| 1 | Diccionario SAIR en fluidos (S=ρ,A=Du/Dt,I=u,R=∇) | [D]/[V] | mecanismos (a)/(b), sin autorreferencia |
| 2 | Γ_a=I∧R=∇×u=ω derivado, no asignado | [D] | identidad algebraica directa |
| 3 | Identidad de Lamb (u·∇)u=∇(|u|²/2)−u×ω | [D] | cálculo vectorial estándar |
| 4 | Stokes como límite singular (3 condiciones) | [D] forma / [F] constante explícita | cada eslabón, teorema citado; adaptación matricial pendiente |
| 5 | Navier-Stokes completo vía covarianza galileana | [D] | D/Dt es la única forma invariante de 1er orden bajo boost |
| 6 | ν=c²(ρ)/γ | 〔DEF〕 operacionalización central | no un teorema, la definición que el resto del paper prueba útil |
| 7 | Razones de viscosidad, ~24.4 órdenes | [V] | verificado por script contra datos citados; supuesto de ρ común, explícito |
| 8 | γ∝ρ, 0.1% en 5 décadas (aire) | [V] | combina dos hechos ya establecidos, no un ajuste nuevo |
| 9 | Calibración absoluta γ_agua≈9×10²² s⁻¹ | [F] condicional | depende de c²(ρ_agua)≈c²_luz, no verificado |
| 10 | Identidad acústica-EM en det=0 | [CE] | consecuencia estructural, no analogía formal |
| 11 | Diagonal prohíbe crecimiento transitorio (G_max=1) | [D] | matriz normal por construcción |
| 12 | No-go: ∇²P no puede dar lift-up | [D] | Hessiano simétrico ⇒ normal, teorema de Schwarz |
| 13 | Cizalla sale del término convectivo (S=∂_yU) | [D] | mismo término que exige la covarianza galileana de §2.2 |
| 14 | G_max~Re²/C, cálculo cerrado (χ=1, χ=2) | [D] | derivado aquí explícito, no solo "verificado numéricamente" |
| 15 | Re_c≈2040-2200 en tubería, valor numérico | [V] cualitativo, no de primer principio | usa C, A₀ de Hof et al. 2003 |
| 16 | Escala absoluta de ρ | [F] | abierto, referido al programa más amplio |
| 17 | Ley de escala c²(ρ) | 〔hipótesis de entrada〕 | no establecida en los papers compañeros citados |

---

*Cuaderno de trabajo — Programa Gamma Space Framework. Julio 2026.*
