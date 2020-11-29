from django.forms import ModelForm
from .models import TaskCreate
from task.models import Task 
class TaskCreateForm(ModelForm):
    class Meta:
        model = TaskCreate
        fields = ['Name','Comment','mincycle','TaskDataTableName','TaskDataTableScheme']

class PassStandardForm(ModelForm):
    class Meta:
        model = Task
        fields = ['pass_standard']
