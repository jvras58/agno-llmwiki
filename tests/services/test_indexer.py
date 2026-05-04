from pathlib import Path
from unittest.mock import MagicMock, patch

from app.services.indexer_service import sync_specific_file


def test_sync_specific_file_ignores_non_md():
    """Garante que o indexador aborta silenciosamente se o arquivo não for .md."""
    fake_knowledge = MagicMock()

    with patch(
        "app.services.indexer_service.get_wiki_knowledge",
        return_value=fake_knowledge,
    ):
        sync_specific_file(Path("/tmp/fake_vault/nota.txt"))

    fake_knowledge.vector_db.upsert.assert_not_called()


def test_sync_specific_file_processes_md(tmp_path):
    """Garante que o indexador lê arquivos .md e chama o upsert."""
    test_md = tmp_path / "teste_sdd.md"
    test_md.write_text(
        "# Teste de Documento\nConteúdo sobre arquitetura.", encoding="utf-8"
    )

    fake_knowledge = MagicMock()

    with patch(
        "app.services.indexer_service.get_wiki_knowledge",
        return_value=fake_knowledge,
    ):
        sync_specific_file(test_md)

    fake_knowledge.vector_db.upsert.assert_called_once()
