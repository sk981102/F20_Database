from django import forms
from raw_data.models import RawDataType, RawDataSeqFile
import datetime

class UploadForm(forms.ModelForm):
        class Meta:
                model = RawDataSeqFile
                fields = ('file', 'raw_data_type', 'term_start', 'term_end', 'round')
                widgets = {'term_start': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),'term_end': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}

        def clean_round(self):
                r = self.cleaned_data.get('round')

                if RawDataSeqFile.objects.filter(round=r).exists():
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
