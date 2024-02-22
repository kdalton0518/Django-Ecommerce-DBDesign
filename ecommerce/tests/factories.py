import uuid
import factory
from faker import Faker
from pytest_factoryboy import register
from ecommerce.apps.inventory import models as inventory_models
from ecommerce.apps.promotion import models as promotion_models
from datetime import datetime


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
        model = inventory_models.Category

    name = factory.Sequence(lambda n: f"Test Category {n}")
    slug = factory.Sequence(lambda n: f"test-category-{n}")


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
        model = inventory_models.Product
        skip_postgeneration_save = True

    web_id = factory.sequence(
        lambda n: f"WEBID-{str(uuid.uuid4()).split('-')[0]}{str(uuid.uuid4()).split('-')[1]}".upper()
    )
    name = factory.Sequence(lambda n: f"Test Product {n}")
    slug = factory.Sequence(lambda n: f"test_product_{n}")
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
        model = inventory_models.ProductType

    name = factory.Sequence(lambda n: f"Test Product Type {n}")


@register
class BrandFactory(factory.django.DjangoModelFactory):
    """
    The BrandFactory class inherits from DjangoModelFactory.
    It is used to create test instances of the Brand model for testing purposes.

    Attributes:
        name (Sequence): A Sequence that generates a unique name for each Brand instance.
    """

    class Meta:
        model = inventory_models.Brand

    name = factory.Sequence(lambda n: f"Test Brand {n}")


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
        model = inventory_models.ProductAttribute

    name = factory.Sequence(lambda n: f"Test Product Attribute {n}")
    description = factory.Sequence(lambda n: f"Test Product Attribute {n} Description")


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
        model = inventory_models.ProductAttributeValue

    product_attribute = factory.SubFactory(ProductAttributeFactory)
    attribute_value = factory.Sequence(lambda n: f"Test Product Attribute Value {n}")


@register
class PromotionTypeFactory(factory.django.DjangoModelFactory):
    """
    The PromotionType class inherits from DjangoModelFactory.
    It is used to create test instances of the PromotionType model for testing purposes.

    Attributes:
        name (Sequence): A Sequence that generates a unique name for each PromotionType instance.
    """

    class Meta:
        model = promotion_models.PromotionType

    name = factory.Sequence(lambda n: f"Test Promotion Type {n}")


@register
class CouponFactory(factory.django.DjangoModelFactory):
    """
    The CouponFactory class inherits from DjangoModelFactory.
    It is used to create test instances of the Coupon model for testing purposes.

    Attributes:
        name (Sequence): A Sequence that generates a unique name for each Coupon instance.
        code (Sequence): A Sequence that generates a unique code for each Coupon instance.
        description (Sequence): A Sequence that generates a unique description for each Coupon instance.
    """

    class Meta:
        model = promotion_models.Coupon

    name = factory.Sequence(lambda n: f"Test Coupon {n}")
    code = factory.Sequence(lambda n: f"TESTCOUPON-{n}")
    description = factory.Sequence(lambda n: f"Test Coupon {n} Description")


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
        weight (Float): A float representing the weight of the product.
    """

    class Meta:
        model = inventory_models.ProductInventory
        skip_postgeneration_save = True

    sku = factory.Sequence(
        lambda n: f"SKU-{str(uuid.uuid4()).split('-')[0]}{str(uuid.uuid4()).split('-')[1]}".upper()
    )
    upc = factory.Sequence(
        lambda n: f"UPC-{str(uuid.uuid4()).split('-')[0]}{str(uuid.uuid4()).split('-')[1]}".upper()
    )
    product_type = factory.SubFactory(ProductTypeFactory)
    product = factory.SubFactory(ProductFactory)
    brand = factory.SubFactory(BrandFactory)
    is_active = 1
    retail_price = 97
    store_price = 92
    weight = 987


@register
class PromotionFactory(factory.django.DjangoModelFactory):
    """
    The PromotionFactory class inherits from DjangoModelFactory.
    It is used to create test instances of the Promotion model for testing purposes.

    Attributes:
        promotion_type (SubFactory): A SubFactory that creates a PromotionType instance for the Promotion instance.
        coupon (SubFactory): A SubFactory that creates a Coupon instance for the Promotion instance.
        name (Sequence): A Sequence that generates a unique name for each Promotion instance.
        description (Sequence): A Sequence that generates a unique description for each Promotion instance.
        promotion_reduction (int): An integer representing the promotion reduction percentage.
        promotion_start (DateTime): A string representing the date and time the promotion starts.
        promotion_end (DateTime): A string representing the date and time the promotion ends.
    """

    class Meta:
        model = promotion_models.Promotion
        skip_postgeneration_save = True

    promotion_type = factory.SubFactory(PromotionTypeFactory)
    coupon = factory.SubFactory(CouponFactory)
    name = factory.Sequence(lambda n: f"Test Promotion {n:03d}")
    description = factory.Sequence(lambda n: f"Test Promotion {n:03d} Description")
    promotion_reduction = 40
    promotion_start = "2024-03-05"
    promotion_end = "2024-03-15"
    products_on_promotion = factory.RelatedFactoryList(ProductInventoryFactory, size=5)


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
        model = inventory_models.Media

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
        model = inventory_models.Stock

    product_inventory = factory.SubFactory(ProductInventoryFactory)
    units = 135
    units_sold = 45
