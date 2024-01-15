from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    The UserAdmin class inherits from Django's ModelAdmin class.
    It represents the admin interface for the User model.
    """

    fieldsets = (
        (None, {"fields": ("id", "username", "email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    readonly_fields = (
        "id",
        "last_login",
    )

    save_on_top = True

    list_display = (
        "id",
        "username",
        "email",
        "is_superuser",
        "is_active",
        "last_login",
    )

    list_filter = ("is_staff", "is_superuser", "is_active", "groups")

    search_fields = ("first_name", "last_name", "email")

    ordering = ("email",)

    filter_horizontal = (
        "groups",
        "user_permissions",
    )
