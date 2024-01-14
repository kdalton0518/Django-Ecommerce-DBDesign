# Import base settings
from ecommerce.settings.base import *


# Set the debug status
DEBUG = True


# Database
DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "ecommerce_db",
        "ENFORCE_SCHEMA": False,
        "CLIENT": {
            "host": "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.1",
        },
    }
}