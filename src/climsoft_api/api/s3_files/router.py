from climsoft_api.config import settings
from climsoft_api.utils.s3 import get_s3_client
from fastapi import APIRouter
from fastapi.responses import Response
from climsoft_api.utils.exception import handle_exceptions

router = APIRouter()


@router.get("/s3/image/{object_key}")
@handle_exceptions
def get_s3_object(object_key):
    s3_client = get_s3_client()
    response = s3_client.get_object(
        Bucket=settings.S3_BUCKET,
        Key=object_key
    )
    return Response(response["Body"].read(),
                    media_type=f"image/{object_key.split('.')[-1]}")
