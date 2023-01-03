from pathlib import Path, PosixPath

import loguru
from pydantic import BaseSettings, Field

_ROOT = Path(__file__).parent


class Settings(BaseSettings):
    ROOT: PosixPath = _ROOT
    UUID: str = Field(..., env="UUID")
    LOGLEVEL: str = "INFO"

    class Config:
        env_file = _ROOT.joinpath(".env")


logger = loguru.logger
settings = Settings()

if __name__ == "__main__":
    logger.info(settings.UUID)
