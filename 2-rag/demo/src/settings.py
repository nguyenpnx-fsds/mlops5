from pydantic_settings import BaseSettings
from pydantic import SecretStr
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Settings for the application."""

    # OpenAI API key
    OPENAI_API_KEY: SecretStr

    class Config:
        """Pydantic config."""

        env_file = "../.env"
        env_file_encoding = "utf-8"


SETTINGS = Settings()  # type: ignore
