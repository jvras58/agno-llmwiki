# Agno LLM Wiki

Uma arquitetura modular em microserviços para gerenciamento de wiki usando Agno e LLMs.

## Arquitetura

O sistema é dividido em módulos/microserviços independentes:

- **config.py**: Configurações globais (caminhos, URLs de banco)
- **knowledge.py**: Serviço de base de conhecimento (Postgres + pgvector)
- **tools.py**: Ferramentas disponíveis para os agentes
- **prompts.py**: Engenharia de prompts e instruções
- **agent.py**: Configuração do agente principal
- **chat.py**: Interface de chat simples
- **chat_service.py**: Serviço de chat via FastAPI
- **knowledge_service.py**: Serviço de conhecimento via FastAPI

## Instalação

```bash
pip install -e .
```

## Uso

### Modo Simples
```bash
python main.py
```

### Serviços Individuais
```bash
# Serviço de Chat
python chat_service.py

# Serviço de Conhecimento
python knowledge_service.py
```

## Dependências

- agno: Framework para agentes
- fastapi: Para microserviços
- uvicorn: Servidor ASGI