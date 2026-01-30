import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    CURRENCY_SYMBOL = os.getenv("CURRENCY_SYMBOL", "R")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///finance.db")
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND = os.getenv(
        "CELERY_RESULT_BACKEND", "redis://localhost:6379/0"
    )
    DEBUG = os.getenv("FLASK_DEBUG", "True").lower() in ("true", "1", "yes")
    STATIC_DIR = "static"

    @classmethod
    def get_currency_symbol(cls: type) -> str:
        return cls.CURRENCY_SYMBOL

    @classmethod
    def get_secret_key(cls: type) -> str:
        return cls.SECRET_KEY

    @classmethod
    def get_database_url(cls: type) -> str:
        return cls.DATABASE_URL

    @classmethod
    def get_celery_broker_url(cls: type) -> str:
        return cls.CELERY_BROKER_URL

    @classmethod
    def get_celery_result_backend(cls: type) -> str:
        return cls.CELERY_RESULT_BACKEND

    @classmethod
    def get_debug_mode(cls: type) -> bool:
        return cls.DEBUG

    @classmethod
    def get_static_dir(cls: type) -> str:
        return cls.STATIC_DIR
