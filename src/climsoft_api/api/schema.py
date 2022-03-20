from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class Response(BaseSchema):
    message: str = Field(title="Message")
    status: str = Field(title="Status")
    _schema: str = None
