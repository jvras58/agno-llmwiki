from fastapi import BackgroundTasks, File, UploadFile
import os
import shutil

from app.core.config import settings
from app.services.indexer_service import sync_specific_file
from app.services.knowledge_service import load_initial_knowledge
from app.api.docs.schema import UploadResponse, SyncResponse


async def upload_document(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
) -> UploadResponse:
    """Recebe um arquivo, salva no diretório base e manda indexar."""

    file_path = os.path.join(settings.vault_path, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    background_tasks.add_task(sync_specific_file, file_path)

    return UploadResponse(message=f"Arquivo {file.filename} salvo e enviado para indexação.")


async def trigger_vault_sync(background_tasks: BackgroundTasks, recreate: bool = False):
    """Força uma sincronização macro do Vault."""
    background_tasks.add_task(load_initial_knowledge, recreate)

    return SyncResponse(
        status="accepted",
        message="A sincronização da base de conhecimento foi iniciada em background."
    )
