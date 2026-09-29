"""
algoritmo_genetico.py
---------------------
GRUPO 2 del reto (metodo poblacional).

El Algoritmo Genetico (AG) es un metodo POBLACIONAL: en lugar de una sola
solucion, mantiene una POBLACION de rutas candidatas y las hace "evolucionar"
generacion tras generacion, imitando la evolucion natural. Cada ruta es un
"individuo"; su calidad se mide con una funcion de aptitud (fitness).

Operadores (los tres pilares vistos en el curso):
  - SELECCION: elegimos padres favoreciendo a los mejores. Usamos seleccion
    por torneo (tomamos k individuos al azar y gana el de menor distancia).
  - CRUZAMIENTO: combinamos dos padres para crear hijos. Para permutaciones
    usamos Order Crossover (OX), que preserva un segmento de un padre y rellena
    el resto respetando el orden del otro, garantizando rutas validas (sin
    ciudades repetidas ni faltantes).
  - MUTACION: introducimos variacion aleatoria. Usamos mutacion por inversion
    (invertir un segmento), equivalente a un movimiento 2-opt aleatorio.

Ademas usamos ELITISMO: el mejor individuo pasa intacto a la siguiente
generacion, para no perder nunca la mejor solucion encontrada.

PSEUDOCODIGO (flujo general):
    poblacion <- rutas aleatorias
    repetir por G generaciones:
        evaluar aptitud de cada individuo
        conservar al mejor (elitismo)
        mientras no se llene la nueva poblacion:
            padre1, padre2 <- seleccion por torneo
            hijo <- cruzamiento OX(padre1, padre2)
            con probabilidad p_mut: mutar(hijo)
            agregar hijo a la nueva poblacion
        poblacion <- nueva poblacion
    devolver el mejor individuo
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "comun"))
from data import N, longitud_ruta


def _torneo(poblacion, distancias, k, rng):
    """Seleccion por torneo: gana el de menor distancia entre k al azar."""
    idx = rng.integers(0, len(poblacion), size=k)
    ganador = idx[np.argmin(distancias[idx])]
    return poblacion[ganador]


def _ox(padre1, padre2, rng):
    """
    Order Crossover (OX).
    1. Copia un segmento aleatorio de padre1 al hijo.
    2. Rellena las posiciones restantes con las ciudades de padre2 en su orden,
       saltando las que ya estan en el hijo.
    Garantiza una permutacion valida.
    """
    n = len(padre1)
    a, b = sorted(rng.integers(0, n, size=2))
    hijo = [-1] * n
    hijo[a:b + 1] = list(padre1[a:b + 1])
    en_hijo = set(hijo[a:b + 1])
    pos = (b + 1) % n
    for ciudad in np.concatenate([padre2[b + 1:], padre2[:b + 1]]):
        if ciudad not in en_hijo:
            hijo[pos] = ciudad
            en_hijo.add(ciudad)
            pos = (pos + 1) % n
    return np.array(hijo)


def _mutacion_inversion(ruta, rng):
    """Mutacion: invierte un segmento aleatorio (2-opt aleatorio)."""
    a, b = sorted(rng.integers(0, len(ruta), size=2))
    ruta[a:b + 1] = ruta[a:b + 1][::-1]
    return ruta


def algoritmo_genetico(tam_poblacion=100, generaciones=300, p_mutacion=0.2,
                       k_torneo=3, semilla=None):
    """
    Algoritmo Genetico para TSP.

    tam_poblacion: numero de individuos por generacion.
    generaciones: numero de iteraciones evolutivas.
    p_mutacion: probabilidad de mutar cada hijo.
    k_torneo: tamano del torneo de seleccion.

    Devuelve dict con mejor_ruta, mejor_dist, iteraciones (= generaciones)
    e historial (mejor distancia por generacion, para convergencia).
    """
    rng = np.random.default_rng(semilla)
    # poblacion inicial: permutaciones aleatorias
    poblacion = [rng.permutation(N) for _ in range(tam_poblacion)]

    mejor_ruta = None
    mejor_dist = np.inf
    historial = []

    for _ in range(generaciones):
        distancias = np.array([longitud_ruta(ind) for ind in poblacion])
        # actualizar mejor global
        i_mejor = int(np.argmin(distancias))
        if distancias[i_mejor] < mejor_dist:
            mejor_dist = distancias[i_mejor]
            mejor_ruta = poblacion[i_mejor].copy()
        historial.append(mejor_dist)

        # ELITISMO: el mejor pasa intacto
        nueva = [poblacion[i_mejor].copy()]
        while len(nueva) < tam_poblacion:
            p1 = _torneo(poblacion, distancias, k_torneo, rng)
            p2 = _torneo(poblacion, distancias, k_torneo, rng)
            hijo = _ox(p1, p2, rng)
            if rng.random() < p_mutacion:
                hijo = _mutacion_inversion(hijo, rng)
            nueva.append(hijo)
        poblacion = nueva

    return {
        "nombre": "Algoritmo Genetico",
        "mejor_ruta": mejor_ruta,
        "mejor_dist": mejor_dist,
        "iteraciones": generaciones,
        "historial": historial,
    }


if __name__ == "__main__":
    r = algoritmo_genetico(semilla=1)
    print(f"{r['nombre']}: dist={r['mejor_dist']:.3f}, gen={r['iteraciones']}")
