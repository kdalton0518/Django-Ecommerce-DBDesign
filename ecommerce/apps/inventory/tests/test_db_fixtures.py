import pytest
from ecommerce.apps.inventory import models
from django.db.utils import IntegrityError


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (
            "3854ab99-a1d0-4324-ad53-4d2673e14b4d",
            "Parent Category 1",
            "parent-category-1",
            1,
        ),
        (
            "0a8b46d8-3d12-4ac2-abd1-1ffc9b93dc04",
            "Parent Category 24",
            "parent-category-24",
            1,
        ),
        (
            "7b624b0e-7d96-4ce9-a1eb-a2ac993cde53",
            "Sub Category 8-13",
            "sub-category-8-13",
            1,
        ),
        (
            "655ccbe3-1671-438c-8345-a52df116de28",
            "Sub Category 11-10",
            "sub-category-11-10",
            1,
        ),
        (
            "43dd27a7-fe16-4710-a04c-ccbef9acd8cd",
            "Sub Category 17-2",
            "sub-category-17-2",
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
            "ee73529d-67ab-4130-a7e5-c5c2581e22a7",
            "e39d5bf3-8037-4d58-a101-2d0c7b49b3b9",
            "Product 0-1",
            "product-0-1",
            "Product 0-1 Description",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "c9fcfa13-9217-4ba6-ae2a-85a4ba16a356",
            "ab44f37f-777e-412d-add8-d624217e6eb9",
            "Product 0-61",
            "product-0-61",
            "Product 0-61 Description",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "3b5b9c9c-eff8-4e88-9c24-35ba78608f30",
            "9fa6cea2-ff8d-4899-b2d7-c380853038d0",
            "Product 2-73",
            "product-2-73",
            "Product 2-73 Description",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "7eca29db-e993-4e97-ade7-6a218e5c7b88",
            "09cbb82e-c17c-4195-a71e-d575197639a4",
            "Product 4-15",
            "product-4-15",
            "Product 4-15 Description",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "634397cd-e251-4c34-a95b-fcf31c42a235",
            "ce4988c4-afec-4cef-8b21-e784e3f225ec",
            "Product 6-69",
            "product-6-69",
            "Product 6-69 Description",
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
    "id, sku, upc, product_type, product, brand, is_active, retail_price, store_price, sale_price, weight, create_at, updated_at",
    [
        (
            "ee9383ae-c8e1-4987-9a67-eed76a1bd29e",
            "26db4b38-9629-41cb-b20b-db09e6692c02",
            "d378381d-a9af-4730-9be4-4a5ad11f01eb",
            "dd9b0db2-65aa-488c-8a5a-42c2c0644840",
            "ee73529d-67ab-4130-a7e5-c5c2581e22a7",
            "0f7cbb26-aa4e-4ee4-b56a-03a890ca6a6b",
            1,
            97,
            92,
            46,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "9871fad4-f456-4d45-b0e8-89dc6b4ac54f",
            "7eca01a7-befb-4323-8120-5ceb04dcaf79",
            "95211a95-c694-4e6c-840a-6135e6079ad4",
            "f86806aa-2d0b-4b14-baa1-a5c88b596519",
            "54af626f-a829-4414-8d6d-c1348f2f0a4f",
            "7f7b2f0c-daa1-461b-85ab-526df4dd1240",
            1,
            97,
            92,
            46,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "b84f91ff-d1ff-4042-a0a9-50f972c1505e",
            "6aaa8d23-abaa-48bf-a403-261ede3be414",
            "7a7ceaea-0618-4813-99f2-4254db36e60d",
            "13d37e96-9ccc-4477-b0bc-273e2b37fbf0",
            "6db01eb0-ff83-493b-8119-b58f52d2ac75",
            "51593972-dbb0-4cc3-996a-53eac0306236",
            1,
            97,
            92,
            46,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "0d88e9a3-33ff-4e8b-af1b-667911484203",
            "855aa53e-b076-4a65-9713-642e73eecd79",
            "a1c21292-cb97-4aad-b75f-4d6c1746ce34",
            "677fd0b1-89fd-4054-a944-5dac5d4f6c76",
            "69aa420e-fa3b-42a5-a764-c013b1481687",
            "dd0bdc0d-796d-4f6c-9106-df91c589e01f",
            1,
            97,
            92,
            46,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "cc05b160-f05e-435c-8b7e-f53a97a7beba",
            "c41bcb5c-f423-49ae-8cb3-b4483e8a761f",
            "4a96fa9d-b78b-444f-95b1-b6982e645a0a",
            "b78b47e5-84fe-4164-82bf-6840432ad6d9",
            "3cea8da3-ae39-4cd2-94a8-58ef6ec35625",
            "2f285e80-c0ee-4668-9cfc-e6b70cb42cf1",
            1,
            97,
            92,
            46,
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
    assert new_product.sale_price == 46
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
            "a7261333-673d-4bd6-88de-25945f9c22ed",
            "ee9383ae-c8e1-4987-9a67-eed76a1bd29e",
            "images/default.png",
            "a default image solid color",
            True,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "90133c39-0c7e-4b4d-ac3f-08ac57dd26e3",
            "50e01079-8c87-4e83-a915-812acbf090b3",
            "images/default.png",
            "a default image solid color",
            True,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "0c4ce2a4-cdde-4aeb-9858-ab12f58d6a20",
            "708ac700-87f1-414e-ba48-720f9975c11f",
            "images/default.png",
            "a default image solid color",
            True,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "6cdfee32-c4b8-4b00-b035-7171fbe758c3",
            "d69ad169-25c2-4fbc-93b3-af71d025cc4b",
            "images/default.png",
            "a default image solid color",
            True,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            "01e0772c-fef7-4bcd-830c-8167d83ec6d8",
            "3ecd6e53-93af-40df-9fba-9972ff6354ef",
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
            "580f64a1-1af0-4bc4-8da9-b5de626a794a",
            "ee9383ae-c8e1-4987-9a67-eed76a1bd29e",
            "2021-09-04 22:14:18",
            135,
            45,
        ),
        (
            "ba895134-a14e-416d-954d-5fb7ddd0021e",
            "23bd0ac4-de91-4240-87b1-c8a8bf15aa08",
            "2021-09-04 22:14:18",
            135,
            45,
        ),
        (
            "d8dca3d1-79a9-47e8-aef9-0e8b7aeec89b",
            "097fec51-8661-4724-a6e0-d6f330377367",
            "2021-09-04 22:14:18",
            135,
            45,
        ),
        (
            "6ea65cf6-41ad-418e-9e0b-a7f28d696430",
            "88573321-14ec-43f7-8d60-2b6c79323375",
            "2021-09-04 22:14:18",
            135,
            45,
        ),
        (
            "2e76b45e-358b-48cd-a818-93ddafc639e5",
            "ec1958e1-8fc7-4ad2-bb66-61e606743bc6",
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
            "c46e3ac8-229a-4a71-afe8-366899d1d7dc",
            "Product Attribute 1",
            "Product Attribute 1 Description",
        ),
        (
            "b8f8939c-e2e5-4b81-92fa-91152570ce72",
            "Product Attribute 15",
            "Product Attribute 15 Description",
        ),
        (
            "6b3fa821-33aa-4852-a106-06ffffc9f301",
            "Product Attribute 22",
            "Product Attribute 22 Description",
        ),
        (
            "6f51169c-e6b2-4b75-b4d9-bf841edb88cf",
            "Product Attribute 30",
            "Product Attribute 30 Description",
        ),
        (
            "8965ab60-0f1f-4fb3-8475-06fdd94d67bb",
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
def test_inventory_product_attrubite_insert_data(
    db, product_attribute_factory, name, description
):
    """
    Test to verify the ProductAttribute model data inserted using the factory.
    """

    new_attribute = product_attribute_factory.create(name=name, description=description)

    assert new_attribute.name == name
    assert new_attribute.description == description


def test_inventory_product_attrubite_uniqueness_integrity(
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
            "f6c6fcdb-9fca-40b3-80dd-5579e8d7ef9a",
            "c46e3ac8-229a-4a71-afe8-366899d1d7dc",
            "Product Attribute Value 0-1",
        ),
        (
            "b71ec6d3-2b01-43e9-819b-8083579790a4",
            "f13b3e0d-6161-4afe-9415-1586ad53d372",
            "Product Attribute Value 8-4",
        ),
        (
            "25f8b8dd-8b31-48a2-b421-ce2bd4b311fa",
            "942034b5-c50b-41f6-9a2b-0215360e5e1e",
            "Product Attribute Value 13-4",
        ),
        (
            "e4339aac-3d75-4aa1-b19a-586ed550d03c",
            "ecc0c77c-194b-4a1e-8444-c9b74e311fe8",
            "Product Attribute Value 19-2",
        ),
        (
            "e42b9fdf-828c-4b9a-856d-ce950e9a9f27",
            "ac85d263-c3bd-4d8d-80b6-c6e1151f4d52",
            "Product Attribute Value 35-3",
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
