from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "HealthAgents API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Multi-Agent Medical Intelligence Platform"

    class Config:
        env_file = ".env"


settings = Settings()