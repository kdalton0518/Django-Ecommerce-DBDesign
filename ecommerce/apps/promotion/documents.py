# from django_elasticsearch_dsl import Document, fields
# from django_elasticsearch_dsl.registries import registry

# from .models import *


# @registry.register_document
# class PromotionTypeDocument(Document):
#     class Index:
#         name = "categories"
#         settings = {"number_of_shards": 1, "number_of_replicas": 0}

#     class Django:
#         model = PromotionType
#         fields = [
#             "id",
#             "name",
#         ]


# @registry.register_document
# class CouponDocument(Document):
#     class Index:
#         name = "products"
#         settings = {"number_of_shards": 1, "number_of_replicas": 0}

#     class Django:
#         model = Coupon
#         fields = [
#             "id",
#             "name",
#             "code",
#             "description",
#         ]


# @registry.register_document
# class PromotionDocument(Document):
#     promotion_type = fields.NestedField(
#         properties={
#             "id": fields.KeywordField(),
#             "name": fields.KeywordField(),
#         }
#     )
#     coupon = fields.NestedField(
#         properties={
#             "id": fields.KeywordField(),
#             "name": fields.KeywordField(),
#             "code": fields.KeywordField(),
#         }
#     )
#     products_on_promotion = fields.NestedField(
#         properties={
#             "id": fields.KeywordField(),
#             "product_inventory": fields.KeywordField(),
#             "promotion_price": fields.FloatField(),
#             "price_override": fields.BooleanField(),
#         }
#     )

#     class Index:
#         name = "product_types"
#         settings = {"number_of_shards": 1, "number_of_replicas": 0}

#     class Django:
#         model = Promotion
#         fields = [
#             "id",
#             "name",
#             "description",
#             "promotion_reduction",
#             "is_active",
#             "is_schedule",
#             "promotion_start",
#             "promotion_end",
#         ]
