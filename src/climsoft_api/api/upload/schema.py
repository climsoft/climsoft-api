from typing import List
from pydantic import Field
from climsoft_api.api.schema import Response, BaseSchema


class FileUploadedToDisk(BaseSchema):
    storage: str = Field("disk", title=_("Storage"))
    filepath: str = Field(title=_("Filepath"))


class FileUploadedToS3(BaseSchema):
    storage: str = Field("s3", title=_("Storage"))
    object_key: str = Field(title=_("Object key"))


class FileUploadedToDiskResponse(Response):
    result: List[FileUploadedToDisk] = Field(title=_("Result"))


class FileUploadedToS3Response(Response):
    result: List[FileUploadedToS3] = Field(title=_("Result"))
