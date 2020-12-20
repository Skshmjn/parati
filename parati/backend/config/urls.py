from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', include(('weather.urls', 'weather'), namespace="weather")),
    path('', include(('tasks.urls', 'task'), namespace="task")),
]
