=======================================================================
OPTIMIZACIÓN DE RUTAS DE ENTREGA (TSP, 15 UBICACIONES)
Reto de metaheurísticas · Diplomado de IA aplicada
=======================================================================

CONTENIDO DEL PAQUETE
---------------------
src/
  comun/
    data.py                           Coordenadas, matriz de distancias, longitud de ruta.
  grupo1_recocido_simulado/
    recocido_simulado.py              Grupo 1: Recocido Simulado (Simulated Annealing).
  grupo2_algoritmo_genetico/
    algoritmo_genetico.py             Grupo 2: Algoritmo Genético (OX + inversión + elitismo).
  grupo3_hill_climbing/
    hill_climbing.py                  Grupo 3: Hill-Climbing con vecindad 2-opt.
  run_experiments.py                  Ejecuta las 3 técnicas x5 corridas; tabla y gráficos.

resultados/
  tabla_comparativa.csv          Resultados numéricos de las 5 corridas.
  ruta_recocido.png              Mejor ruta — Recocido Simulado.
  ruta_genetico.png              Mejor ruta — Algoritmo Genético.
  ruta_hillclimbing.png          Mejor ruta — Hill-Climbing.
  convergencia_comparativa.png   Convergencia de las 3 técnicas.

generar_reporte.py        Construye el PDF de análisis a partir de resultados/.
Reporte_Analisis_Comparativo.pdf   Documento de análisis comparativo (entregable).


CÓMO EJECUTAR
-------------
Requisitos: Python 3.9+, numpy, matplotlib, reportlab.
    pip install numpy matplotlib reportlab

1) Correr los experimentos (genera tabla y gráficos en resultados/):
       cd src
       python run_experiments.py

2) Generar el PDF de análisis (desde la carpeta tsp/):
       python generar_reporte.py


NOTAS IMPORTANTES
-----------------
1. Grupo 3 = Hill-Climbing, NO gradiente. El descenso por gradiente no aplica
   a un TSP: no hay función continua/diferenciable sobre permutaciones. Ver la
   justificación en el PDF, sección 1.

2. El enunciado menciona "vehículos de capacidad limitada" (que describiría un
   CVRP), pero los pasos definen un TSP de ruta única. Aquí se implementó TSP.
   Confirmar el alcance con el instructor.

3. Los resultados son estocásticos: los números pueden variar ligeramente entre
   corridas. Las conclusiones cualitativas se mantienen. Distancia óptima de la
   instancia ≈ 32.22.
=======================================================================
