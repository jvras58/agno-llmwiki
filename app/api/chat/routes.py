from fastapi import APIRouter

from app.api.chat.controller import chat_endpoint, trigger_vault_sync
from app.api.chat.schema import ChatResponse, SyncResponse

router = APIRouter()

router.post("/chat", response_model=ChatResponse, tags=["Chat"])(chat_endpoint)
router.post("/knowledge/sync", response_model=SyncResponse, tags=["Knowledge"])(trigger_vault_sync)
