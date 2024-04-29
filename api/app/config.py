import os
from dotenv import load_dotenv


class Config:
    load_dotenv()

    DEBUG = os.getenv("DEBUG")

    # Whether to seed sample data to db
    SEED = os.getenv("SEED")

    # https://flask.palletsprojects.com/en/2.3.x/quickstart/#sessions
    # python -c 'import secrets; print(secrets.token_hex())'
    SECRET_KEY = os.getenv("SECRET_KEY")
