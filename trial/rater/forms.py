from django import forms
from parsed_data.models import ParsedData

class RateForm(forms.ModelForm):
    class Meta:
        model = ParsedData
        fields = ('quality_score', 'pass_or_not')
        widgets = {'quality_score': forms.Select(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'))), 'pass_or_not': forms.Select(choices=((1, 'Pass'), (0, 'Reject')))}
