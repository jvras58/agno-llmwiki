from unittest.mock import MagicMock

from app.api.chat.controller import get_chat_service


def test_chat_endpoint_success(app, client):
    mock_response = "Esta é uma resposta simulada do Nexus baseada no Vault."

    mock_service = MagicMock()
    mock_service.process_message.return_value = mock_response

    app.dependency_overrides[get_chat_service] = lambda: mock_service
    try:
        response = client.post(
            "/api/v1/chat",
            json={"message": "Como funciona o Spec-Driven Development?"},
        )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json()["reply"] == mock_response
    mock_service.process_message.assert_called_once_with(
        "Como funciona o Spec-Driven Development?"
    )


def test_chat_endpoint_validation_error(client):
    """Garante que o FastAPI (Pydantic) bloqueie payloads inválidos."""
    payload = {"wrong_key": "Teste"}

    response = client.post("/api/v1/chat", json=payload)

    assert response.status_code == 422
