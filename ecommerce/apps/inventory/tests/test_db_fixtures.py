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
            "75025157-1bc9-4285-9cfd-672e80886211",
            "Parent Category 05",
            "parent-category-05",
            1,
        ),
        (
            "61df27b8-3144-401a-8520-d588fa3fadf4",
            "Parent Category 10",
            "parent-category-10",
            1,
        ),
        (
            "9e48e6ae-f401-4c80-926a-e2801152439b",
            "Parent Category 05 - Sub Category 02",
            "parent-category-05-sub-category-02",
            1,
        ),
        (
            "de487603-178c-4fe3-9418-6a91243f2b1b",
            "Parent Category 08 - Sub Category 04",
            "parent-category-08-sub-category-04",
            1,
        ),
        (
            "a511215c-552e-40f8-8363-367f43e80d04",
            "Parent Category 10 - Sub Category 02",
            "parent-category-10-sub-category-02",
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
    "id, web_id, name, slug, is_active, created_at, updated_at",
    [
        (
            "81949235-cf0d-4bd6-844a-444a422d5786",
            "WEBID-2FC7F75709BE",
            "Product 0020",
            "product-0020",
            1,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "022d63aa-9b86-44a6-9748-8b5e6f3bdf6e",
            "WEBID-9A241FC3E549",
            "Product 0040",
            "product-0040",
            1,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "d021a95b-a17d-4567-8cc1-1bb582d6832e",
            "WEBID-B1E41EEB7DFE",
            "Product 0060",
            "product-0060",
            1,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "c047c29d-22e3-4824-889c-db21677edbc9",
            "WEBID-E0996F2CA172",
            "Product 0080",
            "product-0080",
            1,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "013bd94e-f669-41b5-ab6b-1d7d15f33ff8",
            "WEBID-F526D7811BE0",
            "Product 0100",
            "product-0100",
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
        ("WEBID-C1E41EEB7DFF"),
        ("WEBID-F0996F2CA173"),
        ("WEBID-G526D7811BE1"),
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
    "id, sku, upc, product_type, product, brand, is_active, retail_price, store_price, promotion_price, weight, created_at, updated_at",
    [
        (
            "c3e647eb-decc-444d-b530-fbd6424b4026",
            "SKU-45947A116CEF",
            "UPC-6AA225185113",
            "7214a28e-1bc5-462d-bca1-46e9e2191441",
            "bcf3f8e4-f0d0-435d-8c1e-3ee3fc7bd7df",
            "3f8fac29-92fc-4536-9c0a-46d882a96782",
            1,
            97,
            92,
            55.2,
            987,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "a8c87358-cc8e-4db2-8264-d48d93c3d364",
            "SKU-BCD276AAE2D7",
            "UPC-0B61178A3403",
            "6e510c62-d945-42c0-8555-99fb2dd6b64a",
            "4c85410b-c6fa-4154-98a6-f399afce7027",
            "3f8fac29-92fc-4536-9c0a-46d882a96782",
            1,
            97,
            92,
            55.2,
            987,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "45b65b23-44c5-46ea-88a1-dec9d89fc05b",
            "SKU-3969102B4A92",
            "UPC-817F4425D640",
            "266586e0-6621-423d-8f6b-bae43fcc06e4",
            "d487c229-82ab-4bba-9102-2ba1cb798d4d",
            "fd533f28-2491-40f6-bb50-318592e98a0e",
            1,
            97,
            92,
            55.2,
            987,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "db0c06f2-6d03-48f1-bd25-4cfc65fb90dc",
            "SKU-A6448AEABDA9",
            "UPC-3CFA24D92CE2",
            "7ff69010-2355-45e6-a6b7-b6c413dd2ffc",
            "ac5191d1-cd21-462b-955e-373a1bf7c91f",
            "fd533f28-2491-40f6-bb50-318592e98a0e",
            1,
            97,
            92,
            55.2,
            987,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "b47d087d-a460-4a08-b056-c55929315052",
            "SKU-F065242A5029",
            "UPC-5D46D19AC7E8",
            "266586e0-6621-423d-8f6b-bae43fcc06e4",
            "007c2e38-7e05-4c9f-be98-6b527d20bb8f",
            "9a44f44f-a592-4ee3-b43e-f7e0bf3db78e",
            1,
            97,
            92,
            55.2,
            987,
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
    promotion_price,
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
    assert result.promotion_price == Decimal(str(promotion_price))
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
        (
            "Test Product Type 03",
            "Test Brand 03",
        ),
        (
            "Test Product Type 04",
            "Test Brand 04",
        ),
        (
            "Test Product Type 5",
            "Test Brand 05",
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
    assert new_product_inventory.promotion_price == 55.2
    assert new_product_inventory.weight == 987


@pytest.mark.parametrize(
    "name",
    [
        ("Test Product Type 01"),
        ("Test Product Type 02"),
        ("Test Product Type 03"),
        ("Test Product Type 04"),
        ("Test Product Type 05"),
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
        ("Test Product Type 13"),
        ("Test Product Type 14"),
        ("Test Product Type 15"),
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
        ("Test Brand 03"),
        ("Test Brand 04"),
        ("Test Brand 05"),
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
        ("Test Brand 13"),
        ("Test Brand 14"),
        ("Test Brand 15"),
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
            "4eefd318-4430-4cbe-bf51-cef19ccd5a26",
            "19533832-836b-47da-8ebf-b0d4e3acc240",
            "images/default.png",
            "a default image solid color",
            True,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "cca1defe-7ac5-468d-9257-43268fd9eaa3",
            "9ad7d74e-881b-4d04-96d6-a8da0ccaf674",
            "images/default.png",
            "a default image solid color",
            True,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "362247c8-2bb8-4b5b-8ac8-8c6dc8bf7d3e",
            "4d9be56b-feed-4570-a515-fe61bc28e21e",
            "images/default.png",
            "a default image solid color",
            True,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "e0830e6a-460f-41fe-9f76-62e3f191c646",
            "d69f9e11-06e7-4b9d-9615-ad45e3ae4b0b",
            "images/default.png",
            "a default image solid color",
            True,
            "2024-02-15 22:14:18",
            "2024-02-15 22:14:18",
        ),
        (
            "87bf89eb-a6f1-4cf0-888d-b84e7cca228b",
            "fd33bb19-e678-4957-ab71-2b2f07c67540",
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
        ("SKU-98C33E3D2211"),
        ("SKU-BA40E4EF9EAE"),
        ("SKU-282684CCA1CD"),
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
            "b8e233ab-bc57-47d7-b765-0d25d76fccd0",
            "2ce051d9-b107-470a-90d7-a1f3f8d17442",
            "2024-02-15 22:14:18",
            135,
            45,
        ),
        (
            "87b87f49-b924-4893-a500-b914b9c08e17",
            "bfcd7b0b-24c6-40e9-a668-2090982dbad2",
            "2024-02-15 22:14:18",
            135,
            45,
        ),
        (
            "8fd0abc5-4cb9-498d-b0a2-f913f340f492",
            "9dd63498-1c63-4116-9ec5-7488e380398d",
            "2024-02-15 22:14:18",
            135,
            45,
        ),
        (
            "79ee91d1-7088-402c-be9e-c0ac0ba727f0",
            "9f45c36e-e639-4659-916b-84de5b58ec84",
            "2024-02-15 22:14:18",
            135,
            45,
        ),
        (
            "7a9e7e2d-a427-4b58-b3fb-90f193d98da5",
            "0b31921a-30c9-4974-87e9-73677bbf345f",
            "2024-02-15 22:14:18",
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
        ("SKU-4410F9A6A738"),
        ("SKU-FAD708AFCC9A"),
        ("SKU-7A281FE3AB1C"),
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
            "9e7f8df0-c163-4ed8-a532-323067f8b98f",
            "Product Attribute 02",
        ),
        (
            "2a3d2c93-c874-478d-9673-b5283b20057e",
            "Product Attribute 04",
        ),
        (
            "aac747f7-1d7a-46fa-99a6-3aa123e20a14",
            "Product Attribute 06",
        ),
        (
            "c985d780-3097-4845-b263-a8c159c2af04",
            "Product Attribute 08",
        ),
        (
            "7b36e7fa-af91-41ff-872f-ca3ff722ab97",
            "Product Attribute 10",
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
        ("Test Product Attribute 03"),
        ("Test Product Attribute 04"),
        ("Test Product Attribute 05"),
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
        ("Test Product Attribute 13"),
        ("Test Product Attribute 14"),
        ("Test Product Attribute 15"),
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
            "61f5a632-27b9-4018-bd07-7cfc6da73174",
            "68d5dc34-1f2d-4cec-98c7-73c7f57945b5",
            "Product Attribute Value 001 - 02",
        ),
        (
            "f49246c1-c937-4902-b531-a0c2e9665eb4",
            "9e7f8df0-c163-4ed8-a532-323067f8b98f",
            "Product Attribute Value 002 - 02",
        ),
        (
            "3057dce7-299a-4730-bf0f-b4f77242cf77",
            "d5e2b472-5232-4f73-a78a-cdb94462d56c",
            "Product Attribute Value 003 - 02",
        ),
        (
            "a560e912-5cf9-4ff5-95d8-8719772f7a83",
            "2a3d2c93-c874-478d-9673-b5283b20057e",
            "Product Attribute Value 004 - 02",
        ),
        (
            "e12733be-8fc8-4110-a7a2-95558fc36d5b",
            "5da3785b-9bfb-4ac3-823f-dbf80603789f",
            "Product Attribute Value 005 - 02",
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
        ("Test Attribute Value 001 - 02", "Test Attribute 001"),
        ("Test Attribute Value 001 - 03", "Test Attribute 001"),
        ("Test Attribute Value 002 - 01", "Test Attribute 002"),
        ("Test Attribute Value 002 - 02", "Test Attribute 002"),
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
