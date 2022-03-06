from typing import List, Optional

from climsoft_api.api.schema import BaseSchema
from pydantic import constr, Field


class CreateStation(BaseSchema):
    stationId: constr(max_length=255) = Field(title=_("Station ID"))
    stationName: constr(max_length=255) = Field(title=_("Station Name"))
    wmoid: Optional[constr(max_length=20)] = Field(title=_("Wmo ID"))
    icaoid: Optional[constr(max_length=20)] = Field(title=_("Icao ID"))
    latitude: float = Field(title=_("Latitude"))
    qualifier: Optional[constr(max_length=20)] = Field(title=_("Qualifier"))
    longitude: float = Field(title=_("Longitude"))
    elevation: constr(max_length=255) = Field(title=_("Elevation"))
    geoLocationMethod: Optional[constr(max_length=255)] = Field(title=_("Geolocation Method"))
    geoLocationAccuracy: Optional[float] = Field(title=_("Geolocation Accuracy"))
    openingDatetime: Optional[str] = Field(title=_("Opening Datetime"))
    closingDatetime: str = Field(title=_("Closing Datetime"))
    country: constr(max_length=50) = Field(title=_("Country"))
    authority: Optional[constr(max_length=255)] = Field(title=_("Authority"))
    adminRegion: Optional[constr(max_length=255)] = Field(title=_("Admin Region"))
    drainageBasin: Optional[constr(max_length=255)] = Field(title=_("Drainage Basin"))
    wacaSelection: bool = Field(title=_("Waca Selection"))
    cptSelection: bool = Field(title=_("Cpt Selection"))
    stationOperational: bool = Field(title=_("Station Operational"))

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
    stationName: constr(max_length=255) = Field(title=_("Station Name"))
    wmoid: Optional[constr(max_length=20)] = Field(title=_("Wmo ID"))
    icaoid: Optional[constr(max_length=20)] = Field(title=_("Icao ID"))
    latitude: float = Field(title=_("Latitude"))
    qualifier: Optional[constr(max_length=20)] = Field(title=_("Qualifier"))
    longitude: float = Field(title=_("Longitude"))
    elevation: constr(max_length=255) = Field(title=_("Elevation"))
    geoLocationMethod: Optional[constr(max_length=255)] = Field(title=_("Geolocation Method"))
    geoLocationAccuracy: Optional[float] = Field(title=_("Geolocation Accuracy"))
    openingDatetime: Optional[str] = Field(title=_("Opening Datetime"))
    closingDatetime: str = Field(title=_("Closing Datetime"))
    country: constr(max_length=50) = Field(title=_("Country"))
    authority: Optional[constr(max_length=255)] = Field(title=_("Authority"))
    adminRegion: Optional[constr(max_length=255)] = Field(title=_("Admin Region"))
    drainageBasin: Optional[constr(max_length=255)] = Field(title=_("Drainage Basin"))
    wacaSelection: bool = Field(title=_("Waca Selection"))
    cptSelection: bool = Field(title=_("Cpt Selection"))
    stationOperational: bool = Field(title=_("Station Operational"))

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
    openingDatetime: Optional[str] = Field(title=_("Opening Datetime"))
    closingDatetime: str = Field(title=_("Closing Datetime"))

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
    result: List[Station] = Field(title=_("Result"))
    message: str = Field(title=_("Message"))
    status: str = Field(title=_("Status"))


class StationQueryResponse(StationResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
