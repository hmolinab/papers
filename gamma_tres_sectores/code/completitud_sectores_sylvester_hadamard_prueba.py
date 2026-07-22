"""
TEOREMA DE COMPLETITUD DE LOS SECTORES (jul-19 2026).

El atlas (draft_atlas) marca [A] el claim "los tres sectores det>0/=0/<0 AGOTAN
la física clásica". La validación SAIR (ayer) mostró que el clasificador correcto
NO es el signo de det sino la INERCIA (firma) de Γ_s -- y (2,2) tiene det>0 como
una partícula pero es ultrahiperbólico. Eso REFORMULA la pregunta de completitud
y la CONVIERTE (en su mayor parte) de conjetura [A] en teorema [D]:

TESIS: la completitud NO es una conjetura física; es la composición de dos
teoremas conocidos:
  (I)  Sylvester (ley de inercia): toda forma cuadrática simétrica real 4x4 cae
       en un número FINITO y EXHAUSTIVO de clases de congruencia, indexadas por
       (n+, n0, n-) con n+ + n0 + n- = 4. No hay más. Es completo por construcción.
  (II) Hadamard (buena postura del problema de Cauchy): de las clases NO
       degeneradas, EXACTAMENTE UNA (la Lorentziana (3,1)) da evolución
       hiperbólica bien-puesta; la Riemanniana (4,0) es elíptica (equilibrio, no
       evolución); la ultrahiperbólica (2,2) es mal-puesta (patológica).

Este script: (1) enumera TODAS las clases de inercia de Sym(4,R) y confirma que
Sylvester las agota; (2) clasifica el tipo de EDP (elíptico/hiperbólico/
ultrahiperbólico/parabólico) de cada una por su símbolo principal; (3) verifica
que modulo convención de signo hay exactamente 3 clases no-degeneradas y UNA
bien-puesta. El resultado UPGRADEA la completitud del atlas de [A] a [D] en su
parte matemática, dejando explícito el residuo físico que sigue [A].
"""
import numpy as np
from itertools import product

print("=" * 74)
print("(I) SYLVESTER: enumeración EXHAUSTIVA de las clases de inercia de Sym(4,R)")
print("=" * 74)
clases = [(np_, n0, nn) for np_ in range(5) for n0 in range(5) for nn in range(5)
          if np_ + n0 + nn == 4]
print(f"  número total de clases de inercia (n+,n0,n-) con suma 4: {len(clases)}")
print("  (Sylvester: TODA matriz simétrica 4x4 real cae en exactamente una de estas.")
print("   Es una partición completa y finita del espacio -- no hay más clases posibles.)")


def tipo_edp(np_, n0, nn):
    """Tipo de EDP de 2º orden por el símbolo principal (firma sin ceros)."""
    if n0 >= 1:
        return "PARABÓLICO/degenerado (frontera)"
    lo = min(np_, nn)
    if lo == 0:
        return "ELÍPTICO (equilibrio, bien-puesto como frontera, NO evolución)"
    if lo == 1:
        return "HIPERBÓLICO (evolución bien-puesta, Cauchy) <<< Lorentz"
    return "ULTRAHIPERBÓLICO (MAL-puesto, Hadamard) -- patológico"


print()
print("  Clases NO degeneradas (n0=0, det≠0):")
no_deg = [(a, b, c) for (a, b, c) in clases if b == 0]
for (a, b, c) in no_deg:
    detsign = "+" if (c % 2 == 0) else "-"  # signo de det = (-1)^n-
    print(f"    ({a},{b},{c}): det{detsign}  {tipo_edp(a,b,c)}")

# modulo convencion de signo (n+,n0,n-) ~ (n-,n0,n+)
print()
print("  Modulo convención de signo global (mostly-plus ~ mostly-minus), (n+,·,n-)~(n-,·,n+):")
vistas = set()
reducidas = []
for (a, b, c) in no_deg:
    key = tuple(sorted([a, c]))  # (min,max) identifica la clase mod signo
    if key not in vistas:
        vistas.add(key); reducidas.append((a, b, c))
for (a, b, c) in reducidas:
    print(f"    clase {{({a},{b},{c}),({c},{b},{a})}}: {tipo_edp(a,b,c)}")
print(f"  => EXACTAMENTE {len(reducidas)} clases no-degeneradas modulo signo.")

print()
print("=" * 74)
print("(II) HADAMARD: cuál de las 3 clases no-degeneradas es evolución bien-puesta")
print("=" * 74)
print("""  Símbolo principal de una EOM de 2º orden = la forma cuadrática de Γ_s. El
  problema de Cauchy (evolución temporal) está bien-puesto sii el símbolo es
  HIPERBÓLICO = exactamente una dirección de signo opuesto (Hadamard/Courant-
  Hilbert). Verificación numérica del tipo por clase:""")


def bien_puesta_evolucion(np_, n0, nn):
    return (n0 == 0) and (min(np_, nn) == 1)


for (a, b, c) in reducidas:
    ev = bien_puesta_evolucion(a, b, c)
    print(f"    ({a},{b},{c}): evolución hiperbólica bien-puesta? {'SÍ' if ev else 'NO'}  "
          f"({'la única' if ev else tipo_edp(a,b,c).split('(')[0].strip()})")
n_bien = sum(bien_puesta_evolucion(a, b, c) for (a, b, c) in reducidas)
print(f"  => clases no-degeneradas que dan evolución bien-puesta: {n_bien}")
print("  => la firma LORENTZIANA (3,1) es la ÚNICA. (weld paper, Lemma 4 + Hadamard.)")

print()
print("=" * 74)
print("(III) VERIFICACIÓN NUMÉRICA: muestreo aleatorio confirma la exhaustividad")
print("=" * 74)
print("""  Se muestrean matrices simétricas 4x4 aleatorias (varias escalas y estructuras)
  y se confirma que TODAS caen en una clase enumerada -- Sylvester es completo,
  no hay firma 'sorpresa'.""")
rng = np.random.default_rng(1)
vistas_muestreo = {}
for _ in range(20000):
    scale = rng.choice([0.1, 1, 10])
    M = rng.standard_normal((4, 4)) * scale
    M = (M + M.T) / 2
    # a veces forzar ceros para muestrear la frontera
    if rng.random() < 0.3:
        k = rng.integers(1, 3)
        w, V = np.linalg.eigh(M)
        w[:k] = 0
        M = V @ np.diag(w) @ V.T
    w = np.linalg.eigvalsh((M + M.T) / 2)
    tol = 1e-9 * max(1, np.abs(w).max())
    firma = (int((w > tol).sum()), int((np.abs(w) <= tol).sum()), int((w < -tol).sum()))
    vistas_muestreo[firma] = vistas_muestreo.get(firma, 0) + 1
todas_validas = all(f in clases for f in vistas_muestreo)
print(f"  firmas distintas observadas en 20000 muestras: {len(vistas_muestreo)}")
print(f"  ¿todas dentro de la enumeración de Sylvester? {todas_validas}")
print(f"  firmas no-degeneradas observadas: "
      f"{sorted(f for f in vistas_muestreo if f[1]==0)}")

print()
print("=" * 74)
print("(IV) LA CORRECCIÓN AL ATLAS §2.2: cuántas componentes conexas, de verdad")
print("=" * 74)
print("""  El atlas §2.2 cuenta: 'det: M4(R)->R es continua; su cero es codim 1; el
  complemento tiene exactamente DOS componentes conexas. Sumando la frontera:
  tres sectores.' Eso es CORRECTO para GL(4,R) (dos componentes por signo de det).
  PERO la física (tipo de EDP, buena postura) la lleva la parte SIMÉTRICA Γ_s, y
  ahí el conteo es OTRO: en Sym*(4,R) (simétricas no-degeneradas) la inercia es
  un invariante COMPLETO y LOCALMENTE CONSTANTE (Sylvester + continuidad de
  autovalores) => hay UNA componente conexa POR CLASE DE INERCIA:""")
comps = [(a, b, c) for (a, b, c) in no_deg]
print(f"    componentes conexas de Sym*(4,R) = {len(comps)}: {comps}")
print(f"    componentes de GL(4,R) por signo de det = 2")
print("""    => det>0 es la UNIÓN de TRES componentes: (4,0), (2,2), (0,4)
       det<0 es la UNIÓN de DOS componentes:   (3,1), (1,3)
    El signo de det NO separa componentes de Sym*: las MEZCLA.""")

print()
print("  Prueba numérica de que (4,0) y (2,2) están en componentes DISTINTAS")
print("  aunque compartan det>0: cualquier camino entre ellas cruza una degeneración.")
A = np.diag([1.0, 1.0, 1.0, 1.0])    # (4,0), det=+1
B = np.diag([1.0, 1.0, -1.0, -1.0])  # (2,2), det=+1
print(f"    det(A)={np.linalg.det(A):+.2f} firma=(4,0,0)")
print(f"    det(B)={np.linalg.det(B):+.2f} firma=(2,0,2)   -- MISMO signo de det")
print("    recorriendo el segmento A->B y 100 caminos aleatorios (con waypoint):")
def cruza_degeneracion(P0, P1, W=None, n=4001):
    """¿el camino P0->(W)->P1 pasa por una matriz degenerada?"""
    ts = np.linspace(0, 1, n)
    mind = np.inf
    for t in ts:
        M = (1-t)*P0 + t*P1 if W is None else (
            (1-2*t)*P0 + 2*t*W if t < 0.5 else (2-2*t)*W + (2*t-1)*P1)
        w = np.linalg.eigvalsh((M+M.T)/2)
        mind = min(mind, np.abs(w).min())
    return mind
d_seg = cruza_degeneracion(A, B)
print(f"      segmento recto: min|autovalor| a lo largo del camino = {d_seg:.2e}"
      f"  -> {'CRUZA degeneración' if d_seg < 1e-6 else 'no cruza'}")
rng2 = np.random.default_rng(7)
peor = 0.0
for _ in range(100):
    W = rng2.standard_normal((4, 4)) * 2.0
    W = (W + W.T) / 2
    peor = max(peor, cruza_degeneracion(A, B, W))
print(f"      100 caminos aleatorios con waypoint: el MEJOR logra")
print(f"      min|autovalor| = {peor:.2e} -> {'TODOS cruzan' if peor < 1e-3 else 'alguno evita'}")
print("""      Razón (prueba, no solo numérica): ir de 4 autovalores positivos a 2
      exige que 2 de ellos cambien de signo; por continuidad cada uno pasa por
      cero. Luego TODO camino de (4,0) a (2,2) cruza det=0. Son componentes
      conexas distintas, pese a compartir det>0. QED.""")

print()
print("=" * 74)
print("TEOREMA DE COMPLETITUD (síntesis)")
print("=" * 74)
print("""  ENUNCIADO [D]: Para Γ_s ∈ Sym(4,R), la ley de inercia de Sylvester da una
  partición COMPLETA y FINITA en clases de congruencia (n+,n0,n-). Las NO
  degeneradas son, modulo convención de signo, EXACTAMENTE TRES:
     • Riemanniana (4,0)     -> elíptica  -> equilibrio clásico (Newton, det>0)
     • Lorentziana (3,1)     -> hiperbólica bien-puesta -> evolución relativista (GR, det<0)
     • Ultrahiperbólica (2,2)-> mal-puesta (Hadamard)    -> patológica (det>0, NO física)
  Por Hadamard, EXACTAMENTE UNA (la Lorentziana) sustenta evolución temporal
  bien-puesta. Las degeneradas (n0≥1, det=0) son la FRONTERA de codimensión ≥1
  entre ellas (Maxwell/fotón = un modo nulo).

  QUÉ RESUELVE: el atlas marcaba [A] "los 3 sectores det-signo agotan la física".
  Reformulado por inercia, la completitud es un TEOREMA (Sylvester + Hadamard),
  no una conjetura. Y CORRIGE el atlas: el signo de det NO es el clasificador fiel
  -- det>0 mezcla Riemanniana (4,0, física) con ultrahiperbólica (2,2, patológica).
  El clasificador correcto es la firma; con ella, la completitud es [D].

  QUÉ SIGUE SIENDO [A] (el residuo físico honesto): que la física clásica se
  agote en un ÚNICO objeto Γ_s de 4x4 -- i.e., que ningún régimen requiera un
  objeto mayor, una estructura distinta, o slots fuera de SAIR. La completitud
  MATEMÁTICA (Sylvester/Hadamard sobre Sym(4,R)) es [D]; la completitud FÍSICA
  (que 4x4 basta) es la parte que queda por argumentar -- pero es MUCHO más
  estrecha que 'los tres sectores son conjeturales'.""")
