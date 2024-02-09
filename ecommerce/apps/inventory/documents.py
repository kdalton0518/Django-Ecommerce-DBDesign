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
