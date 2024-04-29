import logging
import jwt
from rest_framework.views import APIView
from datetime import datetime, timedelta, timezone
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from cerberus import Validator

from vm_service.utils import custom_exceptions as ce
from service_auth import schemas

# Get an instance of logger
logger = logging.getLogger("service_auth")
c_validator = Validator()


class Authentication(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, slug):
        try:
            if slug in ["authorize", "regenerate-token"]:
                result = authorize(request, slug)
                return result
            else:
                raise ce.InvalidSlug
        except ce.ValidationFailed as vf:
            logger.error("AUTHENTICATION : {}".format(vf))
            raise
        except Exception as e:
            logger.error("AUTHENTICATION : {}".format(e))
            raise ce.InternalServerError


def authorize(request, slug):
    """
    Validates platform code and generate token
    """
    try:
        # Check if platform has access
        if slug == "authorize":
            is_valid = c_validator.validate(
                request.data, schemas.AUTHENTICATION_TOKEN_POST
            )
            if not is_valid:
                raise ce.ValidationFailed(
                    {
                        "message": "Validations Failed.",
                        "data": c_validator.errors,
                    }
                )
            if (
                request.data.get("platform_code")
                == settings.PLATFORM_CODE
            ):
                access_token = generate_access_token(
                    platform_code=settings.PLATFORM_CODE
                )
                refresh_token = generate_refresh_token(
                    platform_code=settings.PLATFORM_CODE
                )

                return Response(
                    {
                        "message": "Access granted",
                        "data": {
                            "access_token": access_token,
                            "refresh_token": refresh_token,
                        },
                    },
                    status=status.HTTP_200_OK,
                )

            return Response(
                {
                    "message": "Access Denied",
                    "data": None,
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        elif slug == "regenerate-token":
            is_valid = c_validator.validate(
                request.data, schemas.REGENERATE_TOKEN_POST
            )
            if not is_valid:
                raise ce.ValidationFailed(
                    {
                        "message": "Validations Failed.",
                        "data": c_validator.errors,
                    }
                )
            return regenerate_token(
                refresh_token=request.data.get("refresh_token")
            )
    except ce.ValidationFailed as vf:
        logger.error("AUTHENTICATION : {}".format(vf))
        raise
    except Exception as e:
        logger.error("AUTHENTICATION : {}".format(e))
        raise ce.InternalServerError


def generate_access_token(platform_code=None):
    """
    Creates access token
    """
    access_token_payload = {
        "platform_code": platform_code,
        "exp": (
            datetime.now()
            + timedelta(days=0, minutes=settings.ACCESS_TOKEN_EXPIRY)
        ),
        "iat": datetime.now(),
    }

    access_token = jwt.encode(
        access_token_payload, settings.SECRET_KEY, algorithm="HS256"
    )

    return access_token


def generate_refresh_token(platform_code):
    """
    Creates refresh token
    """
    refresh_token_payload = {
        "platform_code": platform_code,
        "exp": (
            datetime.now()
            + timedelta(days=0, minutes=settings.REFRESH_TOKEN_EXPIRY)
        ),
        "iat": datetime.now(),
    }

    refresh_token = jwt.encode(
        refresh_token_payload,
        settings.REFRESH_SECRET_KEY,
        algorithm="HS256",
    )

    return refresh_token


def regenerate_token(refresh_token=None):
    """
    Regenerates token
    """
    try:
        payload = jwt.decode(
            refresh_token,
            settings.REFRESH_SECRET_KEY,
            algorithms=["HS256"],
        )

        if payload.get("platform_code") == settings.PLATFORM_CODE:
            return Response(
                {
                    "message": "Token regenerated successfully",
                    "data": {
                        "access_token": generate_access_token(
                            settings.PLATFORM_CODE
                        ),
                        "refresh_token": generate_refresh_token(
                            settings.PLATFORM_CODE
                        ),
                    },
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {
                "message": "Platform Not Found",
                "data": None,
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    except jwt.ExpiredSignatureError as e:
        logger.error("REGENERATE TOKEN: {}".format(e))
        raise ce.ExpiredSignatureError

    except jwt.InvalidSignatureError as e:
        logger.error("REGENERATE TOKEN: {}".format(e))
        raise ce.InvalidSignatureError

    except jwt.DecodeError as e:
        logger.error("REGENERATE TOKEN: {}".format(e))
        raise ce.DecodeError

    except jwt.InvalidTokenError as e:
        logger.error("REGENERATE TOKEN: {}".format(e))
        raise ce.InvalidTokenError
