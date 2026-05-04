from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(..., description="A mensagem ou pergunta enviada pelo usuário.")


class ChatResponse(BaseModel):
    reply: str = Field(..., description="A resposta gerada pelo Agente Nexus.")
