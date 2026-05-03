from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.vectordb.pgvector import PgVector
from agno.knowledge.embedder.sentence_transformer import SentenceTransformerEmbedder
from config.config import VAULT, DB_URL

def create_knowledge_base():
    """Create and configure the knowledge base."""
    knowledge = Knowledge(
        vector_db=PgVector(
            table_name="wiki_vault",
            db_url=DB_URL,
            embedder=SentenceTransformerEmbedder(id="sentence-transformers/all-MiniLM-L6-v2"),
        ),
    )

    # Index the entire vault recursively
    knowledge.add_content(path=VAULT, reader=MarkdownReader(chunk=True))

    return knowledge