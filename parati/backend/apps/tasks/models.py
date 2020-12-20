from django.db import models


class Task(models.Model):
    uuid = models.UUIDField(max_length=15, unique=True)
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # app_label = 'tasks'
        indexes = [
            models.Index(fields=['uuid'])
        ]

    def __str__(self):
        return f"{self.uuid}, {self.title}"


class SubTask(models.Model):
    parent = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='children')
    child_uuid = models.UUIDField(max_length=10, unique=True)
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # app_label = 'tasks'
        indexes = [
            models.Index(fields=['child_uuid'])
        ]

    def __str__(self):
        return f"{self.child_uuid}, {self.title}"
