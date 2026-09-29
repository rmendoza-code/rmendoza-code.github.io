"""Datos base del problema: coordenadas, matriz de distancias y evaluacion de rutas.

Todas las tecnicas (Recocido Simulado, Algoritmo Genetico, Hill-Climbing)
importan de aqui, asi que cualquier ganancia de eficiencia en este modulo
se propaga a las tres.
"""

import numpy as np

# Coordenadas (x, y) de las 15 ubicaciones de entrega.
COORDS = np.array([
    (5, 5),   # Punto 1
    (6, 8),   # Punto 2
    (3, 2),   # Punto 3
    (9, 7),   # Punto 4
    (1, 3),   # Punto 5
    (4, 6),   # Punto 6
    (7, 4),   # Punto 7
    (2, 9),   # Punto 8
    (8, 3),   # Punto 9
    (5, 1),   # Punto 10
    (6, 2),   # Punto 11
    (3, 7),   # Punto 12
    (7, 8),   # Punto 13
    (2, 5),   # Punto 14
    (4, 3),   # Punto 15
], dtype=float)

N = len(COORDS)


def matriz_distancias(coords=COORDS):
    """Matriz NxN de distancias euclidianas entre cada par de ubicaciones."""
    dif = coords[:, None, :] - coords[None, :, :]
    return np.sqrt((dif ** 2).sum(axis=2))


# Se precalcula una sola vez: evita repetir raices cuadradas en cada evaluacion.
D = matriz_distancias()


def longitud_ruta(ruta, D=D):
    """Distancia total de una ruta CERRADA (vuelve al punto de partida).

    Vectorizado con indexado avanzado de numpy en vez de un for-loop en
    Python puro: esta funcion es el hot path del Algoritmo Genetico (se
    evalua una vez por individuo en cada generacion), asi que su costo
    domina el tiempo de ejecucion del experimento completo.
    """
    siguiente = np.roll(ruta, -1)
    return D[ruta, siguiente].sum()
