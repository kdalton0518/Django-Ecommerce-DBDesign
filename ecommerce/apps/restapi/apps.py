from django.apps import AppConfig


class RestapiConfig(AppConfig):
    """
    The RestapiConfig class inherits from Django's AppConfig class.
    It represents the configuration for the restapi app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "ecommerce.apps.restapi"
