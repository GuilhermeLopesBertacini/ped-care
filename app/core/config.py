from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application configuration settings.
    """
    GEMINI_API_KEY: str = Field(..., description="API key for Gemini service")
    DB_HOST: str = Field(..., description="Database host")
    DB_PORT: int = Field(..., description="Database port")
    DB_NAME: str = Field(..., description="Database name")
    DB_USER: str = Field(..., description="Database user")
    DB_PASSWORD: SecretStr = Field(..., description="Database password")
    SECRET_KEY: SecretStr = Field(..., description="Secret key for application")

settings = Settings()