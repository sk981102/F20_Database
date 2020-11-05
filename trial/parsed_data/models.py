from django.db import models
from task.models import Task
from submitter.models import Submitter
from rater.models import Rater
from raw_data.models import RawData

# Create your models here.
class ParsedData(models.Model):

    parsed_id = models.AutoField(primary_key=True)

    title = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Submitter, on_delete=models.CASCADE)
    ordinal = models.ForeignKey(RawData, related_name='brought_ordinal', on_delete=models.CASCADE)
    period_start =models.ForeignKey(RawData, related_name='brought_period_start', on_delete=models.CASCADE)
    period_end =models.ForeignKey(RawData, related_name='brought_period_end', on_delete=models.CASCADE)
    
    num_tuple = models.PositiveIntegerField()
    num_duple = models.PositiveIntegerField()
    percentage_null = models.PositiveIntegerField()
    
    score = models.IntegerField()
    passed = models.BooleanField()

    #relationship
    parsed_from = models.OneToOneField(RawData, on_delete=models.CASCADE)
    raters = models.ManyToManyField(Rater)
