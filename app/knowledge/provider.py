from agno.knowledge.knowledge import Knowledge
from agno.vectordb.pgvector import PgVector
from agno.knowledge.embedder.sentence_transformer import SentenceTransformerEmbedder
from app.core.config import settings


wiki_knowledge = Knowledge(
    data_dir=settings.vault_path,
    db_url_vectordb=settings.db_url_vectordb,
    embedder_model=settings.embedder_model,
    vector_db=PgVector(
        db_url=settings.db_url_vectordb,
        table_name="wiki_embeddings",
        embedder=SentenceTransformerEmbedder(id=settings.embedder_model)
    ),
)