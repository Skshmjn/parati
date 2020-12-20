from rest_framework import serializers


class Weather(object):
    def __init__(self, dt_txt, main):
        self.dt_txt = dt_txt
        self.main = main


class JSONSerializerField(serializers.Field):
    """
     JSONSerializer to serialize main
     Useful when there is multiple level dictionaries and multiple json
     "JSONSerializerField()" Place it in  for custom json field in place of serializers.JSONField()
    """

    def to_representation(self, value):
        # return value
        return {"min_temp": value['temp_min'], "max_temp": value['temp_max']}


class WeatherSerializers(serializers.Serializer):
    dt_txt = serializers.CharField(max_length=50)
    main = serializers.JSONField()

    # Use custom JSONSerializer fields in case of multiple json fields
    def to_representation(self, instance):
        return {"date": instance['dt_txt'],
                "temperatures": {"temp": instance['main']['temp'], "minimum_temperature": instance['main']['temp_min'],
                                 "temperature_maximum": instance['main']['temp_max']}}
