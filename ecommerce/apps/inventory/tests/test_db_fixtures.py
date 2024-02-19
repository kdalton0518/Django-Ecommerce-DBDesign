import pytest
from ecommerce.apps.inventory import models
from django.db.utils import IntegrityError


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (
            "9212c1b6-f7f9-48e8-9978-bff8b6aaa000",
            "Parent Category 1",
            "parent-category-1",
            1,
        ),
        (
            "b8a0430e-e025-4d32-8480-e69821bc2cb5",
            "Parent Category 25",
            "parent-category-25",
            1,
        ),
        (
            "63b6e645-7c43-415f-94a6-da649383d67b",
            "Sub Category 3-8",
            "sub-category-3-8",
            1,
        ),
        (
            "d4a2aefb-0774-4a1a-8a17-957bf2bb6405",
            "Sub Category 11-4",
            "sub-category-11-4",
            1,
        ),
        (
            "604999ad-53fd-48d8-aa33-25771b017c92",
            "Sub Category 20-10",
            "sub-category-20-10",
            1,
        ),
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
        ("Test Category 1", "test-category-1", 1),
        ("Test Category 2", "test-category-2", 1),
        ("Test Category 3", "test-category-3", 1),
        ("Test Category 4", "test-category-4", 1),
        ("Test Category 5", "test-category-5", 1),
    ],
)
def test_inventory_category_insert_data(db, category_factory, name, slug, is_active):
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
            "f82b5c1d-72f5-49e0-ac63-8aec2ac6531a",
            "a19c64cc-83bd-46f8-a81f-e8ca11107c52",
            "Product 1",
            "product-1",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "3915ee45-285d-4c72-83eb-9578685b266f",
            "e9733557-c598-4cd8-b725-c3a7d34c3d80",
            "Product 635",
            "product-635",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "366e9776-2421-4766-b02f-433cd77956da",
            "532eabbe-89b6-4a92-b2c5-b971b67b910f",
            "Product 1304",
            "product-1304",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "500c3fff-da2a-4a99-95e3-6522e3a007c3",
            "74168451-68c2-4e4e-9b38-25771331f7d3",
            "Product 2562",
            "product-2562",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "693f877b-0e9f-460b-90d6-612719bf1ea9",
            "21f68700-8919-47c4-93c9-b9832668142b",
            "Product 3729",
            "product-3729",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
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

    category1 = category_factory.create()
    category2 = category_factory.create()

    product = product_factory.create(category=[category1, category2])

    product = models.Product.objects.get(id=product.id)

    assert product.category.count() == 2
    assert str(category1.id) in [cat.id for cat in product.category.all()]
    assert str(category2.id) in [cat.id for cat in product.category.all()]


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, sku, upc, product_type, product, brand, is_active, retail_price, store_price, weight, create_at, updated_at",
    [
        (
            "81d9e0e0-b2e0-433e-a3c5-ed4053a33f2c",
            "cbc1938b-4da4-4846-9e8b-ad805ca4a2a9",
            "f3f8da2f-4395-479f-9566-022f2590624e",
            "b81fa2f4-0c6a-4c1b-9de8-2056b6ee5feb",
            "f82b5c1d-72f5-49e0-ac63-8aec2ac6531a",
            "30079606-eb77-441e-898e-816b05a03472",
            1,
            97,
            92,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "06d57c12-cb53-4c96-814d-3ec876d1bf27",
            "aca0e545-4e9c-4b4c-98b2-ae38b51f6f45",
            "45a29799-aabf-426b-9c60-39d2750f19bf",
            "0c01b7cc-1a47-4748-80ec-aef3a3d22e2e",
            "d4871fd3-a404-49ed-9a62-de37d9179aff",
            "30079606-eb77-441e-898e-816b05a03472",
            1,
            97,
            92,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "6a3cb551-d4b7-4ec2-ad39-4ee2ab190fc6",
            "e526e9ab-a6f6-4a97-a1ae-6353f5e3543c",
            "cdbc3c2b-ca31-48be-9a30-3e7279137615",
            "b014692d-d3f1-4215-8201-643cc63a9b05",
            "734fad23-8803-4f4d-a0ea-ff8cf0b97256",
            "4d8b5547-cd3c-4af2-92fa-7dc9680b5f39",
            1,
            97,
            92,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "29b13e99-8825-4f51-a94e-2f74c883c38b",
            "2c1a3bc7-87fd-454c-9407-1a57829134ad",
            "ee55dc77-b801-45ab-b679-a21ef1c0be2f",
            "5106cb08-44d0-49c1-94b9-df726fb13218",
            "09b40472-9f3a-4b65-bd53-e695b7eeefe6",
            "d4e49bfe-d244-401b-9861-c3f3e63b90e6",
            1,
            97,
            92,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "a89effdf-72bb-4679-8725-82e02417f916",
            "e355ee6d-3b39-42e7-88a2-701928a2a0d6",
            "fcc8a57b-51f3-45ca-bf28-884cad238085",
            "3f6b1985-f9ab-42a0-b279-40b8ec7a9c64",
            "b98e5842-6346-4ee0-a811-d0b9c6cbe139",
            "dfe155e1-359c-4410-a439-19ca06f0ed7b",
            1,
            97,
            92,
            987,
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
    assert result.weight == weight
    assert result_created_at == create_at
    assert result_updated_at == updated_at


@pytest.mark.parametrize(
    "sku, upc, product_type__name, product__web_id, brand__name",
    [
        (
            "9276b88d-0adc-4215-84dc-a4f69a5ad511",
            "3520cecf-e7da-4726-8029-cd4845aa070f",
            "Test Product Type 1",
            "3c80e56b-84a7-416c-b87b-f0be787ca69e",
            "Test Brand 1",
        ),
        (
            "10ce0e13-521e-4471-a745-e2dafd7da31e",
            "1b346d61-129c-445b-b047-1bbe6b84560d",
            "Test Product Type 2",
            "7784ba24-2389-44e9-91c7-5c4b25c7c1af",
            "Test Brand 2",
        ),
        (
            "bcda7953-262b-4c1b-80b6-ea4d37f7182a",
            "c7a0f29b-5b16-4ba9-8572-1426275bc4fe",
            "Test Product Type 3",
            "0f5ea5af-bca8-4aa8-8430-ab93f9028f21",
            "Test Brand 3",
        ),
        (
            "9889529a-48cc-478e-b3f2-c56ce98035d6",
            "e268b3b3-e81e-4670-a928-e079f60abd09",
            "Test Product Type 4",
            "6a643561-5344-4297-b9f6-77064c9e3677",
            "Test Brand 4",
        ),
        (
            "c145a98b-ae9e-4cea-98fb-c8bc1e0d6992",
            "d137ff43-6e12-4331-9669-d15e17c7c39f",
            "Test Product Type 5",
            "0124a134-6070-4b92-a7e2-ba67e4796f36",
            "Test Brand 5",
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
    assert new_product.weight == 987


def test_inventory_producttype_insert_data(db, product_type_factory):
    """
    Test to verify the ProductType model data inserted using the factory.
    """

    new_type = product_type_factory.create(name="Test Product Type")

    assert new_type.name == "Test Product Type"


def test_inventory_producttype_uniqueness_integrity(db, product_type_factory):
    """
    Test to verify the ProductType model data uniqueness integrity.
    """

    product_type_factory.create(name="Test Product Type")

    with pytest.raises(IntegrityError):
        product_type_factory.create(name="Test Product Type")


@pytest.mark.parametrize(
    "name",
    [
        ("Test Brand 1"),
        ("Test Brand 2"),
        ("Test Brand 3"),
        ("Test Brand 4"),
        ("Test Brand 5"),
    ],
)
def test_inventory_brand_insert_data(db, brand_factory, name):
    """
    Test to verify the Brand model data inserted using the factory.
    """

    new_brand = brand_factory.create(name=name)

    assert new_brand.name == name


def test_inventory_brand_uniqueness_integrity(db, brand_factory):
    """
    Test to verify the Brand model data uniqueness integrity.
    """

    brand_factory.create(name="Test Brand")

    with pytest.raises(IntegrityError):
        brand_factory.create(name="Test Brand")


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_inventory, image, alt_text, is_feature, created_at, updated_at",
    [
        (
            "085bbdbd-b468-4eac-aa2b-0292cfb7daab",
            "81d9e0e0-b2e0-433e-a3c5-ed4053a33f2c",
            "images/default.png",
            "a default image solid color",
            True,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "855c6563-f3f3-437d-b365-82a50365e43b",
            "4af87b9a-3de5-4525-981c-d1d23ca14296",
            "images/default.png",
            "a default image solid color",
            True,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "983e723b-3eb3-46df-894f-cea96b2bc77b",
            "369d4e81-fec6-4721-9b38-4ed66890ce32",
            "images/default.png",
            "a default image solid color",
            True,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "70a4668c-2320-4436-8fc2-718a602ac512",
            "4b7f16e5-7998-416a-b503-fa29482fb73c",
            "images/default.png",
            "a default image solid color",
            True,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "b93f42c6-98e5-42fb-a970-baba439d4df5",
            "cf1a80a3-7194-4dc4-8abf-9d7be515515e",
            "images/default.png",
            "a default image solid color",
            True,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_media_dbfixture(
    db,
    db_fixture_setup,
    id,
    product_inventory,
    image,
    alt_text,
    is_feature,
    created_at,
    updated_at,
):
    """
    Test to verify the Media model data loaded from the fixture.
    """

    result = models.Media.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    assert result.product_inventory.id == product_inventory
    assert result.image == image
    assert result.alt_text == alt_text
    assert result.is_feature == is_feature
    assert result_created_at == created_at
    assert result_updated_at == updated_at


@pytest.mark.parametrize(
    "product_inventory__sku",
    [
        ("56ca5f64-93db-4517-a380-9adac4a9d11c"),
        ("bd8cead1-8f2a-4dc4-81a2-c6415fdb993a"),
        ("98c33e3d-2211-4374-9fd6-c09025e13cc6"),
        ("ba40e4ef-9eae-46d9-bc0b-ed0829d949c0"),
        ("282684cc-a1cd-40ed-9923-4ff9aaf79ba9"),
    ],
)
def test_inventory_media_insert_data(db, media_factory, product_inventory__sku):
    """
    Test to verify the Media model data inserted using the factory.
    """

    new_media = media_factory.create(product_inventory__sku=product_inventory__sku)

    assert new_media.product_inventory.sku == product_inventory__sku
    assert new_media.image == "images/default.png"
    assert new_media.alt_text == "a default image solid color"
    assert new_media.is_feature == 1


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_inventory, last_checked, units, units_sold",
    [
        (
            "a34a551a-8b32-4699-83a5-18a23a3019f5",
            "81d9e0e0-b2e0-433e-a3c5-ed4053a33f2c",
            "2021-09-04 22:14:18",
            135,
            45,
        ),
        (
            "16bfe0d8-6b78-4a3c-ac5d-211dc2c6b232",
            "52ac6b58-850a-46b8-a70b-b85986d35f45",
            "2021-09-04 22:14:18",
            135,
            45,
        ),
        (
            "5b20a714-4473-4fef-98db-0c400145c724",
            "c420854f-b508-4431-a333-bb4e8d27e820",
            "2021-09-04 22:14:18",
            135,
            45,
        ),
        (
            "7f91dac4-42cc-4f77-a652-64a2f7ec2330",
            "ccbda026-b07a-4452-8877-fff66d407ce2",
            "2021-09-04 22:14:18",
            135,
            45,
        ),
        (
            "0972702b-3420-411a-9302-fabc854f1312",
            "5e61c59b-194e-4b70-8cc5-f058b25d589f",
            "2021-09-04 22:14:18",
            135,
            45,
        ),
    ],
)
def test_inventory_stock_dbfixture(
    db,
    db_fixture_setup,
    id,
    product_inventory,
    last_checked,
    units,
    units_sold,
):
    """
    Test to verify the Stock model data loaded from the fixture.
    """

    result = models.Stock.objects.get(id=id)
    result_last_checked = result.last_checked.strftime("%Y-%m-%d %H:%M:%S")

    assert result.product_inventory.id == product_inventory
    assert result_last_checked == last_checked
    assert result.units == units
    assert result.units_sold == units_sold


@pytest.mark.parametrize(
    "product_inventory__sku",
    [
        ("dc3caef3-95cf-468e-a4c3-d20f5209b0eb"),
        ("9f525d9c-5531-42d7-a947-f6c155209103"),
        ("4410f9a6-a738-4eaf-968a-05cd3bc2927b"),
        ("fad708af-cc9a-4e7b-a7c7-845a9cbb3759"),
        ("7a281fe3-ab1c-4d73-87fc-8b05d16203ce"),
    ],
)
def test_inventory_stock_insert_data(db, stock_factory, product_inventory__sku):
    """
    Test to verify the Stock model data inserted using the factory.
    """

    new_stock = stock_factory.create(product_inventory__sku=product_inventory__sku)

    assert new_stock.product_inventory.sku == product_inventory__sku
    assert new_stock.units == 135
    assert new_stock.units_sold == 45


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, description",
    [
        (
            "ef9b6bbb-1b69-4aac-bb21-a2922a0b0a30",
            "Product Attribute 1",
            "Product Attribute 1 Description",
        ),
        (
            "e8e8fe4f-fe44-4f40-a124-a1ca387ace41",
            "Product Attribute 15",
            "Product Attribute 15 Description",
        ),
        (
            "b25da9d7-e690-42b1-bf2a-bf827cef62a7",
            "Product Attribute 22",
            "Product Attribute 22 Description",
        ),
        (
            "d833da40-7ece-48fd-8d2d-89536b3a40f5",
            "Product Attribute 30",
            "Product Attribute 30 Description",
        ),
        (
            "39038145-9348-4070-a3a1-ac2f44cf3390",
            "Product Attribute 44",
            "Product Attribute 44 Description",
        ),
    ],
)
def test_inventory_product_attribute_dbfixture(
    db, db_fixture_setup, id, name, description
):
    """
    Test to verify the ProductAttribute model data loaded from the fixture.
    """

    result = models.ProductAttribute.objects.get(id=id)

    assert result.name == name
    assert result.description == description


@pytest.mark.parametrize(
    "name, description",
    [
        ("Test Product Attribute 1", "Test Product Attribute 1 Description"),
        ("Test Product Attribute 2", "Test Product Attribute 2 Description"),
        ("Test Product Attribute 3", "Test Product Attribute 3 Description"),
        ("Test Product Attribute 4", "Test Product Attribute 4 Description"),
        ("Test Product Attribute 5", "Test Product Attribute 5 Description"),
    ],
)
def test_inventory_product_attribute_insert_data(
    db, product_attribute_factory, name, description
):
    """
    Test to verify the ProductAttribute model data inserted using the factory.
    """

    new_attribute = product_attribute_factory.create(name=name, description=description)

    assert new_attribute.name == name
    assert new_attribute.description == description


def test_inventory_product_attribute_uniqueness_integrity(
    db, product_attribute_factory
):
    """
    Test to verify the ProductAttribute model data uniqueness integrity.
    """

    product_attribute_factory.create(name="Test Product Attribute")

    with pytest.raises(IntegrityError):
        product_attribute_factory.create(name="Test Product Attribute")


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_attribute, attribute_value",
    [
        (
            "6b3a4165-8de3-4437-ac37-c72074e3de32",
            "ef9b6bbb-1b69-4aac-bb21-a2922a0b0a30",
            "Product Attribute Value 1-1",
        ),
        (
            "c24208e4-129f-48fb-85df-7a2ccb941aa6",
            "be05405d-0779-4d25-813d-a8ed09a19d61",
            "Product Attribute Value 5-3",
        ),
        (
            "cee450ba-fbac-4c16-88df-61efaf526b0f",
            "a2f38f38-b213-4eca-866d-0acfe85c635e",
            "Product Attribute Value 11-1",
        ),
        (
            "1fe9e679-8d30-4315-b803-93ec622a1ca0",
            "01380a78-56ba-4a79-93a2-e04d68372e14",
            "Product Attribute Value 16-4",
        ),
        (
            "72cdf8f1-c1a5-4dcf-9279-7bac1beea662",
            "16564be4-1078-4ba3-9c86-2c8c35dcaeea",
            "Product Attribute Value 24-6",
        ),
    ],
)
def test_inventory_product_attribute_value_dbfixture(
    db, db_fixture_setup, id, product_attribute, attribute_value
):
    """
    Test to verify the ProductAttributeValue model data loaded from the fixture.
    """

    result = models.ProductAttributeValue.objects.get(id=id)

    assert result.product_attribute.id == product_attribute
    assert result.attribute_value == attribute_value


@pytest.mark.parametrize(
    "attribute_value, product_attribute__name",
    [
        ("Test Attribute Value 1-1", "Test Attribute 1"),
        ("Test Attribute Value 1-2", "Test Attribute 1"),
        ("Test Attribute Value 1-3", "Test Attribute 1"),
        ("Test Attribute Value 2-1", "Test Attribute 2"),
        ("Test Attribute Value 2-2", "Test Attribute 2"),
    ],
)
def test_inventory_product_attribute_value_insert_data(
    db, product_attribute_value_factory, attribute_value, product_attribute__name
):
    """
    Test to verify the ProductAttributeValue model data inserted using the factory.
    """

    new_attribute_value = product_attribute_value_factory.create(
        attribute_value=attribute_value, product_attribute__name=product_attribute__name
    )

    assert new_attribute_value.attribute_value == attribute_value
    assert new_attribute_value.product_attribute.name == product_attribute__name
