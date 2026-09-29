"""
run_experiments.py
------------------
Ejecuta las tres tecnicas, cada una 5 veces (con semillas distintas para
observar variabilidad y convergencia), registra resultados y genera:
  - tabla comparativa (consola + CSV)
  - grafico de la mejor ruta de cada tecnica
  - grafico comparativo de convergencia

Se ejecuta desde la carpeta src/ :   python run_experiments.py
Las salidas se guardan en ../resultados/
"""

import time
import csv
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")  # backend sin ventana (para guardar archivos)
import matplotlib.pyplot as plt

# cada tecnica vive en su propia carpeta (una por grupo del reto); las
# agregamos al path para poder importarlas desde aqui sin volverlas paquetes.
_SRC = os.path.dirname(__file__)
for _carpeta in ("comun", "grupo1_recocido_simulado", "grupo2_algoritmo_genetico", "grupo3_hill_climbing"):
    sys.path.insert(0, os.path.join(_SRC, _carpeta))

from data import COORDS, longitud_ruta
from hill_climbing import hill_climbing
from recocido_simulado import recocido_simulado
from algoritmo_genetico import algoritmo_genetico

OUT = os.path.join(os.path.dirname(__file__), "..", "resultados")
os.makedirs(OUT, exist_ok=True)

CORRIDAS = 5  # el reto pide al menos 5 ejecuciones por tecnica

# Cada tecnica: (funcion, kwargs fijos). La semilla se cambia por corrida.
#
# NOTA sobre los parametros: se eligio deliberadamente un presupuesto
# computacional MODESTO en cada tecnica. Con 15 ciudades y parametros muy
# generosos, las tres tecnicas encuentran SIEMPRE el mismo optimo global
# (~32.22) con varianza cero, lo que impediria observar la "variabilidad y
# convergencia" que pide el reto y volveria trivial la comparacion. Con un
# presupuesto acotado emerge la naturaleza estocastica de cada metodo y la
# comparacion de eficiencia (calidad vs. tiempo) se vuelve significativa.
TECNICAS = [
    ("Recocido Simulado", recocido_simulado,
     {"T_inicial": 10.0, "enfriamiento": 0.95, "iter_por_T": 20}),
    ("Algoritmo Genetico", algoritmo_genetico,
     {"tam_poblacion": 40, "generaciones": 100, "p_mutacion": 0.2}),
    # Hill-Climbing PLANO (1 reinicio) para exponer su debilidad clasica:
    # el atrapamiento en optimos locales. El random restart se propone despues
    # como MEJORA (paso 5 del reto), coherente con lo visto en el curso.
    ("Hill-Climbing",      hill_climbing,
     {"reinicios": 1}),
]


def correr_todo():
    resumen = []            # filas para la tabla comparativa
    mejores_rutas = {}      # nombre -> (ruta, dist) de la mejor corrida
    mejores_historiales = {}  # nombre -> historial de la mejor corrida

    for nombre, func, kwargs in TECNICAS:
        distancias = []
        tiempos = []
        iters = []
        mejor_dist_tec = np.inf
        mejor_ruta_tec = None
        mejor_hist_tec = None

        for c in range(CORRIDAS):
            t0 = time.perf_counter()
            res = func(semilla=c, **kwargs)
            t1 = time.perf_counter()

            distancias.append(res["mejor_dist"])
            tiempos.append(t1 - t0)
            iters.append(res["iteraciones"])

            if res["mejor_dist"] < mejor_dist_tec:
                mejor_dist_tec = res["mejor_dist"]
                mejor_ruta_tec = res["mejor_ruta"]
                mejor_hist_tec = res["historial"]

        distancias = np.array(distancias)
        tiempos = np.array(tiempos)

        resumen.append({
            "tecnica": nombre,
            "mejor_dist": distancias.min(),
            "dist_promedio": distancias.mean(),
            "dist_peor": distancias.max(),
            "desv_std": distancias.std(),
            "tiempo_prom_s": tiempos.mean(),
            "iter_prom": int(np.mean(iters)),
        })
        mejores_rutas[nombre] = (mejor_ruta_tec, mejor_dist_tec)
        mejores_historiales[nombre] = mejor_hist_tec

        print(f"[{nombre}] mejor={distancias.min():.3f}  "
              f"prom={distancias.mean():.3f}  peor={distancias.max():.3f}  "
              f"std={distancias.std():.3f}  t_prom={tiempos.mean():.3f}s")

    return resumen, mejores_rutas, mejores_historiales


def tabla_csv(resumen):
    ruta_csv = os.path.join(OUT, "tabla_comparativa.csv")
    campos = ["tecnica", "mejor_dist", "dist_promedio", "dist_peor",
              "desv_std", "tiempo_prom_s", "iter_prom"]
    with open(ruta_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for fila in resumen:
            w.writerow({k: (round(v, 4) if isinstance(v, float) else v)
                        for k, v in fila.items()})
    print(f"CSV guardado en {ruta_csv}")


def graficar_ruta(nombre, ruta, dist, archivo):
    plt.figure(figsize=(6, 6))
    # dibujar segmentos de la ruta cerrada
    orden = np.append(ruta, ruta[0])
    xs = COORDS[orden, 0]
    ys = COORDS[orden, 1]
    plt.plot(xs, ys, "-", color="#2a8f82", linewidth=1.6, zorder=1)
    plt.scatter(COORDS[:, 0], COORDS[:, 1], color="#12213b", zorder=2)
    for i, (x, y) in enumerate(COORDS):
        plt.annotate(str(i + 1), (x, y), textcoords="offset points",
                     xytext=(5, 5), fontsize=9, color="#d9603b")
    plt.title(f"{nombre}\nMejor ruta  ·  distancia = {dist:.2f}")
    plt.xlabel("X"); plt.ylabel("Y")
    plt.grid(True, linestyle=":", alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT, archivo), dpi=130)
    plt.close()


def graficar_convergencia(historiales):
    plt.figure(figsize=(8, 5))
    colores = {"Recocido Simulado": "#d9603b",
               "Algoritmo Genetico": "#12213b",
               "Hill-Climbing": "#2a8f82"}
    for nombre, hist in historiales.items():
        # eje x normalizado 0..1 (las tecnicas tienen distinto # de pasos)
        x = np.linspace(0, 1, len(hist))
        plt.plot(x, hist, label=nombre, color=colores.get(nombre), linewidth=1.8)
    plt.title("Convergencia: mejor distancia vs. progreso de la busqueda")
    plt.xlabel("Progreso de la busqueda (normalizado 0-1)")
    plt.ylabel("Mejor distancia encontrada")
    plt.legend()
    plt.grid(True, linestyle=":", alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT, "convergencia_comparativa.png"), dpi=130)
    plt.close()


if __name__ == "__main__":
    resumen, rutas, historiales = correr_todo()
    tabla_csv(resumen)

    archivos = {
        "Recocido Simulado": "ruta_recocido.png",
        "Algoritmo Genetico": "ruta_genetico.png",
        "Hill-Climbing": "ruta_hillclimbing.png",
    }
    for nombre, (ruta, dist) in rutas.items():
        graficar_ruta(nombre, ruta, dist, archivos[nombre])

    graficar_convergencia(historiales)
    print("\nGraficos y tabla generados en la carpeta resultados/")

    # imprimir mejor ruta en terminos de Puntos (1..15) para el reporte
    print("\n--- Mejores rutas (en Puntos 1..15) ---")
    for nombre, (ruta, dist) in rutas.items():
        secuencia = " -> ".join(str(c + 1) for c in ruta)
        print(f"{nombre} ({dist:.2f}): {secuencia} -> {ruta[0] + 1}")
