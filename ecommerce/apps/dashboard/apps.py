from django.apps import AppConfig


class DashboardConfig(AppConfig):
    """
    The DashboardConfig class inherits from Django's AppConfig class.
    It represents the configuration for the dashboard app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "ecommerce.apps.dashboard"
