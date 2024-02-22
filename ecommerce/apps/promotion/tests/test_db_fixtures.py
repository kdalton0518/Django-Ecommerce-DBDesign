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
        ("66e4d5c4-ef28-4fd8-86ea-c5323f0e1817", "Promotion Type 010"),
        ("419776eb-3a2d-4c87-925d-47ae9fa71b9a", "Promotion Type 020"),
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
        ("1e04be4f-734c-4223-96ec-f0bf565defde", "Coupon 010", "COUPON-EBEB400E"),
        ("b370560e-62ab-4f2b-b6d6-0d49cee19ed9", "Coupon 020", "COUPON-B43A4C10"),
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
            "debaef40-1984-4629-b7f7-3140b8d48d86",
            "Promotion 0010",
            34,
            "2024-03-05",
            "2024-03-15",
        ),
        (
            "fa07ec0b-e73f-4b0d-824c-e4bb52f64cf5",
            "Promotion 0020",
            38,
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
        ("Test Promotion 001", 10, "2024-03-05", "2024-03-15"),
        ("Test Promotion 002", 15, "2024-03-05", "2024-03-15"),
        ("Test Promotion 003", 20, "2024-03-05", "2024-03-15"),
        ("Test Promotion 004", 25, "2024-03-05", "2024-03-15"),
        ("Test Promotion 005", 30, "2024-03-05", "2024-03-15"),
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
