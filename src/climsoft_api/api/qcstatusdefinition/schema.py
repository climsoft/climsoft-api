from pydantic import constr
from typing import List
from climsoft_api.api.schema import BaseSchema, Response


class CreateQCStatusDefinition(BaseSchema):
    code: int
    description: constr(max_length=255)


class UpdateQCStatusDefinition(BaseSchema):
    description: constr(max_length=255)


class QCStatusDefinition(CreateQCStatusDefinition):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class QCStatusDefinitionResponse(Response):
    result: List[QCStatusDefinition]


class QCStatusDefinitionQueryResponse(QCStatusDefinitionResponse):
    limit: int
    page: int
    pages: int

