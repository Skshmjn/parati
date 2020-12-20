from django.urls import path, include
from rest_framework import routers

# from backend.apps.tasks.api.viewset import TaskList
from .api.viewset import TaskViewSet, SubTaskViewSet

router = routers.DefaultRouter()
router.register('task', TaskViewSet)
router.register('sub_task', SubTaskViewSet)

urlpatterns = [
    path('', include(router.urls), name='weather_home'),

]
