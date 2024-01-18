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


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, sku, upc, product_type, product, brand, is_active, retail_price, store_price, sale_price, weight, create_at, updated_at",
    [
        (
            "e6ef18d6-5bf8-424c-bdf5-69a315c57d65",
            "bfcb1ae3-213e-441f-8f68-1c88823b4b01",
            "973ba87b-6114-45c3-805c-a545b58c6d34",
            "36377005-174b-4373-9cca-fe7670da2641",
            "770c3ba6-121f-4d2e-91ea-1c448361beb8",
            "6f47e384-112e-4d19-9c33-b6f838c025f8",
            1,
            97,
            92,
            46,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "a7117e52-7ed2-42c0-ae7f-b3e5e8b4abe2",
            "e9766e8f-4acb-4215-8cff-e1977255915e",
            "be6010c2-462e-4f4b-a2f5-0fd8309f7c13",
            "36377005-174b-4373-9cca-fe7670da2641",
            "0d5064dd-b921-4beb-9717-933fac319454",
            "d1ae3974-807b-4dc5-ad5b-b454c2933639",
            1,
            99,
            94,
            47,
            947,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "f1180ad0-435c-4445-ab56-33b21f029dc2",
            "1f7df13c-ed93-443c-9fcc-405683744878",
            "f58e1c09-0b98-4cd4-907b-7a08d1199750",
            "36377005-174b-4373-9cca-fe7670da2641",
            "5673e074-5605-4ecb-9566-95d6dce9824c",
            "fb9f1b70-de04-43d2-b1e5-c7ae2898ee6f",
            1,
            88,
            84,
            42,
            994,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_product_inventory_dbfixture(
    db,
    db_fixture_setup,
    id,
    sku,
    upc,
    product_type,
    product,
    brand,
    is_active,
    retail_price,
    store_price,
    sale_price,
    weight,
    create_at,
    updated_at,
):
    """
    Test to verify the ProductInventory model data loaded from the fixture.
    """

    result = models.ProductInventory.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    assert result.sku == sku
    assert result.upc == upc
    assert result.product_type.id == product_type
    assert result.product.id == product
    assert result.brand.id == brand
    assert result.is_active == is_active
    assert result.retail_price == retail_price
    assert result.store_price == store_price
    assert result.sale_price == sale_price
    assert result.weight == weight
    assert result_created_at == create_at
    assert result_updated_at == updated_at


@pytest.mark.parametrize(
    "sku, upc, product_type__name, product__web_id, brand__name",
    [
        (
            "7d144dfd-df58-46e1-bbb0-df2841c8acd5",
            "7f222ab1-ed99-4139-812f-b53fdb19c205",
            "new_product_1",
            "75e6472f-cdbd-4bb3-9163-d96c15174f99",
            "new_brand_1",
        ),
        (
            "c896801d-a1c8-49aa-bcd8-fe44f894b690",
            "8a9f7576-663e-4a4e-9f1b-4cb1f42c2635",
            "new_product_2",
            "8f0e9bcb-bef8-4cfe-88a2-4cada7e3764e",
            "new_brand_2",
        ),
        (
            "5d6011e1-270f-4e9e-be12-63f3631c42f5",
            "1fcbb1fd-1c81-443f-a3e5-8a33f399fc8d",
            "new_product_3",
            "9e2f97e5-e7a8-48b7-bfc5-7f5f64600071",
            "new_brand_3",
        ),
    ],
)
def test_inventory_product_inventory_insert_data(
    db,
    product_inventory_factory,
    sku,
    upc,
    product_type__name,
    product__web_id,
    brand__name,
):
    """
    Test to verify the ProductInventory model data inserted using the factory.
    """
    new_product = product_inventory_factory.create(
        sku=sku,
        upc=upc,
        product_type__name=product_type__name,
        product__web_id=product__web_id,
        brand__name=brand__name,
    )

    assert new_product.sku == sku
    assert new_product.upc == upc
    assert new_product.product_type.name == product_type__name
    assert new_product.product.web_id == product__web_id
    assert new_product.brand.name == brand__name
    assert new_product.is_active == 1
    assert new_product.retail_price == 97
    assert new_product.store_price == 92
    assert new_product.sale_price == 46
    assert new_product.weight == 987


def test_inventory_db_producttype_insert_data(db, product_type_factory):
    """
    Test to verify the ProductType model data inserted using the factory.
    """
    new_type = product_type_factory.create(name="demo_type")
    assert new_type.name == "demo_type"


def test_inventory_db_producttype_uniqueness_integrity(db, product_type_factory):
    """
    Test to verify the ProductType model data uniqueness integrity.
    """
    product_type_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        product_type_factory.create(name="not_unique")


@pytest.mark.parametrize(
    "name",
    [
        ("demo_brand_1"),
        ("demo_brand_2"),
        ("demo_brand_3"),
    ],
)
def test_inventory_db_brand_insert_data(db, brand_factory, name):
    """
    Test to verify the Brand model data inserted using the factory.
    """
    new_brand = brand_factory.create(name=name)
    assert new_brand.name == name


def test_inventory_db_brand_uniqueness_integrity(db, brand_factory):
    """
    Test to verify the Brand model data uniqueness integrity.
    """
    brand_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        brand_factory.create(name="not_unique")
