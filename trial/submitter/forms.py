from django import forms
from raw_data.models import RawDataType, RawDataSeqFile

class UploadForm(forms.ModelForm):
	class Meta:
		model = RawDataSeqFile
		fields = ('file', 'raw_data_type', 'term_start', 'term_end', 'round')
		widgets = {'term_start': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),'term_end': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}