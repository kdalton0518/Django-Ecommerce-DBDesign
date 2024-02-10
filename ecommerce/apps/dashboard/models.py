import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User model that extends Django's AbstractUser model.
    This model adds a UUID primary key field to the base user model provided by Django.
    The UUID is generated automatically and is not editable. It also overrides the username and email fields
    to make them unique and adds first_name and last_name fields.
    Attributes:
        id (CharField): The primary key for the User model. It's a CharField that gets its default value
                        from the uuid.uuid4 function and is not editable.
        username (CharField): A CharField that stores the username. It is unique and has a maximum length of 30 characters.
        email (EmailField): An EmailField that stores the user's email. It is unique.
        first_name (CharField): A CharField that stores the user's first name. It has a maximum length of 30 characters.
        last_name (CharField): A CharField that stores the user's last name. It has a maximum length of 30 characters.
    """

    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=256
    )
    username = models.CharField(
        unique=True,
        verbose_name="Username",
        error_messages={"unique": ("A user with this username already exists!")},
        max_length=30,
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email Address",
        error_messages={"unique": ("A user with this email already exists!")},
    )
    first_name = models.CharField(max_length=30, verbose_name="First Name")
    last_name = models.CharField(max_length=30, verbose_name="Last Name")

    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email
