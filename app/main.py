
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.docs.routes import router as docs
from app.api.chat.routes import router as chat
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.project_name,
        description="API para o Agente LLM-Wiki Nexus, um assistente inteligente para consulta de conhecimento.",
        version="1.0.0",
        debug=settings.debug
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(docs, prefix="/api/v1")
    app.include_router(chat, prefix="/api/v1")

    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=settings.debug
    )