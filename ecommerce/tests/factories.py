import uuid
import factory
from faker import Faker
from pytest_factoryboy import register
from ecommerce.apps.inventory import models


faker = Faker()


@register
class CategoryFactory(factory.django.DjangoModelFactory):
    """
    The CategoryFactory class inherits from DjangoModelFactory.
    It is used to create test instances of the Category model for testing purposes.

    Attributes:
        name (Sequence): A Sequence that generates a unique name for each Category instance.
        slug (Sequence): A Sequence that generates a unique slug for each Category instance.
    """

    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: f"cat_name_{n}")
    slug = factory.Sequence(lambda n: f"cat_name_{n}")


@register
class ProductFactory(factory.django.DjangoModelFactory):
    """
    The ProductFactory class inherits from DjangoModelFactory.
    It is used to create test instances of the Product model for testing purposes.

    Attributes:
        web_id (LazyFunction): A LazyFunction that generates a unique UUID for each Product instance.
        slug (Sequence): A Sequence that generates a unique slug for each Product instance.
        name (Sequence): A Sequence that generates a unique name for each Product instance.
        description (faker.text): A Faker method that generates a random text for the product description.
        is_active (Boolean): A boolean that indicates whether the product is active. It is always set to True.
        created_at (DateTime): A string representing the date and time the product was created.
        updated_at (DateTime): A string representing the date and time the product was last updated.

    Methods:
        category: A post_generation method that adds categories to the product instance after it is created.
    """

    class Meta:
        model = models.Product
        skip_postgeneration_save = True

    web_id = factory.LazyFunction(uuid.uuid4)
    slug = factory.Sequence(lambda n: f"prod_name_{n}")
    name = factory.Sequence(lambda n: f"prod_name_{n}")
    description = faker.text()
    is_active = True
    created_at = "2021-09-04 22:14:18.279092"
    updated_at = "2021-09-04 22:14:18.279092"

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        if extracted:
            for cat in extracted:
                self.category.add(cat)


@register
class ProductTypeFactory(factory.django.DjangoModelFactory):
    """
    The ProductTypeFactory class inherits from DjangoModelFactory.
    It is used to create test instances of the ProductType model for testing purposes.

    Attributes:
        name (Sequence): A Sequence that generates a unique name for each ProductType instance.
    """

    class Meta:
        model = models.ProductType

    name = factory.Sequence(lambda n: "type_%d" % n)


@register
class BrandFactory(factory.django.DjangoModelFactory):
    """
    The BrandFactory class inherits from DjangoModelFactory.
    It is used to create test instances of the Brand model for testing purposes.

    Attributes:
        name (Sequence): A Sequence that generates a unique name for each Brand instance.
    """

    class Meta:
        model = models.Brand

    name = factory.Sequence(lambda n: "brand_%d" % n)


@register
class ProductInventoryFactory(factory.django.DjangoModelFactory):
    """
    The ProductInventoryFactory class inherits from DjangoModelFactory.
    It is used to create test instances of the ProductInventory model for testing purposes.

    Attributes:
        sku (LazyFunction): A LazyFunction that generates a unique SKU for each ProductInventory instance.
        upc (LazyFunction): A LazyFunction that generates a unique UPC for each ProductInventory instance.
        product_type (SubFactory): A SubFactory that creates a ProductType instance for the ProductInventory instance.
        product (SubFactory): A SubFactory that creates a Product instance for the ProductInventory instance.
        brand (SubFactory): A SubFactory that creates a Brand instance for the ProductInventory instance.
        is_active (Boolean): A boolean that indicates whether the product inventory is active. It is always set to 1.
        retail_price (Decimal): A decimal representing the retail price of the product.
        store_price (Decimal): A decimal representing the store price of the product.
        sale_price (Decimal): A decimal representing the sale price of the product.
        weight (Float): A float representing the weight of the product.
    """

    class Meta:
        model = models.ProductInventory

    sku = factory.LazyFunction(uuid.uuid4)
    upc = factory.LazyFunction(uuid.uuid4)
    product_type = factory.SubFactory(ProductTypeFactory)
    product = factory.SubFactory(ProductFactory)
    brand = factory.SubFactory(BrandFactory)
    is_active = 1
    retail_price = 97
    store_price = 92
    sale_price = 46
    weight = 987


@register
class MediaFactory(factory.django.DjangoModelFactory):
    """
    The MediaFactory class inherits from DjangoModelFactory.
    It is used to create test instances of the Media model for testing purposes.

    Attributes:
        product_inventory (SubFactory): A SubFactory that creates a ProductInventory instance for the Media instance.
        image (str): A string that represents the image file path. It is set to "images/default.png".
        alt_text (str): A string that represents the alternative text for the image. It is set to "a default image solid color".
        is_feature (Boolean): A boolean that indicates whether the image is the default image for the product. It is set to True.
    """

    class Meta:
        model = models.Media

    product_inventory = factory.SubFactory(ProductInventoryFactory)
    image = "images/default.png"
    alt_text = "a default image solid color"
    is_feature = True


@register
class StockFactory(factory.django.DjangoModelFactory):
    """
    The StockFactory class inherits from DjangoModelFactory.
    It is used to create test instances of the Stock model for testing purposes.

    Attributes:
        product_inventory (SubFactory): A SubFactory that creates a ProductInventory instance for the Stock instance.
        units (int): An integer that represents the number of units in stock. It is set to 2.
        units_sold (int): An integer that represents the number of units sold. It is set to 100.
    """

    class Meta:
        model = models.Stock

    product_inventory = factory.SubFactory(ProductInventoryFactory)
    units = 2
    units_sold = 100


@register
class ProductAttributeFactory(factory.django.DjangoModelFactory):
    """
    The ProductAttributeFactory class inherits from DjangoModelFactory.
    It is used to create test instances of the ProductAttribute model for testing purposes.

    Attributes:
        name (Sequence): A Sequence that generates a unique name for each ProductAttribute instance.
        description (Sequence): A Sequence that generates a unique description for each ProductAttribute instance.
    """

    class Meta:
        model = models.ProductAttribute

    name = factory.Sequence(lambda n: f"attribute_name_{n}")
    description = factory.Sequence(lambda n: f"description_{n}")


@register
class ProductAttributeValueFactory(factory.django.DjangoModelFactory):
    """
    The ProductAttributeValueFactory class inherits from DjangoModelFactory.
    It is used to create test instances of the ProductAttributeValue model for testing purposes.

    Attributes:
        product_attribute (SubFactory): A SubFactory that creates a ProductAttribute instance for the ProductAttributeValue instance.
        attribute_value (Sequence): A Sequence that generates a unique attribute value for each ProductAttributeValue instance.
    """

    class Meta:
        model = models.ProductAttributeValue

    product_attribute = factory.SubFactory(ProductAttributeFactory)
    attribute_value = factory.Sequence(lambda n: f"attribute_value_{n}")


@register
class ProductAttributeValuesFactory(factory.django.DjangoModelFactory):
    """
    The ProductAttributeValuesFactory class inherits from DjangoModelFactory.
    It is used to create test instances of the ProductAttributeValues model for testing purposes.

    Attributes:
        attributevalues (SubFactory): A SubFactory that creates a ProductAttributeValue instance for the ProductAttributeValues instance.
        productinventory (SubFactory): A SubFactory that creates a ProductInventory instance for the ProductAttributeValues instance.
    """

    class Meta:
        model = models.ProductAttributeValues

    attributevalues = factory.SubFactory(ProductAttributeValueFactory)
    productinventory = factory.SubFactory(ProductInventoryFactory)


@register
class ProductWithAttributeValuesFactory(ProductInventoryFactory):
    """
    The ProductWithAttributeValuesFactory class inherits from ProductInventoryFactory.
    It is used to create test instances of the ProductInventory model with related ProductAttributeValues instances for testing purposes.

    Attributes:
        attributevalues1 (RelatedFactory): A RelatedFactory that creates a ProductAttributeValues instance related to the ProductInventory instance.
        attributevalues2 (RelatedFactory): A RelatedFactory that creates another ProductAttributeValues instance related to the ProductInventory instance.
    """

    class Meta:
        skip_postgeneration_save = True

    attributevalues1 = factory.RelatedFactory(
        ProductAttributeValuesFactory,
        factory_related_name="productinventory",
    )
    attributevalues2 = factory.RelatedFactory(
        ProductAttributeValuesFactory,
        factory_related_name="productinventory",
    )
