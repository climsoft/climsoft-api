import io
import uuid
from pathlib import Path
import minio
from climsoft_api.utils.s3 import get_minio_client
from climsoft_api.config import Settings


def save_file(settings: Settings, file, file_type):
    file_name = f"{uuid.uuid4().hex}.{file_type.split('/')[-1]}"
    if settings.FILE_STORAGE == "disk":
        return save_file_to_disk(settings, file, file_name)
    elif settings.FILE_STORAGE == "cloud_storage":
        return save_file_to_cloud_storage(settings, file, file_name)
    else:
        raise NotImplemented()


def save_file_to_cloud_storage(settings, file, file_name):
    client: minio.Minio = get_minio_client(settings)
    octet_stream = io.BytesIO(file)
    client.put_object(
        bucket_name=settings.S3_BUCKET,
        object_name=file_name,
        data=octet_stream,
        length=len(octet_stream.getbuffer())
    )

    return {
        "storage": "cloud_storage",
        "object_key": file_name
    }


def save_file_to_disk(settings, file, file_name):
    target_file_path = Path(settings.UPLOAD_DIR).joinpath(file_name)
    with open(target_file_path, "wb") as target_file:
        target_file.write(file)

    return {
        "storage": "disk",
        "filepath": str(target_file_path)
    }
