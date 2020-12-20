from rest_framework import viewsets
from rest_framework.response import Response

from ..api.serializers import TaskSerializer, SubTaskSerializer
from ..models import Task, SubTask
from backend.apps.common import ref_strings
from backend.apps.common.commmon_utils import custom_response
from backend.apps.common.logger import MyLogger

app_name = "Weather"
logger = MyLogger(app_name)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'uuid'

    """
        raise custom Exception for custom responses 
    """
    # @custom_response(logger, success_message=ref_strings.SuccessMessage.success, function_name="task_list")
    # def list(self, request, *args, **kwargs):
    #     return super(TaskViewSet, self).list(request).data
    #
    # @custom_response(logger, success_message=ref_strings.SuccessMessage.create_succesful, function_name="task_create")
    # def create(self, request, *args, **kwargs):
    #     return super(TaskViewSet, self).create(request).data
    #
    # @custom_response(logger, success_message=ref_strings.SuccessMessage.update_successful, function_name="update_list")
    # def update(self, request, *args, **kwargs):
    #     return super(TaskViewSet, self).update(request).data
    #
    # @custom_response(logger, success_message=ref_strings.SuccessMessage.success, function_name="retrieve_list")
    # def retrieve(self, request, *args, **kwargs):
    #     return super(TaskViewSet, self).retrieve(request).data
    #
    # @custom_response(logger, success_message=ref_strings.SuccessMessage.delete_successful, function_name="delete_list")
    # def destroy(self, request, *args, **kwargs):
    #     return super(TaskViewSet, self).destroy(request).data


class SubTaskViewSet(viewsets.ModelViewSet):
    serializer_class = SubTaskSerializer
    queryset = SubTask.objects.all()
    lookup_field = 'child_uuid'
    #
    # @custom_response(logger, success_message=ref_strings.SuccessMessage.success, function_name="task_list")
    # def list(self, request, *args, **kwargs):
    #     return super(SubTaskViewSet, self).list(request).data
    #
    # @custom_response(logger, success_message=ref_strings.SuccessMessage.create_succesful, function_name="task_create")
    # def create(self, request, *args, **kwargs):
    #     return super(SubTaskViewSet, self).create(request).data
    #
    # @custom_response(logger, success_message=ref_strings.SuccessMessage.update_successful, function_name="update_list")
    # def update(self, request, *args, **kwargs):
    #     return super(SubTaskViewSet, self).update(request).data
    #
    # @custom_response(logger, success_message=ref_strings.SuccessMessage.success, function_name="retrieve_list")
    # def retrieve(self, request, *args, **kwargs):
    #     return super(SubTaskViewSet, self).retrieve(request).data
    #
    # @custom_response(logger, success_message=ref_strings.SuccessMessage.delete_successful, function_name="delete_list")
    # def destroy(self, request, *args, **kwargs):
    #     return super(SubTaskViewSet, self).destroy(request).data
