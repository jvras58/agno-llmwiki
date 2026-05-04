from agno.agent import Agent
from agno.models.ollama import Ollama

from app.core.config import settings
from app.core.prompts import INSTRUCTION_PROMPT, WIKI_SYSTEM_PROMPT
from app.knowledge.provider import get_wiki_knowledge
from app.tools.markdown_tools import get_custom_tools


def create_wiki_agent() -> Agent:
    return Agent(
        model=Ollama(id=settings.llm_model, host=settings.ollama_host),
        knowledge=get_wiki_knowledge(),
        tools=get_custom_tools(),
        system_message=WIKI_SYSTEM_PROMPT,
        instructions=INSTRUCTION_PROMPT,
        search_knowledge=True,
        read_chat_history=True,
        markdown=True,
    )
