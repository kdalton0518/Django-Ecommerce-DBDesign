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
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
