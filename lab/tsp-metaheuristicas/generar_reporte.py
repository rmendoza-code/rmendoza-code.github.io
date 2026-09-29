import os
import csv
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Image,
                                Table, TableStyle, PageBreak)
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

BASE = os.path.dirname(__file__)
RES = os.path.join(BASE, "resultados")
OUT_PDF = os.path.join(BASE, "Reporte_Analisis_Comparativo.pdf")

# Datos de portada que pide el metodo de entrega (nombre completo y curso).
NOMBRE_COMPLETO = "Rodrigo Mendoza Cortes"
NOMBRE_CURSO = "Artificial Intelligence Technologies Specialist"

NAVY = colors.HexColor("#12213b")
TEAL = colors.HexColor("#2a8f82")
CORAL = colors.HexColor("#d9603b")
PAPER = colors.HexColor("#f6f1e6")

# ---------------------------------------------------------------------------
# estilos
# ---------------------------------------------------------------------------
styles = getSampleStyleSheet()
styles.add(ParagraphStyle("Titulo", parent=styles["Title"], textColor=NAVY,
                          fontSize=20, spaceAfter=6))
styles.add(ParagraphStyle("Sub", parent=styles["Normal"], textColor=TEAL,
                          fontSize=11, spaceAfter=14, alignment=TA_CENTER))
styles.add(ParagraphStyle("Autor", parent=styles["Normal"], textColor=NAVY,
                          fontSize=11, spaceAfter=4, alignment=TA_CENTER))
styles.add(ParagraphStyle("H2", parent=styles["Heading2"], textColor=NAVY,
                          fontSize=14, spaceBefore=14, spaceAfter=6))
styles.add(ParagraphStyle("H3", parent=styles["Heading3"], textColor=CORAL,
                          fontSize=11.5, spaceBefore=10, spaceAfter=4))
styles.add(ParagraphStyle("Body", parent=styles["Normal"], fontSize=10,
                          leading=15, alignment=TA_JUSTIFY, spaceAfter=6))
styles.add(ParagraphStyle("Pseudo", parent=styles["Code"], fontSize=8.5,
                          leading=11, textColor=colors.HexColor("#1f2534"),
                          backColor=colors.HexColor("#f0ece0"),
                          borderPadding=6, spaceAfter=8))
styles.add(ParagraphStyle("Cap", parent=styles["Normal"], fontSize=8.5,
                          textColor=colors.grey, alignment=TA_CENTER,
                          spaceBefore=2, spaceAfter=12))
styles.add(ParagraphStyle("Celda", parent=styles["Normal"], fontSize=8.5,
                          leading=11))


def P(txt, s="Body"):
    return Paragraph(txt, styles[s])


def leer_tabla():
    filas = []
    with open(os.path.join(RES, "tabla_comparativa.csv"), encoding="utf-8") as f:
        for row in csv.DictReader(f):
            filas.append(row)
    return filas


def bloque_tabla(filas):
    encab = ["Técnica", "Mejor", "Promedio", "Peor", "Desv. std",
             "Tiempo prom. (s)", "Iter/Gen prom."]
    data = [encab]
    for r in filas:
        data.append([
            r["tecnica"],
            f'{float(r["mejor_dist"]):.2f}',
            f'{float(r["dist_promedio"]):.2f}',
            f'{float(r["dist_peor"]):.2f}',
            f'{float(r["desv_std"]):.3f}',
            f'{float(r["tiempo_prom_s"]):.3f}',
            r["iter_prom"],
        ])
    t = Table(data, hAlign="LEFT", colWidths=[3.6*cm, 1.6*cm, 2*cm, 1.6*cm,
                                              2*cm, 2.6*cm, 2.4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#d8cdb2")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PAPER]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def build():
    filas = leer_tabla()
    # localizar valores para la narrativa (por si cambia el orden)
    by = {f["tecnica"]: f for f in filas}
    story = []

    # ---------- portada ----------
    story.append(P("Optimización de rutas de entrega (TSP, 15 ubicaciones)", "Titulo"))
    story.append(P("Análisis comparativo de metaheurísticas · Recocido Simulado · "
                   "Algoritmo Genético · Hill-Climbing", "Sub"))
    story.append(P(NOMBRE_COMPLETO, "Autor"))
    story.append(P(NOMBRE_CURSO, "Autor"))
    story.append(Spacer(1, 14))

    story.append(P("1. Análisis del problema", "H2"))
    story.append(P(
        "El reto es un <b>Problema del Agente Viajero (TSP)</b>: un repartidor debe "
        "visitar 15 ubicaciones de entrega exactamente una vez y regresar al origen, "
        "minimizando la distancia total. Es un problema <b>combinatorio</b>: el número de "
        "rutas posibles crece factorialmente (para 15 ciudades, (15-1)!/2 = 43 mil "
        "millones de rutas distintas). Evaluarlas todas por fuerza bruta es inviable, lo "
        "que justifica el uso de metaheurísticas: encuentran soluciones de calidad en "
        "tiempos razonables sin garantizar el óptimo absoluto."))
    story.append(P(
        "<b>Nota metodológica (dos precisiones del enunciado).</b> (1) El enunciado ofrece "
        "\"Hill-Climbing o Gradiente\" en el Grupo 3, pero el descenso por gradiente es "
        "<b>inaplicable</b> a un TSP: no existe una función continua y diferenciable sobre "
        "permutaciones de ciudades, así que no hay gradiente que calcular. Por eso el Grupo "
        "3 se resuelve con Hill-Climbing. (2) El enunciado menciona \"vehículos de capacidad "
        "limitada\", lo que describiría un CVRP (múltiples vehículos con restricción de "
        "carga); sin embargo, los 15 puntos y los pasos descritos corresponden a un TSP de "
        "ruta única, que es lo aquí implementado. Ambos puntos conviene confirmarlos con el "
        "instructor."))

    # tecnicas seleccionadas
    story.append(P("2. Técnicas implementadas", "H2"))
    story.append(P(
        "Se implementó una técnica de cada grupo, cubriendo las tres familias del curso:", ))
    grupos = [
        ["Grupo", "Técnica elegida", "Familia"],
        ["1", "Recocido Simulado", "Estado único (inspirado en física)"],
        ["2", "Algoritmo Genético", "Poblacional (evolutivo)"],
        ["3", "Hill-Climbing (2-opt)", "Estado único (búsqueda local)"],
    ]
    tg = Table(grupos, hAlign="LEFT", colWidths=[1.5*cm, 5*cm, 7*cm])
    tg.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TEAL),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#d8cdb2")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PAPER]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(tg)
    story.append(Spacer(1, 10))

    # pseudocodigos
    story.append(P("2.1 Recocido Simulado — flujo general", "H3"))
    story.append(P(
        "ruta &larr; permutación aleatoria; T &larr; T_inicial<br/>"
        "repetir hasta enfriar:<br/>"
        "&nbsp;&nbsp;vecino &larr; movimiento 2-opt aleatorio<br/>"
        "&nbsp;&nbsp;delta &larr; dist(vecino) − dist(ruta)<br/>"
        "&nbsp;&nbsp;si delta &lt; 0  o  random() &lt; exp(−delta / T):  aceptar vecino<br/>"
        "&nbsp;&nbsp;T &larr; T × factor_enfriamiento<br/>"
        "devolver la mejor ruta vista", "Pseudo"))
    story.append(P(
        "Clave: acepta empeoramientos con probabilidad exp(−delta/T). A temperatura alta "
        "explora mucho; al enfriarse se vuelve exigente. Así <b>escapa de óptimos locales</b>."))
    story.append(P(
        "<b>Detalles de implementación.</b> Vecindad 2-opt (intercambio de dos aristas); "
        "enfriamiento geométrico T &larr; T×0.95 desde T_inicial=10 hasta T_final=1e-3, con "
        "20 movimientos evaluados por nivel de temperatura. El delta de distancia se calcula "
        "de forma incremental (solo las 4 aristas afectadas), no recalculando la ruta completa "
        "en cada paso."))
    story.append(P(
        "<b>Fidelidad al material del curso.</b> El criterio de aceptación de Metropolis "
        "(exp(−delta/T)), el seguimiento de la mejor solución vista y el enfriamiento "
        "geométrico reproducen exactamente el algoritmo presentado en el curso. La única "
        "diferencia deliberada: el material evalúa un vecino y enfría en cada paso (una "
        "evaluación por nivel de temperatura), mientras que aquí se evalúan 20 vecinos por "
        "nivel antes de enfriar — la práctica estándar de la literatura de Recocido Simulado "
        "(\"longitud de cadena de Markov por temperatura\"), necesaria para que cada nivel de "
        "T tenga oportunidad real de explorar antes de bajar. No altera el algoritmo, solo su "
        "granularidad de enfriamiento."))

    story.append(P("2.2 Algoritmo Genético — flujo general", "H3"))
    story.append(P(
        "población &larr; rutas aleatorias<br/>"
        "repetir por G generaciones:<br/>"
        "&nbsp;&nbsp;evaluar aptitud (1/distancia) de cada individuo<br/>"
        "&nbsp;&nbsp;conservar al mejor (elitismo)<br/>"
        "&nbsp;&nbsp;mientras no se llene la nueva población:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;padres &larr; selección por torneo<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;hijo &larr; cruzamiento OX(padre1, padre2)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;con prob. p_mut: mutar(hijo)  [inversión de segmento]<br/>"
        "devolver el mejor individuo", "Pseudo"))
    story.append(P(
        "Usa los tres operadores del curso: <b>selección</b> (torneo), <b>cruzamiento</b> "
        "(Order Crossover, que garantiza permutaciones válidas) y <b>mutación</b> (inversión). "
        "La diversidad de la población le da robustez."))
    story.append(P(
        "<b>Detalles de implementación.</b> Población de 40 individuos durante 100 "
        "generaciones; selección por torneo con k=3 competidores; mutación con probabilidad "
        "p_mut=0.2; elitismo de 1 individuo (el mejor pasa intacto a la siguiente generación, "
        "así nunca se pierde el mejor hallazgo). Cada individuo es un arreglo de numpy con una "
        "permutación de las 15 ciudades."))

    story.append(P("2.3 Hill-Climbing — flujo general", "H3"))
    story.append(P(
        "ruta &larr; permutación aleatoria<br/>"
        "repetir:<br/>"
        "&nbsp;&nbsp;buscar el mejor movimiento 2-opt que reduzca la distancia<br/>"
        "&nbsp;&nbsp;si existe &rarr; aplicarlo<br/>"
        "&nbsp;&nbsp;si no existe &rarr; óptimo local alcanzado, terminar", "Pseudo"))
    story.append(P(
        "Búsqueda local pura: solo se mueve a vecinos que mejoran. Es rapidísimo, pero se "
        "detiene en el primer óptimo local. Su variante <b>Random Restart</b> (reiniciar "
        "desde varias soluciones) es la mejora natural, y se propone en la sección 5."))
    story.append(P(
        "<b>Detalles de implementación.</b> Se evaluó con un solo reinicio (reinicios=1) en "
        "el experimento principal, a propósito, para exponer su debilidad clásica: el "
        "atrapamiento en óptimos locales (ver sección 5.3 para la variante con reinicios). "
        "Cada iteración explora la vecindad 2-opt completa (todos los pares de aristas, "
        "O(n²)) y aplica el mejor movimiento de mejora, no uno aleatorio."))

    story.append(PageBreak())

    # ---------- resultados ----------
    story.append(P("3. Pruebas y resultados", "H2"))
    story.append(P(
        "Cada técnica se ejecutó <b>5 veces</b> con semillas distintas para observar "
        "variabilidad y convergencia. Se usó deliberadamente un <b>presupuesto computacional "
        "modesto</b>: con parámetros muy amplios las tres técnicas encuentran siempre el "
        "mismo óptimo (~32.22) y la varianza sería cero, lo que impediría comparar su "
        "comportamiento estocástico. La tabla reporta la mejor, promedio y peor distancia de "
        "las 5 corridas, más el tiempo promedio."))
    story.append(bloque_tabla(filas))
    story.append(P("Tabla 1. Resultados sobre 5 corridas por técnica.", "Cap"))

    story.append(P(
        f"<b>Lectura de los números.</b> Las tres técnicas <b>alcanzan el óptimo</b> "
        f"(≈32.22) en su mejor corrida, lo que confirma que 32.22 es la solución óptima (o "
        f"muy cercana) para esta instancia. Las diferencias aparecen en la <b>consistencia</b> "
        f"y el <b>costo</b>:"))
    ag = by["Algoritmo Genetico"]; sa = by["Recocido Simulado"]; hc = by["Hill-Climbing"]
    story.append(P(
        f"• <b>Algoritmo Genético</b> logra el mejor promedio "
        f"({float(ag['dist_promedio']):.2f}) y la menor dispersión "
        f"(std {float(ag['desv_std']):.3f}): la diversidad de la población lo hace el más "
        f"<b>consistente</b>, a cambio de ser el más lento "
        f"({float(ag['tiempo_prom_s']):.3f} s).<br/>"
        f"• <b>Recocido Simulado</b> queda intermedio en calidad "
        f"(promedio {float(sa['dist_promedio']):.2f}) y muy rápido "
        f"({float(sa['tiempo_prom_s']):.3f} s).<br/>"
        f"• <b>Hill-Climbing</b> es <b>el más rápido con enorme diferencia</b> "
        f"({float(hc['tiempo_prom_s']):.3f} s), pero con la mayor variabilidad "
        f"(std {float(hc['desv_std']):.3f}) y la peor peor-corrida "
        f"({float(hc['dist_peor']):.2f}): es el atrapamiento en óptimos locales en acción."))

    story.append(P("4. Visualización", "H2"))
    for archivo, cap in [
        ("ruta_recocido.png", "Figura 1. Mejor ruta — Recocido Simulado."),
        ("ruta_genetico.png", "Figura 2. Mejor ruta — Algoritmo Genético."),
        ("ruta_hillclimbing.png", "Figura 3. Mejor ruta — Hill-Climbing."),
    ]:
        ruta_img = os.path.join(RES, archivo)
        if os.path.exists(ruta_img):
            story.append(Image(ruta_img, width=9*cm, height=9*cm))
            story.append(P(cap, "Cap"))
    story.append(P(
        "Las tres mejores rutas son geométricamente equivalentes (el mismo ciclo óptimo, sin "
        "cruces): la señal visual de una solución 2-opt convergida."))
    story.append(Image(os.path.join(RES, "convergencia_comparativa.png"),
                       width=15*cm, height=9.4*cm))
    story.append(P("Figura 4. Convergencia comparada (mejor distancia vs. progreso "
                   "normalizado de la búsqueda).", "Cap"))
    story.append(P(
        "La curva de Recocido Simulado (naranja) muestra escalones y mesetas: acepta "
        "empeoramientos temporales antes de bajar. El Algoritmo Genético (azul) desciende por "
        "generaciones. Hill-Climbing (verde) cae de forma monótona y rápida hasta su óptimo "
        "local."))

    story.append(PageBreak())

    # ---------- analisis ----------
    story.append(P("5. Análisis comparativo y mejoras", "H2"))
    story.append(P("5.1 ¿Cuál obtuvo mejores resultados y por qué?", "H3"))
    story.append(P(
        "Depende del criterio. En <b>calidad promedio y consistencia</b>, gana el Algoritmo "
        "Genético: su población mantiene varias soluciones diversas simultáneamente, lo que "
        "reduce el riesgo de quedar atrapado en una mala región. En <b>eficiencia pura "
        "(tiempo)</b>, gana Hill-Climbing por dos órdenes de magnitud, aunque paga con "
        "inestabilidad. Un hallazgo relevante para esta instancia pequeña y bien comportada: "
        "las técnicas sofisticadas <b>no superan</b> en calidad al óptimo que también alcanza "
        "una búsqueda local simple; su ventaja real aparecería en instancias mayores o con "
        "paisajes de búsqueda más accidentados."))

    story.append(P("5.2 Ventajas y desventajas de cada enfoque", "H3"))
    # Las columnas de texto largo van envueltas en Paragraph: una celda con un
    # string plano no hace word-wrap en reportlab y el texto se desborda sobre
    # la columna vecina (se ve encimado). Con Paragraph sí respeta colWidths.
    def celda(txt):
        return Paragraph(txt, styles["Celda"])

    vd = [
        ["Técnica", "Ventajas", "Desventajas"],
        [celda("Recocido<br/>Simulado"),
         celda("Escapa de óptimos locales; simple; rápido; un solo estado en memoria."),
         celda("Muy sensible al esquema de enfriamiento; resultado variable si se enfría rápido.")],
        [celda("Algoritmo<br/>Genético"),
         celda("Explora en paralelo; robusto y consistente; bueno en paisajes multimodales."),
         celda("El más costoso; muchos parámetros (población, p_mut, torneo) que ajustar.")],
        [celda("Hill-Climbing"),
         celda("El más rápido y simple; convergencia inmediata."),
         celda("Se atasca en el primer óptimo local; alta varianza sin reinicios.")],
    ]
    tvd = Table(vd, hAlign="LEFT", colWidths=[3*cm, 5.5*cm, 5.5*cm])
    tvd.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#d8cdb2")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PAPER]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(tvd)
    story.append(Spacer(1, 10))

    story.append(P("5.3 Propuesta de mejora por técnica", "H3"))
    story.append(P(
        "• <b>Recocido Simulado:</b> usar un enfriamiento adaptativo (reheating) que suba la "
        "temperatura si la búsqueda se estanca, y calibrar T_inicial con la aceptación "
        "inicial objetivo (~80%).<br/>"
        "• <b>Algoritmo Genético:</b> hibridar con búsqueda local (memético): aplicar 2-opt a "
        "los mejores hijos cada cierto número de generaciones para acelerar la convergencia "
        "sin perder diversidad.<br/>"
        "• <b>Hill-Climbing:</b> añadir <b>Random Restart</b> (varios reinicios) y/o "
        "escalada estocástica; con solo 4–5 reinicios esta instancia alcanza el óptimo de "
        "forma consistente, eliminando la varianza observada."))
    story.append(P(
        "<b>Mejora transversal:</b> para instancias mayores o con capacidad de vehículos "
        "(CVRP), conviene una <b>hibridación</b> — por ejemplo, AG para exploración global "
        "seguido de 2-opt/recocido para refinamiento local — y precálculo de la matriz de "
        "distancias (ya aplicado) para no recalcular raíces cuadradas en cada evaluación."))

    story.append(PageBreak())

    # ---------- conclusiones ----------
    story.append(P("6. Conclusiones", "H2"))
    story.append(P(
        "El problema de ruteo de 15 ubicaciones de entrega se resolvió con tres "
        "metaheurísticas, una por grupo del reto — Recocido Simulado (estado único, "
        "inspirado en física), Algoritmo Genético (poblacional) y Hill-Climbing (estado "
        "único, búsqueda local) — todas construidas sobre la misma vecindad 2-opt, lo que "
        "permite comparar su comportamiento en igualdad de condiciones."))
    story.append(P(
        "Las tres técnicas alcanzan la misma distancia óptima (≈32.22) en su mejor corrida "
        "de las 5 ejecutadas, lo que valida las tres implementaciones de forma cruzada: si "
        "hubiera un error de lógica en alguna, no convergerían de forma independiente al "
        "mismo valor. La diferencia real entre ellas no está en la calidad máxima "
        "alcanzable, sino en la <b>consistencia</b> (qué tan seguido llegan cerca del óptimo) "
        "y el <b>costo computacional</b> por ejecutar la búsqueda."))
    story.append(P(
        "En términos prácticos para una empresa de reparto: si el plan de rutas se calcula "
        "una vez al día y hay margen de tiempo, el <b>Algoritmo Genético</b> es la opción más "
        "confiable por su baja varianza. Si las rutas deben recalcularse en tiempo real "
        "(por ejemplo, ante un pedido de última hora), <b>Hill-Climbing con random restart</b> "
        "da resultados casi tan buenos en una fracción del tiempo. <b>Recocido Simulado</b> "
        "queda como una alternativa intermedia sólida cuando se prefiere un solo estado en "
        "memoria (sin mantener una población completa)."))
    story.append(P(
        "Para escalar esta solución al problema real descrito en el reto — vehículos de "
        "capacidad limitada (CVRP) e instancias con más de 15 puntos — el camino natural es "
        "la hibridación planteada en la sección 5.3: una técnica poblacional para explorar el "
        "espacio de soluciones globalmente, refinada con búsqueda local 2-opt/recocido para "
        "pulir cada ruta candidata."))

    story.append(Spacer(1, 12))
    story.append(P(
        "<i>Reporte generado con resultados reales de la ejecución de run_experiments.py. "
        "Los valores numéricos pueden variar ligeramente entre corridas por la naturaleza "
        "estocástica de los métodos; las conclusiones cualitativas se mantienen.</i>", "Cap"))

    doc = SimpleDocTemplate(OUT_PDF, pagesize=A4,
                            topMargin=1.6*cm, bottomMargin=1.6*cm,
                            leftMargin=1.8*cm, rightMargin=1.8*cm,
                            title="Análisis comparativo TSP")
    doc.build(story)
    print("PDF generado:", OUT_PDF)


if __name__ == "__main__":
    build()
    
