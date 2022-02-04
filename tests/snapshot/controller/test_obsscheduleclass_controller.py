from fastapi.testclient import TestClient


# def test_should_return_first_five_obs_schedule_classs(client: TestClient, get_access_token: str):
#     response = client.get("/climsoft/v1/obs-schedule-class", params={"limit": 5}, headers={
#         "Authorization": f"Bearer {get_access_token}"
#     })
#     assert response.status_code == 200
#     response_data = response.json()
#     assert len(response_data["result"]) == 5

#
# def test_should_return_single_obs_schedule_class(client: TestClient,
#                                                  get_obs_schedule_class: climsoft_models.Obsscheduleclas,
#                                                  get_access_token: str):
#     response = client.get(f"/climsoft/v1/obs-schedule-class/{get_obs_schedule_class.scheduleClass}", headers={
#         "Authorization": f"Bearer {get_access_token}"
#     })
#     assert response.status_code == 200
#     response_data = response.json()
#     assert len(response_data["result"]) == 1
