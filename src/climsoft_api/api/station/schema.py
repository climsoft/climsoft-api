from typing import List, Optional

from climsoft_api.api.schema import BaseSchema
from pydantic import constr, Field


class CreateStation(BaseSchema):
    stationId: constr(max_length=255) = Field(title="Station ID")
    stationName: constr(max_length=255) = Field(title="Station Name")
    wmoid: Optional[constr(max_length=20)] = Field(title="Wmo ID")
    icaoid: Optional[constr(max_length=20)] = Field(title="Icao ID")
    latitude: float = Field(title="Latitude")
    qualifier: Optional[constr(max_length=20)] = Field(title="Qualifier")
    longitude: float = Field(title="Longitude")
    elevation: constr(max_length=255) = Field(title="Elevation")
    geoLocationMethod: Optional[constr(max_length=255)] = Field(title="Geolocation Method")
    geoLocationAccuracy: Optional[float] = Field(title="Geolocation Accuracy")
    openingDatetime: Optional[str] = Field(title="Opening Datetime")
    closingDatetime: str = Field(title="Closing Datetime")
    country: constr(max_length=50) = Field(title="Country")
    authority: Optional[constr(max_length=255)] = Field(title="Authority")
    adminRegion: Optional[constr(max_length=255)] = Field(title="Admin Region")
    drainageBasin: Optional[constr(max_length=255)] = Field(title="Drainage Basin")
    wacaSelection: bool = Field(title="Waca Selection")
    cptSelection: bool = Field(title="Cpt Selection")
    stationOperational: bool = Field(title="Station Operational")

    class Config:
        fields = {
            "stationId": "station_id",
            "stationName": "station_name",
            "geoLocationMethod": "geolocation_method",
            "geoLocationAccuracy": "geolocation_accuracy",
            "openingDatetime": "opening_datetime",
            "closingDatetime": "closing_datetime",
            "adminRegion": "admin_region",
            "drainageBasin": "drainage_basin",
            "wacaSelection": "waca_selection",
            "cptSelection": "cpt_selection",
            "stationOperational": "station_operational"
        }


class UpdateStation(BaseSchema):
    stationName: constr(max_length=255) = Field(title="Station Name")
    wmoid: Optional[constr(max_length=20)] = Field(title="Wmo ID")
    icaoid: Optional[constr(max_length=20)] = Field(title="Icao ID")
    latitude: float = Field(title="Latitude")
    qualifier: Optional[constr(max_length=20)] = Field(title="Qualifier")
    longitude: float = Field(title="Longitude")
    elevation: constr(max_length=255) = Field(title="Elevation")
    geoLocationMethod: Optional[constr(max_length=255)] = Field(title="Geolocation Method")
    geoLocationAccuracy: Optional[float] = Field(title="Geolocation Accuracy")
    openingDatetime: Optional[str] = Field(title="Opening Datetime")
    closingDatetime: str = Field(title="Closing Datetime")
    country: constr(max_length=50) = Field(title="Country")
    authority: Optional[constr(max_length=255)] = Field(title="Authority")
    adminRegion: Optional[constr(max_length=255)] = Field(title="Admin Region")
    drainageBasin: Optional[constr(max_length=255)] = Field(title="Drainage Basin")
    wacaSelection: bool = Field(title="Waca Selection")
    cptSelection: bool = Field(title="Cpt Selection")
    stationOperational: bool = Field(title="Station Operational")

    class Config:
        fields = {
            "stationId": "station_id",
            "stationName": "station_name",
            "geoLocationMethod": "geolocation_method",
            "geoLocationAccuracy": "geolocation_accuracy",
            "openingDatetime": "opening_datetime",
            "closingDatetime": "closing_datetime",
            "adminRegion": "admin_region",
            "drainageBasin": "drainage_basin",
            "wacaSelection": "waca_selection",
            "cptSelection": "cpt_selection",
            "stationOperational": "station_operational"
        }


class Station(CreateStation):
    openingDatetime: Optional[str] = Field(title="Opening Datetime")
    closingDatetime: str = Field(title="Closing Datetime")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "stationId": "station_id",
            "stationName": "station_name",
            "geoLocationMethod": "geolocation_method",
            "geoLocationAccuracy": "geolocation_accuracy",
            "openingDatetime": "opening_datetime",
            "closingDatetime": "closing_datetime",
            "adminRegion": "admin_region",
            "drainageBasin": "drainage_basin",
            "wacaSelection": "waca_selection",
            "cptSelection": "cpt_selection",
            "stationOperational": "station_operational"
        }


class StationResponse(BaseSchema):
    result: List[Station] = Field(title="Result")
    message: str = Field(title="Message")
    status: str = Field(title="Status")


class StationQueryResponse(StationResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
