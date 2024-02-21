from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import IntegrityError


class Command(BaseCommand):
    """
    The Command class inherits from Django's BaseCommand.
    It is used to create a custom management command that can be run using the manage.py script.

    Attributes:
        handle(*args, **kwargs): The main method of the command. It is called when the command is run.
    """

    def handle(self, *args, **kwargs):
        """
        The handle method is the main method of the command.
        It is called when the command is run.
        """

        try:
            # Create and apply migrations
            call_command("makemigrations")
            call_command("migrate")

            # Load fixtures with potential dependencies
            self.load_fixture("main_db_admin_fixture.json")
            self.load_fixture("main_db_type_fixture.json")
            self.load_fixture("main_db_brand_fixture.json")
            self.load_fixture("main_db_product_attribute_fixture.json")
            self.load_fixture("main_db_product_attribute_value_fixture.json")
            self.load_fixture("main_db_category_fixture.json")

            # Load promotion-related fixtures
            self.load_fixture("main_db_promotion_type_fixture.json")
            self.load_fixture("main_db_coupon_fixture.json")
            self.load_fixture("main_db_promotion_fixture.json")

            # Load product-related fixtures
            self.load_fixture("main_db_product_fixture.json")
            self.load_fixture("main_db_product_inventory_fixture.json")

            # Load remaining fixtures
            self.load_fixture("main_db_media_fixture.json")
            self.load_fixture("main_db_stock_fixture.json")

            self.stdout.write(self.style.SUCCESS("Successfully loaded all fixtures."))

        except IntegrityError as e:
            self.stderr.write(self.style.ERROR(f"IntegrityError: {e}"))
            self.stderr.write(self.style.ERROR("Fix the issue and try again."))

    def load_fixture(self, fixture_name):
        """
        Load a single data fixture.

        Args:
            fixture_name (str): The name of the fixture file to load.
        """
        try:
            call_command("loaddata", fixture_name)
            self.stdout.write(
                self.style.SUCCESS(f"Successfully loaded {fixture_name}.")
            )
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error loading {fixture_name}: {e}"))
