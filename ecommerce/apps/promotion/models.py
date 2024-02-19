import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class PromotionType(models.Model):
    """
    The PromotionType class inherits from models.Model.
    It represents a type of promotion in the system.

    Attributes:
        id (CharField): The primary key for the PromotionType model. It's a CharField that gets its default value
                        from the uuid.uuid4 function and is not editable. It has a maximum length of 256 characters.
        name (CharField): A CharField that stores the promotion type name. It is required and has a maximum length of 100 characters.
                          The verbose name is "Promotions Type Name" and the help text is "format: required, max length 100 characters".
                          It is unique across the model.
    """

    id = models.CharField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        max_length=256,
        validators=[MaxValueValidator(256)],
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Promotions Type Name",
        help_text=_("format: required, max length 100 characters"),
        null=False,
        blank=False,
        unique=True,
        validators=[MaxValueValidator(100)],
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Promotion Type"
        verbose_name_plural = "Promotion Types"


class Coupon(models.Model):
    """
    The Coupon class inherits from models.Model.
    It represents a coupon in the system.

    Attributes:
        id (CharField): The primary key for the Coupon model. It's a CharField that gets its default value
                        from the uuid.uuid4 function and is not editable. It has a maximum length of 256 characters.
        name (CharField): A CharField that stores the coupon name. It is required and has a maximum length of 100 characters.
                          The verbose name is "Coupon Name" and the help text is "format: required, max length 100 characters".
        code (CharField): A CharField that stores the coupon code. It is required, unique, and has a maximum length of 20 characters.
                          The verbose name is "Coupon Code" and the help text is "format: required, max length 20 characters".
        description (TextField): A TextField that stores the coupon description. It is required and has a maximum length of 500 characters.
                                 The verbose name is "Coupon Description" and the help text is "format: required, max length 500 characters".
    """

    id = models.CharField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        max_length=256,
        validators=[MaxValueValidator(256)],
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Coupon Name",
        help_text=_("format: required, max length 100 characters"),
        null=False,
        blank=False,
        unique=False,
        validators=[MaxValueValidator(100)],
    )
    code = models.CharField(
        max_length=20,
        verbose_name="Coupon Code",
        help_text=_("format: required, max length 20 characters"),
        null=False,
        blank=False,
        unique=True,
        validators=[MaxValueValidator(20)],
    )
    description = models.TextField(
        verbose_name="Coupon Description",
        help_text=_("format: required, max length 500 characters"),
        null=False,
        blank=False,
        unique=False,
        validators=[MaxValueValidator(500)],
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"


class Promotion(models.Model):
    """
    The Promotion class inherits from models.Model.
    It represents a promotion in the system.

    Attributes:
        id (CharField): The primary key for the Promotion model. It's a CharField that gets its default value
                        from the uuid.uuid4 function and is not editable. It has a maximum length of 256 characters.
        name (CharField): A CharField that stores the promotion name. It is required and has a maximum length of 100 characters.
                          The verbose name is "Promotion Name" and the help text is "format: required, max length 100 characters".
        description (TextField): A TextField that stores the promotion description. It is required and has a maximum length of 500 characters.
                                 The verbose name is "Promotion Description" and the help text is "format: required, max length 500 characters".
        promotion_reduction (IntegerField): An IntegerField that stores the promotion reduction. It is required and its default value is 0.
                                            The verbose name is "Promotion Reduction" and the help text is "format: required, integer".
        is_active (BooleanField): A BooleanField that indicates whether the promotion is active. It is required and its default value is False.
                                  The verbose name is "Promotion Status" and the help text is "format: required, boolean".
        is_schedule (BooleanField): A BooleanField that indicates whether the promotion is scheduled.
                                    It is required and its default value is False.
                                     The verbose name is "Promotion Schedule" and the help text is "format: required, boolean".
        promotion_start (DateField): A DateField that stores the start date of the promotion. It is not required and can be null.
                                     The verbose name is "Promotion Start" and the help text is "format: required, date".
        promotion_end (DateField): A DateField that stores the end date of the promotion. It is not required and can be null.
                                   The verbose name is "Promotion End" and the help text is "format: required, date".
        promotion_type (ForeignKey): A ForeignKey that links to the PromotionType model. It is required.
                                     The verbose name is "Promotion Type" and the help text is "format: required, foreign key".
        coupon (ForeignKey): A ForeignKey that links to the Coupon model. It is not required and can be null.
                             The verbose name is "Coupon" and the help text is "format: required, foreign key".

    Methods:
        clean: This method validates the model instance. It checks that the promotion start date is not greater than the promotion end date,
               and that the promotion reduction is between 0 and 100.
    """

    id = models.CharField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        max_length=256,
        validators=[MaxValueValidator(256)],
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Promotion Name",
        help_text=_("format: required, max length 100 characters"),
        null=False,
        blank=False,
        unique=True,
        validators=[MaxValueValidator(100)],
    )
    description = models.TextField(
        verbose_name="Promotion Description",
        help_text=_("format: required, max length 500 characters"),
        null=False,
        blank=False,
        unique=False,
        validators=[MaxValueValidator(500)],
    )
    promotion_reduction = models.IntegerField(
        verbose_name="Promotion Reduction",
        help_text=_("format: required, integer"),
        default=0,
        null=False,
        blank=False,
        unique=False,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    is_active = models.BooleanField(
        verbose_name="Promotion Status",
        help_text=_("format: required, boolean"),
        default=False,
        null=False,
        blank=False,
        unique=False,
    )
    is_schedule = models.BooleanField(
        verbose_name="Promotion Schedule",
        help_text=_("format: required, boolean"),
        default=False,
        null=False,
        blank=False,
        unique=False,
    )
    promotion_start = models.DateField(
        verbose_name="Promotion Start",
        help_text=_("format: required, date"),
        null=True,
        blank=True,
        unique=False,
    )
    promotion_end = models.DateField(
        verbose_name="Promotion End",
        help_text=_("format: required, date"),
        null=True,
        blank=True,
        unique=False,
    )

    promotion_type = models.ForeignKey(
        PromotionType,
        related_name="promotion_type",
        verbose_name="Promotion Type",
        on_delete=models.PROTECT,
        help_text=_("format: required, foreign key"),
        null=False,
        blank=False,
        unique=False,
    )
    coupon = models.ForeignKey(
        Coupon,
        related_name="coupon",
        verbose_name="Coupon",
        on_delete=models.PROTECT,
        help_text=_("format: required, foreign key"),
        null=True,
        blank=True,
        unique=False,
    )

    def __str__(self):
        return self.name

    def clean(self):
        if self.promotion_start and self.promotion_end:
            if self.promotion_start > self.promotion_end:
                raise ValidationError(
                    _(
                        "Promotion start date cannot be greater than the promotion end date"
                    )
                )

    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"
        ordering = ["-promotion_start", "-promotion_end"]
