import minio
import urllib3.response

from climsoft_api.config import settings
from climsoft_api.utils.s3 import get_minio_client
from fastapi import APIRouter, Request
from fastapi.responses import Response
from climsoft_api.utils.exception import handle_exceptions
from climsoft_api.utils.deployment import override_settings

router = APIRouter()


@router.get("/cloud-storage/image/{object_key}")
def get_s3_object(object_key, request: Request):
    try:
        _settings = override_settings(request.state.settings_override)
    except AttributeError:
        _settings = settings

    client: minio.Minio = get_minio_client(_settings)
    response: urllib3.response.HTTPResponse = client.get_object(
        bucket_name=_settings.S3_BUCKET,
        object_name=object_key
    )

    return Response(response.read(),
                    media_type=f"image/{object_key.split('.')[-1]}")
