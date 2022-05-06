from fastapi.testclient import TestClient
from fornecedorlog.api import api

client = TestClient(api)


def test_create_fornecedor_via_api():
    response = client.post(
        "/fornecedors",
        json={
            "name": "Skol",
            "style": "KornPA",
            "distance": 1,
            "limit": 1,
            "payment": 2,
        },
    )

    assert response.status_code == 201
    result = response.json()
    assert result["name"] == "Skol"
    assert result["id"] == 1
