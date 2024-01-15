import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """
    The Category class inherits from MPTTModel.
    It represents a hierarchical category structure for products.

    Attributes:
        id (CharField): The primary key for the Category model. It's a CharField that gets its default value
                        from the uuid.uuid4 function and is not editable.
        name (CharField): A CharField that stores the category name. It is required and has a maximum length of 100 characters.
        slug (SlugField): A SlugField that stores the URL-friendly version of the category name. It is required and has a maximum length of 100 characters.
        is_active (BooleanField): A BooleanField that indicates whether the category is active. It is required and its default value is True.
        parent (TreeForeignKey): A TreeForeignKey that represents the parent category of the current category. It is not required and can be null.
    """

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


class Product(models.Model):
    """
    The Product class represents a product in the inventory.

    Attributes:
        id (CharField): The primary key for the Product model. It's a CharField that gets its default value
                        from the uuid.uuid4 function and is not editable.
        web_id (CharField): A CharField that stores the product ID. It is required and has a maximum length of 36 characters.
        name (CharField): A CharField that stores the product name. It is required and has a maximum length of 100 characters.
        slug (SlugField): A SlugField that stores the URL-friendly version of the product name. It is required and has a maximum length of 100 characters.
        description (TextField): A TextField that stores the product description. It is required and has no maximum length.
        is_active (BooleanField): A BooleanField that indicates whether the product is active. It is required and its default value is True.
        category (TreeManyToManyField): A ManyToManyField that represents the product category. It is not required and can be null.
        created_at (DateTimeField): A DateTimeField that stores the date and time when the product was created. It is not required and can be null.
        updated_at (DateTimeField): A DateTimeField that stores the date and time when the product was last updated. It is not required and can be null.
    """

    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36
    )
    web_id = models.CharField(
        max_length=36,
        verbose_name="Product Website ID",
        help_text=_("format: required, max length 36 characters"),
        null=False,
        blank=False,
        unique=True,
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Product Name",
        help_text=_("format: required, max length 100 characters"),
        null=False,
        blank=False,
        unique=False,
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name="Product Slug",
        help_text=_(
            "format: required, max length 100 characters, letters, numbers, underscores or hyphens"
        ),
        null=False,
        blank=False,
        unique=False,
    )
    description = models.TextField(
        verbose_name="Product Description",
        help_text=_("format: required, no limit"),
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
    category = TreeManyToManyField(
        Category,
        related_name="products",
        verbose_name="Product Category",
        help_text=_("format: optional, multiple categories allowed"),
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text=_("format: YY-MM-DD hh:mm:ss, auto-generated"),
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
        help_text=_("format: YY-MM-DD hh:mm:ss, auto-generated"),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["name"]

    def __str__(self):
        return self.name
