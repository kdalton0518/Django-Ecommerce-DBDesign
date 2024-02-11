from django.urls import path
from . import views


urlpatterns = [
    path("", views.RestAPIHome.as_view(), name="restapi_home"),
    path(
        "parent_categories/list/",
        views.RestAPIParentCategories.as_view({"get": "list"}),
        name="restapi_parent_categories_list",
    ),
    path(
        "parent_categories/sub_categories/list/",
        views.RestAPISubCategories.as_view({"get": "list"}),
        name="restapi_sub_categories_list",
    ),
    path(
        "parent_categories/sub_categories/products/list/",
        views.RestAPISubCategoriesProducts.as_view({"get": "list"}),
        name="restapi_sub_categories_products_list",
    ),
]
