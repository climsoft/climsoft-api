from fastapi.testclient import TestClient
#
#
# def test_should_return_first_five_station_elements(client: TestClient, get_access_token: str):
#     response = client.get("/climsoft/v1/station-elements", params={"limit": 5}, headers={
#         "Authorization": f"Bearer {get_access_token}"
#     })
#     assert response.status_code == 200
#     response_data = response.json()
#     assert len(response_data["result"]) == 5
#
#
# def test_should_return_single_station_element(client: TestClient, get_access_token: str):
#     response = client.get(f"/climsoft/v1/station-elements/{get_station_element.recordedFrom}/
#     {get_station_element.describedBy}/{get_station_element.recordedWith}/{get_station_element.beginDate}", headers={
#         "Authorization": f"Bearer {get_access_token}"
#     })
#     assert response.status_code == 200
#     response_data = response.json()
#     assert len(response_data["result"]) == 1
#
#
