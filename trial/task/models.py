from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
#from admin.models import Admin

# Create your models here.
class TaskDataTable(models.Model):
    Name=models.CharField(primary_key=True, max_length=100)
    Scheme=models.CharField(max_length=100)

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=100)
    mincycle = models.IntegerField()
    pass_standard=models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
     )
    admin = models.ForeignKey('my_admin.MyAdmin', models.DO_NOTHING, db_column='admin',default=None)

    def __str__(self):
        return self.task_name

    class Meta:
        #managed = False
        db_table = 'task'

class ApplyTask(models.Model):
    submitter = models.ForeignKey('submitter.Submitter', on_delete=models.CASCADE)
    task = models.ForeignKey(Task, models.DO_NOTHING)
    approved = models.IntegerField(default=0) #0 = Not approved, 1= approved

    class Meta:
        #managed = False
        db_table = 'apply_task'
        unique_together = (('submitter', 'task'),)

class TaskSchema(models.Model):
    task_id = models.OneToOneField(Task,primary_key=True,on_delete=models.CASCADE)
    TaskDataTableName = models.CharField(max_length=100)
    TaskDataTableScheme = models.CharField(max_length=10000)

    class Meta:
        #managed = False
        db_table = 'task_schema'

class TaskDataTableSchema(models.Model):
    NullValid = (('Y', 'Yes'), ('N','No'))
    FieldType = (('char', 'Char'), ('int','Int'), ('date','Date'), ('boolean', 'Boolean'))

    field_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey('task.Task', models.DO_NOTHING, default=None)
    field_name = models.CharField(unique=True, max_length=30)
    field_type = models.CharField(max_length=30, choices=FieldType, default="na")
    null_valid = models.CharField(max_length=30, choices=NullValid, default="na")

    def __str__(self):
        return self.field_name

    class Meta:
        db_table = 'task_data_table_schema'


