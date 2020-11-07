from django.db import models

class Submitter(models.Model):
    user_id = models.ForeignKey('user_profile.UserProfile', on_delete=models.CASCADE)
    score = models.FloatField()
