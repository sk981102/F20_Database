from django.db import models


# Create your models here.
class RawDataType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(unique=True, max_length=30)
    task = models.ForeignKey('task.Task', models.DO_NOTHING)
    admin = models.ForeignKey('my_admin.MyAdmin', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'raw_data_type'

class RawDataSeqFile(models.Model):
    seqnumber = models.AutoField(primary_key=True)
    submitter = models.ForeignKey('submitter.Submitter', models.DO_NOTHING)
    raw_data_type = models.ForeignKey(RawDataType, models.DO_NOTHING, db_column='raw_data_type')
    term = models.DateField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'raw_data_seq_file'
