from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


class CustomExceptionHandler(APIException):
    status_code = 300
    default_detail = 'An error occurred.'


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and response.status_code == 400:
        response = CustomExceptionHandler().get_response()

    return response
