import os

from pydantic import BaseSettings
from pydantic.networks import AnyUrl

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))


class Settings(BaseSettings):
    SECRET_KEY: str = "some-random-unique-secret-key"
    DATABASE_URI: AnyUrl = "mysql+mysqldb://root:password@mariadb:3306/climsoft"
    FILE_STORAGE: str = "disk"
    UPLOAD_DIR: str = "/climsoft_uploads"
    S3_BUCKET: str = "climsoft-paper-archive"
    AWS_REGION: str = "eu-west-2"
    AWS_ACCESS_KEY_ID: str = "replace it"
    AWS_SECRET_ACCESS_KEY: str = "replace it"
    S3_SIGNED_URL_VALIDITY: int = 6
    MOUNT_STATIC: bool = True
    MYSQL_DEFAULT_USER: str = "root"

    class Config:
        env_prefix = "CLIMSOFT_"
        case_sensitive = True
        env_file_encoding = "utf-8"


settings = Settings()
