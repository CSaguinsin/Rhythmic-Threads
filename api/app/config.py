import os
from dotenv import load_dotenv

from flask import current_app

load_dotenv()

# General Config
DEBUG = os.getenv("DEBUG")
SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE = os.path.join(current_app.instance_path, "rt_dev.sqlite")
SEED = os.getenv("SEED")
TESTING = False

current_app.url_map.strict_slashes = False
