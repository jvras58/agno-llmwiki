import logging
from pathlib import Path

from agno.knowledge.reader.markdown_reader import MarkdownReader

from app.knowledge.provider import wiki_knowledge

logger = logging.getLogger(__name__)

def sync_specific_file(file_path: str | Path):
    """
    Lê um arquivo Markdown específico e faz o upsert no PgVector.
    """
    path = Path(file_path)
    if not path.exists() or path.suffix != ".md":
        return

    logger.info(f"Vetorizando documento: {path.name}...")

    try:
        reader = MarkdownReader()
        documents = reader.read(file=path)

        if documents:
            wiki_knowledge.vector_db.upsert(documents)
            logger.info(f"Upsert concluído para {path.name}.")

    except Exception as e:
        logger.error(f"Erro ao vetorizar {path.name}: {e}")
