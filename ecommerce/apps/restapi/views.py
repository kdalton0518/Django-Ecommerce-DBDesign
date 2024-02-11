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
        tags=["RestAPI"],
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


class RestAPIParentCategories(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    This viewset automatically provides `list` actions for the parent categories.
    """

    queryset = Category.objects.filter(parent=None)
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_id="restapi_parent_categories_list",
        operation_description="List of Parent Categories",
        manual_parameters=[
            openapi.Parameter(
                name="page",
                default=1,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="page number for the paginated response",
                required=True,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="List of Parent Category objects",
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
        tags=["RestAPI"],
    )
    def list(self, request):
        """
        Override the list method to paginate the queryset manually.
        """

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = CategorySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class RestAPISubCategories(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    This viewset automatically provides `list` actions for the sub categories.
    """

    queryset = Category.objects.filter(parent__isnull=False)
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_id="restapi_sub_categories_list",
        operation_description="List of Sub Categories",
        manual_parameters=[
            openapi.Parameter(
                name="parent_name",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Parent category name",
                required=True,
            ),
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
                description="List of Sub Category objects",
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
        tags=["RestAPI"],
    )
    def list(self, request):
        """
        Override the list method to paginate the queryset manually.
        """

        parent_name = request.query_params.get("parent_name")

        if parent_name is not None:
            self.queryset = self.queryset.filter(parent__name=parent_name)
        else:
            return Response(
                {"detail": "Parent name is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = CategorySerializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data)

            parent = self.queryset.first().parent
            response_data = {
                "count": paginated_response.data["count"],
                "next": paginated_response.data["next"],
                "previous": paginated_response.data["previous"],
                "parent": {
                    "id": parent.id,
                    "name": parent.name,
                    "slug": parent.slug,
                },
                "results": paginated_response.data["results"],
            }

            return Response(response_data)

        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class RestAPISubCategoriesProducts(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    This viewset automatically provides `list` actions for the products in the sub categories.
    """

    queryset = Product.objects.all()
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_id="restapi_sub_categories_products_list",
        operation_description="List of Products in Sub Categories",
        manual_parameters=[
            openapi.Parameter(
                name="sub_category_name",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Sub category name",
                required=True,
            ),
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
                schema=ProductSerializer(many=True),
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
        tags=["RestAPI"],
    )
    def list(self, request):
        """
        Override the list method to paginate the queryset manually.
        """

        sub_category_name = request.query_params.get("sub_category_name")

        if sub_category_name is not None:
            self.queryset = self.queryset.filter(category__name=sub_category_name)
        else:
            return Response(
                {"detail": "Sub category name is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = ProductSerializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data)

            category = Category.objects.get(name=sub_category_name)
            response_data = {
                "count": paginated_response.data["count"],
                "next": paginated_response.data["next"],
                "previous": paginated_response.data["previous"],
                "category": {
                    "id": str(category.id),
                    "name": str(category.name),
                    "slug": str(category.slug),
                    "parent": str(category.parent.id),
                },
                "results": paginated_response.data["results"],
            }

            return Response(response_data)

        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
