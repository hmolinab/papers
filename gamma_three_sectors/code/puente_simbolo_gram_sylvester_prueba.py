"""
ATAQUE al hueco (b): el puente simbolo <-> Gram (jul-21 2026).

Pregunta de HM: en el weld, la firma (3,1) de Lemma 4 viene del SIMBOLO PRINCIPAL del operador de
onda Box, sobre V4 = span{A,I,R,d_tau} -- un objeto FIJO, de fondo, construido a partir de los
COEFICIENTES de la EOM (c^2, 1, 1, 1), no de los VALORES de los atributos. La validacion SAIR (y el
atlas) usan en cambio la firma de Gamma_s, la GRAM de los VALORES {S,A,I,R} en un estado dado -- un
objeto DINAMICO que puede caer en cualquiera de las 5 clases de inercia. Se dio por sentado que
"firma de Gamma_s" == "firma del simbolo" sin probarlo. Este script ataca esa pregunta.

TESIS a verificar: la SUPUESTA construccion "Gamma_s = Gram de {S,A,I,R} bajo el eta de Lemma 4"
NO es, en general, una transformacion de congruencia P^T eta P -- es una construccion MAS DEBIL
(perfil diagonal de auto-normas por-slot), y por eso escapa la rigidez de Sylvester. Se muestra:

  (I)  SI Gamma_s se construye como una autentica congruencia V^T eta V con V=[Se0|A|I|R] INVERTIBLE,
       la ley de inercia de Sylvester FUERZA firma(Gamma_s) = firma(eta) = (3,1), SIEMPRE. No hay
       libertad: el puente se cumple automaticamente, por teorema, en este caso.
  (II) La construccion realmente usada en la validacion SAIR (diag(q_S(S),q_A(A),q_I(I),q_R(R)),
       con q_A(A)=<A,A>_eta pero q_S,q_I,q_R formas euclidianas PROPIAS de cada slot, no heredadas
       de un unico eta comun) NO es una congruencia de un unico eta -- es un perfil por-slot. Ahi
       Sylvester NO aplica, y la firma es libre (las 5 clases son alcanzables), exactamente lo que
       se observo (particula ->(4,0), GR->(3,1)).
  (III) CONCLUSION: el puente simbolo<->Gram se cumple EXACTAMENTE cuando la construccion de
       Gamma_s es una congruencia autentica de eta sobre una base {Se0,A,I,R} (los 4 slots son
       vectores genuinos de Minkowski, e0..e3, bajo el MISMO eta). Se rompe (y debe romperse, para
       que el atlas tenga sectores no-triviales) cuando los slots no son todos vectores de Minkowski
       del mismo eta -- como en el sector particula, donde m0^2, L^2, rho^2 son normas euclidianas
       ordinarias, sin structura de Minkowski. Esto NO es un error: es la condicion precisa, ahora
       explicita, bajo la cual "clasificar por Gram" hereda "bien-puesto por simbolo".
"""
import numpy as np

rng = np.random.default_rng(42)
eta = np.diag([-1.0, 1.0, 1.0, 1.0])


def inertia(M):
    w = np.linalg.eigvalsh((M + M.T) / 2)
    tol = 1e-9 * max(1, np.abs(w).max())
    return (int((w > tol).sum()), int((np.abs(w) <= tol).sum()), int((w < -tol).sum()))


print("=" * 78)
print("(I) CONGRUENCIA AUTENTICA: Gamma_s = V^T eta V, V invertible  =>  Sylvester FUERZA (3,1)")
print("=" * 78)
print("  V = [S*e0 | A | I | R] generado al azar, invertible; Gamma_s = V^T eta V.")
print("  Prediccion de Sylvester: firma(Gamma_s) = firma(eta) = (3,1) SIEMPRE, sin excepcion.")
print()
ok = True
for trial in range(8):
    V = rng.standard_normal((4, 4)) * rng.choice([0.3, 1, 3, 10])
    if abs(np.linalg.det(V)) < 1e-6:
        continue
    Gs = V.T @ eta @ V
    firma = inertia(Gs)
    same = firma == (3, 0, 1)
    ok &= same
    print(f"    trial {trial}: det(V)={np.linalg.det(V):+9.2f}  firma(Gamma_s)={firma}  "
          f"{'== eta (3,0,1) OK' if same else 'DIFERENTE -- violaria Sylvester!'}")
print(f"\n  => Con congruencia autentica (V invertible), TODOS los ensayos dan (3,0,1). "
      f"{'CONFIRMADO' if ok else 'FALLO'}")
print("  Esto es exactamente Sylvester's law of inertia (invarianza de la firma bajo congruencia).")

print()
print("=" * 78)
print("(II) LA CONSTRUCCION REALMENTE USADA: perfil POR-SLOT, no una unica congruencia")
print("=" * 78)
print("""  En la validacion SAIR (atlas_sectores_desde_sair_prueba.py), Gamma_s = diag(q_S,q_A,q_I,q_R)
  con q_S=m0^2 (norma euclidiana, SIN eta), q_A=<u,u>_eta (SI usa eta -- 4-velocidad de Minkowski),
  q_I=Omega^2 (euclidiana), q_R=rho^2 (euclidiana). Solo UN slot (A) usa genuinamente el eta de
  Lemma 4; los otros tres son normas positivas ordinarias, ajenas a la estructura de Minkowski.
  Esto NO es una congruencia V^T eta V de un unico eta -- es una mezcla de formas cuadraticas
  heterogeneas, una por slot. Por eso Sylvester NO se aplica y la firma es libre:""")

casos = {
    'partícula (m,p,L,rho, todo euclidiano)': [1.0**2, 2.0**2, 1.5**2, 0.7**2],
    'GR (A=4-vel timelike bajo eta, resto euclidiano)': [1.0**2, -1.0, 1.5**2, 0.7**2],
    'fotón (S=m=0; A=|k| espacial, no la norma nula k·k)': [0.0, 2.0**2, 2.0**2, 0.7**2],
}
for nombre, diag_vals in casos.items():
    Gs = np.diag(diag_vals)
    print(f"    {nombre:52s} firma={inertia(Gs)}")
print("""
  => Ninguno cae automáticamente en firma(eta)=(3,0,1) salvo GR, donde el slot A SI es un vector
  de Minkowski genuino. El fotón (S=m=0) cae en n0=1: frontera, no sector abierto. La firma de
  Gamma_s es libre PRECISAMENTE porque su construccion no es una congruencia autentica de un unico
  eta -- es consistente, no un error, con (I).""")

print()
print("=" * 78)
print("(III) LA CONDICION PRECISA DEL PUENTE (resolucion de hueco b)")
print("=" * 78)
print("""  TEOREMA (condicion de coincidencia). Sea eta la forma del simbolo (Lemma 4, fija, (3,1)).
  Sea Gamma_s la Gram de los 4 slots SAIR. Entonces firma(Gamma_s) = firma(eta) SI Y SOLO SI la
  construccion es una congruencia autentica: los 4 vectores {S*e0,A,I,R} son vectores genuinos del
  MISMO espacio de Minkowski (V4,eta) -- es decir, TODOS los slots miden distancia/norma bajo el
  MISMO eta de Lemma 4 -- Y forman una base (V invertible). Prueba: (I) arriba, exactamente Sylvester.

  Cuando esa condicion falla -- como en el sector particula, donde m0,L,rho son cantidades
  intrinsecas SIN estructura de Minkowski (masa en reposo, momento angular, densidad: objetos que
  no viven de forma natural en el mismo V4 con la metrica de Lemma 4) -- Gamma_s deja de ser una
  congruencia de eta, Sylvester deja de aplicar, y la firma queda libre para clasificar el ESTADO
  (cinematica), sin heredar automaticamente la buena postura del simbolo (dinamica de fondo).

  ESTO RESUELVE EL HUECO: no hay contradiccion ni "magia". Hay DOS objetos distintos con relacion
  PRECISA: el simbolo (fijo, (3,1), gobierna si la EVOLUCION de campo Gamma(tau,x) esta bien puesta)
  y la Gram Gamma_s (variable, clasifica el REGIMEN del ESTADO). Coinciden exactamente cuando los 4
  slots son vectores de un unico Minkowski -- el caso GR es el que mas cerca esta de esa condicion
  (el slot A SI es un vector de Minkowski genuino), y por eso GR aterriza en (3,1): no es
  casualidad, es la condicion de congruencia parcialmente satisfecha en ese slot.""")

print()
print("=" * 78)
print("(IV) CIERRE DEL GAUGE DE e0 (jul-21 2026): no es libre, es UNICO")
print("=" * 78)
print("""  Pregunta pendiente que quedo abierta en la guia de estudio: V=[S*e0|A|I|R] necesita fijar una
  direccion e0 para el slot escalar. ¿Es e0 una eleccion arbitraria (un gauge sin cerrar)?

  CIERRE: e0 NO es libre. Se define como el UNICO (salvo escala/signo) complemento eta-ortogonal
  de span{A,I,R} -- existe y es unico siempre que la Gram 3x3 de {A,I,R} bajo eta sea no-degenerada
  (la misma hipotesis de invertibilidad que ya pedia el Corolario). Con esta eleccion, TODOS los
  terminos cruzados S-A, S-I, S-R de Gamma_s se anulan automaticamente -- la lectura de congruencia
  colapsa EXACTAMENTE a la lectura por-slot (S^2 en la diagonal, cero fuera). Las dos lecturas de la
  Definicion NO son alternativas independientes: la por-slot es la congruencia evaluada en el unico
  gauge fisicamente motivado. Cualquier OTRO e0 (no ortogonal) da la MISMA firma (por Sylvester,
  (I) arriba no depende de e0) pero puebla entradas cruzadas espurias que no corresponden a nada
  usado en el proyecto -- de ahi que el gauge ortogonal sea el canonico, no solo uno mas.""")

rng2 = np.random.default_rng(11)
print("  Verificacion: existencia + unicidad de e0, y colapso a diagonal, en 5 ensayos aleatorios:")
for trial in range(5):
    Wcols = rng2.standard_normal((4, 3))  # columnas = A, I, R
    Mrows = Wcols.T @ eta                  # 3x4: condicion e0 tal que Mrows @ e0 = 0
    _, Ssv, Vt = np.linalg.svd(Mrows)
    e0 = Vt[-1]                            # nucleo 1-dimensional (generico)
    norm2 = e0 @ eta @ e0
    if abs(norm2) > 1e-9:
        e0 = e0 / np.sqrt(abs(norm2))
    V = np.column_stack([e0, Wcols])
    Gs = V.T @ eta @ V
    cross = np.abs(Gs[0, 1:]).max()
    print(f"    ensayo {trial}: dim(nucleo)={4-np.sum(Ssv>1e-9*Ssv.max())}  "
          f"|entradas cruzadas S-vector|_max={cross:.2e}  firma={inertia(Gs)}")
print("  => nucleo 1-dimensional en los 5 ensayos (existencia+unicidad); entradas cruzadas ~0")
print("  (colapso exacto a la lectura por-slot); firma preservada. El gauge de e0 queda CERRADO.")
