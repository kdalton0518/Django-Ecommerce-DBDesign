from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import *


@registry.register_document
class CategoryDocument(Document):
    parent = fields.KeywordField()

    class Index:
        name = "categories"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "is_active",
        ]

    def prepare_parent(self, instance):
        return str(instance.parent.id) if instance.parent else None


@registry.register_document
class ProductDocument(Document):
    category = fields.ListField(fields.KeywordField())

    class Index:
        name = "products"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Product
        fields = [
            "id",
            "web_id",
            "name",
            "slug",
            "description",
            "is_active",
            "created_at",
            "updated_at",
        ]

    def prepare_category(self, instance):
        return [str(category.id) for category in instance.category.all()]


@registry.register_document
class ProductTypeDocument(Document):
    class Index:
        name = "product_types"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ProductType
        fields = [
            "id",
            "name",
        ]


@registry.register_document
class BrandDocument(Document):
    class Index:
        name = "brands"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Brand
        fields = [
            "id",
            "name",
        ]


@registry.register_document
class ProductAttributeDocument(Document):
    class Index:
        name = "product_attributes"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ProductAttribute
        fields = [
            "id",
            "name",
            "description",
        ]


@registry.register_document
class ProductAttributeValue(Document):
    product_attribute = fields.KeywordField()

    class Index:
        name = "product_attribute_values"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ProductAttributeValue
        fields = [
            "id",
            "attribute_value",
        ]

    def prepare_product_attribute(self, instance):
        return (
            str(instance.product_attribute.id) if instance.product_attribute else None
        )


@registry.register_document
class ProductInventoryDocument(Document):
    product_type = fields.KeywordField()
    product = fields.KeywordField()
    brand = fields.KeywordField()
    attribute_values = fields.ListField(fields.KeywordField())
    promotions = fields.ListField(fields.KeywordField())
    media = fields.NestedField(
        properties={
            "id": fields.KeywordField(),
            "image": fields.FileField(),
            "is_feature": fields.BooleanField(),
        }
    )
    stock = fields.NestedField(
        properties={
            "id": fields.KeywordField(),
            "last_checked": fields.DateField(),
            "units": fields.IntegerField(),
            "units_sold": fields.IntegerField(),
        }
    )

    class Index:
        name = "product_inventories"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "upc",
            "is_active",
            "retail_price",
            "store_price",
            "weight",
            "promotion_price",
            "price_override",
            "is_on_sale",
            "is_digital",
            "created_at",
            "updated_at",
        ]

    def prepare_product_type(self, instance):
        return str(instance.product_type.id) if instance.product_type else None

    def prepare_product(self, instance):
        return str(instance.product.id) if instance.product else None

    def prepare_brand(self, instance):
        return str(instance.brand.id) if instance.brand else None

    def prepare_attribute_values(self, instance):
        return [str(value.id) for value in instance.attribute_values.all()]

    def prepare_promotions(self, instance):
        return [str(promotion.id) for promotion in instance.promotions.all()]

    def prepare_media(self, instance):
        return [
            {
                "id": str(media.id),
                "image": media.image.url if media.image else None,
                "is_feature": media.is_feature if media.is_feature else False,
            }
            for media in Media.objects.filter(product_inventory=instance)
        ]

    def prepare_stock(self, instance):
        return [
            {
                "id": str(stock.id),
                "last_checked": stock.last_checked,
                "units": stock.units,
                "units_sold": stock.units_sold,
            }
            for stock in Stock.objects.filter(product_inventory=instance)
        ]


@registry.register_document
class MediaDocument(Document):
    product_inventory = fields.KeywordField()
    image = fields.FileField()

    class Index:
        name = "medias"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Media
        fields = [
            "id",
            "alt_text",
            "is_feature",
            "created_at",
            "updated_at",
        ]

    def prepare_product_inventory(self, instance):
        return (
            str(instance.product_inventory.id) if instance.product_inventory else None
        )

    def prepare_image(self, instance):
        return instance.image.url if instance.image else None


@registry.register_document
class StockDocument(Document):
    product_inventory = fields.KeywordField()

    class Index:
        name = "stocks"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Stock
        fields = [
            "id",
            "last_checked",
            "units",
            "units_sold",
        ]

    def prepare_product_inventory(self, instance):
        return (
            str(instance.product_inventory.id) if instance.product_inventory else None
        )
