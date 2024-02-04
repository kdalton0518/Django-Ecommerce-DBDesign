from django.urls import path
from . import views


urlpatterns = [
    path("", views.DemoHomeView.as_view(), name="demo_home"),
    path(
        "parent_categories/",
        views.DemoParentCategoriesView.as_view(),
        name="demo_parent_categories",
    ),
    path(
        "sub_categories/<str:parent_category_id>/",
        views.DemoSubCategoriesView.as_view(),
        name="demo_sub_categories",
    ),
    path(
        "products/<str:category_id>/",
        views.DemoProductsView.as_view(),
        name="demo_products",
    ),
]
