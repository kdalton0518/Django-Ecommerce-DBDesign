# Import base settings
from ecommerce.settings.base import *


# Set the debug status
DEBUG = True


# PostgreSQL database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "ecommerce",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
