from django.core.management import call_command
from django.core.management.base import BaseCommand


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

        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
        call_command("loaddata", "db_product_fixture.json")
        call_command("loaddata", "db_type_fixture.json")
        call_command("loaddata", "db_brand_fixture.json")
        call_command("loaddata", "db_product_inventory_fixture.json")
        call_command("loaddata", "db_media_fixture.json")
        call_command("loaddata", "db_stock_fixture.json")
