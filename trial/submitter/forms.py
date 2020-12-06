from django import forms
from raw_data.models import RawDataType, RawDataSeqFile
from submitter.models import Submitter
from task.models import Task
import datetime
from django.shortcuts import get_object_or_404


class UploadForm(forms.ModelForm):
        class Meta:
                model = RawDataSeqFile
                fields = ('file', 'raw_data_type', 'term_start', 'term_end', 'round')
                widgets = {'term_start': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),'term_end': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}

        def __init__(self, task, submitter, *args, **kwargs):
                super(UploadForm, self).__init__(*args, **kwargs)
                self.fields['raw_data_type'].queryset = RawDataType.objects.filter(task=task).distinct()
                self.task = task
                self.submitter = submitter
                
        def clean_round(self):
                r = self.cleaned_data.get('round')
                data_types = RawDataType.objects.filter(task=self.task).values('type_id').distinct()
                
                if RawDataSeqFile.objects.filter(round=r, raw_data_type__in=data_types, submitter=self.submitter).exists():
                        raise forms.ValidationError('이미 제출한 회차입니다. 제출된 파일들의 회차를 확인한 후 다시 입력해주세요')

                return r

        def clean_term_start(self):
                start = self.cleaned_data.get('term_start')

                if start > datetime.date.today():
                        raise forms.ValidationError('오늘 이후의 데이터를 제출할 수 없습니다. 시작 기간을 확인해주세요')
                
                return start

        def clean_term_end(self):
                end = self.cleaned_data.get('term_end')

                if end > datetime.date.today():
                        raise forms.ValidationError('오늘 이후의 데이터를 제출할 수 없습니다. 끝 기간을 확인해주세요')
                
                return end
