import datetime

from pydantic import BaseModel, constr, Field
from typing import Optional, List
from climsoft_api.api.schema import Response


field_mapping = {
    "stationId": "station_id",
    "elementId": "element_id",
    "entryDatetime": "entry_datetime"
}


class CreateFormMonthly(BaseModel):
    stationId: constr(max_length=255)
    elementId: int
    yyyy: int
    mm_01: Optional[constr(max_length=255)]
    mm_02: Optional[constr(max_length=255)]
    mm_03: Optional[constr(max_length=255)]
    mm_04: constr(max_length=255)
    mm_05: Optional[constr(max_length=255)]
    mm_06: Optional[constr(max_length=255)]
    mm_07: Optional[constr(max_length=255)]
    mm_08: Optional[constr(max_length=255)]
    mm_09: Optional[constr(max_length=255)]
    mm_10: Optional[constr(max_length=255)]
    mm_11: Optional[constr(max_length=255)]
    mm_12: Optional[constr(max_length=255)]
    flag01: Optional[constr(max_length=255)]
    flag02: Optional[constr(max_length=255)]
    flag03: Optional[constr(max_length=255)]
    flag04: Optional[constr(max_length=255)]
    flag05: Optional[constr(max_length=255)]
    flag06: Optional[constr(max_length=255)]
    flag07: Optional[constr(max_length=255)]
    flag08: Optional[constr(max_length=255)]
    flag09: Optional[constr(max_length=255)]
    flag10: Optional[constr(max_length=255)]
    flag11: Optional[constr(max_length=255)]
    flag12: Optional[constr(max_length=255)]
    period01: Optional[constr(max_length=255)]
    period02: Optional[constr(max_length=255)]
    period03: Optional[constr(max_length=255)]
    period04: Optional[constr(max_length=255)]
    period05: Optional[constr(max_length=255)]
    period06: Optional[constr(max_length=255)]
    period07: Optional[constr(max_length=255)]
    period08: Optional[constr(max_length=255)]
    period09: Optional[constr(max_length=255)]
    period10: Optional[constr(max_length=255)]
    period11: Optional[constr(max_length=255)]
    period12: Optional[constr(max_length=255)]
    signature: Optional[constr(max_length=50)]
    entryDatetime: Optional[datetime.datetime]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class UpdateFormMonthly(BaseModel):
    mm_01: Optional[constr(max_length=255)]
    mm_02: Optional[constr(max_length=255)]
    mm_03: Optional[constr(max_length=255)]
    mm_04: Optional[constr(max_length=255)]
    mm_05: Optional[constr(max_length=255)]
    mm_06: Optional[constr(max_length=255)]
    mm_07: Optional[constr(max_length=255)]
    mm_08: Optional[constr(max_length=255)]
    mm_09: Optional[constr(max_length=255)]
    mm_10: Optional[constr(max_length=255)]
    mm_11: Optional[constr(max_length=255)]
    mm_12: Optional[constr(max_length=255)]
    flag01: Optional[constr(max_length=255)]
    flag02: Optional[constr(max_length=255)]
    flag03: Optional[constr(max_length=255)]
    flag04: Optional[constr(max_length=255)]
    flag05: Optional[constr(max_length=255)]
    flag06: Optional[constr(max_length=255)]
    flag07: Optional[constr(max_length=255)]
    flag08: Optional[constr(max_length=255)]
    flag09: Optional[constr(max_length=255)]
    flag10: Optional[constr(max_length=255)]
    flag11: Optional[constr(max_length=255)]
    flag12: Optional[constr(max_length=255)]
    period01: Optional[constr(max_length=255)]
    period02: Optional[constr(max_length=255)]
    period03: Optional[constr(max_length=255)]
    period04: Optional[constr(max_length=255)]
    period05: Optional[constr(max_length=255)]
    period06: Optional[constr(max_length=255)]
    period07: Optional[constr(max_length=255)]
    period08: Optional[constr(max_length=255)]
    period09: Optional[constr(max_length=255)]
    period10: Optional[constr(max_length=255)]
    period11: Optional[constr(max_length=255)]
    period12: Optional[constr(max_length=255)]
    signature: Optional[constr(max_length=50)]
    entryDatetime: Optional[datetime.datetime]

    class Config:
        fields = field_mapping
        allow_population_by_field_name = True


class FormMonthly(CreateFormMonthly):

    class Config:
        fields = field_mapping
        allow_population_by_field_name = True
        orm_mode = True


class FormMonthlyResponse(Response):
    result: List[FormMonthly] = Field(title="Result")


class FormMonthlyQueryResponse(FormMonthlyResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
