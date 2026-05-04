from fastapi import HTTPException

from app.api.chat.schema import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

chat_service = ChatService()


async def chat_endpoint(request: ChatRequest):
    """Envia uma mensagem para o Agente Nexus."""
    try:
        reply_content = chat_service.process_message(request.message)
        return ChatResponse(reply=reply_content)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro interno do agente: {str(e)}"
        ) from e
