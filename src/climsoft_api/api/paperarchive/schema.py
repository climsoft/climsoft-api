import datetime
from typing import List

import \
    climsoft_api.api.paperarchivedefinition.schema as paperarchivedefinition_schema
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, Field


class CreatePaperArchive(BaseSchema):
    belongsTo: constr(max_length=255) = Field(title="Belongs To")
    formDatetime: str = Field(title="Form Datetime")
    image: constr(max_length=255) = Field(title="Image")
    classifiedInto: constr(max_length=50) = Field(title="Classified Into")

    class Config:
        fields = {
            "belongsTo": "belongs_to",
            "formDatetime": "form_datetime",
            "classifiedInto": "classified_into",
        }


class UpdatePaperArchive(BaseSchema):
    image: constr(max_length=255) = Field(title="Image")


class PaperArchive(CreatePaperArchive):
    formDatetime: datetime.datetime = Field(title="Form Datetime")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "belongsTo": "belongs_to",
            "formDatetime": "form_datetime",
            "classifiedInto": "classified_into",
        }


class PaperArchiveResponse(Response):
    result: List[PaperArchive] = Field(title="Result")


class PaperArchiveWithStationAndPaperArchiveDefinition(PaperArchive):
    station: station_schema.Station = Field(title="Station")
    paperarchivedefinition: paperarchivedefinition_schema.PaperArchiveDefinition = Field(title="Paper Archive Definition")


class PaperArchiveWithStationAndPaperArchiveDefinitionResponse(Response):
    result: List[PaperArchiveWithStationAndPaperArchiveDefinition] = Field(title="Result")


class PaperArchiveQueryResponse(PaperArchiveResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
