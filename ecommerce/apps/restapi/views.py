from rest_framework.response import Response
from rest_framework import status
from rest_framework import views, viewsets, mixins, pagination

from ecommerce.apps.inventory.models import *
from .serializers import *

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class RestAPIHome(views.APIView):
    """
    This class-based view handles the home endpoint of the REST API.
    """

    @swagger_auto_schema(
        operation_id="restapi_home",
        operation_description="Welcome to the E-commerce REST API",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Welcome to the E-commerce REST API",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "message": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Welcome message",
                        ),
                        "status": openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description="Status code",
                        ),
                    },
                ),
            )
        },
        tags=["RestAPI Home"],
    )
    def get(self, request):
        """
        This method handles the GET request for the home endpoint.
        It returns a welcome message and a status code.
        """
        return Response(
            {
                "message": "Welcome to the E-commerce REST API",
                "status": status.HTTP_200_OK,
            }
        )


class RestAPICategories(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    """
    This viewset automatically provides `list` and `retrieve` actions for the categories.
    """

    queryset = Category.objects.all()
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_id="restapi_categories_list",
        operation_description="List of Categories",
        manual_parameters=[
            openapi.Parameter(
                name="page",
                default=1,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Page number for the paginated response",
                required=True,
            ),
            openapi.Parameter(
                name="parent_name",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Parent category name",
                required=False,
                default=None,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="List of Category objects",
                schema=CategorySerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Page not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Invalid page.",
                        ),
                    },
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Parent category not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Parent category not found.",
                        ),
                    },
                ),
            ),
        },
        tags=["Categories"],
    )
    def list(self, request):
        """
        Override the list method to paginate the queryset manually.
        """

        page = request.query_params.get("page", 1)
        parent_name = request.query_params.get("parent_name")

        if page is not None:
            queryset = self.queryset.filter(parent__name=parent_name)

            if not queryset.exists():
                return Response(
                    {"detail": "Parent category not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            page = self.paginate_queryset(queryset)

            if parent_name == None:
                serializer = ParentCategorySerializer(page, many=True)
            else:
                serializer = CategorySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id="restapi_categories_retrieve",
        operation_description="Retrieve a Category by ID",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Category object",
                schema=CategorySerializer(),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Category ID required",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Category ID required.",
                        ),
                    },
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Category not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Category not found.",
                        ),
                    },
                ),
            ),
        },
        tags=["Categories"],
    )
    def retrieve(self, request, id=None):
        """
        Override the retrieve method to return the category details.
        """

        if id is None:
            return Response(
                {"detail": "Category ID required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            queryset = self.queryset.get(id=id)
            serializer = CategorySerializer(queryset)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response(
                {"detail": "Category not found."},
                status=status.HTTP_404_NOT_FOUND,
            )


class RestAPICategoriesProducts(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    This viewset automatically provides `list` action for the products under a category.
    """

    queryset = Product.objects.all()
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_id="restapi_categories_products_list",
        operation_description="List of Products under a Category",
        manual_parameters=[
            openapi.Parameter(
                name="page",
                default=1,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Page number for the paginated response",
                required=True,
            ),
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                description="Category ID",
                required=True,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Products under a Category",
                schema=CategorySerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Page not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Invalid page.",
                        ),
                    },
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Category not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Category not found.",
                        ),
                    },
                ),
            ),
        },
        tags=["Categories"],
    )
    def list(self, request, id=None):
        """
        Override the list method to paginate the queryset manually.
        """

        page = request.query_params.get("page", 1)
        category_id = id

        if page is not None:
            queryset = self.queryset.filter(category__id=category_id)

            if not queryset.exists():
                return Response(
                    {"detail": "Category not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            page = self.paginate_queryset(queryset)
            serializer = ProductListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductListSerializer(self.queryset, many=True)
        return Response(serializer.data)


class RestAPIProductTypes(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    """
    This viewset automatically provides `list` and `retrieve` actions for the product types.
    """

    queryset = ProductType.objects.all()
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_id="restapi_product_types_list",
        operation_description="List of Categories",
        manual_parameters=[
            openapi.Parameter(
                name="page",
                default=1,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Page number for the paginated response",
                required=True,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="List of ProductType objects",
                schema=CategorySerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Page not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Invalid page.",
                        ),
                    },
                ),
            ),
        },
        tags=["ProductType"],
    )
    def list(self, request):
        """
        Override the list method to paginate the queryset manually.
        """

        page = self.paginate_queryset(self.queryset)

        if page is not None:
            serializer = ProductTypeSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductTypeSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id="restapi_product_types_retrieve",
        operation_description="Retrieve a ProductType by ID",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="ProductType object",
                schema=ProductTypeSerializer(),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="ProductType ID required",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="ProductType ID required.",
                        ),
                    },
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="ProductType not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="ProductType not found.",
                        ),
                    },
                ),
            ),
        },
        tags=["ProductType"],
    )
    def retrieve(self, request, id=None):
        """
        Override the retrieve method to return the productType details.
        """

        if id is None:
            return Response(
                {"detail": "ProductType ID required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            queryset = self.queryset.get(id=id)
            serializer = ProductTypeSerializer(queryset)
            return Response(serializer.data)
        except ProductType.DoesNotExist:
            return Response(
                {"detail": "ProductType not found."},
                status=status.HTTP_404_NOT_FOUND,
            )


class RestAPIProductTypesProducts(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    This viewset automatically provides `list` action for the products under a product type.
    """

    queryset = ProductInventory.objects.all()
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_id="restapi_product_types_products_list",
        operation_description="List of Products under a Product Type",
        manual_parameters=[
            openapi.Parameter(
                name="page",
                default=1,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Page number for the paginated response",
                required=True,
            ),
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                description="Product Type ID",
                required=True,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Products under a Product Type",
                schema=ProductListSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Page not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Invalid page.",
                        ),
                    },
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Product Type not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Product Type not found.",
                        ),
                    },
                ),
            ),
        },
        tags=["ProductType"],
    )
    def list(self, request, id=None):
        """
        Override the list method to paginate the queryset manually.
        """

        page = request.query_params.get("page", 1)
        product_type_id = id

        if page is not None:
            queryset = self.queryset.filter(product_type__id=product_type_id)

            if not queryset.exists():
                return Response(
                    {"detail": "Product Type not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            page = self.paginate_queryset(queryset)
            serializer = ProductInventoryProductSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductInventoryProductSerializer(self.queryset, many=True)
        return Response(serializer.data)


class RestAPIBrands(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    """
    This viewset automatically provides `list` and `retrieve` actions for the brands.
    """

    queryset = Brand.objects.all()
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_id="restapi_brands_list",
        operation_description="List of Brands",
        manual_parameters=[
            openapi.Parameter(
                name="page",
                default=1,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Page number for the paginated response",
                required=True,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="List of Brand objects",
                schema=BrandSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Page not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Invalid page.",
                        ),
                    },
                ),
            ),
        },
        tags=["Brands"],
    )
    def list(self, request):
        """
        Override the list method to paginate the queryset manually.
        """

        page = self.paginate_queryset(self.queryset)

        if page is not None:
            serializer = BrandSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id="restapi_brands_retrieve",
        operation_description="Retrieve a Brand by ID",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Brand object",
                schema=BrandSerializer(),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Brand ID required",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Brand ID required.",
                        ),
                    },
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Brand not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Brand not found.",
                        ),
                    },
                ),
            ),
        },
        tags=["Brands"],
    )
    def retrieve(self, request, id=None):
        """
        Override the retrieve method to return the brand details.
        """

        if id is None:
            return Response(
                {"detail": "Brand ID required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            queryset = self.queryset.get(id=id)
            serializer = BrandSerializer(queryset)
            return Response(serializer.data)
        except Brand.DoesNotExist:
            return Response(
                {"detail": "Brand not found."},
                status=status.HTTP_404_NOT_FOUND,
            )


class RestAPIBrandsProducts(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    This viewset automatically provides `list` action for the products under a brand.
    """

    queryset = ProductInventory.objects.all()
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_id="restapi_brands_products_list",
        operation_description="List of Products under a Brand",
        manual_parameters=[
            openapi.Parameter(
                name="page",
                default=1,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Page number for the paginated response",
                required=True,
            ),
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                description="Brand ID",
                required=True,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Products under a Brand",
                schema=ProductListSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Page not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Invalid page.",
                        ),
                    },
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Brand not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Brand not found.",
                        ),
                    },
                ),
            ),
        },
        tags=["Brands"],
    )
    def list(self, request, id=None):
        """
        Override the list method to paginate the queryset manually.
        """

        page = request.query_params.get("page", 1)
        brand_id = id

        if page is not None:
            queryset = self.queryset.filter(brand__id=brand_id)

            if not queryset.exists():
                return Response(
                    {"detail": "Brand not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            page = self.paginate_queryset(queryset)
            serializer = ProductInventoryProductSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductInventoryProductSerializer(self.queryset, many=True)
        return Response(serializer.data)


class RestAPIProducts(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    """
    This viewset automatically provides `list` and `retrieve` actions for the products.
    """

    queryset = Product.objects.all()
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_id="restapi_products_list",
        operation_description="List of Products",
        manual_parameters=[
            openapi.Parameter(
                name="page",
                default=1,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Page number for the paginated response",
                required=True,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="List of Product objects",
                schema=ProductListSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Page not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Invalid page.",
                        ),
                    },
                ),
            ),
        },
        tags=["Products"],
    )
    def list(self, request):
        """
        Override the list method to paginate the queryset manually.
        """

        page = self.paginate_queryset(self.queryset)

        if page is not None:
            serializer = ProductListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id="restapi_products_retrieve",
        operation_description="Retrieve a Product by ID",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Product object",
                schema=ProductRetrieveSerializer(),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Product ID required",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Product ID required.",
                        ),
                    },
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Product not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Product not found.",
                        ),
                    },
                ),
            ),
        },
        tags=["Products"],
    )
    def retrieve(self, request, id=None):
        """
        Override the retrieve method to return the product details.
        """

        if id is None:
            return Response(
                {"detail": "Product ID required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            queryset = self.queryset.get(id=id)
            serializer = ProductRetrieveSerializer(queryset)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(
                {"detail": "Product not found."},
                status=status.HTTP_404_NOT_FOUND,
            )


class RestAPIProductInventory(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    """
    This viewset automatically provides `list` and `retrieve` actions for the product inventory.
    """

    queryset = ProductInventory.objects.all()
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_id="restapi_product_inventory_list",
        operation_description="List of Product Inventory",
        manual_parameters=[
            openapi.Parameter(
                name="page",
                default=1,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Page number for the paginated response",
                required=True,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="List of ProductInventory objects",
                schema=ProductInventoryListSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Page not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Invalid page.",
                        ),
                    },
                ),
            ),
        },
        tags=["Product Inventory"],
    )
    def list(self, request):
        """
        Override the list method to paginate the queryset manually.
        """

        page = self.paginate_queryset(self.queryset)

        if page is not None:
            serializer = ProductInventoryListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductInventoryListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id="restapi_product_inventory_retrieve",
        operation_description="Retrieve a Product Inventory by ID",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="ProductInventory object",
                schema=ProductInventoryRetrieveSerializer(),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="ProductInventory ID required",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="ProductInventory ID required.",
                        ),
                    },
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="ProductInventory not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="ProductInventory not found.",
                        ),
                    },
                ),
            ),
        },
        tags=["Product Inventory"],
    )
    def retrieve(self, request, id=None):
        """
        Override the retrieve method to return the product inventory details.
        """

        if id is None:
            return Response(
                {"detail": "ProductInventory ID required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            queryset = self.queryset.get(id=id)
            serializer = ProductInventoryRetrieveSerializer(queryset)
            return Response(serializer.data)
        except ProductInventory.DoesNotExist:
            return Response(
                {"detail": "ProductInventory not found."},
                status=status.HTTP_404_NOT_FOUND,
            )


class RestAPIPromotions(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    """
    This viewset automatically provides `list` and `retrieve` actions for the promotions.
    """

    queryset = Promotion.objects.all()
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_id="restapi_promotions_list",
        operation_description="List of Promotions",
        manual_parameters=[
            openapi.Parameter(
                name="page",
                default=1,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Page number for the paginated response",
                required=True,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="List of Promotion objects",
                schema=PromotionListSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Page not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Invalid page.",
                        ),
                    },
                ),
            ),
        },
        tags=["Promotions"],
    )
    def list(self, request):
        """
        Override the list method to paginate the queryset manually.
        """

        page = self.paginate_queryset(self.queryset)

        if page is not None:
            serializer = PromotionListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PromotionListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id="restapi_promotions_retrieve",
        operation_description="Retrieve a Promotion by ID",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Promotion object",
                schema=PromotionRetrieveSerializer(),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Promotion ID required",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Promotion ID required.",
                        ),
                    },
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Promotion not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Promotion not found.",
                        ),
                    },
                ),
            ),
        },
        tags=["Promotions"],
    )
    def retrieve(self, request, id=None):
        """
        Override the retrieve method to return the promotion details.
        """

        if id is None:
            return Response(
                {"detail": "Promotion ID required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            queryset = self.queryset.get(id=id)
            serializer = PromotionRetrieveSerializer(queryset)
            return Response(serializer.data)
        except Promotion.DoesNotExist:
            return Response(
                {"detail": "Promotion not found."},
                status=status.HTTP_404_NOT_FOUND,
            )


class RestAPIPromotionsProductInventories(
    viewsets.GenericViewSet, mixins.ListModelMixin
):
    """
    This viewset automatically provides `list` action for the product inventories under a promotion.
    """

    queryset = ProductInventory.objects.all()
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_id="restapi_promotions_product_inventories_list",
        operation_description="List of Product Inventories under a Promotion",
        manual_parameters=[
            openapi.Parameter(
                name="page",
                default=1,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Page number for the paginated response",
                required=True,
            ),
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                description="Promotion ID",
                required=True,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Product Inventories under a Promotion",
                schema=ProductInventoryListSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Page not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Invalid page.",
                        ),
                    },
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Promotion not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Promotion not found.",
                        ),
                    },
                ),
            ),
        },
        tags=["Promotions"],
    )
    def list(self, request, id=None):
        """
        Override the list method to paginate the queryset manually.
        """

        page = request.query_params.get("page", 1)
        promotion_id = id

        if page is not None:
            queryset = self.queryset.filter(promotions__id=promotion_id)

            if not queryset.exists():
                return Response(
                    {"detail": "Promotion not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            page = self.paginate_queryset(queryset)
            serializer = ProductInventoryListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductInventoryListSerializer(self.queryset, many=True)
        return Response(serializer.data)
