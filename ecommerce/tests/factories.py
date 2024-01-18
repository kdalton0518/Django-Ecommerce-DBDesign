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
