from pydantic_settings import BaseSettings

from typing import Optional

from config.constants import Constants

class Settings(Constants, BaseSettings):
    BOT_TOKEN: str
    BOT_WEBHOOK_PATH: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    FASTAPI_HOST: Optional[str]
    FASTAPI_PORT: Optional[int]

    @property
    def db_url(self) -> str:
        protocol='postgresql+asyncpg'
        user_data = f'{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}'
        server_data = f'{self.POSTGRES_HOST}:{self.POSTGRES_PORT}'
        return f'{protocol}://{user_data}@{server_data}/{self.POSTGRES_DB}'

    @property
    def bot_webhook_url(self) -> str:
        return f'{self.FASTAPI_HOST}:{self.FASTAPI_PORT}/{self.BOT_WEBHOOK_PATH}'

    class Config:
        env_file = 'config/.env'


settings = Settings()
