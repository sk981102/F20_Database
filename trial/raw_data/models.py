from django.db import models


# Create your models here.
class RawDataType(models.Model):
	type_id = models.AutoField(primary_key=True)
	type_name = models.CharField(unique=True, max_length=30)
	task = models.ForeignKey('task.Task', models.DO_NOTHING,default=None)
	admin = models.ForeignKey('my_admin.MyAdmin', models.DO_NOTHING,default=None)
	
	def __str__(self):
		return self.type_name
		
	class Meta:
        #managed = False
		db_table = 'raw_data_type'

class RawDataSeqFile(models.Model):
	file = models.FileField(upload_to='', null=True)
	seqnumber = models.AutoField(primary_key=True)
	submitter = models.ForeignKey('submitter.Submitter', models.DO_NOTHING,default=None)
	raw_data_type = models.ForeignKey(RawDataType, models.DO_NOTHING, db_column='raw_data_type',default=None)
	term_start = models.DateField(null=True)
	term_end = models.DateField(null=True)
	round = models.IntegerField()

	class Meta:
		#managed = False
		db_table = 'raw_data_seq_file'