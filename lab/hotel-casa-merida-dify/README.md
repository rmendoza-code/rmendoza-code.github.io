# Hotel Casa Mérida Boutique — asistente multi-agente (Dify)

Asistente conversacional para huéspedes de un hotel boutique en Mérida, Yucatán. Exportación DSL de Dify (`agente-hotel-merida.dify.yml`, modo *advanced-chat*).

## Arquitectura
```
Usuario ─▶ Clasificador de preguntas ─┬─▶ Agente Reservaciones  ─┐
                                      ├─▶ Agente Facturación     ─┼─▶ Respuesta
                                      └─▶ Agente Disponibilidad  ─┘
```
- **Enrutamiento:** un nodo *question-classifier* decide qué agente atiende (reservación, factura CFDI o disponibilidad/tarifas).
- **Agentes:** estrategia *function calling* con `gpt-4o-mini`, memoria de conversación y una persona definida por agente.
- **Herramientas por agente:** `search_info_hotel` (fuente oficial de información del hotel), Google Sheets `batch_get` (disponibilidad y tarifas), Tavily y Wikipedia.
- **Citas de fuente** (`retriever_resource`) activadas.

## Qué demuestra
Arquitectura agéntica · tool calling · lógica de decisión (router) · memoria · prompts por rol · integración con un sistema de negocio (Sheets).

## Siguiente versión (en construcción)
Port a **Python + LangGraph**: RAG sobre base vectorial con políticas del hotel, validación de datos fiscales (RFC) como guardrail, aprobación humana antes de emitir factura y set de evaluación.

## Importar
Dify → *Studio* → *Import DSL file* → seleccionar el `.yml`. Reconectar el proveedor de OpenAI, Tavily y Google Sheets.
