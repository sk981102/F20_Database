from django.db import models
from user_profile.models import UserProfile


class Rater(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
