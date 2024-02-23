from typing import Any
from django.contrib import admin
from ecommerce.apps.promotion.models import *
from ecommerce.apps.promotion.tasks import *


@admin.register(PromotionType)
class PromotionTypeAdmin(admin.ModelAdmin):
    """
    The PromotionTypeAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the PromotionType model.
    """

    list_display = ("name",)
    fields = (
        "id",
        "name",
    )
    readonly_fields = ("id",)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    """
    The CouponAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the Coupon model.
    """

    list_display = ("name", "code")
    filter = (
        "id",
        "name",
        "code",
        "description",
    )
    search_fields = ("name", "code", "description")
    readonly_fields = (
        "id",
        "code",
    )


class ProductsOnPromotionInline(admin.TabularInline):
    """
    The ProductsOnPromotionInline class inherits from Django's TabularInline class.
    It represents the inline interface for the ProductsOnPromotion model.
    """

    model = Promotion.products_on_promotion.through
    extra = 1


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    """
    The PromotionAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the Promotion model.
    """

    list_display = ("name", "promotion_reduction", "is_active", "is_schedule")
    filter = (
        "id",
        "name",
        "description",
        "promotion_reduction",
        "is_active",
        "is_schedule",
        "promotion_start",
        "promotion_end",
        "promotion_type",
        "coupon",
    )
    list_filter = (
        "promotion_reduction",
        "is_active",
        "is_schedule",
        "promotion_start",
        "promotion_end",
    )
    search_fields = ("name", "description")
    autocomplete_fields = ("coupon",)
    readonly_fields = ("id",)
    inlines = [ProductsOnPromotionInline]

    def save_model(self, request, obj, form, change) -> None:
        """
        The save_model method allows us to override the default behavior of the save_model method.
        """
        super().save_model(request, obj, form, change)
        promotion_prices(obj.id)
        promotion_management.delay()
