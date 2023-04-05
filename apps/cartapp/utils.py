from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first, 
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['code'] = response.status_code
        response.data['status_code'] = response.status_code
        response.data['referenceError'] = "Detail Not Found"
        try:
            response.data['reason'] = str(exc)
            response.data['message'] = str(exc)
            if str(exc) == "":
                response.data['reason'] = "Please provide valid ID"
                response.data['message'] = "Please provide valid ID"
        except Exception as e:
            response.data['reason'] = str(exc)
            response.data['message'] = str(exc)
            pass
        response.data['@baseType'] = "ShoppingCart"
        response.data['@schemaLocation'] = "ShoppingCart"
        response.data['@type'] = "ShoppingCart"

    return response