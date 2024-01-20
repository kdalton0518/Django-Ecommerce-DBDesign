from django.contrib import admin
from ecommerce.apps.inventory.models import (
    Category,
    Product,
    ProductType,
    Brand,
    ProductInventory,
    ProductAttribute,
    ProductAttributeValue,
    ProductAttributeValues,
)


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


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    """
    The ProductTypeAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the ProductType model.
    """

    list_display = (
        "id",
        "name",
    )
    search_fields = ("name",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
    The BrandAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the Brand model.
    """

    list_display = (
        "id",
        "name",
    )
    search_fields = ("name",)


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    """
    The ProductInventoryAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the ProductInventory model.
    """

    list_display = (
        "product_type",
        "product",
        "brand",
        "is_active",
        "retail_price",
        "store_price",
        "sale_price",
        "weight",
    )
    list_filter = ("is_active",)
    search_fields = (
        "product_type__name, product__name",
        "brand__name",
        "retail_price",
        "store_price",
        "sale_price",
        "weight",
    )
    autocomplete_fields = ("product",)


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    """
    The ProductAttributeAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the ProductAttribute model.
    """

    list_display = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name", "description")


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    """
    The ProductAttributeValueAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the ProductAttributeValue model.
    """

    list_display = ("id", "product_attribute", "attribute_value")
    list_filter = ("product_attribute", "attribute_value")
    search_fields = ("product_attribute", "attribute_value")
    autocomplete_fields = ["product_attribute"]


@admin.register(ProductAttributeValues)
class ProductAttributeValuesAdmin(admin.ModelAdmin):
    """
    The ProductAttributeValuesAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the ProductAttributeValues model.
    """

    list_display = ("id", "attributevalues", "productinventory")
    list_filter = ("attributevalues", "productinventory")
    search_fields = ("attributevalues", "productinventory")
    autocomplete_fields = ("attributevalues", "productinventory")
