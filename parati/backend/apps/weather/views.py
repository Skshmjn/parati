# Create your views here.
import json
import sys

from django.views.generic import TemplateView

from backend.apps.common import ref_strings
from backend.apps.common.commmon_utils import CustomException, error_response, get_error_traceback
from backend.apps.common.logger import MyLogger
from backend.apps.weather.utils import request_open_api

app_name = "Weather"
logger = MyLogger(app_name)


class WeatherIndex(TemplateView):
    """
        Returning HTML Template
    """
    template_name = "weather.html"

    def get_context_data(self, *args, **kwargs):
        try:
            context = super(WeatherIndex, self).get_context_data(*args, **kwargs)

            results = request_open_api(logger)
            context['data'] = results
            return context
        except CustomException as error:
            return error_response({'error': error})

        except Exception as e:
            error = get_error_traceback(sys, e)
            logger.error_logger('weather page: %s' % error)
            return error_response({'error': ref_strings.CommonErrorMessage.some_error_occurred})
