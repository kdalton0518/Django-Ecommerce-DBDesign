import pytest
from ecommerce.apps.inventory import models
from django.db.utils import IntegrityError


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        ("160343b7-ea3d-4d82-85e5-7103baaf889e", "fashion", "fashion", 1),
        ("9100a263-4504-42a5-a348-7ff179961488", "trainers", "trainers", 1),
        ("a3089a38-6282-4e0c-bf24-b5807d2e7337", "baseball", "baseball", 1),
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


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, web_id, name, slug, description, is_active, created_at, updated_at",
    [
        (
            "770c3ba6-121f-4d2e-91ea-1c448361beb8",
            "6cc7d508-8ebf-488a-a1fa-f80f8d9cc73f",
            "widstar running sneakers",
            "widstar-running-sneakers",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "8848423c-2fde-4c64-9ced-60db33f35afa",
            "4de854e0-3e0b-4c61-a12c-135457140fe9",
            "impact puse dance shoe",
            "impact-puse-dance-shoe",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "2530d906-abce-4c2b-9f86-e446f3ab3954",
            "98c315c1-c26c-4531-a1d8-6ad1910cf68a",
            "aerosoes loipowp sandals",
            "aerosoes-loipowp-sandals",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_product_dbfixture(
    db,
    db_fixture_setup,
    id,
    web_id,
    name,
    slug,
    description,
    is_active,
    created_at,
    updated_at,
):
    """
    Test to verify the Product model data loaded from the fixture.
    """
    result = models.Product.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    assert result.web_id == web_id
    assert result.name == name
    assert result.slug == slug
    assert result.description == description
    assert result.is_active == is_active
    assert result_created_at == created_at
    assert result_updated_at == updated_at


def test_inventory_product_uniqueness_integrity(db, product_factory, category_factory):
    """
    Test to verify the Product model data uniqueness integrity.
    """
    new_web_id = product_factory.create(web_id="2a409e2d-d929-4f04-a6f8-a6719d1d57b6")
    with pytest.raises(IntegrityError):
        product_factory.create(web_id=new_web_id.web_id)


@pytest.mark.dbfixture
def test_inventory_product_insert_data(db, product_factory, category_factory):
    """
    Test to verify the Product model data inserted using the factory.
    """

    product = product_factory.create(
        category=(
            "160343b7-ea3d-4d82-85e5-7103baaf889e",
            "2cd01d6c-c413-4bd7-905f-3acac2b691ab",
        )
    )

    all_categories_count = product.category.all().count()

    assert "160343b7-ea3d-4d82-85e5-7103baaf889e" == product.category.all()[0].id
    assert "2cd01d6c-c413-4bd7-905f-3acac2b691ab" == product.category.all()[1].id
    assert all_categories_count == 2
