from typing import List

import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreateStationQualifier(BaseSchema):
    qualifier: constr(max_length=255) = Field(title="Qualifier")
    qualifierBeginDate: constr(max_length=50) = Field(title="Qualifier Begin Date")
    qualifierEndDate: constr(max_length=50) = Field(title="Qualifier End Date")
    belongsTo: constr(max_length=255) = Field(title="Belongs To")
    stationTimeZone: int = Field(title="Station Timezone")
    stationNetworkType: constr(max_length=255) = Field(title="Station Network Type")

    class Config:
        fields = {
            "qualifierBeginDate": "qualifier_begin_date",
            "qualifierEndDate": "qualifier_end_date",
            "belongsTo": "belongs_to",
            "stationTimeZone": "station_timezone",
            "stationNetworkType": "station_network_type",
        }


class UpdateStationQualifier(BaseSchema):
    stationTimeZone: int = Field(title="Station Timezone")
    stationNetworkType: constr(max_length=255) = Field(title="Station Network Type")

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
    result: List[StationQualifier] = Field(title="Result")


class StationQualifierWithStation(StationQualifier):
    station: station_schema.Station = Field(title="Station")


class StationQualifierWithStationResponse(Response):
    result: List[StationQualifierWithStation] = Field(title="Result")


class StationQualifierQueryResponse(StationQualifierResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
