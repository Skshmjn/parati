from rest_framework import serializers

from ..models import Task, SubTask


class ChildrenSubTask(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ("child_uuid", "title")


class TaskSerializer(serializers.ModelSerializer):
    children = ChildrenSubTask(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'uuid', 'children')


class SubTaskSerializer(serializers.ModelSerializer):
    # parent = serializers.SerializerMethodField()

    parent_uuid = serializers.UUIDField(write_only=True)

    def create(self, validated_data):
        task = Task.objects.get(uuid=validated_data.pop('parent_uuid', None))
        validated_data['parent'] = task
        return super().create(validated_data)

    class Meta:
        model = SubTask

        fields = ("child_uuid", "title", 'parent_uuid')
