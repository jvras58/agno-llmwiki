import os

import pytest
from fastapi.testclient import TestClient

from app.main import create_app

os.environ["PROJECT_NAME"] = "Nexus Test"
os.environ["VAULT_INTERNAL_PATH"] = "/tmp/fake_vault"

@pytest.fixture
def app():
    """Retorna a instância da aplicação FastAPI."""
    return create_app()

@pytest.fixture
def client(app):
    """Retorna o TestClient do FastAPI para chamadas HTTP."""
    return TestClient(app)
