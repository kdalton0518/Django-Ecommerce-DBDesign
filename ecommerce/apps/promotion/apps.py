from django.apps import AppConfig


class PromotionConfig(AppConfig):
    """
    The PromotionConfig class inherits from Django's AppConfig class.
    It represents the configuration for the promotion app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "ecommerce.apps.promotion"
