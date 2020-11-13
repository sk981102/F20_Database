from django.db import models


class Rater(models.Model):
    user_id = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
