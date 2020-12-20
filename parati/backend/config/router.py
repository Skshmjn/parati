

from rest_framework import routers

# from backend.apps.tasks.api.viewset import TaskList
from backend.apps.tasks.views import TaskList

router = routers.DefaultRouter()
router.register('tasks', TaskList)
