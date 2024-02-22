import os

from celery import Celery


# Set the django settings env path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings.dev")


# Create the celery app
app = Celery("ecommerce")


# Load the celery config from the settings
app.config_from_object("django.conf:settings", namespace="CELERY")


# Auto discover the tasks
app.autodiscover_tasks()
