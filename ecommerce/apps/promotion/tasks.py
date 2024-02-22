from decimal import Decimal
from math import ceil

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
