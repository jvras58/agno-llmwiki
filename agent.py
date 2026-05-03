from agno.agent import Agent
from agno.models.groq import Groq
from config.knowledge import create_knowledge_base
from tools import create_tools
from config.prompts import get_agent_instructions

def create_agent():
    """Create and configure the main agent."""
    knowledge = create_knowledge_base()
    tools = create_tools()
    instructions = get_agent_instructions()

    agent = Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        instructions=instructions,
        tools=tools,
        knowledge=knowledge,
        search_knowledge=True,  # RAG agent
        markdown=True,
        add_history_to_context=True,
    )

    return agent