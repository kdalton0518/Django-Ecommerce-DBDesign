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
