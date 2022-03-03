from typing import List, Optional
from pydantic import constr
from climsoft_api.api.schema import BaseSchema, Response
import climsoft_api.api.station.schema as station_schema
import climsoft_api.api.instrument.schema as instrument_schema
import climsoft_api.api.obselement.schema as obselement_schema
import climsoft_api.api.obsscheduleclass.schema as obsscheduleclass_schema

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
    recordedFrom: constr(max_length=255)
    describedBy: Optional[int]
    recordedWith: Optional[constr(max_length=255)]
    instrumentcode: Optional[constr(max_length=6)]
    scheduledFor: Optional[constr(max_length=255)]
    height: Optional[float]
    beginDate: Optional[constr(max_length=50)]
    endDate: Optional[constr(max_length=255)]

    class Config:
        fields = field_names


class UpdateStationElement(BaseSchema):
    instrumentcode: Optional[constr(max_length=6)]
    scheduledFor: Optional[constr(max_length=255)]
    height: Optional[float]
    endDate: Optional[constr(max_length=255)]

    class Config:
        fields = field_names


class StationElement(CreateStationElement):
    class Config:
        orm_mode = True
        fields = field_names
        allow_population_by_field_name = True


class StationElementResponse(Response):
    result: List[StationElement]


class StationElementWithChildren(StationElement):
    obselement: Optional[obselement_schema.ObsElement]
    station: Optional[station_schema.Station]
    instrument: Optional[instrument_schema.Instrument]
    obsscheduleclas: Optional[obsscheduleclass_schema.ObsScheduleClass]

    class Config:
        orm_mode = True
        fields = {
            **field_names,
            "obselement": "obs_element",
            "obsscheduleclas": "obs_schedule_class",
        }
        allow_population_by_field_name = True


class StationElementWithStation(BaseSchema):
    describedBy: Optional[int]
    recordedWith: Optional[constr(max_length=255)]
    instrumentcode: Optional[constr(max_length=6)]
    scheduledFor: Optional[constr(max_length=255)]
    height: Optional[float]
    beginDate: Optional[constr(max_length=50)]
    endDate: Optional[constr(max_length=255)]

    station: Optional[station_schema.Station]

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
    result: List[StationElementWithChildren]


class StationElementWithStationQueryResponse(Response):
    status: str = "success"
    result: List[StationElementWithStation]
    limit: int
    page: int
    pages: int


class StationElementQueryResponse(StationElementResponse):
    limit: int
    page: int
    pages: int

