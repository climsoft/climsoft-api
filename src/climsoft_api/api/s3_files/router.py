from fastapi import APIRouter
from climsoft_api.utils.s3 import get_s3_client
from climsoft_api.config import settings
from fastapi.responses import Response

router = APIRouter()


@router.get("/image/{object_key}")
def get_s3_object(object_key):
    s3_client = get_s3_client()
    response = s3_client.get_object(
        Bucket=settings.S3_BUCKET,
        Key=object_key
    )
    return Response(response["Body"].read(), media_type=f"image/{object_key.split('.')[-1]}")

