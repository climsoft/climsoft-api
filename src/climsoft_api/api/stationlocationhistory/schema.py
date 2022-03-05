import datetime
from typing import List
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


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

    class Config:
        fields = {
            "belongsTo": "belongs_to",
            "stationType": "station_type",
            "geolocation_method": "geolocationMethod",
            "openingDatetime": "opening_datetime",
            "closingDatetime": "closing_datetime",
            "adminRegion": "admin_region",
            "drainageBasin": "drainage_basin",
        }


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

    class Config:
        fields = {
            "stationType": "station_type",
            "geolocation_method": "geolocationMethod",
            "closingDatetime": "closing_datetime",
            "adminRegion": "admin_region",
            "drainageBasin": "drainage_basin",
        }


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
        fields = {
            "belongsTo": "belongs_to",
            "stationType": "station_type",
            "geolocation_method": "geolocationMethod",
            "openingDatetime": "opening_datetime",
            "closingDatetime": "closing_datetime",
            "adminRegion": "admin_region",
            "drainageBasin": "drainage_basin",
        }


class StationLocationHistoryWithStation(StationLocationHistory):
    station: station_schema.Station


class StationLocationHistoryResponse(Response):
    result: List[StationLocationHistory] = Field(title=_("Result"))


class StationLocationHistoryWithStationResponse(Response):
    result: List[StationLocationHistoryWithStation] = Field(title=_("Result"))


class StationLocationHistoryQueryResponse(StationLocationHistoryResponse):
    limit: int = Field(title=_("Limit"))
    page: int
    pages: int
