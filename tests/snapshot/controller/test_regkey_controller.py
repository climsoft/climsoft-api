from fastapi.testclient import TestClient


def test_should_return_first_five_obselements(client: TestClient):
    response = client.get("/climsoft/v1/reg-keys", params={"limit": 5})
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_station(client: TestClient):
    response = client.get(f"/climsoft/v1/reg-keys/key00")

    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
