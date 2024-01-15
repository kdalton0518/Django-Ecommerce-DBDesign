from django.contrib import admin
from ecommerce.apps.inventory.models import Category


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
