from django.db import models
#from admin.models import Admin

# Create your models here.
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    min_cycle = models.DurationField()

    #relationship
#    participants = models.ManyToManyField(submitter.models.Submitter, through='Participation')
#    creator = models.ForeignKey(Admin, on_delete=models.CASCADE)
    

class Participation(models.Model):
    passed = models.BooleanField()
