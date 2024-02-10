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

    class Index:
        name = "product_inventories"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ProductInventory
        fields = [
            "sku",
            "upc",
            "is_active",
            "retail_price",
            "store_price",
            "sale_price",
            "weight",
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
            "last_checked",
            "units",
            "units_sold",
        ]

    def prepare_product_inventory(self, instance):
        return (
            str(instance.product_inventory.id) if instance.product_inventory else None
        )
