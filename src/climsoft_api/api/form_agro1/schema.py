import datetime

from pydantic import BaseModel, constr, Field
from typing import Optional, List
from climsoft_api.api.schema import Response


field_mapping = {
    "stationId": "station_id",
    "Val_Elem101": "val_elem101",
    "Val_Elem102": "val_elem102",
    "Val_Elem103": "val_elem103",
    "Val_Elem105": "val_elem105",
    "Val_Elem002": "val_elem002",
    "Val_Elem003": "val_elem003",
    "Val_Elem099": "val_elem099",
    "Val_Elem072": "val_elem072",
    "Val_Elem073": "val_elem073",
    "Val_Elem074": "val_elem074",
    "Val_Elem554": "val_elem554",
    "Val_Elem075": "val_elem075",
    "Val_Elem076": "val_elem076",
    "Val_Elem561": "val_elem561",
    "Val_Elem562": "val_elem562",
    "Val_Elem563": "val_elem563",
    "Val_Elem513": "val_elem513",
    "Val_Elem005": "val_elem005",
    "Val_Elem504": "val_elem504",
    "Val_Elem532": "val_elem532",
    "Val_Elem137": "val_elem137",
    "Val_Elem018": "val_elem018",
    "Val_Elem518": "val_elem518",
    "Val_Elem511": "val_elem511",
    "Val_Elem512": "val_elem512",
    "Val_Elem503": "val_elem503",
    "Val_Elem515": "val_elem515",
    "Val_Elem564": "val_elem564",
    "Val_Elem565": "val_elem565",
    "Val_Elem566": "val_elem566",
    "Val_Elem531": "val_elem531",
    "Val_Elem530": "val_elem530",
    "Val_Elem541": "val_elem541",
    "Val_Elem542": "val_elem542",
    "Flag101": "flag101",
    "Flag102": "flag102",
    "Flag103": "flag103",
    "Flag105": "flag105",
    "Flag002": "flag002",
    "Flag003": "flag003",
    "Flag099": "flag099",
    "Flag072": "flag072",
    "Flag073": "flag073",
    "Flag074": "flag074",
    "Flag554": "flag554",
    "Flag075": "flag075",
    "Flag076": "flag076",
    "Flag561": "flag561",
    "Flag562": "flag562",
    "Flag563": "flag563",
    "Flag513": "flag513",
    "Flag005": "flag005",
    "Flag504": "flag504",
    "Flag532": "flag532",
    "Flag137": "flag137",
    "Flag018": "flag018",
    "Flag518": "flag518",
    "Flag511": "flag511",
    "Flag512": "flag512",
    "Flag503": "flag503",
    "Flag515": "flag515",
    "Flag564": "flag564",
    "Flag565": "flag565",
    "Flag566": "flag566",
    "Flag531": "flag531",
    "Flag530": "flag530",
    "Flag541": "flag541",
    "Flag542": "flag542",
    "entryDatetime": "entry_datetime"
}


class CreateFormAgro1(BaseModel):
    stationId: constr(max_length=50)
    yyyy: int
    mm: int
    dd: int
    Val_Elem101: Optional[constr(max_length=6)]
    Val_Elem102: Optional[constr(max_length=6)]
    Val_Elem103: Optional[constr(max_length=6)]
    Val_Elem105: Optional[constr(max_length=6)]
    Val_Elem002: Optional[constr(max_length=6)]
    Val_Elem003: Optional[constr(max_length=6)]
    Val_Elem099: Optional[constr(max_length=6)]
    Val_Elem072: Optional[constr(max_length=6)]
    Val_Elem073: Optional[constr(max_length=6)]
    Val_Elem074: Optional[constr(max_length=6)]
    Val_Elem075: Optional[constr(max_length=6)]
    Val_Elem076: Optional[constr(max_length=6)]
    Val_Elem561: Optional[constr(max_length=6)]
    Val_Elem562: Optional[constr(max_length=6)]
    Val_Elem563: Optional[constr(max_length=6)]
    Val_Elem513: Optional[constr(max_length=6)]
    Val_Elem005: Optional[constr(max_length=6)]
    Val_Elem504: Optional[constr(max_length=6)]
    Val_Elem532: Optional[constr(max_length=6)]
    Val_Elem137: Optional[constr(max_length=6)]
    Val_Elem018: Optional[constr(max_length=6)]
    Val_Elem518: Optional[constr(max_length=6)]
    Val_Elem511: Optional[constr(max_length=6)]
    Val_Elem512: Optional[constr(max_length=6)]
    Val_Elem503: Optional[constr(max_length=6)]
    Val_Elem515: Optional[constr(max_length=6)]
    Val_Elem564: Optional[constr(max_length=6)]
    Val_Elem565: Optional[constr(max_length=6)]
    Val_Elem566: Optional[constr(max_length=6)]
    Val_Elem531: Optional[constr(max_length=6)]
    Val_Elem530: Optional[constr(max_length=6)]
    Val_Elem541: Optional[constr(max_length=6)]
    Val_Elem542: Optional[constr(max_length=6)]
    Flag101: Optional[constr(max_length=1)]
    Flag102: Optional[constr(max_length=1)]
    Flag103: Optional[constr(max_length=1)]
    Flag105: Optional[constr(max_length=1)]
    Flag002: Optional[constr(max_length=1)]
    Flag003: Optional[constr(max_length=1)]
    Flag099: Optional[constr(max_length=1)]
    Flag072: Optional[constr(max_length=1)]
    Flag073: Optional[constr(max_length=1)]
    Flag074: Optional[constr(max_length=1)]
    Flag554: Optional[constr(max_length=1)]
    Flag075: Optional[constr(max_length=1)]
    Flag076: Optional[constr(max_length=1)]
    Flag561: Optional[constr(max_length=1)]
    Flag562: Optional[constr(max_length=1)]
    Flag563: Optional[constr(max_length=1)]
    Flag513: Optional[constr(max_length=1)]
    Flag005: Optional[constr(max_length=1)]
    Flag504: Optional[constr(max_length=1)]
    Flag532: Optional[constr(max_length=1)]
    Flag137: Optional[constr(max_length=1)]
    Flag018: Optional[constr(max_length=1)]
    Flag518: Optional[constr(max_length=1)]
    Flag511: Optional[constr(max_length=1)]
    Flag512: Optional[constr(max_length=1)]
    Flag503: Optional[constr(max_length=1)]
    Flag515: Optional[constr(max_length=1)]
    Flag564: Optional[constr(max_length=1)]
    Flag565: Optional[constr(max_length=1)]
    Flag566: Optional[constr(max_length=1)]
    Flag531: Optional[constr(max_length=1)]
    Flag530: Optional[constr(max_length=1)]
    Flag541: Optional[constr(max_length=1)]
    Flag542: Optional[constr(max_length=1)]
    signature: Optional[constr(max_length=45)]
    entryDatetime: Optional[datetime.datetime]

    class Config:
        fields = field_mapping
        allow_population_by_field_name = True


class UpdateFormAgro1(BaseModel):
    Val_Elem101: Optional[constr(max_length=6)]
    Val_Elem102: Optional[constr(max_length=6)]
    Val_Elem103: Optional[constr(max_length=6)]
    Val_Elem105: Optional[constr(max_length=6)]
    Val_Elem002: Optional[constr(max_length=6)]
    Val_Elem003: Optional[constr(max_length=6)]
    Val_Elem099: Optional[constr(max_length=6)]
    Val_Elem072: Optional[constr(max_length=6)]
    Val_Elem073: Optional[constr(max_length=6)]
    Val_Elem074: Optional[constr(max_length=6)]
    Val_Elem075: Optional[constr(max_length=6)]
    Val_Elem076: Optional[constr(max_length=6)]
    Val_Elem561: Optional[constr(max_length=6)]
    Val_Elem562: Optional[constr(max_length=6)]
    Val_Elem563: Optional[constr(max_length=6)]
    Val_Elem513: Optional[constr(max_length=6)]
    Val_Elem005: Optional[constr(max_length=6)]
    Val_Elem504: Optional[constr(max_length=6)]
    Val_Elem532: Optional[constr(max_length=6)]
    Val_Elem137: Optional[constr(max_length=6)]
    Val_Elem018: Optional[constr(max_length=6)]
    Val_Elem518: Optional[constr(max_length=6)]
    Val_Elem511: Optional[constr(max_length=6)]
    Val_Elem512: Optional[constr(max_length=6)]
    Val_Elem503: Optional[constr(max_length=6)]
    Val_Elem515: Optional[constr(max_length=6)]
    Val_Elem564: Optional[constr(max_length=6)]
    Val_Elem565: Optional[constr(max_length=6)]
    Val_Elem566: Optional[constr(max_length=6)]
    Val_Elem531: Optional[constr(max_length=6)]
    Val_Elem530: Optional[constr(max_length=6)]
    Val_Elem541: Optional[constr(max_length=6)]
    Val_Elem542: Optional[constr(max_length=6)]
    Flag101: Optional[constr(max_length=1)]
    Flag102: Optional[constr(max_length=1)]
    Flag103: Optional[constr(max_length=1)]
    Flag105: Optional[constr(max_length=1)]
    Flag002: Optional[constr(max_length=1)]
    Flag003: Optional[constr(max_length=1)]
    Flag099: Optional[constr(max_length=1)]
    Flag072: Optional[constr(max_length=1)]
    Flag073: Optional[constr(max_length=1)]
    Flag074: Optional[constr(max_length=1)]
    Flag554: Optional[constr(max_length=1)]
    Flag075: Optional[constr(max_length=1)]
    Flag076: Optional[constr(max_length=1)]
    Flag561: Optional[constr(max_length=1)]
    Flag562: Optional[constr(max_length=1)]
    Flag563: Optional[constr(max_length=1)]
    Flag513: Optional[constr(max_length=1)]
    Flag005: Optional[constr(max_length=1)]
    Flag504: Optional[constr(max_length=1)]
    Flag532: Optional[constr(max_length=1)]
    Flag137: Optional[constr(max_length=1)]
    Flag018: Optional[constr(max_length=1)]
    Flag518: Optional[constr(max_length=1)]
    Flag511: Optional[constr(max_length=1)]
    Flag512: Optional[constr(max_length=1)]
    Flag503: Optional[constr(max_length=1)]
    Flag515: Optional[constr(max_length=1)]
    Flag564: Optional[constr(max_length=1)]
    Flag565: Optional[constr(max_length=1)]
    Flag566: Optional[constr(max_length=1)]
    Flag531: Optional[constr(max_length=1)]
    Flag530: Optional[constr(max_length=1)]
    Flag541: Optional[constr(max_length=1)]
    Flag542: Optional[constr(max_length=1)]
    signature: Optional[constr(max_length=45)]
    entryDatetime: Optional[datetime.datetime]

    class Config:
        fields = field_mapping
        allow_population_by_field_name = True


class FormAgro1(CreateFormAgro1):
    class Config:
        fields = field_mapping
        allow_population_by_field_name = True
        orm_mode = True


class FormAgro1Response(Response):
    result: List[FormAgro1] = Field(title="Result")


class FormAgro1QueryResponse(FormAgro1Response):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
