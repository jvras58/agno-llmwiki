from fastapi import APIRouter

from app.api.docs.controller import trigger_vault_sync, upload_document
from app.api.docs.schema import SyncResponse, UploadResponse

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
