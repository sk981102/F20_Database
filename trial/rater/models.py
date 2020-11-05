from django.db import models
from user_profile.models import UserProfile
from django_mysql.models import ListCharField


class Rater(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rated_tasks = ListCharField(max_length=100, base_field=models.CharField(max_length=100))
