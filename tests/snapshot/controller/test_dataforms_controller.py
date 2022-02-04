from fastapi.testclient import TestClient


def test_should_return_first_five_data_forms(client: TestClient):
    response = client.get("/v1/data-forms", params={"limit": 5})
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_data_form(
        client: TestClient,
):
    response = client.get(f"/v1/data-forms/form_agro1")

    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
