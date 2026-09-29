# LexMex — chatbot legal con RAG (Langflow + AstraDB)

Proyecto de la **Misión 4** del módulo *Prompt Engineering y Agentes LLM con herramientas Low-Code* (Diplomado en Tecnologías de IA, Tec de Monterrey). Caso: un despacho necesita responder consultas legales a partir de normativa dispersa.

## Pipeline
```
URL (Código Civil Federal) ─▶ Split Text ─▶ OpenAI Embeddings ─▶ AstraDB (vector store)
                                                                     │ búsqueda semántica
Pregunta del usuario ───────────────────────────────▶ Parser ◀───────┘
                                                        │ contexto
                                         Prompt Template ─▶ OpenAI Model ─▶ Respuesta
```

## Qué demuestra
RAG de punta a punta · chunking · embeddings · base de datos vectorial · prompt con contexto recuperado.

## Importar
Langflow → *Import* → `lexmex-rag.langflow.json`. Configurar variables de OpenAI y el token/endpoint de AstraDB (vacíos en esta exportación).
