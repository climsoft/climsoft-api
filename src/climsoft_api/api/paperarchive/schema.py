import datetime
from typing import List

import \
    climsoft_api.api.paperarchivedefinition.schema as paperarchivedefinition_schema
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, Field


class CreatePaperArchive(BaseSchema):
    belongsTo: constr(max_length=255) = Field(title=_("Belongs To"))
    formDatetime: str = Field(title=_("Form Datetime"))
    image: constr(max_length=255) = Field(title=_("Image"))
    classifiedInto: constr(max_length=50) = Field(title=_("Classified Into"))

    class Config:
        fields = {
            "belongsTo": "belongs_to",
            "formDatetime": "form_datetime",
            "classifiedInto": "classified_into",
        }


class UpdatePaperArchive(BaseSchema):
    image: constr(max_length=255) = Field(title=_("Image"))


class PaperArchive(CreatePaperArchive):
    formDatetime: datetime.datetime = Field(title=_("Form Datetime"))

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
    station: station_schema.Station = Field(title=_("Station"))
    paperarchivedefinition: paperarchivedefinition_schema.PaperArchiveDefinition = Field(title=_("Paper Archive Definition"))


class PaperArchiveWithStationAndPaperArchiveDefinitionResponse(Response):
    result: List[PaperArchiveWithStationAndPaperArchiveDefinition] = Field(title=_("Result"))


class PaperArchiveQueryResponse(PaperArchiveResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
