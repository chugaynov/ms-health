from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    NAME: str = "FastAPI Application"
    OPENAPI_PREFIX: str = ""
    VERSION: str = "0.1.0"
    ADDRESS: str = "0.0.0.0"
    PORT: int = 8080
    LOG_DEFAULT_FORMATTER: str = "uvicorn.logging.DefaultFormatter"


class SentrySettings(BaseSettings):
    DSN: str = ""
    ENVIRONMENT: str = "development"


class Settings(BaseSettings):
    APP: AppSettings = AppSettings()
    SENTRY: SentrySettings = SentrySettings()


settings = Settings()