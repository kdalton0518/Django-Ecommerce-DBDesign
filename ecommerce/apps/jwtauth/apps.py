from django.apps import AppConfig


class JwtauthConfig(AppConfig):
    """
    The JwtauthConfig class inherits from Django's AppConfig class.
    It represents the configuration for the jwtauth app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "ecommerce.apps.jwtauth"
