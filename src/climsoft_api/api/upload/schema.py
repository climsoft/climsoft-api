from typing import List
from pydantic import Field
from climsoft_api.api.schema import Response, BaseSchema


class FileUploadedToDisk(BaseSchema):
    storage: str = "disk"
    filepath: str


class FileUploadedToS3(BaseSchema):
    storage: str = "s3"
    object_key: str


class FileUploadedToDiskResponse(Response):
    result: List[FileUploadedToDisk] = Field(title=_("Result"))


class FileUploadedToS3Response(Response):
    result: List[FileUploadedToS3] = Field(title=_("Result"))
