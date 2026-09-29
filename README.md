# Portafolio — Rodrigo Mendoza Cortés

Agentic AI & Data Engineer. Sitio estático (HTML/CSS/JS puro, sin build ni dependencias) publicado con GitHub Pages en https://rmendoza-code.github.io

## Estructura
- `index.html` — landing: preloader, hero, perfil, servicios, **AI Lab** (ventanas por proyecto con demo, arquitectura y código), matriz capacidades → evidencia, diplomado Tec, Datos & BI, trayectoria, stack, FAQ y contacto (ES/EN)
- `lab/` — exportaciones saneadas de agentes (Dify, n8n + MCP, Langflow RAG, Make) y proyectos Python del diplomado, cada uno con README
- `assets/site/` — estilos, script, fuentes autoalojadas (Archivo, JetBrains Mono) e imágenes del sitio
- `assets/og-image.png` — vista previa para LinkedIn / redes (1200×630)
- `dashboards/` — casos de estudio: recreaciones HTML de dashboards de Power BI (datos de muestra)
- `assets/i18n.js`, `assets/lang-procurement.js` — traducciones usadas por los dashboards
- `CV_Rodrigo_Mendoza_Cortes.pdf` — CV descargable
- `404.html` — página de error

## Editar
- Textos en español: directamente en `index.html`.
- Textos en inglés: objeto `EN` al inicio de `assets/site/main.js` (misma clave que `data-i18n`).
- Colores: variables en `:root` de `assets/site/styles.css` (gris `#E8E8E8`, cobalto `#3B4FE0`, lima `#B8E08C`).

## Probar en local
```bash
python3 -m http.server 8000   # y abre http://localhost:8000
```

La versión anterior del sitio ("cuaderno de datos") quedó guardada en el tag `v1`.
