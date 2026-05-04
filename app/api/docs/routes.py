from fastapi import APIRouter
from app.api.docs.controller import upload_document, trigger_vault_sync
from app.api.docs.schema import UploadResponse, SyncResponse

router = APIRouter()

router.post(
    "/knowledge/upload",
    response_model=UploadResponse,
    tags=["Knowledge"],
)(upload_document)

router.post(
    "/knowledge/sync",
    response_model=SyncResponse,
    tags=["Knowledge"]
)(trigger_vault_sync)
