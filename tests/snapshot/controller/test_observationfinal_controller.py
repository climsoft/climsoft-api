from faker import Faker
from fastapi.testclient import TestClient


def test_should_return_first_five_observation_finals(client: TestClient):
    response = client.get("/climsoft/v1/observation-finals", params={"limit": 5})
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_observation_final(client: TestClient):
    response = client.get(
        f"/climsoft/v1/observation-finals/67774010/4/2000-01-19 06:00:00")
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
