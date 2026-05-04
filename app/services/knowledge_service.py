import logging
from app.knowledge.provider import wiki_knowledge

logger = logging.getLogger(__name__)

def load_initial_knowledge(recreate: bool = False):
    """
    Realiza a carga em lote (batch) de todo o diretório configurado.
    Ideal para o primeiro setup da aplicação ou para reindexações completas (recreate=True).
    
    Para indexações dinâmicas de arquivos individuais no dia a dia, 
    o sistema conta com a arquitetura baseada no Watchdog.
    """
    logger.info("Iniciando a carga macro da base de conhecimento...")
    
    try:
        wiki_knowledge.load(recreate=recreate)
        logger.info("Carga da base de conhecimento concluída com sucesso.")
    except Exception as e:
        logger.error(f"Falha ao carregar a base de conhecimento: {e}")
        raise e