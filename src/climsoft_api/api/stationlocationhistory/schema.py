import datetime

from pydantic import constr
from typing import List
from climsoft_api.api.schema import BaseSchema, Response
import climsoft_api.api.station.schema as station_schema


class CreateStationLocationHistory(BaseSchema):
    belongsTo: constr(max_length=255)
    openingDatetime: str
    stationType: constr(max_length=255)
    geoLocationMethod: constr(max_length=255)
    geoLocationAccuracy: float
    closingDatetime: str
    latitude: float
    longitude: float
    elevation: int
    authority: constr(max_length=255)
    adminRegion: constr(max_length=255)
    drainageBasin: constr(max_length=255)


class UpdateStationLocationHistory(BaseSchema):
    stationType: constr(max_length=255)
    geoLocationMethod: constr(max_length=255)
    geoLocationAccuracy: float
    closingDatetime: str
    latitude: float
    longitude: float
    elevation: int
    authority: constr(max_length=255)
    adminRegion: constr(max_length=255)
    drainageBasin: constr(max_length=255)


class StationLocationHistory(BaseSchema):
    belongsTo: constr(max_length=255)
    openingDatetime: datetime.datetime
    stationType: constr(max_length=255)
    geoLocationMethod: constr(max_length=255)
    geoLocationAccuracy: float
    closingDatetime: datetime.datetime
    latitude: float
    longitude: float
    elevation: int
    authority: constr(max_length=255)
    adminRegion: constr(max_length=255)
    drainageBasin: constr(max_length=255)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class StationLocationHistoryWithStation(StationLocationHistory):
    station: station_schema.Station


class StationLocationHistoryResponse(Response):
    result: List[StationLocationHistory]


class StationLocationHistoryWithStationResponse(Response):
    result: List[StationLocationHistoryWithStation]
