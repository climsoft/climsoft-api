import logging
from typing import Union

from climsoft_api.api.upload.schema import (
    FileUploadedToDiskResponse,
    FileUploadedToS3Response
)
from climsoft_api.config import settings
from climsoft_api.services import file_upload_service
from climsoft_api.utils.response import get_success_response, get_error_response
from fastapi import APIRouter, UploadFile, File
from climsoft_api.utils.response import translate_schema


router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.post(
    "/image"
)
async def upload_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        file_type = file.content_type
        if not file_type.startswith("image"):
            raise TypeError(_("Only image files are supported."))

        filepath = file_upload_service.save_file(
            settings.FILE_STORAGE,
            contents,
            file_type
        )

        return get_success_response(
            result=[filepath],
            message=_("Image uploaded successfully!"),
            schema=[
                translate_schema(
                    _,
                    FileUploadedToDiskResponse.schema()
                ),
                translate_schema(
                    _,
                    FileUploadedToS3Response.schema()
                )
            ]
        )
    except TypeError:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(message=_("Failed uploading image!"))
