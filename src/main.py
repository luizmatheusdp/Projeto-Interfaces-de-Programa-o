import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="API de Municípios do Ceará",
    description="API para consulta de dados públicos de municípios do Ceará.",
    version="0.1.0",
)


@app.get("/")
def inicio():
    return {
        "mensagem": "API de Municípios do Ceará",
        "status": "online"
    }


@app.get("/municipios/{codigo}")
def consultar_municipio(codigo: str):
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{codigo}"

    try:
        resposta = httpx.get(url, timeout=10)
    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Não foi possível consultar o serviço do IBGE."
        )

    if resposta.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="Município não encontrado."
        )

    if resposta.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail="O serviço do IBGE retornou um erro."
        )

    dados = resposta.json()

    return {
        "codigo": dados["id"],
        "nome": dados["nome"],
        "microrregiao": dados["microrregiao"]["mesorregiao"]["UF"]["sigla"]
    }
