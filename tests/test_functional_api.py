from fastapi.testclient import TestClient

from fornecedorlog.api import api


client = TestClient(api)


def test_create_fornecedor_via_api():
    response = client.post(
        "/fornecedors",
        json={
            "name": "Fornecedor B",
            "cidade": "NJ",
            "pagamento": 1,
            "image": 1,
            "limite": 2,
        },
    )
    assert response.status_code == 201
    result = response.json()
    assert result["name"] == "Fornecedor B"
    assert result["id"] == 1


def test_list_fornecedors():
    response = client.get("/fornecedors")
    assert response.status_code == 200
    result = response.json()
    assert len(result) == 0
