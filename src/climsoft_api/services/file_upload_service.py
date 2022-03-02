import uuid
from pathlib import Path
from climsoft_api.utils.s3 import get_s3_client, create_presigned_url
from climsoft_api.config import settings
import io


def save_file(storage, file, file_type):
    file_name = f"{uuid.uuid4().hex}.{file_type.split('/')[-1]}"
    if storage == "disk":
        return save_file_to_disk(file, file_name)
    elif storage == "s3":
        return save_file_to_s3(file, file_name)
    else:
        raise NotImplemented()


def save_file_to_s3(file, file_name):
    s3_client = get_s3_client()
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

