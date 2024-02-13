from rest_framework import serializers
from ecommerce.apps.inventory.models import *


class ParentCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the parent category.
    """

    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """

    parent = ParentCategorySerializer()

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "parent"]


class SimpleCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """

    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductType model.
    """

    class Meta:
        model = ProductType
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    """
    Serializer for the Brand model.
    """

    class Meta:
        model = Brand
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """

    category = SimpleCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductRetrieveSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """

    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"


class SimpleProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """

    class Meta:
        model = Product
        fields = ["id", "web_id", "name"]


class ProductInventoryListSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductInventory model.
    """

    class Meta:
        model = ProductInventory
        fields = "__all__"


class ProductInventoryProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductInventory model.
    """

    product = SimpleProductSerializer()

    class Meta:
        model = ProductInventory
        fields = "__all__"


class ProductAttributeSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductAttribute model.
    """

    class Meta:
        model = ProductAttribute
        fields = "__all__"


class SimpleProductAttributeSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductAttribute model.
    """

    class Meta:
        model = ProductAttribute
        fields = ["id", "name"]


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductAttributeValues model.
    """

    product_attribute = SimpleProductAttributeSerializer()

    class Meta:
        model = ProductAttributeValue
        fields = "__all__"


class ProductInventoryRetrieveSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductInventory model.
    """

    product_type = ProductTypeSerializer()
    product = SimpleProductSerializer()
    brand = BrandSerializer()
    attribute_values = ProductAttributeValueSerializer(many=True)

    class Meta:
        model = ProductInventory
        fields = "__all__"
