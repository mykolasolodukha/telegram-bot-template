from pydantic import BaseSettings, PostgresDsn, RedisDsn, validator, ValidationError
from typing import Optional

class Settings(BaseSettings):
    """Settings for the Telegram bot."""

    TELEGRAM_BOT_TOKEN: str

    class Config:
        """Configuration for the settings."""
        env_file = ".env"

settings = Settings()
