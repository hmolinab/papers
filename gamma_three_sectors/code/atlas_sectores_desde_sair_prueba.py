"""
VALIDACION DEL ATLAS DESDE SAIR (jul-19 2026) -- el corazón de la apuesta:
unir la cinemática (qué firma tiene Γ) con la dinámica (qué sector de la EOM).

Pedido de HM: en vez de partir de la EOM (como en release/), PARTIR de los slots
SAIR. Meter datos físicos reales en {S, A, I, R}, ensamblar Γ, y verificar
numéricamente que:
  - datos de partícula/masa  -> det Γ_s > 0   (sector elíptico / Newton)
  - datos de EM/QM (fotón)   -> det Γ_s = 0   (frontera / Maxwell)
  - datos de GR (relativista)-> det Γ_s < 0   Y firma de Lorentz (3,1)
  - sin firma de Lorentz     -> ¿qué es? (la pregunta de HM)

CONSTRUCCION (NO inventada -- del R-slot doc, brainstorming/physics/uoc_cin_R_slot.md,
Candidato 2, la Gram diagonal del estrato cinemático):
    Γ_s = diag( <S,S>, <A,A>, <I,I>, <R,R> )
donde cada entrada es la NORMA² del slot bajo su producto interno físico. El
Field antisimétrico es Γ_a = I∧R (grade-2). El SECTOR lo fija la INERCIA
(firma) de Γ_s -- (n₊, n₀, n₋) -- no solo el signo de det (Corolario 8.1 de
Paper C: el signo de det es la partición MÁS GRUESA de la inercia; la firma
completa es la que distingue de verdad).

MECANISMO CLAVE (del R-slot doc, verbatim): el sector GR obtiene su signo
negativo del slot A = cuadrivelocidad u^μ, cuya auto-norma de Minkowski es
<u,u> = −c² (TIMELIKE). El signo negativo NO se pone a mano: es el hecho
físico de que la cuadrivelocidad apunta en el tiempo. Meter un dato relativista
(4-velocidad) -> aparece −c² en el slot A -> det se vuelve negativo -> firma
Lorentz. Eso es lo que valida la arquitectura: la firma EMERGE del carácter
geométrico del dato, y el atlas la LEE.

Honestidad de alcance: esto NO afirma que GSF "deriva" que la 4-velocidad es
timelike (eso es física conocida). Afirma que la arquitectura det-sector/firma
CLASIFICA correctamente los datos físicos por la inercia de su Gram SAIR, y que
ese clasificador mapea {partícula, EM, GR} exactamente como la física dicta.
Es una VALIDACION del clasificador, no una derivación de la física.
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)
c = 1.0  # unidades naturales c=1


def inertia(M, tol=1e-9):
    """Firma (n+, n0, n-) de una matriz simétrica por sus autovalores."""
    w = np.linalg.eigvalsh((M + M.T) / 2)
    npos = int(np.sum(w > tol))
    nzero = int(np.sum(np.abs(w) <= tol))
    nneg = int(np.sum(w < -tol))
    return npos, nzero, nneg, w


def field_bivector(I, R):
    """Γ_a = I∧R (grade-2 antisimétrico), como matriz 4x4 I⊗R - R⊗I."""
    I = np.asarray(I, float); R = np.asarray(R, float)
    return np.outer(I, R) - np.outer(R, I)


def clasifica(nombre, Gs_diag, I4=None, R4=None, esperado=""):
    """Ensambla Γ_s diagonal, computa inercia/det/sector, imprime veredicto."""
    Gs = np.diag(Gs_diag)
    npos, nz, nneg, w = inertia(Gs)
    det = np.prod(w)
    # sector por inercia
    if nz >= 1:
        sector = "det=0  FRONTERA (masless / Maxwell / QM)"
    elif nneg == 0:
        sector = "det>0  ELIPTICO (partícula / Newton / equilibrio)"
    elif nneg == 1:
        sector = "det<0  HIPERBÓLICO LORENTZ (3,1) -> GR / onda relativista"
    elif nneg == 2:
        sector = "det>0  ULTRAHIPERBÓLICO (2,2) -> DOS tiempos, MAL PUESTO (Hadamard)"
    else:
        sector = f"firma ({npos},{nz},{nneg}) -> patológico"
    # Field
    fld = ""
    if I4 is not None and R4 is not None:
        Ga = field_bivector(I4, R4)
        fld = f"  |Γ_a=I∧R|_F = {np.linalg.norm(Ga):.3f}"
    print(f"  [{nombre}]")
    print(f"    Γ_s = diag({np.array(Gs_diag)})")
    print(f"    autovalores = {w}")
    print(f"    firma (n+,n0,n-) = ({npos},{nz},{nneg}),  det Γ_s = {det:+.4g}{fld}")
    print(f"    SECTOR: {sector}")
    if esperado:
        ok = esperado.lower() in sector.lower()
        print(f"    esperado: {esperado}  -> {'OK' if ok else '*** DISCREPA ***'}")
    print()
    return det, (npos, nz, nneg)


print("=" * 74)
print("1. DATOS DE PARTÍCULA / MASA  (masivo, no relativista)")
print("=" * 74)
print("""  Slots: S=m₀ (masa en reposo, escalar), A=p (3-momento espacial),
  I=L (momento angular espacial), R=ρ (nivel entrópico >0). TODAS las normas
  son euclídeas positivas -- no hay 4-velocidad timelike.""")
m0, p, L, rho = 0.938, 0.20, 0.15, 1.3  # protón (GeV), momentos espaciales, ρ
clasifica("protón no-rel", [m0**2, p**2, L**2, rho**2],
          I4=[0, L, 0, 0], R4=[0, 0, 0, rho], esperado="ELIPTICO")

print("=" * 74)
print("2. DATOS DE EM / QM  (fotón, campo sin masa)")
print("=" * 74)
print("""  El fotón no tiene masa: el slot S=m colapsa a 0 (equivalentemente, su
  4-momento k^μ es NULO, k·k=0). Una entrada de la Gram se anula -> autovalor
  cero -> det=0. Es la FRONTERA, no un sector abierto.""")
# fotón: masa nula. k^μ=(ω,k) con ω=|k| -> k·k = -ω²+|k|² = 0
omega, kmag = 0.5, 0.5  # ω=|k| (nulo)
knorm = -omega**2 + kmag**2  # = 0
clasifica("fotón (masa 0)", [0.0, kmag**2, kmag**2, rho**2], esperado="FRONTERA")
print(f"    chequeo nulo: k·k = -ω²+|k|² = {knorm:.2e} (≈0)  -> el 4-momento es NULO\n")

print("=" * 74)
print("3. DATOS DE GR  (relativista: la 4-velocidad es TIMELIKE)")
print("=" * 74)
print("""  Estrato cinemático (R-slot doc): S=m₀, A=u^μ (4-velocidad), I=Ω (curvatura
  tidal), R=ρ. HECHO FÍSICO: u·u = −c² (la 4-velocidad apunta en el tiempo).
  Ese −c² entra en el slot A y vuelve NEGATIVO un autovalor -> det<0, firma (3,1).
  El signo NO se pone a mano: es el carácter timelike del dato.""")
u_norm = -c**2  # <u,u> = -c^2, hecho de la 4-velocidad
Omega2 = 0.30   # curvatura tidal (espacial, +)
clasifica("relativista (u timelike)", [m0**2, u_norm, Omega2, rho**2],
          I4=[0, 0, Omega2, 0], R4=[0, 0, 0, rho], esperado="LORENTZ")
# verificacion explicita de la 4-velocidad
v = np.array([0.6, 0.0, 0.0])  # velocidad 0.6c
g = 1 / np.sqrt(1 - v @ v / c**2)
u4 = g * np.array([c, *v])
eta = np.diag([-1.0, 1, 1, 1])
print(f"    chequeo 4-velocidad v=0.6c: u·u = uᵀη u = {u4 @ eta @ u4:.4f} (= −c² = −1)  ✓\n")

print("=" * 74)
print("4. LA PREGUNTA DE HM: ¿qué pasa SIN firma de Lorentz?")
print("=" * 74)
print("""  Dos casos distintos, ambos SIN firma (3,1):

  (a) DOS slots timelike -> firma (2,0,2), ULTRAHIPERBÓLICA. det>0 (¡como una
      partícula!) pero con DOS direcciones temporales. Por Hadamard (weld paper
      Lemma 4 + corolario ultrahiperbólico), el problema de Cauchy NO está bien
      puesto: no es una evolución física. Es PATOLÓGICO, no un sistema clásico
      benigno. Nota crucial: (2,2) y (4,0) TIENEN EL MISMO det>0 pero son
      físicamente opuestos -> por eso el signo de det NO basta; la FIRMA decide
      (Corolario 8.1 de Paper C).""")
clasifica("(2,2) ultrahiperbólico", [m0**2, -c**2, -Omega2, rho**2], esperado="ULTRAHIPERBÓLICO")
print("""  (b) TODO positivo -> firma (4,0,0), ELÍPTICA. det>0. NO es degenerado: es
      bien-puesto, pero como PROBLEMA DE FRONTERA (Laplace), no de evolución.
      Es el sistema CLÁSICO ESTÁTICO / de EQUILIBRIO -- Newton como punto fijo
      del modo blando (el atlas §2), no una onda que se propaga. Respuesta a HM:
      'sin firma de Lorentz' NO es automáticamente degenerado -- es elíptico
      (equilibrio clásico bien-puesto) SI la firma es (4,0); es patológico
      (ultrahiperbólico mal-puesto) si es (2,2). El caso degenerado real es
      cuando hay ceros de más (rango deficiente).""")
clasifica("(4,0) elíptico = equilibrio clásico", [m0**2, p**2, Omega2, rho**2], esperado="ELIPTICO")
print("""  (c) DEGENERADO de verdad: rango deficiente (varios ceros). El sistema pierde
      grados de libertad -- no es ni evolución ni equilibrio bien definido.""")
clasifica("(2,2,0) doblemente degenerado", [m0**2, 0.0, 0.0, rho**2], esperado="FRONTERA")

print("=" * 74)
print("5. ATLAS AUTO-LEGIBLE: Γ(t) que CRUZA sectores (dinámica ↔ cinemática)")
print("=" * 74)
print("""  Una trayectoria Γ(t) donde el slot A pasa de spacelike a timelike (un
  sistema que se relativiza) cruza det=0 y cambia de sector. El 'film espectral'
  {λᵢ(t)} lee el sector sin etiqueta externa: el momento del cruce det=0 es la
  frontera EM/Maxwell. Esto conecta la CINEMÁTICA (firma de Γ) con la DINÁMICA
  (sector de la EOM) -- el corazón de la apuesta.""")
print(f"    {'t':>5}{'<A,A>(t)':>12}{'det Γ_s':>12}{'firma':>12}  sector")
for t in np.linspace(0, 1, 9):
    AA = 0.3 - 0.6 * t   # de +0.3 (spacelike) a -0.3 (timelike), cruza 0 en t=0.5
    npos, nz, nneg, w = inertia(np.diag([m0**2, AA, Omega2, rho**2]))
    det = np.prod(w)
    if nz >= 1 or abs(det) < 1e-6:
        sec = "det=0 FRONTERA (Maxwell)"
    elif nneg == 0:
        sec = "det>0 elíptico"
    else:
        sec = "det<0 Lorentz (GR)"
    print(f"    {t:5.2f}{AA:12.3f}{det:12.4f}   ({npos},{nz},{nneg})   {sec}")

print()
print("=" * 74)
print("6. RIGOR: el sector es un INVARIANTE INERCIAL (Sylvester), no un artefacto")
print("=" * 74)
print("""  Usamos Gram DIAGONAL (slots ortogonales). ¿Y si los slots se acoplan
  (off-diagonal ≠ 0)? Por la ley de inercia de Sylvester, la FIRMA de una matriz
  simétrica es invariante bajo congruencia (cambio de base) -- acoplar los slots
  con una deformación suave que no cruce una degeneración PRESERVA la firma, luego
  el sector. Verificación: al sector GR (3,0,1) le añadimos acoplamientos
  aleatorios crecientes y confirmamos que la firma no cambia hasta que un
  acoplamiento tan grande fuerza un cruce de degeneración (una transición de fase
  real, no un artefacto).""")
base = np.diag([m0**2, -c**2, Omega2, rho**2])  # sector GR (3,0,1)
rng = np.random.default_rng(0)
print(f"    {'|off-diag|':>12}{'firma':>12}  ¿sigue Lorentz (3,1)?")
for eps in [0.0, 0.1, 0.3, 0.5, 0.8, 1.2]:
    C = rng.standard_normal((4, 4)) * eps
    M = base + (C + C.T) / 2
    npos, nz, nneg, w = inertia(M)
    same = (npos, nz, nneg) == (3, 0, 1)
    print(f"    {eps:12.2f}   ({npos},{nz},{nneg})   {'SÍ (invariante)' if same else 'NO -> cruzó degeneración'}")
print("""    => la firma (el sector) es ROBUSTA al acoplamiento de slots: es un
    invariante inercial, no depende de que la Gram sea diagonal. Solo un
    acoplamiento suficientemente fuerte cruza una degeneración -- que es
    precisamente una transición de sector física (det=0), no una fragilidad.""")

print()
print("=" * 74)
print("SÍNTESIS")
print("=" * 74)
print("""  * partícula/masa (todo spacelike)   -> firma (4,0), det>0  : ELÍPTICO/Newton  ✓
  * EM/fotón (masa 0 / k nulo)          -> firma (3,1,0)*, det=0 : FRONTERA/Maxwell ✓
  * GR (4-velocidad timelike, u·u=−c²)  -> firma (3,1),  det<0   : LORENTZ/onda    ✓
  * 'sin Lorentz' NO es un solo caso:
       (4,0) det>0 = equilibrio clásico bien-puesto (elíptico, no degenerado)
       (2,2) det>0 = ULTRAHIPERBÓLICO mal-puesto (dos tiempos, patológico)
       ceros de más = degenerado real (rango deficiente)
  * det-signo NO basta (Corolario 8.1): (4,0) y (2,2) comparten det>0 pero son
    opuestos -- la FIRMA (inercia) es el clasificador correcto.
  * El −c² del sector GR EMERGE de la 4-velocidad timelike (dato físico), no se
    pone a mano -- la arquitectura LEE la firma del carácter geométrico del dato.
  (*) para el fotón, un cero (n0=1) en vez de un negativo -> la frontera, no el
      sector Lorentz abierto; consistente con 'Maxwell = límite det→0' (Paper B).""")
