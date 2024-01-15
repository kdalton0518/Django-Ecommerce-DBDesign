import pytest
from ecommerce.apps.inventory import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        ("467b7e7b-569a-4ba8-a1eb-8ec7a15f0c3b", "fashion", "fashion", 1),
        ("4ed7f8fb-fe79-4bd1-a0f1-6ee0523914f7", "trainers", "trainers", 1),
        ("0882963a-6c4f-4c23-9e47-a0209d8d6393", "baseball", "baseball", 1),
    ],
)
def test_inventory_category_dbfixture(db, db_fixture_setup, id, name, slug, is_active):
    """
    Test to verify the Category model data loaded from the fixture.
    """
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "name, slug, is_active",
    [
        ("fashion", "fashion", 1),
        ("trainers", "trainers", 1),
        ("baseball", "baseball", 1),
    ],
)
def test_inventory_db_category_insert_data(db, category_factory, name, slug, is_active):
    """
    Test to verify the Category model data inserted using the factory.
    """
    result = category_factory.create(name=name, slug=slug, is_active=is_active)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active
