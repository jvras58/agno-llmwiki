from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config.knowledge import create_knowledge_base

app = FastAPI(title="Agno LLM Wiki Knowledge Service")

class SearchRequest(BaseModel):
    query: str
    limit: int = 5

class SearchResponse(BaseModel):
    results: list

knowledge = create_knowledge_base()

@app.post("/search", response_model=SearchResponse)
async def search_knowledge(request: SearchRequest):
    """Endpoint for searching the knowledge base."""
    try:
        results = knowledge.search(request.query, limit=request.limit)
        return SearchResponse(results=[r.to_dict() for r in results])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)