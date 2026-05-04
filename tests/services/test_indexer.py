from pathlib import Path
from unittest.mock import patch

from app.services.indexer_service import sync_specific_file


def test_sync_specific_file_ignores_non_md():
    """Garante que o indexador aborta silenciosamente se o arquivo não for .md."""

    # Mock do banco vetorial para garantir que o upsert NUNCA seja chamado
    with patch('app.knowledge.provider.wiki_knowledge.vector_db.upsert') as mock_upsert:
        # Passamos um arquivo fictício .txt
        sync_specific_file(Path("/tmp/fake_vault/nota.txt"))

    # O upsert não deve ter sido chamado
    mock_upsert.assert_not_called()


def test_sync_specific_file_processes_md(tmp_path):
    """Garante que o indexador lê arquivos .md e chama o upsert."""

    # Cria um arquivo Markdown real temporário para o teste
    test_md = tmp_path / "teste_sdd.md"
    test_md.write_text("# Teste de Documento\nConteúdo sobre arquitetura.")

    # Mock do upsert do PgVector
    with patch('app.knowledge.provider.wiki_knowledge.vector_db.upsert') as mock_upsert:
        # Executa a função
        sync_specific_file(test_md)

    # Garante que o método de upsert do banco foi chamado
    mock_upsert.assert_called_once()
