from fastapi import APIRouter

from app.api.chat.controller import chat_endpoint
from app.api.chat.schema import ChatResponse

router = APIRouter()

router.post(
    "/chat",
    response_model=ChatResponse,
    tags=["Chat"],
)(chat_endpoint)
