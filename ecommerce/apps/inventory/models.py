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
        default=uuid.uuid4,
        verbose_name="Product Website ID",
        help_text=_("format: required, max length 36 characters"),
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


class ProductType(models.Model):
    """
    The ProductType class represents the type of a product.

    Attributes:
        id (CharField): The primary key for the ProductType model. It's a CharField that gets its default value
                        from the uuid.uuid4 function and is not editable.
        name (CharField): A CharField that stores the type of the product. It is required, unique, and has a maximum length of 255 characters.
    """

    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Type of Product"),
        help_text=_("format: required, unique, max-255"),
    )

    class Meta:
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    """
    The Brand class represents the brand of a product.

    Attributes:
        id (CharField): The primary key for the Brand model. It's a CharField that gets its default value
                        from the uuid.uuid4 function and is not editable.
        name (CharField): A CharField that stores the name of the brand. It is required, unique, and has a maximum length of 255 characters.
    """

    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Brand Name"),
        help_text=_("format: required, unique, max-255"),
    )

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ["name"]

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    """
    The ProductAttribute class represents the attributes of a product.

    Attributes:
        id (CharField): The primary key for the ProductAttribute model. It's a CharField that gets its default value
                        from the uuid.uuid4 function and is not editable.
        name (CharField): A CharField that stores the name of the product attribute. It is required, unique, and has a maximum length of 255 characters.
        description (TextField): A TextField that stores the description of the product attribute. It is required.
    """

    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Product Attribute Name"),
        help_text=_("format: required, unique, max-255"),
    )
    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Product Attribute Description"),
        help_text=_("format: required"),
    )

    class Meta:
        verbose_name = "Product Attribute"
        verbose_name_plural = "Product Attributes"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name


class ProductAttributeValue(models.Model):
    """
    The ProductAttributeValue class represents the value of a product attribute.

    Attributes:
        id (CharField): The primary key for the ProductAttributeValue model. It's a CharField that gets its default value
                        from the uuid.uuid4 function and is not editable.
        product_attribute (ForeignKey): A ForeignKey that links to a ProductAttribute instance.
        attribute_value (CharField): A CharField that stores the value of the product attribute. It is required and has a maximum length of 255 characters.
    """

    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36
    )
    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name="product_attribute",
        on_delete=models.PROTECT,
    )
    attribute_value = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Attribute Value"),
        help_text=_("format: required, max-255"),
    )

    class Meta:
        verbose_name = "Product Attribute Value"
        verbose_name_plural = "Product Attribute Values"

    def __str__(self):
        return f"{self.product_attribute.name} : {self.attribute_value}"


class ProductInventory(models.Model):
    """
    The ProductInventory class represents a product's inventory details.

    Attributes:
        id (CharField): The primary key for the ProductInventory model. It's a CharField that gets its default value
                        from the uuid.uuid4 function and is not editable.
        sku (CharField): A CharField that stores the product's Stock Keeping Unit (SKU). It is required and has a maximum length of 36 characters.
        upc (CharField): A CharField that stores the product's Universal Product Code (UPC). It is required and has a maximum length of 36 characters.
        product_type (ForeignKey): A ForeignKey that links to the ProductType model. It represents the type of the product.
        product (ForeignKey): A ForeignKey that links to the Product model. It represents the product itself.
        brand (ForeignKey): A ForeignKey that links to the Brand model. It represents the brand of the product.
        attribute_values (ManyToManyField): A ManyToManyField that represents the product attributes of the product.
        is_active (BooleanField): A BooleanField that indicates whether the product is active. It is required and its default value is True.
        retail_price (DecimalField): A DecimalField that stores the recommended retail price of the product. It is required and has a maximum value of 999.99.
        store_price (DecimalField): A DecimalField that stores the regular store price of the product. It is required and has a maximum value of 999.99.
        sale_price (DecimalField): A DecimalField that stores the sale price of the product. It is required and has a maximum value of 999.99.
        weight (FloatField): A FloatField that stores the weight of the product. It is required.
        created_at (DateTimeField): A DateTimeField that stores the date and time when the product inventory was created. It is not editable.
        updated_at (DateTimeField): A DateTimeField that stores the date and time when the product inventory was last updated.
    """

    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36
    )
    sku = models.CharField(
        default=uuid.uuid4,
        editable=False,
        max_length=36,
        verbose_name="Product Stock Keeping Unit",
        help_text=_("format: required, max length 36 characters"),
        null=False,
        blank=False,
        unique=True,
    )
    upc = models.CharField(
        default=uuid.uuid4,
        editable=False,
        max_length=36,
        verbose_name="Product Universal Product Code",
        help_text=_("format: required, max length 36 characters"),
        null=False,
        blank=False,
        unique=True,
    )
    product_type = models.ForeignKey(
        ProductType, related_name="product_type", on_delete=models.PROTECT
    )
    product = models.ForeignKey(
        Product, related_name="product", on_delete=models.PROTECT
    )
    brand = models.ForeignKey(Brand, related_name="brand", on_delete=models.PROTECT)
    attribute_values = models.ManyToManyField(
        ProductAttributeValue,
        related_name="product_attribute_values",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Product Visibility"),
        help_text=_("format: true=product visible"),
    )
    retail_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Recommended Retail Price"),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    store_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Regular Store Price"),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    sale_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Sale Price"),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    weight = models.FloatField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Product Weight"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date Sub-Product Created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date Sub-Product Updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        verbose_name = "Product Inventory"
        verbose_name_plural = "Product Inventories"

    def __str__(self):
        return self.product.name


class Media(models.Model):
    """
    The Media class represents the media associated with a product inventory.

    Attributes:
        id (CharField): The primary key for the Media model. It's a CharField that gets its default value
                        from the uuid.uuid4 function and is not editable.
        product_inventory (ForeignKey): A ForeignKey that links to a ProductInventory instance.
        image (ImageField): An ImageField that stores the image of the product. It is required and has a default image.
        alt_text (CharField): A CharField that stores the alternative text for the image. It is required and has a maximum length of 255 characters.
        is_feature (BooleanField): A BooleanField that indicates whether the image is the default image for the product.
        created_at (DateTimeField): A DateTimeField that stores the date and time the media was created. It is automatically set when the media is created.
        updated_at (DateTimeField): A DateTimeField that stores the date and time the media was last updated. It is automatically set when the media is updated.

    Meta:
        verbose_name (str): A string that provides a human-readable name for the Media model.
        verbose_name_plural (str): A string that provides a human-readable plural name for the Media model.
    """

    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36
    )
    product_inventory = models.ForeignKey(
        ProductInventory,
        on_delete=models.PROTECT,
        related_name="media_product_inventory",
    )
    image = models.ImageField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Product Image"),
        upload_to="images/",
        default="images/default.png",
        help_text=_("format: required, default-default.png"),
    )
    alt_text = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Alternative Text"),
        help_text=_("format: required, max-255"),
    )
    is_feature = models.BooleanField(
        default=False,
        verbose_name=_("Product Default Image"),
        help_text=_("format: default=false, true=default image"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Product Visibility"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date Sub-Product Created"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")


class Stock(models.Model):
    """
    The Stock class represents the stock of a product inventory.

    Attributes:
        id (CharField): The primary key for the Stock model. It's a CharField that gets its default value
                        from the uuid.uuid4 function and is not editable.
        product_inventory (OneToOneField): A OneToOneField that links to a ProductInventory instance.
        last_checked (DateTimeField): A DateTimeField that stores the date and time the stock was last checked. It can be null and blank.
        units (IntegerField): An IntegerField that stores the number of units in stock. It is required and has a default value of 0.
        units_sold (IntegerField): An IntegerField that stores the number of units sold. It is required and has a default value of 0.
    """

    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36
    )
    product_inventory = models.OneToOneField(
        ProductInventory,
        related_name="product_inventory",
        on_delete=models.PROTECT,
    )
    last_checked = models.DateTimeField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("Inventory Stock Check Date"),
        help_text=_("format: Y-m-d H:M:S, null-true, blank-true"),
    )
    units = models.IntegerField(
        default=0,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Units/Qty Of Stock"),
        help_text=_("format: required, default-0"),
    )
    units_sold = models.IntegerField(
        default=0,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Units Sold to Date"),
        help_text=_("format: required, default-0"),
    )

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

    def __str__(self):
        return self.product.name
