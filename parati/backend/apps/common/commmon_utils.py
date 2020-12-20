import os
import sys

from django.http import JsonResponse

from backend.apps.common import ref_strings


def get_error_traceback(sys, e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    return "%s || %s || %s || %s" % (exc_type, f_name, exc_tb.tb_lineno, e)


def success_response(params={}):
    return_params = dict()
    return_params['success'] = True
    return_params['message'] = params.get('success_resp', {}).success
    return_params['success_code'] = params.get('success_resp', {}).code
    return_params['data'] = params.get('data')
    # return_params['count'] = params.get('count', '')
    return JsonResponse(return_params)


def error_response(params={}):
    return_params = dict()
    return_params['success'] = False
    return_params['message'] = params.get('error', {}).error
    return_params['error_code'] = params.get('error', {}).code
    return_params['data'] = {}
    return JsonResponse(return_params)


class CustomException(Exception):
    """
    Exception class for showing Exceptions to End User
    """

    def __init__(self, error):
        self.error = error.error
        self.code = error.code


def custom_response(logger, success_message, function_name):
    def inner(func):
        """
        Decorator : To check who is hitting the end points
        """

        def who(*args, **kwargs):
            try:

                # Call Main Function
                response = func(*args, **kwargs)
                return success_response({'success_resp': success_message,
                                         'data': response})

            except CustomException as e:
                return error_response({'error': e})

            except Exception as e:
                print(e)
                error = get_error_traceback(sys, e)
                logger.error_logger(f'{function_name} : {error}')
                return error_response({'error': ref_strings.CommonErrorMessage.some_error_occurred})

        return who

    return inner
