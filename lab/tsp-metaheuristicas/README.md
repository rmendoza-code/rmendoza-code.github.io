# Optimización de rutas de entrega (TSP, 15 ubicaciones)

Proyecto del módulo **Fundamentos de Metaheurísticas** — Diplomado en Tecnologías de IA, Tec de Monterrey. Python puro (numpy, matplotlib, reportlab).

| Técnica | Mejor | Promedio (5 corridas) | Desv. | Tiempo prom. |
|---|---|---|---|---|
| Recocido Simulado | 32.22 | 33.04 | 0.78 | 0.134 s |
| Algoritmo Genético (OX + inversión + elitismo) | 32.22 | **32.35** | **0.26** | 0.616 s |
| Hill-Climbing (2-opt) | 32.22 | 32.96 | 0.93 | **0.004 s** |

Las tres alcanzan el óptimo de la instancia (≈ 32.22); el genético es el más consistente y hill-climbing el más rápido. El reporte completo está en `Reporte_Analisis_Comparativo.pdf`; detalles de ejecución en `README.txt`.

**Criterio técnico:** el enunciado ofrecía "Hill-Climbing o Gradiente"; el gradiente no aplica a permutaciones (no hay función continua diferenciable), así que se justificó Hill-Climbing.
