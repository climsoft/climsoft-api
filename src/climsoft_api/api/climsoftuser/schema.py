import enum
from typing import List
from pydantic import constr
from climsoft_api.api.schema import Response, BaseSchema


class ClimsoftUserRole(str, enum.Enum):
    ClimsoftAdmin: str = "ClimsoftAdmin"
    ClimsoftDeveloper: str = "ClimsoftDeveloper"
    ClimsoftMetadata: str = "ClimsoftMetadata"
    ClimsoftOperator: str = "ClimsoftOperator"
    ClimsoftOperatorSupervisor: str = "ClimsoftOperatorSupervisor"
    ClimsoftProducts: str = "ClimsoftProducts"
    ClimsoftQC: str = "ClimsoftQC"
    ClimsoftRainfall: str = "ClimsoftRainfall"
    ClimsoftTranslator: str = "ClimsoftTranslator"


class CreateClimsoftUser(BaseSchema):
    userName: str
    userRole: str

    class Config:
        fields = {
            "userName": "username",
            "userRole": "role"
        }


class ClimsoftUser(BaseSchema):
    userName: str
    userRole: ClimsoftUserRole

    class Config:
        fields = {
            "userName": "username",
            "userRole": "role"
        }
        allow_population_by_field_name = True
        orm_mode = True


class ClimsoftUserResponse(Response):
    result: List[ClimsoftUser]


class ClimsoftUserQueryResponse(ClimsoftUserResponse):
    limit: int
    page: int
    pages: int
