from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    database_host: str = Field(env="DATABASE_HOST")
    database_port: int = Field(5432, env="DATABASE_PORT")
    database_name: str = Field(env="DATABASE_NAME")
    database_username: str = Field(..., env="DATABASE_USER")  # <--- здесь alias
    database_password: str = Field(env="DATABASE_PASSWORD")

    def get_asynk_database_url(self) -> str:
        url = f"""postgresql+asyncpg://{self.database_username}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_name}"""
        return url

    def get_synk_database_url(self) -> str:
        url = f"""postgresql://{self.database_username}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_name}"""
        return url


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()