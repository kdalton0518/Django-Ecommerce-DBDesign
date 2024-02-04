from django.apps import AppConfig


class ManagementConfig(AppConfig):
    """
    The ManagementConfig class inherits from Django's AppConfig class.
    It represents the configuration for the management app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "ecommerce.apps.management"
