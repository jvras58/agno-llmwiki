from pydantic import BaseModel, Field


class UploadResponse(BaseModel):
    message: str = Field(
        ...,
        description="Mensagem de confirmação sobre o upload e indexação.",
    )


class SyncResponse(BaseModel):
    status: str = Field(
        ...,
        description="O status da sincronização.",
    )
    message: str = Field(
        ...,
        description="Uma mensagem informativa sobre o resultado da sincronização.",
    )
