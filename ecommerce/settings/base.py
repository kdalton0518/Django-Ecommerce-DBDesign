# Imports
import dotenv
import os
from pathlib import Path
import datetime


# Load environment variables
dotenv.load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "5xy#)2=e^fe%!ilv+o&6h&t&ar=@uc9_^#q8gc7y5kl@(#u)q)"


# Set the auth user model
AUTH_USER_MODEL = "dashboard.User"


# Installed apps list
INSTALLED_APPS = [
    # Default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party apps
    "corsheaders",
    "django_extensions",
    "django_bootstrap5",
    "django_elasticsearch_dsl",
    "rest_framework",
    "drf_yasg",
    # Internal apps
    "ecommerce.apps.dashboard.apps.DashboardConfig",
    "ecommerce.apps.inventory.apps.InventoryConfig",
    "ecommerce.apps.management.apps.ManagementConfig",
    "ecommerce.apps.demo.apps.DemoConfig",
    "ecommerce.apps.promotion.apps.PromotionConfig",
    "ecommerce.apps.jwtauth.apps.JwtauthConfig",
    "ecommerce.apps.restapi.apps.RestapiConfig",
]


# Set the CORS origin whitelist
CORS_ALLOWED_ORIGINS = ["https://*"]


# Middleware list
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Root URL configuration
ROOT_URLCONF = "ecommerce.urls"


# Set templates config
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# WSGI application
WSGI_APPLICATION = "ecommerce.wsgi.application"


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_L10N = True
# USE_TZ = True


# Default auto field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Set the static files URL
STATIC_URL = "/static/"

# Set the static files root
STATIC_ROOT = BASE_DIR.parent / "staticfiles" / "static"


# # Set the static files directories
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]


# Set the static files storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Elastic search configuration
ELASTICSEARCH_DSL = {
    "default": {
        "hosts": ["http://esearch:9200", "http://esearch:9300"],
        "http_auth": ("admin", "admin"),
    }
}


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    # "DEFAULT_THROTTLE_RATES": {"anon": "10/hour", "user": "100/hour"},
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": [
        "Bearer",
    ],
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(minutes=60),
}
