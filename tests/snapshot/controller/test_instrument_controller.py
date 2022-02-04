# import pytest
# from fastapi.testclient import TestClient
# from opencdms.models.climsoft import v4_1_1_core as climsoft_models


# def test_should_return_first_five_instruments(client: TestClient, get_access_token: str):
#     response = client.get("/climsoft/v1/instruments", params={"limit": 5}, headers={
#         "Authorization": f"Bearer {get_access_token}"
#     })
#     assert response.status_code == 200
#     response_data = response.json()
#     assert len(response_data["result"]) == 5
#
#
# def test_should_return_single_instrument(client: TestClient, get_instrument: climsoft_models.Instrument,
#                                          get_access_token: str):
#     response = client.get(f"/climsoft/v1/instruments/{get_instrument.instrumentId}", headers={
#         "Authorization": f"Bearer {get_access_token}"
#     })
#     assert response.status_code == 200
#     response_data = response.json()
#     assert len(response_data["result"]) == 1
