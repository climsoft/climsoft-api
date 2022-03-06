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
    recordedFrom: constr(max_length=255) = Field(title=_("Recorded From"))
    describedBy: Optional[int] = Field(title=_("Described By"))
    recordedWith: Optional[constr(max_length=255)] = Field(title=_("Recorded With"))
    instrumentcode: Optional[constr(max_length=6)] = Field(title=_("Instrument Code"))
    scheduledFor: Optional[constr(max_length=255)] = Field(title=_("Scheduled For"))
    height: Optional[float] = Field(title=_("Height"))
    beginDate: Optional[constr(max_length=50)] = Field(title=_("Begin Date"))
    endDate: Optional[constr(max_length=255)] = Field(title=_("End Date"))

    class Config:
        fields = field_names


class UpdateStationElement(BaseSchema):
    instrumentcode: Optional[constr(max_length=6)] = Field(title=_("Instrument Code"))
    scheduledFor: Optional[constr(max_length=255)] = Field(title=_("Scheduled For"))
    height: Optional[float] = Field(title=_("Height"))
    endDate: Optional[constr(max_length=255)] = Field(title=_("End Date"))

    class Config:
        fields = field_names


class StationElement(CreateStationElement):
    class Config:
        orm_mode = True
        fields = field_names
        allow_population_by_field_name = True


class StationElementResponse(Response):
    result: List[StationElement] = Field(title=_("Result"))


class StationElementWithChildren(StationElement):
    obselement: Optional[obselement_schema.ObsElement] = Field(title=_("Obs Element"))
    station: Optional[station_schema.Station] = Field(title=_("Station"))
    instrument: Optional[instrument_schema.Instrument] = Field(title=_("Instrument"))
    obsscheduleclas: Optional[obsscheduleclass_schema.ObsScheduleClass] = Field(title=_("Obs Schedule Class"))

    class Config:
        orm_mode = True
        fields = {
            **field_names,
            "obselement": "obs_element",
            "obsscheduleclas": "obs_schedule_class",
        }
        allow_population_by_field_name = True


class StationElementWithStation(BaseSchema):
    describedBy: Optional[int] = Field(title=_("Described By"))
    recordedWith: Optional[constr(max_length=255)] = Field(title=_("Recorded With"))
    instrumentcode: Optional[constr(max_length=6)] = Field(title=_("Instrument Code"))
    scheduledFor: Optional[constr(max_length=255)] = Field(title=_("Scheduled For"))
    height: Optional[float] = Field(title=_("Height"))
    beginDate: Optional[constr(max_length=50)] = Field(title=_("Begin Date"))
    endDate: Optional[constr(max_length=255)] = Field(title=_("End Date"))

    station: Optional[station_schema.Station] = Field(title=_("Station"))

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
    result: List[StationElementWithChildren] = Field(title=_("Result"))


class StationElementWithStationQueryResponse(Response):
    status: str = Field("success", title=_("Status"))
    result: List[StationElementWithStation] = Field(title=_("Result"))
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))


class StationElementQueryResponse(StationElementResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
