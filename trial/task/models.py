from django.db import models
#from admin.models import Admin

# Create your models here.
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=100)
    mincycle = models.IntegerField()
    admin = models.ForeignKey('my_admin.MyAdmin', models.DO_NOTHING, db_column='admin',default=None)

    class Meta:
        #managed = False
        db_table = 'task'

class ApplyTask(models.Model):
    submitter = models.OneToOneField('submitter.Submitter', models.DO_NOTHING, primary_key=True)
    task = models.ForeignKey(Task, models.DO_NOTHING,default=None)
    approved = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'apply_task'
        unique_together = (('submitter', 'task'),)


