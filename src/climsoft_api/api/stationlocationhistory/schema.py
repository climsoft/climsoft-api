import datetime
from typing import List, Optional
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreateStationLocationHistory(BaseSchema):
    belongsTo: constr(max_length=255) = Field(title="Belongs To")
    openingDatetime: str = Field(title="Opening Datetime")
    stationType: constr(max_length=255) = Field(title="Station Type")
    geoLocationMethod: constr(max_length=255) = Field(title="Geolocation Method")
    geoLocationAccuracy: float = Field(title="Geolocation Accuracy")
    closingDatetime: str = Field(title="Closing Datetime")
    latitude: float = Field(title="Latitude")
    longitude: float = Field(title="Longitude")
    elevation: int = Field(title="Elevation")
    authority: constr(max_length=255) = Field(title="Authority")
    adminRegion: constr(max_length=255) = Field(title="Admin Region")
    drainageBasin: constr(max_length=255) = Field(title="Drainage Basin")

    class Config:
        fields = {
            "belongsTo": "belongs_to",
            "stationType": "station_type",
            "geolocationMethod": "geolocation_method",
            "openingDatetime": "opening_datetime",
            "closingDatetime": "closing_datetime",
            "adminRegion": "admin_region",
            "drainageBasin": "drainage_basin",
        }


class UpdateStationLocationHistory(BaseSchema):
    stationType: constr(max_length=255) = Field(title="Station Type")
    geoLocationMethod: constr(max_length=255) = Field(title="Geolocation Method")
    geoLocationAccuracy: float = Field(title="Geolocation Accuracy")
    closingDatetime: str = Field(title="Closing Datetime")
    latitude: float = Field(title="Latitude")
    longitude: float = Field(title="Longitude")
    elevation: int = Field(title="Elevation")
    authority: constr(max_length=255) = Field(title="Authority")
    adminRegion: constr(max_length=255) = Field(title="Admin Region")
    drainageBasin: constr(max_length=255) = Field(title="Drainage Basin")

    class Config:
        fields = {
            "stationType": "station_type",
            "geolocationMethod": "geolocation_method",
            "closingDatetime": "closing_datetime",
            "adminRegion": "admin_region",
            "drainageBasin": "drainage_basin",
        }


class StationLocationHistory(BaseSchema):
    belongsTo: Optional[constr(max_length=255)] = Field(title="Belongs To")
    openingDatetime: Optional[datetime.datetime] = Field(title="Opening Datetime")
    stationType: Optional[constr(max_length=255)] = Field(title="Station Type")
    geoLocationMethod: Optional[constr(max_length=255)] = Field(title="Geolocation Method")
    geoLocationAccuracy: Optional[float] = Field(title="Geolocation History")
    closingDatetime: Optional[datetime.datetime] = Field(title="Closing Datetime")
    latitude: Optional[float] = Field(title="Latitude")
    longitude: Optional[float] = Field(title="Longitude")
    elevation: Optional[int] = Field(title="Elevation")
    authority: Optional[constr(max_length=255)] = Field(title="Authority")
    adminRegion: Optional[constr(max_length=255)] = Field(title="Admin Region")
    drainageBasin: Optional[constr(max_length=255)] = Field(title="Drainage Basin")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "belongsTo": "belongs_to",
            "stationType": "station_type",
            "geolocationMethod": "geolocation_method",
            "geolocationAccuracy": "geolocation_accuracy",
            "openingDatetime": "opening_datetime",
            "closingDatetime": "closing_datetime",
            "adminRegion": "admin_region",
            "drainageBasin": "drainage_basin",
        }
        json_encoders = {
            datetime.datetime: lambda dt: str(dt).replace("T", " ")
        }


class StationLocationHistoryWithStation(StationLocationHistory):
    station: station_schema.Station = Field(title="Code")


class StationLocationHistoryResponse(Response):
    result: List[StationLocationHistory] = Field(title="Result")


class StationLocationHistoryWithStationResponse(Response):
    result: List[StationLocationHistoryWithStation] = Field(title="Result")


class StationLocationHistoryQueryResponse(StationLocationHistoryResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
