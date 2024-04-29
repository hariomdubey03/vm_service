import logging
import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from vm_service.utils import custom_exceptions as ce


# Get an instance of logger
logger = logging.getLogger("service_auth")


class Authentication(BaseAuthentication):
    """
    JWT authentication class
    """

    def authenticate(self, request):
        """
        Authenticate function
        """
        try:
            authorization_header = (
                request.headers.get("Authorization")
                if request.headers.get("Authorization")
                else None
            )

            api_key = (
                request.headers.get("API-Key")
                if request.headers.get("API-Key")
                else None
            )

            if authorization_header:
                access_token = authorization_header.split(" ")[1]

                payload = jwt.decode(
                    access_token,
                    settings.SECRET_KEY,
                    algorithms=["HS256"],
                )

                if (
                    payload.get("platform_code")
                    == settings.PLATFORM_CODE
                ):
                    return payload.get("platform_code"), None
                else:
                    raise exceptions.NotFound(
                        detail="Platform Not Found"
                    )

            elif api_key:
                if not api_key:
                    raise ce.APIKeyMissing

                if api_key == settings.API_KEY:
                    return api_key, None
                else:
                    raise exceptions.NotFound(detail="Invalid API Key")

            raise exceptions.AuthenticationFailed

        except jwt.ExpiredSignatureError as e:
            logger.error("AUTHENTICATION : {}".format(e))
            raise ce.ExpiredSignatureError

        except jwt.InvalidSignatureError as e:
            logger.error("AUTHENTICATION : {}".format(e))
            raise ce.InvalidSignatureError

        except jwt.DecodeError as e:
            logger.error("AUTHENTICATION : {}".format(e))
            raise ce.DecodeError

        except jwt.InvalidTokenError as e:
            logger.error("AUTHENTICATION : {}".format(e))
            raise ce.InvalidTokenError
