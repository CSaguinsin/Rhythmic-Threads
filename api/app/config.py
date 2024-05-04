import os

from dotenv import load_dotenv
from flask import current_app

load_dotenv()

# General Config
DEBUG = os.getenv("DEBUG")
SEED = os.getenv("SEED")
TESTING = False

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE = os.path.join(current_app.instance_path, "rt_dev.sqlite")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_TOKEN_LOCATION = ["cookies", "headers"]

current_app.url_map.strict_slashes = False
