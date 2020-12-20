import json
import sys

import requests

from backend.apps.common import ref_strings
from backend.apps.common.commmon_utils import CustomException, get_error_traceback, error_response
from backend.apps.weather.api.serializers import WeatherSerializers
from backend.config.settings import OPEN_API_URL, OPEN_API_KEY, OPEN_API_HOST


def request_open_api(logger):
    try:
        # Creating request
        url = OPEN_API_URL
        querystring = {"q": "bangalore ,in"}
        headers = {
            'x-rapidapi-key': OPEN_API_KEY,
            'x-rapidapi-host': OPEN_API_HOST
        }

        # Getting response From Open Weather Api
        response = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)

        # Just for demonstration purpose that third party api message can be customised and use as per our requirements
        if response.get("cod") != "200" and response['message'] == "city not found":
            raise CustomException(
                ref_strings.CommonErrorMessage.city_not_found)

        if "cod" not in response or response.get("cod") != "200":
            raise CustomException(
                ref_strings.CommonErrorMessage.field_errors(response['message']))

        return WeatherSerializers(response['list'], many=True).data

    except CustomException:
        raise

    except Exception as e:
        error = get_error_traceback(sys, e)
        logger.error_logger('weather api utils : %s' % error)
        raise
