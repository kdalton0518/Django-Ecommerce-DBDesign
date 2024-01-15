from django.apps import AppConfig


class InventoryConfig(AppConfig):
    """
    The InventoryConfig class inherits from Django's AppConfig class.
    It represents the configuration for the inventory app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "ecommerce.apps.inventory"
