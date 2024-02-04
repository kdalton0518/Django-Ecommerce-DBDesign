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
        "parent_category/<slug:parent_category_slug>/sub_categories/",
        views.DemoSubCategoriesView.as_view(),
        name="demo_sub_categories",
    ),
    path(
        "sub_category/<slug:category_slug>/products/",
        views.DemoSubCategoriesProductsView.as_view(),
        name="demo_sub_categories_products",
    ),
    path(
        "product/<slug:product_slug>/details/",
        views.DemoProductDetailView.as_view(),
        name="demo_product_detail",
    ),
    path(
        "product_types/",
        views.DemoProductTypesView.as_view(),
        name="demo_product_types",
    ),
    path(
        "product_type/<str:product_type_id>/products/",
        views.DemoProductTypeProductsView.as_view(),
        name="demo_product_type_products",
    ),
    path(
        "brands/",
        views.DemoBrandsView.as_view(),
        name="demo_brands",
    ),
    path(
        "brand/<str:brand_id>/products/",
        views.DemoBrandProductsView.as_view(),
        name="demo_brand_products",
    ),
]
