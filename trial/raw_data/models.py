from django.db import models
from task.models import Task
from submitter.models import Submitter

# Create your models here.
class RawData(models.Model):
    raw_id = models.AutoField(primary_key=True)
    extension = models.CharField(max_length=5)
    #schema =
    #mapping = 
    ordinal = models.PositiveIntegerField()
    period_start = models.DateField()
    period_end = models.DateField()

    
    #relationship
    submitter = models.ForeignKey(Submitter, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
