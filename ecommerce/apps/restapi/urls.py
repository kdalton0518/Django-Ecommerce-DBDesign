from django.urls import path
from . import views


urlpatterns = [
    path("", views.RestAPIHome.as_view(), name="restapi_home"),
    path(
        "categories/",
        views.RestAPICategories.as_view({"get": "list"}),
        name="restapi_categories_list",
    ),
    path(
        "categories/<str:id>/",
        views.RestAPICategories.as_view({"get": "retrieve"}),
        name="restapi_categories_retrieve",
    ),
    path(
        "product_types/",
        views.RestAPIProductTypes.as_view({"get": "list"}),
        name="restapi_product_types_list",
    ),
    path(
        "product_types/<str:id>/",
        views.RestAPIProductTypes.as_view({"get": "retrieve"}),
        name="restapi_product_types_retrieve",
    ),
    path(
        "brands/",
        views.RestAPIBrands.as_view({"get": "list"}),
        name="restapi_brands_list",
    ),
    path(
        "brands/<str:id>/",
        views.RestAPIBrands.as_view({"get": "retrieve"}),
        name="restapi_brands_retrieve",
    ),
    path(
        "products/",
        views.RestAPIProducts.as_view({"get": "list"}),
        name="restapi_products_list",
    ),
    path(
        "products/<str:id>/",
        views.RestAPIProducts.as_view({"get": "retrieve"}),
        name="restapi_products_retrieve",
    ),
    path(
        "product_inventory/",
        views.RestAPIProductInventory.as_view({"get": "list"}),
        name="restapi_product_inventory_list",
    ),
    path(
        "product_inventory/<str:id>/",
        views.RestAPIProductInventory.as_view({"get": "retrieve"}),
        name="restapi_product_inventory_retrieve",
    ),
]