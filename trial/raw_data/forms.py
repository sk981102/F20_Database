from django import forms
from .models import RawDataType, RawDataTypeSchema

class DataTypeForm(forms.ModelForm):

    class Meta:
        model = RawDataType
        fields = ('type_id', 'type_name', 'task', 'admin')

class DataTypeSchemaForm(forms.ModelForm):

    class Meta:
        model = RawDataTypeSchema
        fields = ('type_id', 'field_name', 'field_type', 'null_value', 'mapping_field')