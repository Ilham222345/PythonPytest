from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    base_url: str
    username: str
    password: str
    environment: str = "def"

    class Config:
        env_file = Path(__file__).resolve().parent.parent / ".env.test"
        env_file_encoding = "utf-8"


settings = Settings()
