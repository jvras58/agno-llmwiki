from agno.knowledge.embedder.sentence_transformer import SentenceTransformerEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.pgvector import PgVector

from app.core.config import settings

# data_dir = settings.vault_path

wiki_knowledge = Knowledge(
    vector_db=PgVector(
        db_url=settings.db_url_vectordb,
        table_name="wiki_embeddings",
        embedder=SentenceTransformerEmbedder(id=settings.embedder_model),
    ),
)
