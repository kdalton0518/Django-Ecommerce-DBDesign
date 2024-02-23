from decimal import Decimal
from math import ceil
from datetime import datetime

from celery import shared_task
from django.db import transaction


from ecommerce.apps.promotion.models import Promotion, ProductsOnPromotion
from ecommerce.apps.inventory.models import ProductInventory


@shared_task
def promotion_prices(promotion_id):
    """
    This task calculates the new prices for the products in a promotion

    Attributes:
        promotion_reduction (int): The reduction percentage for the promotion
        promotion_id (str): The id of the promotion
    """

    # Run the code and rollback the transaction if an error occurs
    with transaction.atomic():
        # Get the promotion
        promotion = Promotion.objects.get(id=promotion_id)

        # Get the products on the promotion
        products_on_promotion = ProductsOnPromotion.objects.filter(
            promotion__id=promotion_id
        )

        # Traverse over the products
        for prod_promo in products_on_promotion:
            # Get the product inventory
            product_inventory = ProductInventory.objects.get(
                id=prod_promo.product_inventory.id
            )

            # Calculate the new price
            new_price = ceil(
                product_inventory.store_price
                * Decimal((100 - promotion.promotion_reduction) / 100)
            )

            # Update the promotion price
            prod_promo.promotion_price = new_price
            prod_promo.save()


@shared_task
def promotion_prices_all():
    """
    This task calculates the new prices for the products in a promotion
    """

    # Run the code and rollback the transaction if an error occurs
    with transaction.atomic():
        # Get the products on the promotion
        products_on_promotion = ProductsOnPromotion.objects.all()

        # Traverse over the products
        for prod_promo in products_on_promotion:
            # Get the product inventory
            product_inventory = prod_promo.product_inventory

            # Get the promotion
            promotion = prod_promo.promotion

            # Calculate the new price
            new_price = ceil(
                product_inventory.store_price
                * Decimal((100 - promotion.promotion_reduction) / 100)
            )

            # Update the promotion price
            prod_promo.promotion_price = new_price
            prod_promo.save()


@shared_task
def promotion_management():
    """
    This task manages the promotions that are scheduled and active
    """

    # Run the code and rollback the transaction if an error occurs
    with transaction.atomic():
        # Get all the promotions that are scheduled
        promotions = Promotion.objects.filter(is_schedule=True)

        # Get the current date
        current_date = datetime.now().date()

        # Traverse over the promotions
        for promo in promotions:
            # If the promotion is scheduled
            if promo.is_schedule:
                # If the promotion end date is less than the current date
                if promo.promotion_end < current_date:
                    # Set the promotion to inactive and unscheduled
                    promo.is_active = False
                    promo.is_schedule = False
                    promo.save()
                else:
                    if promo.promotion_start <= current_date:
                        # Set the promotion to active
                        promo.is_active = True
                        promo.save()

                        # Call the promotion prices task
                        promotion_prices(promo.id)

                    else:
                        # Set the promotion to inactive
                        promo.is_active = False
                        promo.save()
