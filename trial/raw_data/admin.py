from django.contrib import admin
from .models import RawDataType,RawDataSeqFile

admin.site.register(RawDataSeqFile)
admin.site.register(RawDataType)
