FROM astral-sh/uv:python3.12-bookworm-slim AS builder

# Define o diretório de trabalho
WORKDIR /app

# Ativa o modo de link otimizado do uv e evita a criação de bytecode
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Instala as dependências primeiro (cache layer)
# Copia apenas os arquivos de lock e projeto
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

# Copia o código da aplicação
COPY app/ ./app/

# Sincroniza o projeto
RUN uv sync --frozen --no-dev

# Define o PATH para usar o ambiente virtual criado pelo uv
ENV PATH="/app/.venv/bin:$PATH"