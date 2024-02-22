from decimal import Decimal
from math import ceil

import pytest
from ecommerce.apps.promotion.models import ProductsOnPromotion
from ecommerce.apps.promotion.tasks import promotion_prices


@pytest.mark.parametrize(
    "promotion_reduction_1, promotion_reduction_2",
    [
        (20, 25),
        (30, 35),
    ],
)
def test_celery_promotion_prices(
    db,
    promotion_factory,
    product_inventory_factory,
    promotion_reduction_1,
    promotion_reduction_2,
):
    """
    Test to verify the promotion prices are updated using the Celery task.
    """

    # Create new promotions
    new_promotion_1 = promotion_factory(promotion_reduction=promotion_reduction_1)
    new_promotion_2 = promotion_factory(promotion_reduction=promotion_reduction_2)

    # Create new product inventories
    product_invent_1 = product_inventory_factory(retail_price=100, store_price=90)
    product_invent_2 = product_inventory_factory(retail_price=200, store_price=190)

    # Assign the products to the promotions
    new_promotion_1.products_on_promotion.add(product_invent_1, product_invent_2)
    new_promotion_2.products_on_promotion.add(product_invent_1, product_invent_2)

    # Save the promotions
    new_promotion_1.save()
    new_promotion_2.save()

    # Run the Celery task
    promotion_prices(new_promotion_1.id)
    promotion_prices(new_promotion_2.id)

    # Traverse over the promotions
    for promo in [new_promotion_1, new_promotion_2]:
        # Traverse over the products
        for prod_promo in ProductsOnPromotion.objects.filter(promotion__id=promo.id):
            # Check if the price is updated
            assert prod_promo.promotion_price == Decimal(
                ceil(
                    prod_promo.product_inventory.store_price
                    * Decimal((100 - promo.promotion_reduction) / 100)
                )
            )
