import io
import uuid
from pathlib import Path
from climsoft_api.config import settings
from climsoft_api.utils.s3 import get_s3_client


def save_file(settings, file, file_type):
    file_name = f"{uuid.uuid4().hex}.{file_type.split('/')[-1]}"
    if settings.storage == "disk":
        return save_file_to_disk(file, file_name)
    elif settings.storage == "s3":
        return save_file_to_s3(settings, file, file_name)
    else:
        raise NotImplemented()


def save_file_to_s3(settings, file, file_name):
    s3_client = get_s3_client(settings)
    s3_client.upload_fileobj(
        io.BytesIO(file),
        settings.S3_BUCKET,
        file_name
    )
    return {
        "storage": "s3",
        "object_key": file_name
    }


def save_file_to_disk(file, file_name):
    target_file_path = Path(settings.UPLOAD_DIR).joinpath(file_name)
    with open(target_file_path, "wb") as target_file:
        target_file.write(file)

    return {
        "storage": "disk",
        "filepath": str(target_file_path)
    }
