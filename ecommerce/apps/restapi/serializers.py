from rest_framework import serializers
from ecommerce.apps.inventory.models import *


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "parent"]


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """

    class Meta:
        model = Product
        fields = "__all__"
