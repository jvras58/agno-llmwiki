from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # Configurações do Projeto
    project_name: str = "Nexus LLM-Wiki"
    debug: bool = False
    
    # Configurações do LLM
    llm_model: str = Field(default="llama3", description="Modelo a ser utilizado")
    ollama_host: str = Field(default="http://localhost:11434", description="URL base do Ollama")
    
    # Caminhos e Diretórios com alias para compatibilidade com o container
    vault_path: str = Field(..., alias="vault_internal_path", description="Caminho absoluto para os arquivos Markdown locais")

    # Configurações do Banco de Dados
    db_url_vectordb: str = Field(default="postgresql+psycopg://user:pass@localhost:5432/vectordb", description="URL de conexão do banco de dados")

    # Configurações do Embedder
    embedder_model: str = Field(default="sentence-transformers/all-MiniLM-L6-v2", description="Modelo de embedder a ser utilizado")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()