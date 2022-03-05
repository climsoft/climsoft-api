import datetime
from typing import List

import \
    climsoft_api.api.paperarchivedefinition.schema as paperarchivedefinition_schema
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, Field


class CreatePaperArchive(BaseSchema):
    belongsTo: constr(max_length=255)
    formDatetime: str
    image: constr(max_length=255)
    classifiedInto: constr(max_length=50)

    class Config:
        fields = {
            "belongsTo": "belongs_to",
            "formDatetime": "form_datetime",
            "classifiedInto": "classified_into",
        }


class UpdatePaperArchive(BaseSchema):
    image: constr(max_length=255)


class PaperArchive(CreatePaperArchive):
    formDatetime: datetime.datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "belongsTo": "belongs_to",
            "formDatetime": "form_datetime",
            "classifiedInto": "classified_into",
        }


class PaperArchiveResponse(Response):
    result: List[PaperArchive] = Field(title=_("Result"))


class PaperArchiveWithStationAndPaperArchiveDefinition(PaperArchive):
    station: station_schema.Station
    paperarchivedefinition: paperarchivedefinition_schema.PaperArchiveDefinition


class PaperArchiveWithStationAndPaperArchiveDefinitionResponse(Response):
    result: List[PaperArchiveWithStationAndPaperArchiveDefinition]


class PaperArchiveQueryResponse(PaperArchiveResponse):
    limit: int = Field(title=_("Limit"))
    page: int
    pages: int
