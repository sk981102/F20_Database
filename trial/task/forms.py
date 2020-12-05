from django import forms
from .models import TaskDataTableSchema


class TaskDataTableSchemaForm(forms.ModelForm):

    class Meta:
        model = TaskDataTableSchema
        fields = ('task_id', 'field_name', 'field_type', 'null_valid')