import logging
import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from app.core.config import settings
from app.services.indexer_service import sync_specific_file

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)


class ObsidianVaultHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.last_processed = {}
        self.cooldown_seconds = 2.0

    def process_event(self, event):
        if event.is_directory or not event.src_path.endswith(".md"):
            return

        current_time = time.time()
        file_path = event.src_path

        if (
            file_path in self.last_processed
            and current_time - self.last_processed[file_path] < self.cooldown_seconds
        ):
            return

        self.last_processed[file_path] = current_time
        logger.info(
            f"Evento detectado ({event.event_type}): {os.path.basename(file_path)}"
        )

        sync_specific_file(file_path)

    def on_created(self, event):
        self.process_event(event)

    def on_modified(self, event):
        self.process_event(event)


def start_watcher():
    vault_path = settings.vault_path

    if not os.path.exists(vault_path):
        logger.error(
            f"O diretório {vault_path} não existe. "
            "Verifique suas variáveis de ambiente."
        )
        return

    event_handler = ObsidianVaultHandler()
    observer = Observer()

    observer.schedule(event_handler, vault_path, recursive=True)

    observer.start()
    logger.info(f"👀 Watchdog iniciado. Monitorando Vault em: {vault_path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logger.info("Watchdog encerrado.")

    observer.join()


if __name__ == "__main__":
    start_watcher()
