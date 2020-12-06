from django.contrib import admin
from .models import RawDataType,RawDataSeqFile,RawDataTypeSchema,RawDataTypeRequest

admin.site.register(RawDataSeqFile)
admin.site.register(RawDataType)
admin.site.register(RawDataTypeSchema)
admin.site.register(RawDataTypeRequest)
