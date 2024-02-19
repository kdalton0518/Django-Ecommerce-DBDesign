from django.contrib import admin
from ecommerce.apps.promotion.models import *


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
    list_filter = ("name",)
    search_fields = ("name",)
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
    list_filter = ("name", "code")
    search_fields = ("name", "code", "description")
    readonly_fields = (
        "id",
        "code",
    )


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
        "name",
        "promotion_reduction",
        "is_active",
        "is_schedule",
        "promotion_start",
        "promotion_end",
    )
    search_fields = ("name", "description")
    autocomplete_fields = ("coupon",)
    readonly_fields = ("id",)
