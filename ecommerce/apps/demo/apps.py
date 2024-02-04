from django.apps import AppConfig


class DemoConfig(AppConfig):
    """
    The DemoConfig class inherits from Django's AppConfig class.
    It represents the configuration for the demo app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "ecommerce.apps.demo"
