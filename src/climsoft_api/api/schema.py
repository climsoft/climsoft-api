from pydantic import BaseModel, Field
from typing import Optional
from fastapi import Form


class BaseSchema(BaseModel):
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class Response(BaseSchema):
    message: str = Field(title="Message")
    status: str = Field(title="Status")
    _schema: str = None


class CurrentUser(BaseModel):
    username: str
    deployment_key: str = None


class TokenSchema(BaseModel):
    access_token: str
    username: str


class PasswordRequestForm:
    def __init__(
        self,
        grant_type: str = Form(None, regex="password"),
        username: str = Form(...),
        password: str = Form(...),
        scope: str = Form(""),
        client_id: Optional[str] = Form(None),
        client_secret: Optional[str] = Form(None),
    ):
        self.grant_type = grant_type
        self.username = username
        self.password = password
        self.scope = scope.split()
        self.client_id = client_id
        self.client_secret = client_secret
