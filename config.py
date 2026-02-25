import os
from dotenv import load_dotenv

load_dotenv() # loads variables from .env


# TODO: Load SECRET_KEY and CURRENCY_SYMBOL from environment variables using python-dotenv
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret") # try read the SECRET_KEY from env, and default value if the variable isn't found
    CURRENCY_SYMBOL = os.getenv("CURRENCY_SYMBOL", "$")

    @classmethod
    def get_currency_symbol(cls : type) -> str:
        return cls.CURRENCY_SYMBOL
    
    @classmethod
    def get_secret_key(cls : type) -> str:
        return cls.SECRET_KEY