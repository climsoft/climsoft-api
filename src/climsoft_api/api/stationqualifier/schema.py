from pydantic import constr
from typing import List
from climsoft_api.api.schema import BaseSchema, Response
import climsoft_api.api.station.schema as station_schema


class CreateStationQualifier(BaseSchema):
    qualifier: constr(max_length=255)
    qualifierBeginDate: constr(max_length=50)
    qualifierEndDate: constr(max_length=50)
    belongsTo: constr(max_length=255)
    stationTimeZone: int
    stationNetworkType: constr(max_length=255)


class UpdateStationQualifier(BaseSchema):
    stationTimeZone: int
    stationNetworkType: constr(max_length=255)


class StationQualifier(CreateStationQualifier):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class StationQualifierResponse(Response):
    result: List[StationQualifier]


class StationQualifierWithStation(StationQualifier):
    station: station_schema.Station


class StationQualifierWithStationResponse(Response):
    result: List[StationQualifierWithStation]
