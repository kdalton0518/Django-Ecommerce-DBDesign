# Import os
import os


# Import base settings
from ecommerce.settings.base import *


# Set the debug status
DEBUG = False


# Set allowed hosts
ALLOWED_HOSTS = [".vercel.app"]


# Database
DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "ecommerce_db",
        "ENFORCE_SCHEMA": False,
        "CLIENT": {
            "host": os.environ["MONGO_DB_URI"],
            "username": os.environ["MONGO_DB_USERNAME"],
            "password": os.environ["MONGO_DB_PASSWORD"],
        },
    }
}