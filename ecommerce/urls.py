from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.shortcuts import render
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Django E-commerce REST API",
        default_version="v1",
        description="A Django E-commerce REST API",
        contact=openapi.Contact(email="rohit.vilas.ingole@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        lambda request: render(request, "base.html"),
        name="home",
    ),
    path("demo/", include("ecommerce.apps.demo.urls")),
    path("restapi/jwtauth/", include("ecommerce.apps.jwtauth.urls")),
    path("restapi/", include("ecommerce.apps.restapi.urls")),
    path(
        "restapi/swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "restapi/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "restapi/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
