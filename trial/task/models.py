from django.db import models
#from admin.models import Admin

# Create your models here.
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,default="")
    description = models.TextField()
    min_cycle = models.DurationField()


    #relationship
    participants = models.ManyToManyField("submitter.Submitter", through='Participate')
    creator = models.ForeignKey("my_admin.MyAdmin", on_delete=models.RESTRICT,default=0)
    # 1:N or M:N Determine
    raters = models.ForeignKey("rater.Rater", on_delete=models.RESTRICT,default=1)

    def __str__(self):
        return self.title
    

class Participate(models.Model):
    task_id = models.ForeignKey(Task,on_delete=models.CASCADE)
    submitter_id=models.ForeignKey("submitter.Submitter",on_delete=models.CASCADE)
    passed = models.BooleanField()


