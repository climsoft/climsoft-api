import datetime

from pydantic import BaseModel, Field, constr
from typing import Optional, List
from climsoft_api.api.schema import Response


field_mapping = {
    "stationId": "station_id",
    "entryDatetime": "entry_datetime"
}


class CreateFormSynoptic2Tdcf(BaseModel):
    stationId: constr(max_length=10)
    yyyy: int
    mm: int
    dd: int
    hh: int
    _106: Optional[constr(max_length=6)]
    _107: Optional[constr(max_length=6)]
    _399: Optional[constr(max_length=5)]
    _301: Optional[constr(max_length=8)]
    _185: Optional[constr(max_length=6)]
    _101: Optional[constr(max_length=5)]
    _103: Optional[constr(max_length=5)]
    _105: Optional[constr(max_length=50)]
    _110: Optional[constr(max_length=5)]
    _114: Optional[constr(max_length=5)]
    _115: Optional[constr(max_length=5)]
    _168: Optional[constr(max_length=5)]
    _192: Optional[constr(max_length=5)]
    _169: Optional[constr(max_length=5)]
    _170: Optional[constr(max_length=5)]
    _171: Optional[constr(max_length=5)]
    _119: Optional[constr(max_length=5)]
    _116: Optional[constr(max_length=5)]
    _117: Optional[constr(max_length=5)]
    _118: Optional[constr(max_length=5)]
    _123: Optional[constr(max_length=5)]
    _120: Optional[constr(max_length=5)]
    _121: Optional[constr(max_length=5)]
    _122: Optional[constr(max_length=5)]
    _127: Optional[constr(max_length=5)]
    _124: Optional[constr(max_length=5)]
    _125: Optional[constr(max_length=5)]
    _126: Optional[constr(max_length=5)]
    _131: Optional[constr(max_length=5)]
    _128: Optional[constr(max_length=5)]
    _129: Optional[constr(max_length=5)]
    _130: Optional[constr(max_length=5)]
    _167: Optional[constr(max_length=5)]
    _197: Optional[constr(max_length=50)]
    _193: Optional[constr(max_length=5)]
    _18: Optional[constr(max_length=6)]
    _532: Optional[constr(max_length=6)]
    _132: Optional[constr(max_length=6)]
    _5: Optional[constr(max_length=6)]
    _174: Optional[constr(max_length=50)]
    _3: Optional[constr(max_length=5)]
    _2: Optional[constr(max_length=5)]
    _85: Optional[constr(max_length=50)]
    _111: Optional[constr(max_length=5)]
    _112: Optional[constr(max_length=5)]
    flag1: Optional[constr(max_length=1)]
    flag2: Optional[constr(max_length=1)]
    flag3: Optional[constr(max_length=1)]
    flag4: Optional[constr(max_length=1)]
    flag5: Optional[constr(max_length=1)]
    flag6: Optional[constr(max_length=1)]
    flag7: Optional[constr(max_length=1)]
    flag8: Optional[constr(max_length=1)]
    flag9: Optional[constr(max_length=1)]
    flag10: Optional[constr(max_length=1)]
    flag11: Optional[constr(max_length=1)]
    flag12: Optional[constr(max_length=1)]
    flag13: Optional[constr(max_length=1)]
    flag14: Optional[constr(max_length=1)]
    flag15: Optional[constr(max_length=1)]
    flag16: Optional[constr(max_length=1)]
    flag17: Optional[constr(max_length=1)]
    flag18: Optional[constr(max_length=1)]
    flag19: Optional[constr(max_length=1)]
    flag20: Optional[constr(max_length=1)]
    flag21: Optional[constr(max_length=1)]
    flag22: Optional[constr(max_length=1)]
    flag23: Optional[constr(max_length=1)]
    flag24: Optional[constr(max_length=1)]
    flag25: Optional[constr(max_length=1)]
    flag26: Optional[constr(max_length=1)]
    flag27: Optional[constr(max_length=1)]
    flag28: Optional[constr(max_length=1)]
    flag29: Optional[constr(max_length=1)]
    flag30: Optional[constr(max_length=1)]
    flag31: Optional[constr(max_length=1)]
    flag32: Optional[constr(max_length=1)]
    flag33: Optional[constr(max_length=1)]
    flag34: Optional[constr(max_length=1)]
    flag35: Optional[constr(max_length=1)]
    flag36: Optional[constr(max_length=1)]
    flag37: Optional[constr(max_length=1)]
    flag38: Optional[constr(max_length=1)]
    flag39: Optional[constr(max_length=1)]
    flag40: Optional[constr(max_length=1)]
    flag41: Optional[constr(max_length=1)]
    flag42: Optional[constr(max_length=1)]
    flag43: Optional[constr(max_length=1)]
    flag44: Optional[constr(max_length=1)]
    flag45: Optional[constr(max_length=1)]
    signature: Optional[constr(max_length=50)]
    entryDatetime: Optional[datetime.datetime]

    class Config:
        allow_population_by_field_name = True
        fields = field_mapping


class UpdateFormSynoptic2Tdcf(BaseModel):
    _106: Optional[constr(max_length=6)]
    _107: Optional[constr(max_length=6)]
    _399: Optional[constr(max_length=5)]
    _301: Optional[constr(max_length=8)]
    _185: Optional[constr(max_length=6)]
    _101: Optional[constr(max_length=5)]
    _103: Optional[constr(max_length=5)]
    _105: Optional[constr(max_length=50)]
    _110: Optional[constr(max_length=5)]
    _114: Optional[constr(max_length=5)]
    _115: Optional[constr(max_length=5)]
    _168: Optional[constr(max_length=5)]
    _192: Optional[constr(max_length=5)]
    _169: Optional[constr(max_length=5)]
    _170: Optional[constr(max_length=5)]
    _171: Optional[constr(max_length=5)]
    _119: Optional[constr(max_length=5)]
    _116: Optional[constr(max_length=5)]
    _117: Optional[constr(max_length=5)]
    _118: Optional[constr(max_length=5)]
    _123: Optional[constr(max_length=5)]
    _120: Optional[constr(max_length=5)]
    _121: Optional[constr(max_length=5)]
    _122: Optional[constr(max_length=5)]
    _127: Optional[constr(max_length=5)]
    _124: Optional[constr(max_length=5)]
    _125: Optional[constr(max_length=5)]
    _126: Optional[constr(max_length=5)]
    _131: Optional[constr(max_length=5)]
    _128: Optional[constr(max_length=5)]
    _129: Optional[constr(max_length=5)]
    _130: Optional[constr(max_length=5)]
    _167: Optional[constr(max_length=5)]
    _197: Optional[constr(max_length=50)]
    _193: Optional[constr(max_length=5)]
    _18: Optional[constr(max_length=6)]
    _532: Optional[constr(max_length=6)]
    _132: Optional[constr(max_length=6)]
    _5: Optional[constr(max_length=6)]
    _174: Optional[constr(max_length=50)]
    _3: Optional[constr(max_length=5)]
    _2: Optional[constr(max_length=5)]
    _85: Optional[constr(max_length=50)]
    _111: Optional[constr(max_length=5)]
    _112: Optional[constr(max_length=5)]
    flag1: Optional[constr(max_length=1)]
    flag2: Optional[constr(max_length=1)]
    flag3: Optional[constr(max_length=1)]
    flag4: Optional[constr(max_length=1)]
    flag5: Optional[constr(max_length=1)]
    flag6: Optional[constr(max_length=1)]
    flag7: Optional[constr(max_length=1)]
    flag8: Optional[constr(max_length=1)]
    flag9: Optional[constr(max_length=1)]
    flag10: Optional[constr(max_length=1)]
    flag11: Optional[constr(max_length=1)]
    flag12: Optional[constr(max_length=1)]
    flag13: Optional[constr(max_length=1)]
    flag14: Optional[constr(max_length=1)]
    flag15: Optional[constr(max_length=1)]
    flag16: Optional[constr(max_length=1)]
    flag17: Optional[constr(max_length=1)]
    flag18: Optional[constr(max_length=1)]
    flag19: Optional[constr(max_length=1)]
    flag20: Optional[constr(max_length=1)]
    flag21: Optional[constr(max_length=1)]
    flag22: Optional[constr(max_length=1)]
    flag23: Optional[constr(max_length=1)]
    flag24: Optional[constr(max_length=1)]
    flag25: Optional[constr(max_length=1)]
    flag26: Optional[constr(max_length=1)]
    flag27: Optional[constr(max_length=1)]
    flag28: Optional[constr(max_length=1)]
    flag29: Optional[constr(max_length=1)]
    flag30: Optional[constr(max_length=1)]
    flag31: Optional[constr(max_length=1)]
    flag32: Optional[constr(max_length=1)]
    flag33: Optional[constr(max_length=1)]
    flag34: Optional[constr(max_length=1)]
    flag35: Optional[constr(max_length=1)]
    flag36: Optional[constr(max_length=1)]
    flag37: Optional[constr(max_length=1)]
    flag38: Optional[constr(max_length=1)]
    flag39: Optional[constr(max_length=1)]
    flag40: Optional[constr(max_length=1)]
    flag41: Optional[constr(max_length=1)]
    flag42: Optional[constr(max_length=1)]
    flag43: Optional[constr(max_length=1)]
    flag44: Optional[constr(max_length=1)]
    flag45: Optional[constr(max_length=1)]
    signature: Optional[constr(max_length=50)]
    entryDatetime: Optional[datetime.datetime]

    class Config:
        allow_population_by_field_name = True
        fields = field_mapping


class FormSynoptic2Tdcf(CreateFormSynoptic2Tdcf):

    class Config:
        allow_population_by_field_name = True
        fields = field_mapping
        orm_mode = True


class FormSynoptic2TdcfResponse(Response):
    result: List[FormSynoptic2Tdcf] = Field(title="Result")


class FormSynoptic2TdcfQueryResponse(FormSynoptic2TdcfResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")

