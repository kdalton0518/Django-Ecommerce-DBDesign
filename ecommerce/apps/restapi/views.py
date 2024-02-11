from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class RestAPIHome(APIView):
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
        tags=["Home"],
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
