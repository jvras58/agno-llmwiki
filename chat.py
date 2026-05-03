from agent import create_agent

def start_chat():
    """Start the chat interface."""
    agent = create_agent()

    # Example query
    query = (
        "Encontre todos os READMEs que falam de 'autenticação' e crie "
        "'_Index/Autenticacao.md' linkando cada um com [[wikilinks]] e um resumo."
    )

    agent.print_response(query)

if __name__ == "__main__":
    start_chat()