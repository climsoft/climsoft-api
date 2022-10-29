from climsoft_api.config import settings
from climsoft_api.utils.s3 import get_s3_client
from fastapi import APIRouter, Request
from fastapi.responses import Response
from climsoft_api.utils.exception import handle_exceptions
from climsoft_api.utils.deployment import override_settings

router = APIRouter()


@router.get("/s3/image/{object_key}")
@handle_exceptions
def get_s3_object(object_key, request: Request):
    _settings = override_settings(request.state.settings_override)
    s3_client = get_s3_client(_settings)
    response = s3_client.get_object(
        Bucket=_settings.S3_BUCKET,
        Key=object_key
    )
    return Response(response["Body"].read(),
                    media_type=f"image/{object_key.split('.')[-1]}")
