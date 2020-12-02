from django import forms
from .models import RawDataType

class DataTypeForm(forms.ModelForm):

    class Meta:
        model = RawDataType
        fields = ('type_id', 'type_name', 'task', 'admin')