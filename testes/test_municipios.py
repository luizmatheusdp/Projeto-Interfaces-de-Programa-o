from unittest.mock import patch

from fastapi.testclient import TestClient
  
from src.main import app

client = TestClient(app)

DADOS_FORTALEZA = {
    "id": 2304400,
    "nome": "Fortaleza",
    "microrregiao": {
        "id": 23016,
        "nome": "Fortaleza",
        "mesorregiao": {
            "id": 2303,
            "nome": "Metropolitana de Fortaleza",
            "UF": {
                "id": 23,
                "sigla": "CE",
                "nome": "Ceará",
                "regiao": {"id": 2, "sigla": "NE", "nome": "Nordeste"}
            }
        }
    },
    "regiao-imediata": {
        "id": 230001,
        "nome": "Fortaleza",
        "regiao-intermediaria": {
            "id": 2301,
            "nome": "Fortaleza",
            "UF": {
                "id": 23,
                "sigla": "CE",
                "nome": "Ceará",
                "regiao": {"id": 2, "sigla": "NE", "nome": "Nordeste"}
            }
        }
    },
}


def test_fortaleza_devolve_200():
    with patch("src.main.httpx.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = DADOS_FORTALEZA

        resposta = client.get("/municipios/2304400")

    assert resposta.status_code == 200


def test_codigo_invalido_devolve_404():
    for codigo in ("9999999", "abc"):
        with patch("src.main.httpx.get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = []

            resposta = client.get(f"/municipios/{codigo}")

        assert resposta.status_code == 404


DADOS_RIO = {
    "id": 3304557,
    "nome": "Rio de Janeiro",
    "microrregiao": {
        "id": 33017,
        "nome": "Rio de Janeiro",
        "mesorregiao": {
            "id": 3306,
            "nome": "Metropolitana do Rio de Janeiro",
            "UF": {
                "id": 33,
                "sigla": "RJ",
                "nome": "Rio de Janeiro",
                "regiao": {"id": 3, "sigla": "SE", "nome": "Sudeste"}
            }
        }
    },
    "regiao-imediata": {
        "id": 330001,
        "nome": "Rio de Janeiro",
        "regiao-intermediaria": {
            "id": 3301,
            "nome": "Rio de Janeiro",
            "UF": {
                "id": 33,
                "sigla": "RJ",
                "nome": "Rio de Janeiro",
                "regiao": {"id": 3, "sigla": "SE", "nome": "Sudeste"}
            }
        }
    },
}


def test_codigo_fora_do_ce_devolve_404():
    with patch("src.main.httpx.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = DADOS_RIO

        resposta = client.get("/municipios/3304557")

    assert resposta.status_code == 404
