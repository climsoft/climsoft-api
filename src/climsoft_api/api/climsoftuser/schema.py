import enum
from typing import List
from pydantic import Field

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
    userName: str = Field(title=_("Username"))
    userRole: ClimsoftUserRole = Field(title=_("Role"))

    class Config:
        fields = {
            "userName": "username",
            "userRole": "role"
        }


class ClimsoftUser(BaseSchema):
    userName: str = Field(title=_("Username"))
    userRole: ClimsoftUserRole = Field(title=_("Role"))

    class Config:
        fields = {
            "userName": "username",
            "userRole": "role"
        }
        allow_population_by_field_name = True
        orm_mode = True


class ClimsoftUserResponse(Response):
    result: List[ClimsoftUser] = Field(title=_("Result"))


class ClimsoftUserQueryResponse(ClimsoftUserResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
