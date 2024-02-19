from rest_framework import serializers
from ecommerce.apps.inventory.models import *
from ecommerce.apps.promotion.models import *


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

    media = serializers.SerializerMethodField()
    stock = serializers.SerializerMethodField()

    class Meta:
        model = ProductInventory
        fields = "__all__"

    def get_media(self, obj):
        return [
            item["image"]
            for item in Media.objects.filter(product_inventory=obj).values("image")
        ]

    def get_stock(self, obj):
        return Stock.objects.filter(product_inventory=obj).values(
            "units", "units_sold", "last_checked"
        )

    # def get_promotions(self, obj):
    #     return [item["id"] for item in obj.promotions.values("id")]


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


class ProductInventoryPromotionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Promotion model.
    """

    class Meta:
        model = Promotion
        fields = ["id", "name", "promotion_reduction", "is_active", "is_schedule"]


class ProductInventoryRetrieveSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductInventory model.
    """

    product_type = ProductTypeSerializer()
    product = SimpleProductSerializer()
    brand = BrandSerializer()
    attribute_values = ProductAttributeValueSerializer(many=True)
    media = serializers.SerializerMethodField()
    stock = serializers.SerializerMethodField()
    promotions = ProductInventoryPromotionSerializer(many=True)

    class Meta:
        model = ProductInventory
        fields = "__all__"

    def get_media(self, obj):
        return Media.objects.filter(product_inventory=obj).values(
            "id", "image", "alt_text", "is_feature"
        )

    def get_stock(self, obj):
        return Stock.objects.filter(product_inventory=obj).values(
            "id", "units", "units_sold", "last_checked"
        )


class PromotionTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for the PromotionType model.
    """

    class Meta:
        model = PromotionType
        fields = "__all__"


class PromotionCouponSerializer(serializers.ModelSerializer):
    """
    Serializer for the Coupon model.
    """

    class Meta:
        model = Coupon
        exclude = ["description"]


class PromotionListSerializer(serializers.ModelSerializer):
    """
    Serializer for the Promotion model.
    """

    promotion_type = PromotionTypeSerializer()
    coupon = PromotionCouponSerializer()

    class Meta:
        model = Promotion
        exclude = ["description"]


class PromotionRetrieveSerializer(serializers.ModelSerializer):
    """
    Serializer for the Promotion model.
    """

    promotion_type = PromotionTypeSerializer()
    coupon = PromotionCouponSerializer()

    class Meta:
        model = Promotion
        fields = "__all__"
