import logging
from pathlib import Path
import loguru
from airtest.core.android import Android
from pydantic import Field
from pydantic_settings import BaseSettings
from airtest.core import api

_ROOT = Path(__file__).parent


class Settings(BaseSettings):
    ROOT: Path = _ROOT
    UUID: str = Field(..., alias="UUID")
    LOGLEVEL: str = Field(default="ERROR", alias="LOGLEVEL")

    class Config:
        env_file = _ROOT.joinpath("env.toml")


settings = Settings()

logging.getLogger("airtest").setLevel(settings.LOGLEVEL)  # airtest日志级别
logger = loguru.logger

# device: Android = api.init_device(uuid=settings.UUID)

if __name__ == '__main__':
    print(settings.UUID)