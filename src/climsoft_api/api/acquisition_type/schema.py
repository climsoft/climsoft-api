from typing import List
from pydantic import Field
from climsoft_api.api.schema import Response, BaseSchema


class CreateAcquisitionType(BaseSchema):
    code: int = Field(title=_("Code"))
    description: str = Field(title=_("Description"))


class UpdateAcquisitionType(BaseSchema):
    description: str = Field(title=_("Description"))


class AcquisitionType(CreateAcquisitionType):
    class Config:
        orm_mode = True


class AcquisitionTypeResponse(Response):
    result: List[AcquisitionType] = Field(title=_("Result"))


class AcquisitionTypeQueryResponse(AcquisitionTypeResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
