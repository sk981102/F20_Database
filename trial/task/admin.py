from django.contrib import admin
from .models import Task, ApplyTask, TaskDataTableSchema

admin.site.register(Task)
admin.site.register(ApplyTask)
admin.site.register(TaskDataTableSchema)
