from django.contrib import admin
from ecommerce.apps.inventory.models import (
    Category,
    Product,
    ProductType,
    Brand,
    ProductInventory,
    ProductAttribute,
    ProductAttributeValue,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    The CategoryAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the Category model.
    """

    list_display = (
        "name",
        "parent",
    )
    fields = (
        "id",
        "name",
        "slug",
        "parent",
    )
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("id",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    The ProductAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the Product model.
    """

    list_display = (
        "name",
        "is_active",
    )
    fields = (
        "id",
        "web_id",
        "name",
        "slug",
        "description",
        "is_active",
        "category",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    autocomplete_fields = ("category",)
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = (
        "id",
        "web_id",
        "created_at",
        "updated_at",
    )


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    """
    The ProductTypeAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the ProductType model.
    """

    list_display = ("name",)
    fields = (
        "id",
        "name",
    )
    search_fields = ("name",)
    readonly_fields = ("id",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
    The BrandAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the Brand model.
    """

    list_display = ("name",)
    fields = (
        "id",
        "name",
    )
    search_fields = ("name",)
    readonly_fields = ("id",)


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    """
    The ProductInventoryAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the ProductInventory model.
    """

    list_display = (
        "product",
        "brand",
        "is_active",
        "is_on_sale",
        "is_digital",
    )
    fields = (
        "id",
        "sku",
        "upc",
        "product_type",
        "product",
        "brand",
        "attribute_values",
        "is_active",
        "retail_price",
        "store_price",
        "weight",
        "promotions",
        "promotion_price",
        "price_override",
        "is_on_sale",
        "is_digital",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "is_active",
        "is_on_sale",
        "is_digital",
    )
    search_fields = (
        "product_type__name, product__name",
        "brand__name",
        "is_on_sale",
        "is_digital",
    )
    autocomplete_fields = ("product",)
    readonly_fields = (
        "id",
        "sku",
        "upc",
        "created_at",
        "updated_at",
    )


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    """
    The ProductAttributeAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the ProductAttribute model.
    """

    list_display = ("name",)
    fields = ("id", "name", "description")
    search_fields = ("name", "description")
    readonly_fields = ("id",)


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    """
    The ProductAttributeValueAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the ProductAttributeValue model.
    """

    list_display = ("product_attribute", "attribute_value")
    fields = ("id", "product_attribute", "attribute_value")
    search_fields = ("product_attribute", "attribute_value")
    autocomplete_fields = ["product_attribute"]
    readonly_fields = ("id",)
