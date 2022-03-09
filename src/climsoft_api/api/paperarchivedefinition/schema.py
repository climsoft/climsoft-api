from typing import List

from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, Field


class CreatePaperArchiveDefinition(BaseSchema):
    formId: constr(max_length=50) = Field(title="Form ID")
    description: constr(max_length=255) = Field(title="Description")

    class Config:
        fields = {"formId": "form_id"}


class UpdatePaperArchiveDefinition(BaseSchema):
    description: constr(max_length=255) = Field(title="Description")


class PaperArchiveDefinition(CreatePaperArchiveDefinition):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {"formId": "form_id"}


class PaperArchiveDefinitionResponse(Response):
    result: List[PaperArchiveDefinition] = Field(title="Result")


class PaperArchiveDefinitionQueryResponse(PaperArchiveDefinitionResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
