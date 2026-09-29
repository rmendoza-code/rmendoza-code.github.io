# AI Lab — Rodrigo Mendoza Cortés

Exportaciones reales (saneadas) de agentes, flujos RAG y automatizaciones con LLMs que he construido, más proyectos en Python del **diplomado en Tecnologías de IA del Tec de Monterrey**. Cada carpeta trae un README con arquitectura, qué demuestra y cómo importarlo.

> Todas las credenciales, IDs de hojas, webhooks, correos y endpoints fueron reemplazados por marcadores como `<CREDENTIAL>` o `<SHEET_ID>`. Para correr un flujo hay que conectar tus propias cuentas.

| Proyecto | Plataforma | Qué demuestra |
|---|---|---|
| [`hotel-casa-merida-dify/`](hotel-casa-merida-dify/) | Dify | Multi-agente con clasificador/enrutador, 3 agentes con *function calling*, memoria, herramienta de conocimiento y Google Sheets |
| [`n8n-mcp-agentes/`](n8n-mcp-agentes/) | n8n | Servidor **MCP** propio, agente enrutador que consume MCP, webhooks, sub-workflows, agente de voz en Telegram y workflow de errores |
| [`lexmex-rag-langflow/`](lexmex-rag-langflow/) | Langflow + AstraDB | **RAG**: carga → chunking → embeddings → base vectorial → LLM con contexto |
| [`make-automatizaciones-llm/`](make-automatizaciones-llm/) | Make | Agente de voz (Vapi) con webhooks y agenda, extracción de facturas con LLM, minutas automáticas |
| [`tsp-metaheuristicas/`](tsp-metaheuristicas/) | Python | Recocido simulado, algoritmo genético y hill-climbing (2-opt) comparados en un TSP de 15 puntos |

**En construcción:** migración del agente del hotel a **Python + LangGraph** con RAG sobre base vectorial, guardrails, aprobación humana (human-in-the-loop) y evaluación.
