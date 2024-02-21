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
        "categories/<str:id>/products/",
        views.RestAPICategoriesProducts.as_view({"get": "list"}),
        name="restapi_categories_products_list",
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
        "product_types/<str:id>/products/",
        views.RestAPIProductTypesProducts.as_view({"get": "list"}),
        name="restapi_product_types_products_list",
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
        "brands/<str:id>/products",
        views.RestAPIBrandsProducts.as_view({"get": "list"}),
        name="restapi_brands_products_list",
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
    path(
        "promotions/",
        views.RestAPIPromotions.as_view({"get": "list"}),
        name="restapi_promotions_list",
    ),
    path(
        "promotions/<str:id>/",
        views.RestAPIPromotions.as_view({"get": "retrieve"}),
        name="restapi_promotions_retrieve",
    ),
    path(
        "promotions/<str:id>/product_inventories/",
        views.RestAPIPromotionsProductInventories.as_view({"get": "list"}),
        name="restapi_promotions_product_inventories_list",
    ),
]
