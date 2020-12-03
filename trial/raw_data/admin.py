from django.contrib import admin
from .models import RawDataType,RawDataSeqFile,RawDataTypeSchema

admin.site.register(RawDataSeqFile)
admin.site.register(RawDataType)
admin.site.register(RawDataTypeSchema)
