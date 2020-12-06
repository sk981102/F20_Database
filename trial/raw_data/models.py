from django.db import models


# Create your models here.
class RawDataType(models.Model):
	#Admin = (('admin', 'Admin'))
	type_id = models.AutoField(primary_key=True)
	type_name = models.CharField(unique=True, max_length=30)
	task = models.ForeignKey('task.Task', models.DO_NOTHING,default=None,db_column='task')
	admin = models.ForeignKey('my_admin.MyAdmin', models.DO_NOTHING,default=None)

	def __str__(self):
		return self.type_name
		
	class Meta:
        #managed = False
		db_table = 'raw_data_type'

class RawDataTypeRequest(models.Model):
	request_id = models.AutoField(primary_key=True)
	task = models.ForeignKey('task.Task', models.DO_NOTHING,default=None,db_column='task')
	content = models.CharField(max_length=100)
		
	class Meta:
        #managed = False
		db_table = 'raw_data_type_request'
		
class RawDataSeqFile(models.Model):
	file = models.FileField(upload_to='', null=True)
	seqnumber = models.AutoField(primary_key=True)
	submitter = models.ForeignKey('submitter.Submitter', on_delete=models.CASCADE,default=None)
	raw_data_type = models.ForeignKey(RawDataType, models.DO_NOTHING, db_column='raw_data_type',default=None)
	term_start = models.DateField(null=True)
	term_end = models.DateField(null=True)
	round = models.IntegerField()

	class Meta:
		#managed = False:
		db_table = 'raw_data_seq_file'

#newly created for raw datatype schema
class RawDataTypeSchema(models.Model):
	NullValid = (('Y', 'Yes'), ('N', 'No'))
	FieldType = (('char', 'Char'), ('int', 'Int'), ('date', 'Date'), ('boolean','Boolean'))

	#field_id = models.AutoField(primary_key=True)
	type_id = models.ForeignKey('raw_data.RawDataType', models.DO_NOTHING, default=None)
	field_name = models.CharField(max_length=30)
	field_type = models.CharField(max_length=30, choices=FieldType, default="na")
	null_value = models.CharField(max_length=10, choices=NullValid, default="na")
	mapping_field = models.ForeignKey('task.TaskDataTableSchema', models.DO_NOTHING, default=None)

	class Meta:
		db_table = 'raw_data_type_schema'
