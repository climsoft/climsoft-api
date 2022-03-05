from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    class Config:
        allow_population_by_field_name = True


class Response(BaseSchema):
    message: str = Field(title=_("Message"))
    status: str = Field(title=_("Status"))
