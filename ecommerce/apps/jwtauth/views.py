from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainPairView as DefaultTokenObtainPairView,
    TokenRefreshView as DefaultTokenRefreshView,
    TokenVerifyView as DefaultTokenVerifyView,
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class TokenObtainPairView(DefaultTokenObtainPairView):
    @swagger_auto_schema(
        operation_id="token_obtain_pair",
        operation_description="Custom JWT Obtain Pair View",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Token pair successfully obtained",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "access": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Access token",
                        ),
                        "refresh": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Refresh token",
                        ),
                    },
                ),
            ),
            status.HTTP_401_UNAUTHORIZED: openapi.Response(
                description="Unauthorized",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="No active account found with the given credentials",
                        ),
                    },
                ),
            ),
        },
        tags=["JWT Authentication"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TokenRefreshView(DefaultTokenRefreshView):
    @swagger_auto_schema(
        operation_id="token_refresh",
        operation_description="Custom JWT Refresh View",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Token successfully refreshed",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "access": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Access token",
                        )
                    },
                ),
            ),
            status.HTTP_401_UNAUTHORIZED: openapi.Response(
                description="Token is invalid",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Token is invalid or expired",
                        ),
                        "code": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="token_not_valid",
                        ),
                    },
                ),
            ),
        },
        tags=["JWT Authentication"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TokenVerifyView(DefaultTokenVerifyView):
    @swagger_auto_schema(
        operation_id="token_verify",
        operation_description="Custom JWT Verify View",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Token is valid",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={},
                ),
            ),
            status.HTTP_401_UNAUTHORIZED: openapi.Response(
                description="Token is invalid",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Token is invalid or expired",
                        ),
                        "code": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="token_not_valid",
                        ),
                    },
                ),
            ),
        },
        tags=["JWT Authentication"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
