from typing import List
from climsoft_api.api.schema import Response, BaseSchema


class CreateAcquisitionType(BaseSchema):
    code: int
    description: str


class UpdateAcquisitionType(BaseSchema):
    description: str


class AcquisitionType(CreateAcquisitionType):

    class Config:
        orm_mode = True


class AcquisitionTypeResponse(Response):
    result: List[AcquisitionType]


