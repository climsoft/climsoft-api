from typing import List
from pydantic import Field
from climsoft_api.api.schema import Response, BaseSchema


class CreateAcquisitionType(BaseSchema):
    code: int = Field(title="Code")
    description: str = Field(title="Description")


class UpdateAcquisitionType(BaseSchema):
    description: str = Field(title="Description")


class AcquisitionType(CreateAcquisitionType):
    class Config:
        orm_mode = True


class AcquisitionTypeResponse(Response):
    result: List[AcquisitionType] = Field(title="Result")


class AcquisitionTypeQueryResponse(AcquisitionTypeResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
