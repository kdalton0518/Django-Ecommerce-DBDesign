from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import *


@registry.register_document
class CategoryDocument(Document):
    parent = fields.ObjectField(
        properties={
            "id": fields.KeywordField(),
            "name": fields.TextField(),
            "slug": fields.KeywordField(),
            "is_active": fields.BooleanField(),
        }
    )

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


@registry.register_document
class ProductDocument(Document):
    category = fields.ListField(
        fields.ObjectField(
            properties={
                "id": fields.KeywordField(),
                "name": fields.TextField(),
                "slug": fields.KeywordField(),
                "is_active": fields.BooleanField(),
            }
        )
    )

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
