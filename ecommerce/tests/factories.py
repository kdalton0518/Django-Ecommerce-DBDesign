import factory
from faker import Faker
from pytest_factoryboy import register
from ecommerce.apps.inventory import models


faker = Faker()


@register
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: f"cat_name_{n}")
    slug = factory.Sequence(lambda n: f"cat_name_{n}")
