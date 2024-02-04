# Import base settings
from ecommerce.settings.base import *


# Set the debug status
DEBUG = False


# Set allowed hosts
ALLOWED_HOSTS = [".vercel.app"]


# PostgreSQL database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ecommerce",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
