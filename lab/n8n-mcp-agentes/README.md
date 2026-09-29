# Agentes y servidor MCP en n8n

Cinco workflows exportados de n8n que forman un pequeño sistema de agentes.

| Archivo | Qué hace |
|---|---|
| `mcp-server.json` | **Servidor MCP** (`MCP Server Trigger`) que expone 4 herramientas: fecha/hora, crear evento en Google Calendar, búsqueda web (SerpAPI vía HTTP) y enviar email con Gmail. |
| `agente-enrutador-mcp.json` | Sub-workflow que recibe una solicitud clasificada y la **enruta con un Switch** a Slack, Notion, Gmail o Google Sheets; para ciertos casos, un **agente (OpenAI/Anthropic) usa el cliente MCP** para agendar una reunión de 15 min. |
| `asistente-interno-webhook.json` | Punto de entrada por **webhook**: valida la entrada, llama a un sub-workflow de clasificación y luego al enrutador, y responde al webhook. |
| `telegram-agent.json` | Agente en **Telegram** que recibe notas de voz, las transcribe, resume la necesidad con un LLM y responde con audio generado. |
| `error-workflow.json` | **Workflow de errores** genérico: cualquier falla dispara una alerta en Slack. |

## Qué demuestra
MCP (servidor y cliente) · tool calling · webhooks y APIs REST · orquestación con sub-workflows · enrutamiento por reglas + LLM · manejo de errores pensando en producción.

## Importar
n8n → *Workflows* → *Import from file*. Reasignar credenciales (`<CREDENTIAL>`) y la URL del servidor MCP.
