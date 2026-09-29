"""
recocido_simulado.py
--------------------
GRUPO 1 del reto (metodo de estado unico).

El Recocido Simulado (Simulated Annealing) es un metodo de ESTADO UNICO
inspirado en el proceso fisico de recocido de materiales: se calienta el metal
y se enfria lentamente para que los atomos se acomoden en una estructura de
baja energia. Aqui, la "energia" es la distancia de la ruta.

La idea clave que lo distingue de Hill-Climbing: acepta movimientos que
EMPEORAN la solucion con cierta probabilidad. Esa probabilidad depende de la
"temperatura" T. Al inicio T es alta (aceptamos casi cualquier cosa, exploramos
mucho); conforme T baja, nos volvemos exigentes (solo aceptamos mejoras). Esto
le permite ESCAPAR de optimos locales, algo que Hill-Climbing no puede hacer.

Criterio de aceptacion (Metropolis):
    si delta < 0            -> aceptar siempre (es una mejora)
    si delta >= 0           -> aceptar con probabilidad exp(-delta / T)

PSEUDOCODIGO (flujo general):
    ruta <- permutacion aleatoria
    T <- T_inicial
    repetir hasta enfriar:
        vecino <- movimiento 2-opt aleatorio sobre la ruta
        delta  <- dist(vecino) - dist(ruta)
        si delta < 0 o random() < exp(-delta / T):
            ruta <- vecino
        T <- T * factor_enfriamiento
    devolver la mejor ruta vista
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "comun"))
from data import N, longitud_ruta, D


def _delta_2opt(ruta, i, j, D=D):
    """Cambio de distancia al invertir el segmento i+1..j (calculo incremental)."""
    n = len(ruta)
    a, b = ruta[i], ruta[(i + 1) % n]
    c, d = ruta[j], ruta[(j + 1) % n]
    return (D[a, c] + D[b, d]) - (D[a, b] + D[c, d])


def recocido_simulado(T_inicial=100.0, T_final=1e-3, enfriamiento=0.9970,
                      iter_por_T=30, semilla=None):
    """
    Recocido Simulado con vecindad 2-opt y enfriamiento geometrico.

    T_inicial / T_final: temperaturas de arranque y paro.
    enfriamiento: factor multiplicativo por paso (T <- T * factor). < 1.
    iter_por_T: movimientos evaluados antes de bajar la temperatura.
    semilla: reproducibilidad.

    Devuelve dict con mejor_ruta, mejor_dist, iteraciones e historial (mejor
    distancia acumulada, para graficar convergencia).
    """
    rng = np.random.default_rng(semilla)
    ruta = rng.permutation(N)
    dist_actual = longitud_ruta(ruta)

    mejor_ruta = ruta.copy()
    mejor_dist = dist_actual

    T = T_inicial
    iteraciones = 0
    historial = []

    while T > T_final:
        for _ in range(iter_por_T):
            iteraciones += 1
            # elegir dos cortes i < j al azar para un movimiento 2-opt
            i, j = sorted(rng.integers(0, N, size=2))
            if i == j:
                continue
            delta = _delta_2opt(ruta, i, j)
            # criterio de Metropolis
            if delta < 0 or rng.random() < np.exp(-delta / T):
                ruta[i + 1:j + 1] = ruta[i + 1:j + 1][::-1]
                dist_actual += delta
                if dist_actual < mejor_dist:
                    mejor_dist = dist_actual
                    mejor_ruta = ruta.copy()
        historial.append(mejor_dist)
        T *= enfriamiento

    return {
        "nombre": "Recocido Simulado",
        "mejor_ruta": mejor_ruta,
        "mejor_dist": mejor_dist,
        "iteraciones": iteraciones,
        "historial": historial,
    }


if __name__ == "__main__":
    r = recocido_simulado(semilla=1)
    print(f"{r['nombre']}: dist={r['mejor_dist']:.3f}, iter={r['iteraciones']}")
