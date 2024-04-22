import os
from dotenv import load_dotenv


class Config:
    load_dotenv()

    DEBUG = os.getenv("DEBUG")

    # https://flask.palletsprojects.com/en/2.3.x/quickstart/#sessions
    # python -c 'import secrets; print(secrets.token_hex())'
    SECRET_KEY = os.getenv("SECRET_KEY")
