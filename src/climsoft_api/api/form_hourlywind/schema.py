import datetime

from pydantic import BaseModel, constr
from typing import Optional, List
from climsoft_api.api.schema import Response, Field


field_mapping = {
    "stationId": "station_id",
    "entryDatetime": "entry_datetime"
}


class CreateFormHourlyWind(BaseModel):
    stationId: constr(max_length=255)
    yyyy: int
    mm: int
    dd: int
    elem_112_00: Optional[constr(max_length=255)]
    elem_112_01: Optional[constr(max_length=255)]
    elem_112_02: Optional[constr(max_length=255)]
    elem_112_03: Optional[constr(max_length=255)]
    elem_112_04: Optional[constr(max_length=255)]
    elem_112_05: Optional[constr(max_length=255)]
    elem_112_06: Optional[constr(max_length=255)]
    elem_112_07: Optional[constr(max_length=255)]
    elem_112_08: Optional[constr(max_length=255)]
    elem_112_09: Optional[constr(max_length=255)]
    elem_112_10: Optional[constr(max_length=255)]
    elem_112_11: Optional[constr(max_length=255)]
    elem_112_12: Optional[constr(max_length=255)]
    elem_112_13: Optional[constr(max_length=255)]
    elem_112_14: Optional[constr(max_length=255)]
    elem_112_15: Optional[constr(max_length=255)]
    elem_112_16: Optional[constr(max_length=255)]
    elem_112_17: Optional[constr(max_length=255)]
    elem_112_18: Optional[constr(max_length=255)]
    elem_112_19: Optional[constr(max_length=255)]
    elem_112_20: Optional[constr(max_length=255)]
    elem_112_21: Optional[constr(max_length=255)]
    elem_112_22: Optional[constr(max_length=255)]
    elem_112_23: Optional[constr(max_length=255)]
    elem_111_00: Optional[constr(max_length=255)]
    elem_111_01: Optional[constr(max_length=255)]
    elem_111_02: Optional[constr(max_length=255)]
    elem_111_03: Optional[constr(max_length=255)]
    elem_111_04: Optional[constr(max_length=255)]
    elem_111_05: Optional[constr(max_length=255)]
    elem_111_06: Optional[constr(max_length=255)]
    elem_111_07: Optional[constr(max_length=255)]
    elem_111_08: Optional[constr(max_length=255)]
    elem_111_09: Optional[constr(max_length=255)]
    elem_111_10: Optional[constr(max_length=255)]
    elem_111_11: Optional[constr(max_length=255)]
    elem_111_12: Optional[constr(max_length=255)]
    elem_111_13: Optional[constr(max_length=255)]
    elem_111_14: Optional[constr(max_length=255)]
    elem_111_15: Optional[constr(max_length=255)]
    elem_111_16: Optional[constr(max_length=255)]
    elem_111_17: Optional[constr(max_length=255)]
    elem_111_18: Optional[constr(max_length=255)]
    elem_111_19: Optional[constr(max_length=255)]
    elem_111_20: Optional[constr(max_length=255)]
    elem_111_21: Optional[constr(max_length=255)]
    elem_111_22: Optional[constr(max_length=255)]
    elem_111_23: Optional[constr(max_length=255)]
    ddflag00: Optional[constr(max_length=255)]
    ddflag01: Optional[constr(max_length=255)]
    ddflag02: Optional[constr(max_length=255)]
    ddflag03: Optional[constr(max_length=255)]
    ddflag04: Optional[constr(max_length=255)]
    ddflag05: Optional[constr(max_length=255)]
    ddflag06: Optional[constr(max_length=255)]
    ddflag07: Optional[constr(max_length=255)]
    ddflag08: Optional[constr(max_length=255)]
    ddflag09: Optional[constr(max_length=255)]
    ddflag10: Optional[constr(max_length=255)]
    ddflag11: Optional[constr(max_length=255)]
    ddflag12: Optional[constr(max_length=255)]
    ddflag13: Optional[constr(max_length=255)]
    ddflag14: Optional[constr(max_length=255)]
    ddflag15: Optional[constr(max_length=255)]
    ddflag16: Optional[constr(max_length=255)]
    ddflag17: Optional[constr(max_length=255)]
    ddflag18: Optional[constr(max_length=255)]
    ddflag19: Optional[constr(max_length=255)]
    ddflag20: Optional[constr(max_length=255)]
    ddflag21: Optional[constr(max_length=255)]
    ddflag22: Optional[constr(max_length=255)]
    ddflag23: Optional[constr(max_length=255)]
    total: Optional[constr(max_length=50)]
    signature: Optional[constr(max_length=50)]
    entryDatetime: Optional[datetime.datetime]

    class Config:
        fields = field_mapping
        allow_population_by_field_name = True


class UpdateFormHourlyWind(BaseModel):
    elem_112_00: Optional[constr(max_length=255)]
    elem_112_01: Optional[constr(max_length=255)]
    elem_112_02: Optional[constr(max_length=255)]
    elem_112_03: Optional[constr(max_length=255)]
    elem_112_04: Optional[constr(max_length=255)]
    elem_112_05: Optional[constr(max_length=255)]
    elem_112_06: Optional[constr(max_length=255)]
    elem_112_07: Optional[constr(max_length=255)]
    elem_112_08: Optional[constr(max_length=255)]
    elem_112_09: Optional[constr(max_length=255)]
    elem_112_10: Optional[constr(max_length=255)]
    elem_112_11: Optional[constr(max_length=255)]
    elem_112_12: Optional[constr(max_length=255)]
    elem_112_13: Optional[constr(max_length=255)]
    elem_112_14: Optional[constr(max_length=255)]
    elem_112_15: Optional[constr(max_length=255)]
    elem_112_16: Optional[constr(max_length=255)]
    elem_112_17: Optional[constr(max_length=255)]
    elem_112_18: Optional[constr(max_length=255)]
    elem_112_19: Optional[constr(max_length=255)]
    elem_112_20: Optional[constr(max_length=255)]
    elem_112_21: Optional[constr(max_length=255)]
    elem_112_22: Optional[constr(max_length=255)]
    elem_112_23: Optional[constr(max_length=255)]
    elem_111_00: Optional[constr(max_length=255)]
    elem_111_01: Optional[constr(max_length=255)]
    elem_111_02: Optional[constr(max_length=255)]
    elem_111_03: Optional[constr(max_length=255)]
    elem_111_04: Optional[constr(max_length=255)]
    elem_111_05: Optional[constr(max_length=255)]
    elem_111_06: Optional[constr(max_length=255)]
    elem_111_07: Optional[constr(max_length=255)]
    elem_111_08: Optional[constr(max_length=255)]
    elem_111_09: Optional[constr(max_length=255)]
    elem_111_10: Optional[constr(max_length=255)]
    elem_111_11: Optional[constr(max_length=255)]
    elem_111_12: Optional[constr(max_length=255)]
    elem_111_13: Optional[constr(max_length=255)]
    elem_111_14: Optional[constr(max_length=255)]
    elem_111_15: Optional[constr(max_length=255)]
    elem_111_16: Optional[constr(max_length=255)]
    elem_111_17: Optional[constr(max_length=255)]
    elem_111_18: Optional[constr(max_length=255)]
    elem_111_19: Optional[constr(max_length=255)]
    elem_111_20: Optional[constr(max_length=255)]
    elem_111_21: Optional[constr(max_length=255)]
    elem_111_22: Optional[constr(max_length=255)]
    elem_111_23: Optional[constr(max_length=255)]
    ddflag00: Optional[constr(max_length=255)]
    ddflag01: Optional[constr(max_length=255)]
    ddflag02: Optional[constr(max_length=255)]
    ddflag03: Optional[constr(max_length=255)]
    ddflag04: Optional[constr(max_length=255)]
    ddflag05: Optional[constr(max_length=255)]
    ddflag06: Optional[constr(max_length=255)]
    ddflag07: Optional[constr(max_length=255)]
    ddflag08: Optional[constr(max_length=255)]
    ddflag09: Optional[constr(max_length=255)]
    ddflag10: Optional[constr(max_length=255)]
    ddflag11: Optional[constr(max_length=255)]
    ddflag12: Optional[constr(max_length=255)]
    ddflag13: Optional[constr(max_length=255)]
    ddflag14: Optional[constr(max_length=255)]
    ddflag15: Optional[constr(max_length=255)]
    ddflag16: Optional[constr(max_length=255)]
    ddflag17: Optional[constr(max_length=255)]
    ddflag18: Optional[constr(max_length=255)]
    ddflag19: Optional[constr(max_length=255)]
    ddflag20: Optional[constr(max_length=255)]
    ddflag21: Optional[constr(max_length=255)]
    ddflag22: Optional[constr(max_length=255)]
    ddflag23: Optional[constr(max_length=255)]
    total: Optional[constr(max_length=50)]
    signature: Optional[constr(max_length=50)]
    entryDatetime: Optional[datetime.datetime]

    class Config:
        fields = field_mapping
        allow_population_by_field_name = True


class FormHourlyWind(CreateFormHourlyWind):

    class Config:
        fields = field_mapping
        allow_population_by_field_name = True
        orm_mode = True


class FormHourlyWindResponse(Response):
    result: List[FormHourlyWind] = Field(title="Result")


class FormHourlyWindQueryResponse(FormHourlyWindResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")


