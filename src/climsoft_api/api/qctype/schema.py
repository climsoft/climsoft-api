from typing import List

from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr


class CreateQCType(BaseSchema):
    code: int
    description: constr(max_length=255)


class UpdateQCType(BaseSchema):
    description: constr(max_length=255)


class QCType(CreateQCType):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class QCTypeResponse(Response):
    result: List[QCType]


class QCTypeQueryResponse(QCTypeResponse):
    limit: int
    page: int
    pages: int
