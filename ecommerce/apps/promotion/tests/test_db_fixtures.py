import pytest
from ecommerce.apps.promotion import models
from django.conf import settings
from django.utils import timezone
from decimal import Decimal


# Activate time zone
timezone.activate(settings.TIME_ZONE)


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name",
    [
        ("57cc369f-f5aa-4137-94eb-19e4b6d767cb", "Promotion Type 010"),
        ("6cb1ffd4-a8b8-4e60-b2f4-d97b9a4f085c", "Promotion Type 020"),
        ("c76617cf-107d-4e90-85aa-548f90ff1c20", "Promotion Type 030"),
        ("d1441d31-b432-427f-9d71-331567247725", "Promotion Type 040"),
        ("46075341-38a0-45e7-ada4-e3436d1810e5", "Promotion Type 050"),
    ],
)
def test_promotion_type_dbfixture(db, db_fixture_setup, id, name):
    """
    Test to verify the PromotionType model data loaded from the fixture.
    """

    result = models.PromotionType.objects.get(id=id)

    assert result.id == id
    assert result.name == name


@pytest.mark.parametrize(
    "name",
    [
        ("Test Promotion Type 001"),
        ("Test Promotion Type 002"),
        ("Test Promotion Type 003"),
        ("Test Promotion Type 004"),
        ("Test Promotion Type 005"),
    ],
)
def test_promotion_type_insert_data(db, promotion_type_factory, name):
    """
    Test to verify the PromotionType model data inserted using the factory.
    """

    new_promotion_type = promotion_type_factory.create(name=name)

    assert new_promotion_type.name == name


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, code",
    [
        ("20d0ed9d-0b0d-413b-afed-418042707ec7", "Coupon 010", "COUPON-08ED4C55"),
        ("26611939-e956-4b61-88de-14459b73ed2f", "Coupon 020", "COUPON-F9814538"),
        ("8628bd0d-fadc-430b-969b-87c0f1a76e2a", "Coupon 030", "COUPON-85064841"),
        ("ea35ad5d-0ee7-445c-93b3-1340bcaead01", "Coupon 040", "COUPON-55144A03"),
        ("11ab3602-edbe-4f44-bbab-e27b89d62ee3", "Coupon 050", "COUPON-1A97498E"),
    ],
)
def test_coupon_dbfixture(db, db_fixture_setup, id, name, code):
    """
    Test to verify the Coupon model data loaded from the fixture.
    """

    result = models.Coupon.objects.get(id=id)

    assert result.id == id
    assert result.name == name
    assert result.code == code


@pytest.mark.parametrize(
    "name, code",
    [
        ("Test Coupon 001", "COUPON-25CF4EB"),
        ("Test Coupon 002", "COUPON-F830472"),
        ("Test Coupon 003", "COUPON-49724C7"),
        ("Test Coupon 004", "COUPON-59FB455"),
        ("Test Coupon 005", "COUPON-642944E"),
    ],
)
def test_coupon_insert_data(db, coupon_factory, name, code):
    """
    Test to verify the Coupon model data inserted using the factory.
    """

    new_coupon = coupon_factory.create(name=name, code=code)

    assert new_coupon.name == name
    assert new_coupon.code == code


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, promotion_reduction, promotion_start, promotion_end",
    [
        (
            "4fc3ace7-0211-424c-8e70-03fe951ae69a",
            "Promotion 010",
            40,
            "2024-03-05",
            "2024-03-15",
        ),
        (
            "59ea5c93-6a73-4be3-bf8e-c25b6473988b",
            "Promotion 020",
            40,
            "2024-03-05",
            "2024-03-15",
        ),
        (
            "8f85e07f-e0ae-4197-b753-e1ea65601f50",
            "Promotion 030",
            40,
            "2024-03-05",
            "2024-03-15",
        ),
        (
            "47346a34-88d1-4f50-9c7c-d13cc6eca951",
            "Promotion 040",
            40,
            "2024-03-05",
            "2024-03-15",
        ),
        (
            "b0f5d48b-abbd-4ccf-8139-31db5a071a4a",
            "Promotion 050",
            40,
            "2024-03-05",
            "2024-03-15",
        ),
    ],
)
def test_promotion_dbfixture(
    db, db_fixture_setup, id, name, promotion_reduction, promotion_start, promotion_end
):
    """
    Test to verify the Promotion model data loaded from the fixture.
    """

    result = models.Promotion.objects.get(id=id)
    result_promotion_start = result.promotion_start.strftime("%Y-%m-%d")
    result_promotion_end = result.promotion_end.strftime("%Y-%m-%d")

    assert result.id == id
    assert result.name == name
    assert result.promotion_reduction == promotion_reduction
    assert result_promotion_start == promotion_start
    assert result_promotion_end == promotion_end


@pytest.mark.parametrize(
    "name, promotion_reduction, promotion_start, promotion_end",
    [
        ("Test Promotion 001", 40, "2024-03-05", "2024-03-15"),
        ("Test Promotion 002", 40, "2024-03-05", "2024-03-15"),
        ("Test Promotion 003", 40, "2024-03-05", "2024-03-15"),
        ("Test Promotion 004", 40, "2024-03-05", "2024-03-15"),
        ("Test Promotion 005", 40, "2024-03-05", "2024-03-15"),
    ],
)
def test_promotion_insert_data(
    db, promotion_factory, name, promotion_reduction, promotion_start, promotion_end
):
    """
    Test to verify the Promotion model data inserted using the factory.
    """

    new_promotion = promotion_factory.create(
        name=name,
        promotion_reduction=promotion_reduction,
        promotion_start=promotion_start,
        promotion_end=promotion_end,
    )

    assert new_promotion.name == name
    assert new_promotion.promotion_reduction == promotion_reduction
    assert new_promotion.promotion_start == promotion_start
    assert new_promotion.promotion_end == promotion_end
