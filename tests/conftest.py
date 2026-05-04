import os

os.environ.setdefault("PROJECT_NAME", "Nexus Test")
os.environ.setdefault("VAULT_INTERNAL_PATH", "/tmp/fake_vault")

from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from app.api.chat.controller import get_chat_service
from app.main import create_app


@pytest.fixture
def app():
    """Retorna a instância da aplicação FastAPI com dependências mockadas."""
    application = create_app()
    application.dependency_overrides[get_chat_service] = lambda: MagicMock()
    return application


@pytest.fixture
def client(app):
    """Retorna o TestClient do FastAPI para chamadas HTTP."""
    return TestClient(app)
