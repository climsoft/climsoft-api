import inflection
from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        alias_generator = lambda x: inflection.camelize(x, False)  # noqa
        allow_population_by_field_name = True


class Response(BaseSchema):
    message: str
    status: str
