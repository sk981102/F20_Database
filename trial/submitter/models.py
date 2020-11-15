from django.db import models

class Submitter(models.Model):
    user_id = models.OneToOneField('accounts.UserProfile', on_delete=models.CASCADE, primary_key=True)
    score = models.FloatField(default=0.0)

    class Meta:
        #managed = False
        db_table = 'submitter'