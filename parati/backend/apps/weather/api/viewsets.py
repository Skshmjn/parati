import sys

from rest_framework import views

from backend.apps.common import ref_strings
from backend.apps.common.commmon_utils import success_response, get_error_traceback, error_response, CustomException, \
    custom_response
from backend.apps.common.logger import MyLogger
from ..utils import request_open_api

app_name = 'Weather'
logger = MyLogger(app_name)


class WeatherApiView(views.APIView):

    @custom_response(logger, success_message=ref_strings.SuccessMessage.success, function_name="weather_api")
    def get(self, request):
        return request_open_api(logger)
