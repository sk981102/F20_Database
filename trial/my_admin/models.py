from django.db import models

# Create your models here.
class MyAdmin(models.Model):
    user_id = models.ForeignKey('user_profile.UserProfile', on_delete=models.CASCADE)

