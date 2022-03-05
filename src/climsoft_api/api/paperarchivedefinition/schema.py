from typing import List

from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr


class CreatePaperArchiveDefinition(BaseSchema):
    formId: constr(max_length=50)
    description: constr(max_length=255)

    class Config:
        fields = {"formId": "form_id"}


class UpdatePaperArchiveDefinition(BaseSchema):
    description: constr(max_length=255)


class PaperArchiveDefinition(CreatePaperArchiveDefinition):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {"formId": "form_id"}


class PaperArchiveDefinitionResponse(Response):
    result: List[PaperArchiveDefinition]


class PaperArchiveDefinitionQueryResponse(PaperArchiveDefinitionResponse):
    limit: int
    page: int
    pages: int
