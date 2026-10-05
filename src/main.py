from fastapi import FastAPI

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
    return {
        "codigo": codigo,
        "mensagem": "Consulta de município"
    }
