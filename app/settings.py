from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    RATE_LIMITING_ENABLE: bool = False
    RATE_LIMITING_FREQUENCY: str = "2/3seconds"

    # CORS settings
    CORS_ORIGINS: list[str] = ["*"]  # Default to allow all origins
    # Redis / cache settings
    REDIS_URL: str = "redis://localhost:6379/0"
    CACHE_EXPIRE: int = 60  # seconds


settings = Settings()
