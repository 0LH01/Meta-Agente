import requests
from models import AgentCreate, Agent

agentes_criados = []  # Banco simples em memória (substitua por DB como SQLite ou MongoDB depois)
next_id = 1

def criar_agente(agent_data: AgentCreate) -> Agent:
    global next_id
    # Simulação de criação - aqui você chama APIs reais
    if agent_data.tipo == "GPTMaker":
        # Exemplo: Chame API do GPTMaker (substitua com endpoint real)
        response = requests.post("https://gptmaker.ai/api/create", json=agent_data.params)
        if response.status_code != 200:
            raise ValueError("Erro ao criar no GPTMaker")
    elif agent_data.tipo == "Lindy":
        # Similar para Lindy.ai
        response = requests.post("https://www.lindy.ai/api/agents/create", json=agent_data.params)
        # ... verifique resposta
    # Adicione mais tipos conforme os agentes que listei antes

    novo_agente = Agent(id=next_id, tipo=agent_data.tipo, nome=agent_data.nome, descricao=agent_data.descricao)
    agentes_criados.append(novo_agente)
    next_id += 1
    return novo_agente

def listar_agentes() -> List[Agent]:
    return agentes_criados
