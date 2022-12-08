from pathlib import Path

import loguru
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    ROOT: Path = Path(__file__).parent
    UUID: str = Field(..., env="UUID")
    LOGLEVEL: str = "INFO"

    class Config:
        env_file = ".env"


logger = loguru.logger
settings = Settings()

if __name__ == "__main__":
    logger.info(settings.UUID)
