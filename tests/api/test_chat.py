
from unittest.mock import patch


def test_chat_endpoint_success(client):
    mock_response = "Esta é uma resposta simulada do Nexus baseada no Vault."

    with patch(
        "app.api.chat.routes.chat_service.process_message",
        return_value=mock_response,
    ):
        response = client.post(
            "/api/v1/chat",
            json={"message": "Como funciona o Spec-Driven Development?"},
        )

    assert response.status_code == 200
    assert response.json()["reply"] == mock_response

def test_chat_endpoint_validation_error(client):
    """Garante que o FastAPI (Pydantic) bloqueie payloads inválidos."""
    payload = {"wrong_key": "Teste"}

    response = client.post("/api/v1/chat", json=payload)

    assert response.status_code == 422
