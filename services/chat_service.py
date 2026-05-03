from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import create_agent

app = FastAPI(title="Agno LLM Wiki Chat Service")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

agent = create_agent()

@app.post("/chat", response_model=QueryResponse)
async def chat_endpoint(request: QueryRequest):
    """Endpoint for chatting with the agent."""
    try:
        response = agent.run(request.query)
        return QueryResponse(response=response.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)