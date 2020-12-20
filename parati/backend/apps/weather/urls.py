from django.urls import path

from .api.viewsets import WeatherApiView

urlpatterns = [
    path('', WeatherApiView.as_view(), name='weather_home'),

]
