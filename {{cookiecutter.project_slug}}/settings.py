from pydantic import BaseSettings, PostgresDsn, RedisDsn, validator, ValidationError
from typing import Optional

class Settings(BaseSettings):
    """Settings for the Telegram bot."""

    TELEGRAM_BOT_TOKEN: str
    DATABASE_URL: Optional[str] = None
    REDIS_URL: Optional[str] = None

    @validator("DATABASE_URL", "REDIS_URL", pre=True, always=True)
    def check_url_scheme(cls, value: Optional[str]):
        if value is None:
            return value

        # Now, validate against the DSN types
        try:
            if "postgres" in value:
                return PostgresDsn.validate(value)
            # elif "redis" in value:
            #     return RedisDsn.validate(value)
        except ValidationError:
            raise ValueError(f"Invalid URL provided for {value}")

        return value

    class Config:
        """Configuration for the settings."""
        env_file = ".env"

settings = Settings()
