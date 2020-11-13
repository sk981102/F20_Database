from django.db import models

# Create your models here.
class MyAdmin(models.Model):
    user_id = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)

