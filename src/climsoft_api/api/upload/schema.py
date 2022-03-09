from typing import List
from pydantic import Field
from climsoft_api.api.schema import Response, BaseSchema


class FileUploadedToDisk(BaseSchema):
    storage: str = Field("disk", title="Storage")
    filepath: str = Field(title="Filepath")


class FileUploadedToS3(BaseSchema):
    storage: str = Field("s3", title="Storage")
    object_key: str = Field(title="Object key")


class FileUploadedToDiskResponse(Response):
    result: List[FileUploadedToDisk] = Field(title="Result")


class FileUploadedToS3Response(Response):
    result: List[FileUploadedToS3] = Field(title="Result")
