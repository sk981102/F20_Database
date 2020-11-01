from django.db import models
from user_profile.models import UserProfile


class Submitter(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    score = models.FloatField()
