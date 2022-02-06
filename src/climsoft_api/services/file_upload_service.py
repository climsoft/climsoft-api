import uuid
from pathlib import Path


def save_file(storage, file, file_type):
    file_name = f"{uuid.uuid4().hex}.{file_type.split('/')[-1]}"
    if storage == "disk":
        return save_file_to_disk(file, file_name)
    elif storage == "s3":
        return save_file_to_s3(file, file_name)
    else:
        raise NotImplemented()


def save_file_to_s3(file, file_name):
    pass


def save_file_to_disk(file, file_name):
    target_file_path = Path("/uploads").joinpath(file_name)
    with open(target_file_path, "wb") as target_file:
        target_file.write(file)

    return target_file_path

