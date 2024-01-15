from django.contrib import admin
from ecommerce.apps.inventory.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    The CategoryAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the Category model.
    """

    list_display = (
        "name",
        "slug",
        "parent",
    )
    list_filter = ("parent",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    The ProductAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the Product model.
    """

    list_display = (
        "web_id",
        "name",
        "slug",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    autocomplete_fields = ("category",)
    prepopulated_fields = {"slug": ("name",)}
