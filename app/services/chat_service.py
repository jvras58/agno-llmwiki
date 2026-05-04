import logging

from app.agents.wiki_agent import create_wiki_agent

logger = logging.getLogger(__name__)


class ChatService:
    def __init__(self):

        self.agent = create_wiki_agent()

    def process_message(self, message: str) -> str:
        """
        Recebe a mensagem da API, processa com o agente Nexus e retorna o texto.
        """
        logger.info(f"Processando mensagem: {message[:50]}...")

        try:
            response = self.agent.run(message)
            return response.content
        except Exception as e:
            logger.error(f"Erro ao processar mensagem no Agente: {e}")
            raise e
