from pathlib import Path, PosixPath, WindowsPath

import loguru
from pydantic import Field
from pydantic_settings import BaseSettings

_ROOT = Path(__file__).parent


class Settings(BaseSettings):
    ROOT: Path = _ROOT
    UUID: str = Field(..., env="UUID")
    LOGLEVEL: str = "INFO"

    class Config:
        env_file = _ROOT.joinpath("env.toml")


logger = loguru.logger
settings = Settings()

if __name__ == "__main__":
    logger.info(settings.ROOT)
