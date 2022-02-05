from fastapi.testclient import TestClient


# def test_should_return_first_five_observation_initials(client: TestClient, get_access_token: str):
#     response = client.get("/climsoft/v1/observation-initials", params={"limit": 5}, headers={
#         "Authorization": f"Bearer {get_access_token}"
#     })
#     assert response.status_code == 200
#     response_data = response.json()
#     assert len(response_data["result"]) == 5
#
#
# def test_should_return_single_observation_initial(client: TestClient,
#                                                   get_observation_initial: climsoft_models.Observationinitial,
#                                                   get_access_token: str):
#     response = client.get(
#         f"/climsoft/v1/observation-initials/{get_observation_initial.recordedFrom}/{get_observation_initial.describedBy}/{get_observation_initial.obsDatetime}/{get_observation_initial.qcStatus}/{get_observation_initial.acquisitionType}",
#         headers={
#             "Authorization": f"Bearer {get_access_token}"
#         })
#     assert response.status_code == 200
#     response_data = response.json()
#     print(response_data)
#     assert len(response_data["result"]) == 1
