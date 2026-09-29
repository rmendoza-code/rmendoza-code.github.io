# CLAUDE.md — Portafolio de Rodrigo Mendoza Cortés

Contexto para retomar el trabajo en cualquier computadora o sesión (Claude Code, Cowork o humano). Léelo completo antes de tocar algo.

## Objetivo
Sitio personal publicado con GitHub Pages en https://rmendoza-code.github.io — posiciona a Rodrigo como **Agentic AI & Data Engineer** para vacantes de *Generative / Agentic AI Engineer* (LLMs, RAG, tool calling, MCP, guardrails, human-in-the-loop, integraciones, IA en producción). El CV en PDF enlaza directamente a secciones del sitio.

## Reglas de contenido (no negociables)
- **No inventar.** Solo hechos que Rodrigo haya dicho, que estén en su CV o en sus archivos. Si falta un dato, preguntar o marcarlo como pendiente.
- **Recreaciones, no datos reales.** Toda pantalla con cifras de CIMMYT u otros clientes es recreación con datos de muestra y debe decirlo en la propia pantalla.
- **Nada sensible en el repo (es público):** credenciales, IDs de hojas, webhooks, endpoints, correos de terceros. Las exportaciones de `lab/` se sanean con `tools/lab/sanitize.py` y se revisan con grep antes de publicar.
- **Honestidad en la matriz de capacidades:** ✓ solo con evidencia enlazada; ◐ para lo que está en construcción.
- Correo público: `rdgo.mendoza@gmail.com` (se arma en runtime con JS contra bots). LinkedIn `/in/rodrigomzc`.

## Estructura
| Ruta | Qué es |
|---|---|
| `index.html` | Landing: preloader 0→100, hero con figura 3D, perfil + métricas, servicios, **AI Lab** (`#ai-lab`, 6 ventanas), matriz **capacidades → evidencia** (`#capacidades`), **diplomado Tec** (`#diplomado`, `#tsp`), **Datos & BI** (`#dashboards`), trayectoria, stack, FAQ, contacto |
| `assets/site/styles.css`, `main.js` | Estilos y lógica del landing. **Textos en inglés en el objeto `EN` de `main.js`** (misma clave que `data-i18n`); el español vive en el HTML |
| `assets/site/case.css` | Estilos compartidos de las páginas de caso |
| `assets/site/fonts/`, `img/` | Fuentes autoalojadas (Archivo, JetBrains Mono) e imágenes (figuras 3D en WebP) |
| `dashboards/procurement-analytics.html` | Caso completo PR→PO con dashboard interactivo |
| `dashboards/cloud-billing.html`, `training-app.html` | Casos CIMMYT con recreación interactiva (datos/contenido de muestra) |
| `dashboards/financial-execution.html`, `rams-mantenimiento.html` | Páginas "en construcción" con vista previa |
| `assets/i18n.js` + `I18N.register({...})` | Motor ES⇄EN de las páginas de `dashboards/` (traduce nodos de texto exactos) |
| `lab/` | Exportaciones saneadas de agentes (Dify, n8n + MCP, Langflow RAG, Make) y proyecto TSP en Python, cada una con README |
| `CV_Rodrigo_Mendoza_Cortes.pdf` | CV publicado (se genera desde `tools/cv/cv.html`) |
| `tools/` | Fuentes de trabajo: CV en HTML, imagen OG, saneador de `lab/`, originales de las figuras 3D y hoja de personaje |

## Sistema de diseño
- Colores: fondo `#E8E8E8`, tinta `#111214`, cobalto `#3B4FE0` (acento en claro), lima `#B8E08C` (acento en oscuro).
- Tipografía del sitio: **Archivo** (variable, condensada 62% en títulos) + **JetBrains Mono** (etiquetas).
- Tipografía del CV: **DM Sans** + **Fira Code** (la del CV original de Rodrigo). CV sobrio, una columna, amigable con ATS: no subir el `letter-spacing` de los títulos (rompe la extracción de texto).
- Figuras 3D: personaje de `tools/assets/hoja-de-personaje.png`, fondo transparente, generadas en Higgsfield (gpt_image_2_5). Receta: mismo personaje, camisa blanca, pantalón negro, reloj con correa cobalto.
- CSP estricta en `index.html`: solo `'self'`, `data:` para imágenes y `frame-src https://udify.app` (demo en vivo del agente del hotel). Si agregas otro iframe o host, actualiza la CSP.

## Flujo de trabajo
1. Editar HTML/CSS/JS directamente (sitio estático, sin build).
2. Probar en local: `python3 -m http.server 8000` → http://localhost:8000 (revisa ES y EN, escritorio y móvil).
3. Verificar enlaces y anclas antes de publicar (todas las anclas que usa el CV: `ai-lab, capacidades, lab-hotel, lab-mcp, lab-rag, lab-fabric, lab-auto, lab-langgraph, tsp, dashboards`).
4. Regenerar derivados si cambió su fuente: `node tools/render.js cv` y `node tools/render.js og` (requiere Playwright).
5. `git add -A && git commit && git push origin main` → GitHub Pages publica en 1–2 min.

## Estado al 2026-09-29
- Publicado: v2 (rediseño), v3 (AI Lab + matriz + diplomado), v4 (dashboards rediseñados), CVs.
- **Pendiente de push:** commit "Casos Cloud billing y Training App + auditoría de enlaces" y este `CLAUDE.md` + `tools/`.
- Postulación en curso: vacante *Generative / Agentic AI Engineer* (reclutadora: Myrna Arredondo, myrna.arredondo@mystratis.com). Correo redactado; enviar con el CV adjunto.

## Pendientes / siguientes pasos
1. **Proyecto insignia:** portar el concierge del hotel a Python + LangGraph (RAG con base vectorial, guardrails, validación de RFC, `interrupt()` para aprobación humana, evaluación, demo pública). Al terminar, actualizar `#lab-langgraph`, la matriz (◐ → ✓) y el CV.
2. Confirmar estado de módulos 5–6 del diplomado (hoy marcados "En curso").
3. Completar casos Financial Execution y RAMS (hoy "en construcción").
4. Decidir si se nombra a CIMMYT en las páginas de caso o se generaliza.
5. Limitar gasto de OpenAI del agente público de Dify.
6. Seguridad local (fuera del repo): en `Downloads\Datos_y_codigo` había una llave de cuenta de servicio de Google Cloud y un token tipo AstraDB en texto plano → revocar y borrar.

## Convenciones de git
- Rama `main`, mensajes en español describiendo el cambio.
- Nunca subir `.bundle`, zips ni archivos de `Downloads`.
