from typing import List, Optional

import climsoft_api.api.instrument.schema as instrument_schema
import climsoft_api.api.obselement.schema as obselement_schema
import climsoft_api.api.obsscheduleclass.schema as obsscheduleclass_schema
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field

field_names = {
    "recordedFrom": "recorded_from",
    "describedBy": "described_by",
    "recordedWith": "recorded_with",
    "instrumentcode": "instrument_code",
    "scheduledFor": "scheduled_for",
    "beginDate": "begin_date",
    "endDate": "end_date",
}


class CreateStationElement(BaseSchema):
    recordedFrom: constr(max_length=255) = Field(title="Recorded From")
    describedBy: Optional[int] = Field(title="Described By")
    recordedWith: Optional[constr(max_length=255)] = Field(title="Recorded With")
    instrumentcode: Optional[constr(max_length=6)] = Field(title="Instrument Code")
    scheduledFor: Optional[constr(max_length=255)] = Field(title="Scheduled For")
    height: Optional[float] = Field(title="Height")
    beginDate: Optional[constr(max_length=50)] = Field(title="Begin Date")
    endDate: Optional[constr(max_length=255)] = Field(title="End Date")

    class Config:
        fields = field_names


class UpdateStationElement(BaseSchema):
    instrumentcode: Optional[constr(max_length=6)] = Field(title="Instrument Code")
    scheduledFor: Optional[constr(max_length=255)] = Field(title="Scheduled For")
    height: Optional[float] = Field(title="Height")
    endDate: Optional[constr(max_length=255)] = Field(title="End Date")

    class Config:
        fields = field_names


class StationElement(CreateStationElement):
    class Config:
        orm_mode = True
        fields = field_names
        allow_population_by_field_name = True


class StationElementResponse(Response):
    result: List[StationElement] = Field(title="Result")


class StationElementWithChildren(StationElement):
    obselement: Optional[obselement_schema.ObsElement] = Field(title="Obs Element")
    station: Optional[station_schema.Station] = Field(title="Station")
    instrument: Optional[instrument_schema.Instrument] = Field(title="Instrument")
    obsscheduleclas: Optional[obsscheduleclass_schema.ObsScheduleClass] = Field(title="Obs Schedule Class")

    class Config:
        orm_mode = True
        fields = {
            **field_names,
            "obselement": "obs_element",
            "obsscheduleclas": "obs_schedule_class",
        }
        allow_population_by_field_name = True


class StationElementWithStation(BaseSchema):
    describedBy: Optional[int] = Field(title="Described By")
    recordedWith: Optional[constr(max_length=255)] = Field(title="Recorded With")
    instrumentcode: Optional[constr(max_length=6)] = Field(title="Instrument Code")
    scheduledFor: Optional[constr(max_length=255)] = Field(title="Scheduled For")
    height: Optional[float] = Field(title="Height")
    beginDate: Optional[constr(max_length=50)] = Field(title="Begin Date")
    endDate: Optional[constr(max_length=255)] = Field(title="End Date")

    station: Optional[station_schema.Station] = Field(title="Station")

    class Config:
        orm_mode = True
        fields = {
            **field_names,
            "obselement": "obs_element",
            "obsscheduleclas": "obs_schedule_class",
            "station": "recorded_from"
        }
        allow_population_by_field_name = True


class StationElementWithChildrenResponse(Response):
    result: List[StationElementWithChildren] = Field(title="Result")


class StationElementWithStationQueryResponse(Response):
    status: str = Field("success", title="Status")
    result: List[StationElementWithStation] = Field(title="Result")
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")


class StationElementQueryResponse(StationElementResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
