from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "HealthAgents API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Multi-Agent Medical Intelligence Platform"

    GOOGLE_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()