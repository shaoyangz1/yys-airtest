import logging
from pathlib import Path
import loguru
from pydantic import Field
from pydantic_settings import BaseSettings
from airtest.core import api

_ROOT = Path(__file__).parent


class Settings(BaseSettings):
    ROOT: Path = _ROOT
    UUID: str = Field(..., env="UUID")
    LOGLEVEL: str = "ERROR"

    class Config:
        env_file = _ROOT.joinpath("env.toml")


settings = Settings()
logging.getLogger("airtest").setLevel(settings.LOGLEVEL)  # airtest日志级别
logger = loguru.logger
api.init_device(uuid=settings.UUID)
