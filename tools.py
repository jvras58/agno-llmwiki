from agno.tools.file import FileTools
from config.config import VAULT

def create_tools():
    """Create and configure tools for the agent."""
    return [FileTools(base_dir=VAULT, all=True)]  # read/save/list/search/delete