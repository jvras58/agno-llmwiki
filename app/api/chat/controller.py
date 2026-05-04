from functools import lru_cache

from fastapi import Depends, HTTPException

from app.api.chat.schema import ChatRequest, ChatResponse
from app.services.chat_service import ChatService


@lru_cache(maxsize=1)
def get_chat_service() -> ChatService:
    return ChatService()


async def chat_endpoint(
    request: ChatRequest,
    service: ChatService = Depends(get_chat_service),
):
    """Envia uma mensagem para o Agente Nexus."""
    try:
        reply_content = service.process_message(request.message)
        return ChatResponse(reply=reply_content)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro interno do agente: {str(e)}"
        ) from e
