import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Category Name",
        help_text=_("format: required, max length 100 characters"),
        null=False,
        blank=False,
        unique=False,
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name="Category Slug",
        help_text=_(
            "format: required, max length 100 characters, letters, numbers, underscores or hyphens"
        ),
        null=False,
        blank=False,
        unique=False,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Is Active",
        help_text=_("format: required, default True"),
        null=False,
        blank=False,
    )

    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name="Parent Category",
        help_text=_("format: optional"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name
