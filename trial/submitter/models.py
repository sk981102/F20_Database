from django.db import models

class Submitter(models.Model):
    user_id = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
    score = models.FloatField()
