import os


from pydantic import BaseSettings
from pydantic.networks import AnyUrl

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))


class Settings(BaseSettings):
    SECRET_KEY: str
    DATABASE_URI: AnyUrl

    class Config:
        env_prefix = "CLIMSOFT_"
        case_sensitive = True
        env_file_encoding = "utf-8"


settings = Settings()
