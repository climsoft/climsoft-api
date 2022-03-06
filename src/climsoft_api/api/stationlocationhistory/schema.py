import datetime
from typing import List
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreateStationLocationHistory(BaseSchema):
    belongsTo: constr(max_length=255) = Field(title=_("Belongs To"))
    openingDatetime: str = Field(title=_("Opening Datetime"))
    stationType: constr(max_length=255) = Field(title=_("Station Type"))
    geoLocationMethod: constr(max_length=255) = Field(title=_("Geolocation Method"))
    geoLocationAccuracy: float = Field(title=_("Geolocation Accuracy"))
    closingDatetime: str = Field(title=_("Closing Datetime"))
    latitude: float = Field(title=_("Latitude"))
    longitude: float = Field(title=_("Longitude"))
    elevation: int = Field(title=_("Elevation"))
    authority: constr(max_length=255) = Field(title=_("Authority"))
    adminRegion: constr(max_length=255) = Field(title=_("Admin Region"))
    drainageBasin: constr(max_length=255) = Field(title=_("Drainage Basin"))

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
    stationType: constr(max_length=255) = Field(title=_("Station Type"))
    geoLocationMethod: constr(max_length=255) = Field(title=_("Geolocation Method"))
    geoLocationAccuracy: float = Field(title=_("Geolocation Accuracy"))
    closingDatetime: str = Field(title=_("Closing Datetime"))
    latitude: float = Field(title=_("Latitude"))
    longitude: float = Field(title=_("Longitude"))
    elevation: int = Field(title=_("Elevation"))
    authority: constr(max_length=255) = Field(title=_("Authority"))
    adminRegion: constr(max_length=255) = Field(title=_("Admin Region"))
    drainageBasin: constr(max_length=255) = Field(title=_("Drainage Basin"))

    class Config:
        fields = {
            "stationType": "station_type",
            "geolocation_method": "geolocationMethod",
            "closingDatetime": "closing_datetime",
            "adminRegion": "admin_region",
            "drainageBasin": "drainage_basin",
        }


class StationLocationHistory(BaseSchema):
    belongsTo: constr(max_length=255) = Field(title=_("Belongs To"))
    openingDatetime: datetime.datetime = Field(title=_("Opening Datetime"))
    stationType: constr(max_length=255) = Field(title=_("Station Type"))
    geoLocationMethod: constr(max_length=255) = Field(title=_("Geolocation Method"))
    geoLocationAccuracy: float = Field(title=_("Geolocation History"))
    closingDatetime: datetime.datetime = Field(title=_("Closing Datetime"))
    latitude: float = Field(title=_("Latitude"))
    longitude: float = Field(title=_("Longitude"))
    elevation: int = Field(title=_("Elevation"))
    authority: constr(max_length=255) = Field(title=_("Authority"))
    adminRegion: constr(max_length=255) = Field(title=_("Admin Region"))
    drainageBasin: constr(max_length=255) = Field(title=_("Drainage Basin"))

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
    station: station_schema.Station = Field(title=_("Code"))


class StationLocationHistoryResponse(Response):
    result: List[StationLocationHistory] = Field(title=_("Result"))


class StationLocationHistoryWithStationResponse(Response):
    result: List[StationLocationHistoryWithStation] = Field(title=_("Result"))


class StationLocationHistoryQueryResponse(StationLocationHistoryResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
