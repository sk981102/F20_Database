from django.forms import ModelForm
from .models import TaskCreate
 
class TaskCreateForm(ModelForm):
    class Meta:
        model = TaskCreate
        fields = ['Name','Comment','TaskDataTableName','TaskDataTableScheme']
