# Automatizaciones con LLMs (Make)

| Archivo | Qué hace |
|---|---|
| `agente-voz-vapi.make.json` | Backend de un **agente de voz (Vapi)**: recibe llamadas por webhook, consulta disponibilidad en Google Calendar, agenda o propone alternativa, confirma por email y responde al webhook. |
| `extraccion-facturas-llm.make.json` | Vigila una carpeta de Drive, extrae los datos de cada factura con un LLM a JSON estructurado y los registra en Google Sheets. |
| `minutas-automaticas.make.json` | Toma transcripciones de reuniones (Fireflies), genera minuta, título y resumen con LLM, crea el documento y lo envía por correo. |

## Qué demuestra
Integración de LLMs con sistemas empresariales · webhooks · salida estructurada (JSON) · enrutamiento condicional.

## Importar
Make → *Create scenario* → *Import blueprint*. Reconectar las conexiones (`<CONNECTION>`).
