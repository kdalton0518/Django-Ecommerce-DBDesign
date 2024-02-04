from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.shortcuts import render


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        lambda request: render(request, "base.html"),
        name="home",
    ),
    path("demo/", include("ecommerce.apps.demo.urls")),
]
