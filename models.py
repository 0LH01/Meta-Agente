from pydantic import BaseModel
from typing import Optional, List

class AgentCreate(BaseModel):
    tipo: str  # ex: "GPTMaker", "Lindy", "Botpress"
    nome: str
    descricao: Optional[str] = None
    params: Optional[dict] = {}  # Parâmetros extras, como API keys ou configs

class Agent(BaseModel):
    id: int
    tipo: str
    nome: str
    status: str = "criado"  # Pode ser "criado", "ativo", "erro"
    descricao: Optional[str] = None
