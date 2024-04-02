import os
from dotenv import load_dotenv
import secrets

load_dotenv()


class Settings:
    SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL")
    ACCESS_TOKEN_EXPIRATION_MINUTES: int = int(os.environ.get("ACCESS_TOKEN_EXPIRATION_MINUTES"))
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    # JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or secrets.token_urlsafe(32)
