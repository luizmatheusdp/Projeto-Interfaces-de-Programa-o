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
