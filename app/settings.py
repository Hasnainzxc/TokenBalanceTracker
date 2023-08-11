# app/settings.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_db_url: str
   
    coingecko_api_url: str

    class Config:
        env_file = ".env"

settings = Settings()
