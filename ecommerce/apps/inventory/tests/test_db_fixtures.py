import pytest
from ecommerce.apps.inventory import models
from django.db.utils import IntegrityError
from django.conf import settings
from django.utils import timezone
from decimal import Decimal


# Activate time zone
timezone.activate(settings.TIME_ZONE)


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (
            "2866ab3f-68c9-4a2c-9dc2-87bb6017f534",
            "Parent Category 05",
            "parent-category-05",
            1,
        ),
        (
            "d126b53f-0fbb-4810-ab1c-60dd9fa4c35c",
            "Parent Category 05 - Sub Category 05",
            "parent-category-05-sub-category-05",
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
        ("Test Category 01", "test-category-1", 1),
        ("Test Category 02", "test-category-2", 1),
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
    "id, web_id, name, slug, is_active, created_at, updated_at",
    [
        (
            "ccb75d32-8f7f-4fa1-9ff2-b75a6063ae48",
            "WEBID-3416B295F997",
            "Product 0020",
            "product-0020",
            1,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "9a41ebdf-468f-4434-8a54-45310b133c1d",
            "WEBID-6124C8F9066D",
            "Product 0040",
            "product-0040",
            1,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
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
    is_active,
    created_at,
    updated_at,
):
    """
    Test to verify the Product model data loaded from the fixture.
    """

    result = models.Product.objects.get(id=id)
    result_created_at = timezone.localtime(result.created_at).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    result_updated_at = timezone.localtime(result.updated_at).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    assert result.web_id == web_id
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active
    assert result_created_at == created_at
    assert result_updated_at == updated_at


@pytest.mark.parametrize(
    "web_id",
    [
        ("WEBID-3FC7F75709BF"),
        ("WEBID-1A241FC3E541"),
    ],
)
def test_inventory_product_uniqueness_integrity(db, product_factory, web_id):
    """
    Test to verify the Product model data uniqueness integrity.
    """

    new_web_id = product_factory.create(web_id=web_id)

    with pytest.raises(IntegrityError):
        product_factory.create(web_id=new_web_id.web_id)


@pytest.mark.dbfixture
@pytest.mark.parametrize("categories", [(2), (3), (4), (5), (6)])
def test_inventory_product_insert_data(
    db, product_factory, category_factory, categories
):
    """
    Test to verify the Product model data inserted using the factory.
    """

    category_list = [category_factory.create() for _ in range(categories)]

    product = product_factory.create(category=category_list)
    product = models.Product.objects.get(id=product.id)

    assert product.category.count() == categories
    for cat in category_list:
        assert str(cat.id) in [cat.id for cat in product.category.all()]


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, sku, upc, product_type, product, brand, is_active, retail_price, store_price, weight, created_at, updated_at",
    [
        (
            "9852dcfd-b916-4bef-a7b8-659d6dbd2535",
            "SKU-0E62956AE8BA",
            "UPC-5C60A6BCED03",
            "5bc4b5f2-5b0c-45cf-bd93-db619a3163c2",
            "386656dd-dc59-4e65-90b1-3af8608d063d",
            "93d321ed-c93b-4ceb-b046-30f0d2311804",
            1,
            268,
            163,
            297,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "b40922f8-1438-450a-8de6-c1648e7b94d0",
            "SKU-8354E8805A1B",
            "UPC-768CA4E09A0A",
            "102778a9-1f01-4ff0-ab1e-d8308fae62bf",
            "6742e29c-d857-473e-9c72-3c8cf2353f16",
            "a77c3a48-133e-4bdb-b0ec-1f825de6c9a5",
            1,
            712,
            487,
            157,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
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
    created_at,
    updated_at,
):
    """
    Test to verify the ProductInventory model data loaded from the fixture.
    """

    result = models.ProductInventory.objects.get(id=id)
    result_created_at = timezone.localtime(result.created_at).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    result_updated_at = timezone.localtime(result.updated_at).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    assert result.sku == sku
    assert result.upc == upc
    assert result.product_type.id == product_type
    assert result.product.id == product
    assert result.brand.id == brand
    assert result.is_active == is_active
    assert result.retail_price == retail_price
    assert result.store_price == store_price
    assert result.weight == weight
    assert result_created_at == created_at
    assert result_updated_at == updated_at


@pytest.mark.parametrize(
    "product_type__name, brand__name",
    [
        (
            "Test Product Type 01",
            "Test Brand 01",
        ),
        (
            "Test Product Type 02",
            "Test Brand 02",
        ),
    ],
)
def test_inventory_product_inventory_insert_data(
    db,
    product_inventory_factory,
    product_type__name,
    brand__name,
):
    """
    Test to verify the ProductInventory model data inserted using the factory.
    """

    new_product_inventory = product_inventory_factory.create(
        product_type__name=product_type__name,
        brand__name=brand__name,
    )

    assert new_product_inventory.product_type.name == product_type__name
    assert new_product_inventory.brand.name == brand__name
    assert new_product_inventory.is_active == 1
    assert new_product_inventory.retail_price == 97
    assert new_product_inventory.store_price == 92
    assert new_product_inventory.weight == 987


@pytest.mark.parametrize(
    "name",
    [
        ("Test Product Type 01"),
        ("Test Product Type 02"),
    ],
)
def test_inventory_producttype_insert_data(db, product_type_factory, name):
    """
    Test to verify the ProductType model data inserted using the factory.
    """

    new_type = product_type_factory.create(name=name)

    assert new_type.name == name


@pytest.mark.parametrize(
    "name",
    [
        ("Test Product Type 11"),
        ("Test Product Type 12"),
    ],
)
def test_inventory_producttype_uniqueness_integrity(db, product_type_factory, name):
    """
    Test to verify the ProductType model data uniqueness integrity.
    """

    product_type_factory.create(name=name)

    with pytest.raises(IntegrityError):
        product_type_factory.create(name=name)


@pytest.mark.parametrize(
    "name",
    [
        ("Test Brand 01"),
        ("Test Brand 02"),
    ],
)
def test_inventory_brand_insert_data(db, brand_factory, name):
    """
    Test to verify the Brand model data inserted using the factory.
    """

    new_brand = brand_factory.create(name=name)

    assert new_brand.name == name


@pytest.mark.parametrize(
    "name",
    [
        ("Test Brand 11"),
        ("Test Brand 12"),
    ],
)
def test_inventory_brand_uniqueness_integrity(db, brand_factory, name):
    """
    Test to verify the Brand model data uniqueness integrity.
    """

    brand_factory.create(name=name)

    with pytest.raises(IntegrityError):
        brand_factory.create(name=name)


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_inventory, image, alt_text, is_feature, created_at, updated_at",
    [
        (
            "ebfd5fff-8687-416c-8879-4dd14fc34b18",
            "92a1d7ce-24ba-41b4-b0b5-ebc155708b46",
            "images/default.png",
            "a default image solid color",
            True,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "aa555b9f-085f-4a47-9f57-a647ebc25c92",
            "878eac95-1e06-4758-bf49-108d399269e1",
            "images/default.png",
            "a default image solid color",
            True,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
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
    result_created_at = timezone.localtime(result.created_at).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    result_updated_at = timezone.localtime(result.updated_at).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    assert result.product_inventory.id == product_inventory
    assert result.image == image
    assert result.alt_text == alt_text
    assert result.is_feature == is_feature
    assert result_created_at == created_at
    assert result_updated_at == updated_at


@pytest.mark.parametrize(
    "product_inventory__sku",
    [
        ("SKU-56CA5F6493DB"),
        ("SKU-BD8CEAD18F2A"),
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
            "b7ae373b-519f-4975-a211-6afb338b1b4d",
            "83322dbc-9ca0-4649-9a83-9fd4dec0eed9",
            "2024-02-15 22:14:18",
            66,
            60,
        ),
        (
            "acae856c-c345-4517-95a8-69ca6d7c06d0",
            "62b2351f-89f5-4e68-b7e3-7e31cb010a41",
            "2024-02-15 22:14:18",
            81,
            74,
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
    result_last_checked = timezone.localtime(result.last_checked).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    assert result.product_inventory.id == product_inventory
    assert result_last_checked == last_checked
    assert result.units == units
    assert result.units_sold == units_sold


@pytest.mark.parametrize(
    "product_inventory__sku",
    [
        ("SKU-DC3CAEF395CF"),
        ("SKU-9F525D9C5531"),
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
    "id, name",
    [
        (
            "375f0c2a-e7e7-4331-87c7-74fc85c96aa0",
            "Product Attribute 02",
        ),
        (
            "39de9817-e88f-4163-881f-98fb9f81bbc9",
            "Product Attribute 04",
        ),
    ],
)
def test_inventory_product_attribute_dbfixture(db, db_fixture_setup, id, name):
    """
    Test to verify the ProductAttribute model data loaded from the fixture.
    """

    result = models.ProductAttribute.objects.get(id=id)

    assert result.id == id
    assert result.name == name


@pytest.mark.parametrize(
    "name",
    [
        ("Test Product Attribute 01"),
        ("Test Product Attribute 02"),
    ],
)
def test_inventory_product_attribute_insert_data(db, product_attribute_factory, name):
    """
    Test to verify the ProductAttribute model data inserted using the factory.
    """

    new_attribute = product_attribute_factory.create(name=name)

    assert new_attribute.name == name


@pytest.mark.parametrize(
    "name",
    [
        ("Test Product Attribute 11"),
        ("Test Product Attribute 12"),
    ],
)
def test_inventory_product_attribute_uniqueness_integrity(
    db, product_attribute_factory, name
):
    """
    Test to verify the ProductAttribute model data uniqueness integrity.
    """

    product_attribute_factory.create(name=name)

    with pytest.raises(IntegrityError):
        product_attribute_factory.create(name=name)


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_attribute, attribute_value",
    [
        (
            "e051a5ef-3f27-43f7-9a2b-587eda139e1f",
            "a0bb245f-2cf3-4b1a-923a-8157690f0a2c",
            "Product Attribute Value 001 - 02",
        ),
        (
            "27c54cad-de1d-4800-a6f6-22a77c84852d",
            "375f0c2a-e7e7-4331-87c7-74fc85c96aa0",
            "Product Attribute Value 002 - 02",
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

    assert result.id == id
    assert result.product_attribute.id == product_attribute
    assert result.attribute_value == attribute_value


@pytest.mark.parametrize(
    "attribute_value, product_attribute__name",
    [
        ("Test Attribute Value 001 - 01", "Test Attribute 001"),
        ("Test Attribute Value 002 - 01", "Test Attribute 002"),
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
