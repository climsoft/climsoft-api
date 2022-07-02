import datetime
from climsoft_api.api.schema import Response
from pydantic import BaseModel, constr, Field
from typing import Optional, List


field_mapping = {
    "stationId": "station_id",
    "elementId": "element_id",
    "entryDatetime": "entry_datetime"
}


class CreateFormHourly(BaseModel):
    stationId: constr(max_length=50)
    elementId: int
    yyyy: int
    mm: int
    dd: int
    hh_00: Optional[constr(max_length=50)]
    hh_01: Optional[constr(max_length=50)]
    hh_02: Optional[constr(max_length=50)]
    hh_03: Optional[constr(max_length=50)]
    hh_04: Optional[constr(max_length=50)]
    hh_05: Optional[constr(max_length=50)]
    hh_06: Optional[constr(max_length=50)]
    hh_07: Optional[constr(max_length=50)]
    hh_08: Optional[constr(max_length=50)]
    hh_09: Optional[constr(max_length=50)]
    hh_10: Optional[constr(max_length=50)]
    hh_11: Optional[constr(max_length=50)]
    hh_12: Optional[constr(max_length=50)]
    hh_13: Optional[constr(max_length=50)]
    hh_14: Optional[constr(max_length=50)]
    hh_15: Optional[constr(max_length=50)]
    hh_16: Optional[constr(max_length=50)]
    hh_17: Optional[constr(max_length=50)]
    hh_18: Optional[constr(max_length=50)]
    hh_19: Optional[constr(max_length=50)]
    hh_20: Optional[constr(max_length=50)]
    hh_21: Optional[constr(max_length=50)]
    hh_22: Optional[constr(max_length=50)]
    hh_23: Optional[constr(max_length=50)]
    flag00: Optional[constr(max_length=50)]
    flag01: Optional[constr(max_length=50)]
    flag02: Optional[constr(max_length=50)]
    flag03: Optional[constr(max_length=50)]
    flag04: Optional[constr(max_length=50)]
    flag05: Optional[constr(max_length=50)]
    flag06: Optional[constr(max_length=50)]
    flag07: Optional[constr(max_length=50)]
    flag08: Optional[constr(max_length=50)]
    flag09: Optional[constr(max_length=50)]
    flag10: Optional[constr(max_length=50)]
    flag11: Optional[constr(max_length=50)]
    flag12: Optional[constr(max_length=50)]
    flag13: Optional[constr(max_length=50)]
    flag14: Optional[constr(max_length=50)]
    flag15: Optional[constr(max_length=50)]
    flag16: Optional[constr(max_length=50)]
    flag17: Optional[constr(max_length=50)]
    flag18: Optional[constr(max_length=50)]
    flag19: Optional[constr(max_length=50)]
    flag20: Optional[constr(max_length=50)]
    flag21: Optional[constr(max_length=50)]
    flag22: Optional[constr(max_length=50)]
    flag23: Optional[constr(max_length=50)]
    total: Optional[constr(max_length=50)]
    signature: Optional[constr(max_length=50)]
    entryDatetime: Optional[datetime.datetime]

    class Config:
        orm_mode = False
        allow_population_by_field_name = True
        fields = field_mapping


class UpdateFormHourly(BaseModel):
    hh_00: Optional[constr(max_length=50)]
    hh_01: Optional[constr(max_length=50)]
    hh_02: Optional[constr(max_length=50)]
    hh_03: Optional[constr(max_length=50)]
    hh_04: Optional[constr(max_length=50)]
    hh_05: Optional[constr(max_length=50)]
    hh_06: Optional[constr(max_length=50)]
    hh_07: Optional[constr(max_length=50)]
    hh_08: Optional[constr(max_length=50)]
    hh_09: Optional[constr(max_length=50)]
    hh_10: Optional[constr(max_length=50)]
    hh_11: Optional[constr(max_length=50)]
    hh_12: Optional[constr(max_length=50)]
    hh_13: Optional[constr(max_length=50)]
    hh_14: Optional[constr(max_length=50)]
    hh_15: Optional[constr(max_length=50)]
    hh_16: Optional[constr(max_length=50)]
    hh_17: Optional[constr(max_length=50)]
    hh_18: Optional[constr(max_length=50)]
    hh_19: Optional[constr(max_length=50)]
    hh_20: Optional[constr(max_length=50)]
    hh_21: Optional[constr(max_length=50)]
    hh_22: Optional[constr(max_length=50)]
    hh_23: Optional[constr(max_length=50)]
    flag00: Optional[constr(max_length=50)]
    flag01: Optional[constr(max_length=50)]
    flag02: Optional[constr(max_length=50)]
    flag03: Optional[constr(max_length=50)]
    flag04: Optional[constr(max_length=50)]
    flag05: Optional[constr(max_length=50)]
    flag06: Optional[constr(max_length=50)]
    flag07: Optional[constr(max_length=50)]
    flag08: Optional[constr(max_length=50)]
    flag09: Optional[constr(max_length=50)]
    flag10: Optional[constr(max_length=50)]
    flag11: Optional[constr(max_length=50)]
    flag12: Optional[constr(max_length=50)]
    flag13: Optional[constr(max_length=50)]
    flag14: Optional[constr(max_length=50)]
    flag15: Optional[constr(max_length=50)]
    flag16: Optional[constr(max_length=50)]
    flag17: Optional[constr(max_length=50)]
    flag18: Optional[constr(max_length=50)]
    flag19: Optional[constr(max_length=50)]
    flag20: Optional[constr(max_length=50)]
    flag21: Optional[constr(max_length=50)]
    flag22: Optional[constr(max_length=50)]
    flag23: Optional[constr(max_length=50)]
    total: Optional[constr(max_length=50)]
    signature: Optional[constr(max_length=50)]
    entryDatetime: Optional[datetime.datetime]

    class Config:
        orm_mode = False
        allow_population_by_field_name = True
        fields = field_mapping


class FormHourly(CreateFormHourly):

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = field_mapping


class FormHourlyResponse(Response):
    result: List[FormHourly] = Field(title="Result")


class FormHourlyQueryResponse(FormHourlyResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
