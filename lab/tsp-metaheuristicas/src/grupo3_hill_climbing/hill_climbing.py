# GRUPO 3 del reto.

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "comun"))
from data import N, longitud_ruta, D


def _mejor_vecino_2opt(ruta, D=D):
    """Explora toda la vecindad 2-opt y devuelve el mejor movimiento de mejora.

    Devuelve (i, j, delta), o None si ningun movimiento reduce la distancia
    (optimo local). El delta se calcula de forma incremental, sobre las 4
    aristas afectadas, en vez de recalcular la ruta completa en cada paso.
    """
    n = len(ruta)
    mejor_delta = 0.0
    mejor_mov = None
    for i in range(n - 1):
        for j in range(i + 1, n):
            a, b = ruta[i], ruta[(i + 1) % n]      # arista (a, b)
            c, d = ruta[j], ruta[(j + 1) % n]      # arista (c, d)
            if a == c or b == d:
                continue
            delta = (D[a, c] + D[b, d]) - (D[a, b] + D[c, d])
            if delta < mejor_delta - 1e-12:
                mejor_delta = delta
                mejor_mov = (i, j)
    if mejor_mov is None:
        return None
    return mejor_mov[0], mejor_mov[1], mejor_delta


def hill_climbing(reinicios=30, semilla=None):
    """Hill-Climbing 2-opt con reinicios aleatorios.

    reinicios: cuantas veces reiniciamos desde una solucion aleatoria.
    semilla: para reproducibilidad.
    Devuelve dict con mejor_ruta, mejor_dist, iteraciones (movimientos
    aplicados en total) e historial (mejor distancia tras cada reinicio,
    para graficar convergencia).
    """
    rng = np.random.default_rng(semilla)
    mejor_ruta_global = None
    mejor_dist_global = np.inf
    iteraciones = 0
    historial = []

    for _ in range(reinicios):
        ruta = rng.permutation(N)
        dist = longitud_ruta(ruta)
        # registrar la distancia inicial de este reinicio
        historial.append(min(mejor_dist_global, dist))
        # subir la colina hasta el optimo local
        while True:
            mov = _mejor_vecino_2opt(ruta)
            if mov is None:
                break  # optimo local alcanzado
            i, j, delta = mov
            ruta[i + 1:j + 1] = ruta[i + 1:j + 1][::-1]
            dist += delta
            iteraciones += 1
            historial.append(min(mejor_dist_global, dist))

        if dist < mejor_dist_global:
            mejor_dist_global = dist
            mejor_ruta_global = ruta.copy()

    return {
        "nombre": "Hill-Climbing (2-opt + reinicios)",
        "mejor_ruta": mejor_ruta_global,
        "mejor_dist": mejor_dist_global,
        "iteraciones": iteraciones,
        "historial": historial,
    }


if __name__ == "__main__":
    r = hill_climbing(reinicios=30, semilla=1)
    print(f"{r['nombre']}: dist={r['mejor_dist']:.3f}, iter={r['iteraciones']}")
