# Nexus LLM-Wiki 🧠

Um agente inteligente focado em atuar como um "segundo cérebro" sobre um *Vault* local do Obsidian. Construído com foco em privacidade (utilizando modelos locais) e desenhado sob princípios de **Spec-Driven Development (SDD)**, garantindo contratos claros entre a API, o comportamento do agente e a ingestão de dados.

## 📝 O que é o Vault do Obsidian?

O **Obsidian** é um aplicativo poderoso de anotações focado na criação de um "segundo cérebro". Ele armazena suas anotações localmente em arquivos de texto simples (Markdown), permitindo que você crie links entre as ideias (como uma Wiki pessoal).

O diretório principal onde o Obsidian salva todos esses arquivos `.md` e pastas é chamado de **Vault** (Cofre). 

Neste projeto, o Agente Nexus atua como uma camada de inteligência artificial em cima desse diretório. Em vez de você buscar palavras-chave manualmente, o agente lê, entende o contexto semântico das suas anotações (respeitando headers, links e tags) e interage com você, podendo até mesmo deduzir e escrever novas memórias no próprio Vault.

### 📂 Testando com o Vault de Exemplo

Se você não usa o Obsidian ou quer apenas testar a aplicação, o repositório inclui uma pasta `vault_examples/` com documentos pré-configurados.

Basta apontar a variável `VAULT_PATH` no seu arquivo `.env` para essa pasta local:
`VAULT_PATH="./vault_examples"`

## 🧠 Memória Ativa (O Agente que Escreve)

Diferente de sistemas RAG (Retrieval-Augmented Generation) tradicionais que apenas *leem* documentos, o **Nexus atua de forma bidirecional**. Ele não é apenas um consumidor do seu Vault, mas um participante ativo na construção do seu conhecimento.

A arquitetura foi desenhada para suportar um fluxo contínuo de "Memória Ativa":

1. **Tomada de Decisão:** Durante a interação, o modelo (Llama 3) é instruído via System Prompt a identificar deduções importantes, preferências do usuário ou novos fatos.
2. **Escrita via Tools:** Ao identificar uma informação relevante, o agente utiliza o `FileTools` (do framework Agno) para criar e salvar autonomamente um arquivo Markdown (ex: na pasta `memoria/` do seu Vault).
3. **O Ciclo Reativo (Watchdog):** Imediatamente após o agente salvar o arquivo físico no disco, o serviço *Watchdog* que roda em background detecta a criação do arquivo.
4. **Auto-Atualização:** O Watchdog aciona o `MarkdownReader`, gera os embeddings e faz o *upsert* no PgVector. 

### Exemplo Prático de Fluxo

*   **Usuário:** *"Nexus, estou tendo muita dificuldade em focar na escrita teórica do meu projeto hoje, prefiro programar. Anote isso."*
*   **Ação do Agente:** O agente reconhece o comando, cria um arquivo `memoria/preferencias_trabalho.md` no seu Obsidian documentando esse padrão de comportamento.
*   **Vetorização:** O sistema reativo lê esse novo arquivo e atualiza o banco de dados em milissegundos.
*   **Dias Depois:** Se o usuário pedir *"Sugira uma tarefa para hoje"*, o agente fará uma busca no RAG, encontrará a memória que ele mesmo escreveu e poderá sugerir: *"Considerando que dias atrás você registrou uma preferência por codar quando está sem foco para teoria, que tal começarmos pela modelagem de dados da API hoje?"*

Tudo isso acontece sem que o usuário precise abrir o Obsidian para registrar a nota manualmente. O agente escreve *para* você, no *seu* próprio sistema de arquivos local.

## 🏗️ Arquitetura

O projeto adota uma estrutura modular, separando a lógica de negócio (Agente), os serviços (Backend/API) e o processamento de dados (Workers).

```text
llm-wiki/
├── app/
│   ├── api/
│   │   └── routes.py             # Endpoints FastAPI (Chat e Sync)
│   ├── agents/
│   │   └── wiki_agent.py         # Configuração do Agno Agent (Llama 3)
│   ├── core/
│   │   ├── config.py             # Validação de ambiente com Pydantic
│   │   └── prompts.py            # Contratos de comportamento do Agente
│   ├── knowledge/
│   │   └── provider.py           # Conexão com PgVector
│   ├── services/
│   │   ├── chat_service.py       # Lógica de conversação
│   │   ├── indexer_service.py    # Geração de embeddings e upsert
│   │   └── knowledge_service.py  # Carga em lote (batch load)
│   ├── tools/
│   │   └── markdown_tools.py     # Ferramentas de escrita no Vault
│   ├── workers/
│   │   └── vault_watcher.py      # Watchdog para indexação reativa
│   └── main.py                   # Ponto de entrada da aplicação (ASGI)
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
└── uv.lock
```

## 🚀 Tecnologias

*   **Agentes & Orquestração LLM:** [Agno](https://github.com/agno-ai/agno)
*   **LLM Local:** Ollama (Llama 3)
*   **Banco de Dados Vetorial:** PostgreSQL + PgVector
*   **Backend / API:** FastAPI
*   **Validação & Configuração:** Pydantic Settings
*   **Sincronização em Background:** Watchdog
*   **Gerenciamento de Pacotes e Build:** `uv` (Astral)
*   **Containerização:** Docker & Docker Compose

## ✨ Principais Funcionalidades

1.  **RAG 100% Local:** Contextualização de respostas baseada nos seus arquivos Markdown (`.md`) sem enviar dados confidenciais para APIs externas.
2.  **Sincronização Reativa (Desacoplada):** O serviço *Watchdog* roda em paralelo observando o diretório do seu Obsidian. Ao editar e salvar uma nota, os embeddings correspondentes são atualizados no PgVector instantaneamente.
3.  **Memória Ativa:** O Agente Nexus possui acesso a ferramentas de sistema de arquivos que permitem a ele criar ou editar notas na subpasta `memoria/` quando julgar que uma informação nova deve ser lembrada.
4.  **API Pronta para Frontend:** Endpoints tipados e documentados nativamente (Swagger/OpenAPI) para consumo por interfaces web (Next.js, etc).

## ⚙️ Pré-requisitos

*   [Docker](https://www.docker.com/) e Docker Compose instalados.
*   [Ollama](https://ollama.com/) instalado na máquina host com o modelo de preferência baixado (ex: `ollama run llama3`).

## 🛠️ Configuração e Execução

### 1. Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto (use o `.env.example` como base se houver):

```env
PROJECT_NAME="Nexus LLM-Wiki"
DEBUG=True

# Configurações do Modelo
LLM_MODEL="llama3"
# Use [http://host.docker.internal:11434](http://host.docker.internal:11434) se o Ollama estiver rodando nativamente na sua máquina (fora do Docker)
OLLAMA_HOST="[http://host.docker.internal:11434](http://host.docker.internal:11434)"

# Mapeamento do Diretório do Obsidian
VAULT_PATH="C:/Caminho/Para/Seu/Obsidian/Vault" # Substitua pelo seu caminho real
VAULT_INTERNAL_PATH="/app/vault"
```

### 2. Subindo a Infraestrutura

Utilize o Docker Compose para fazer o build via `uv` e subir o Banco de Dados, a API e o Worker simultaneamente:

```bash
docker compose up --build
```

**Serviços iniciados:**
*   `db` (PgVector) na porta `5432`
*   `api` (FastAPI) na porta `8000` -> Acesse a documentação em `http://localhost:8000/docs`
*   `watcher` (Worker) rodando em background aguardando modificações no disco.

## 📡 Endpoints Principais

*   `POST /api/v1/chat`: Recebe a mensagem do usuário e retorna a resposta do Agente baseada no RAG.
*   `POST /api/v1/knowledge/sync`: Aciona manualmente uma recarga/sincronização completa (batch) do Vault.



## 📚 Referências e Documentação Oficial (Agno)

A arquitetura e as integrações deste projeto foram baseadas nos seguintes módulos da documentação oficial do Agno:

### Ingestão de Dados e Conhecimento
*   [Markdown Reader (Conceitos)](https://docs.agno.com/knowledge/concepts/readers/markdown-reader) - Base para a leitura semântica dos arquivos do Obsidian.
*   [Exemplo: Markdown Reader Async](https://docs.agno.com/examples/knowledge/readers/md-reader-async) - Estratégia de ingestão de documentos.
*   [Gerenciamento de Base de Conhecimento](https://docs.agno.com/agent-os/knowledge/manage-knowledge) - Padrões para manipulação do vetor de dados.

### Banco de Dados Vetorial e Embeddings
*   [PgVector (Overview)](https://docs.agno.com/knowledge/vector-stores/pgvector/overview#pgvector-vector-database) - Configuração do storage de vetores no PostgreSQL.
*   [Sentence Transformer Embedder](https://docs.agno.com/examples/knowledge/embedders/sentence-transformer-embedder) - Modelos de embedding para otimização da busca vetorial local.

### Ferramentas do Agente e Memória
*   [File Toolkit (Local)](https://docs.agno.com/tools/toolkits/local/file) - Permite ao agente criar, ler e editar anotações (memória ativa).
*   [Chat History](https://docs.agno.com/history/overview#chat-history) - Implementação de persistência do contexto conversacional.


## 🤝 Contribuindo

Este projeto utiliza o gerenciador de pacotes `uv` para desenvolvimento ultrarrápido.

```bash
# Sincronizar as dependências localmente
uv sync

# Ativar o ambiente virtual criado
source .venv/bin/activate # ou .venv\Scripts\activate no Windows
```