import json
import logging
from climsoft_api.api.upload.schema import (
    FileUploadedToDiskResponse,
    FileUploadedToS3Response
)
from climsoft_api.services import file_upload_service
from climsoft_api.utils.response import get_success_response, get_error_response
from fastapi import APIRouter, UploadFile, File, Request
from climsoft_api.utils.response import translate_schema
from climsoft_api.utils.deployment import override_settings
from climsoft_api.config import settings

router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.post(
    "/file-upload/image"
)
async def upload_image(request: Request, file: UploadFile = File(...)):
    try:
        _settings = override_settings(request.state.settings_override)
    except AttributeError:
        _settings = settings
    try:
        contents = await file.read()
        file_type = file.content_type
        if not file_type.startswith("image"):
            raise TypeError(_("Only image files are supported."))

        filepath = file_upload_service.save_file(
            _settings,
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
