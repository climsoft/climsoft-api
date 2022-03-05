from typing import List

import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr


class CreateStationQualifier(BaseSchema):
    qualifier: constr(max_length=255)
    qualifierBeginDate: constr(max_length=50)
    qualifierEndDate: constr(max_length=50)
    belongsTo: constr(max_length=255)
    stationTimeZone: int
    stationNetworkType: constr(max_length=255)

    class Config:
        fields = {
            "qualifierBeginDate": "qualifier_begin_date",
            "qualifierEndDate": "qualifier_end_date",
            "belongsTo": "belongs_to",
            "stationTimeZone": "station_timezone",
            "stationNetworkType": "station_network_type",
        }


class UpdateStationQualifier(BaseSchema):
    stationTimeZone: int
    stationNetworkType: constr(max_length=255)

    class Config:
        fields = {
            "stationTimeZone": "station_timezone",
            "stationNetworkType": "station_network_type",
        }


class StationQualifier(CreateStationQualifier):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "qualifierBeginDate": "qualifier_begin_date",
            "qualifierEndDate": "qualifier_end_date",
            "belongsTo": "belongs_to",
            "stationTimeZone": "station_timezone",
            "stationNetworkType": "station_network_type",
        }


class StationQualifierResponse(Response):
    result: List[StationQualifier]


class StationQualifierWithStation(StationQualifier):
    station: station_schema.Station


class StationQualifierWithStationResponse(Response):
    result: List[StationQualifierWithStation]


class StationQualifierQueryResponse(StationQualifierResponse):
    limit: int
    page: int
    pages: int
