---
aliases:
  - Nexus
  - Agente Wiki
tags:
  - ai
  - arquitetura
  - fastapi
  - agno
status: em_desenvolvimento
---
# Projeto Nexus - Arquitetura Base

> [!info] Resumo do Projeto
> O **Nexus** é um agente de conhecimento local focado em RAG sobre o Vault do Obsidian, operando de forma 100% privada e offline.

## Stack Tecnológica
- **Orquestração de Agentes:** [[Agno Framework]]
- **Banco Vetorial:** PgVector (PostgreSQL)
- **Modelos:** LLMs locais rodando via Ollama (Llama 3)
- **Backend:** FastAPI

## Decisões Arquiteturais
Decidimos substituir o [[CrewAI]] pelo **Agno** devido à melhor aderência aos nossos princípios de [[Spec-Driven Development (SDD)]] e à facilidade na ingestão de documentos. Todo o fluxo de ingestão ocorre em background utilizando a biblioteca `watchdog` para não travar a API.