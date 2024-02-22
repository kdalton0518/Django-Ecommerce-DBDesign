import pytest
from django.core.management import call_command


@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load DB data fixtures for testing.
    This fixture loads a set of predefined data into the database before the tests run.
    It uses Django's `call_command` function to load data from JSON fixtures.
    The fixture is session-scoped, so the data is loaded only once per test session.
    Args:
        django_db_setup (fixture): A pytest-django fixture that sets up the test database.
        django_db_blocker (fixture): A pytest-django fixture that provides a context manager for blocking database access.
    """
    with django_db_blocker.unblock():
        call_command("makemigrations")
        call_command("migrate")

        # Load admin-related fixtures
        call_command("loaddata", "db_admin_fixture.json")

        # Load inventory-related fixtures
        call_command(
            "loaddata",
            "db_type_fixture.json",
        )
        call_command(
            "loaddata",
            "db_brand_fixture.json",
        )
        call_command(
            "loaddata",
            "db_product_attribute_fixture.json",
        )
        call_command(
            "loaddata",
            "db_product_attribute_value_fixture.json",
        )
        call_command(
            "loaddata",
            "db_category_fixture.json",
        )

        # Load product-related fixtures
        call_command(
            "loaddata",
            "db_product_fixture.json",
        )
        call_command(
            "loaddata",
            "db_product_inventory_fixture.json",
        )

        # Load promotion-related fixtures
        call_command(
            "loaddata",
            "db_promotion_type_fixture.json",
        )
        call_command(
            "loaddata",
            "db_coupon_fixture.json",
        )
        call_command(
            "loaddata",
            "db_promotion_fixture.json",
        )

        # Load remaining fixtures
        call_command(
            "loaddata",
            "db_media_fixture.json",
        )
        call_command(
            "loaddata",
            "db_stock_fixture.json",
        )
