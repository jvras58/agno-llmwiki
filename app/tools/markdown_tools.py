
import os
from agno.tools.file import FileTools
from app.core.config import settings

def get_custom_tools() -> list:
    """
    Retorna a lista de ferramentas disponíveis para o agente Nexus.
    O FileTools é injetado apontando estritamente para o diretório raiz do Vault.
    """
    memory_dir = os.path.join(settings.vault_path, "memoria")
    os.makedirs(memory_dir, exist_ok=True)
    
    wiki_file_tools = FileTools(
        base_dir=settings.vault_path
    )
    
    return [wiki_file_tools]