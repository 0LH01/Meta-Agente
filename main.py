from fastapi import FastAPI, HTTPException
from models import AgentCreate, Agent
from services import criar_agente, listar_agentes

app = FastAPI(title="Agente Meta API", description="API para criar e gerenciar agentes de IA")

@app.post("/agentes/", response_model=Agent)
async def create_agent(agent: AgentCreate):
    try:
        return criar_agente(agent)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/agentes/", response_model=list[Agent])
async def get_agents():
    return listar_agentes()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
