from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo para receber a requisição
class DescricaoRequest(BaseModel):
    descricao: str

# Função para analisar a descrição e mapear PDM/Base de Dados
def identificar_pdm_base(descricao: str):
    descricao = descricao.lower()

    # Regras básicas de identificação
    if "vendas" in descricao:
        return "Relatório de Vendas", "BD_Vendas_2024"
    elif "clientes" in descricao:
        return "Cadastro de Clientes", "BD_Clientes"
    elif "financeiro" in descricao:
        return "Relatório Financeiro", "BD_Financeiro"
    else:
        return "Não identificado", "Desconhecida"

# Endpoint para processar a descrição
@app.post("/api/analisar-descricao")
async def analisar_descricao(dados: DescricaoRequest):
    pdm, base_de_dados = identificar_pdm_base(dados.descricao)

    return {
        "pdm": pdm,
        "base_de_dados": base_de_dados
    }
