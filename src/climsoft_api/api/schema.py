from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        allow_population_by_field_name = True


class Response(BaseSchema):
    message: str
    status: str
