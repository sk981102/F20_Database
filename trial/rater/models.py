from django.db import models


class Rater(models.Model):
    user_id = models.ForeignKey('accounts.UserProfile', models.DO_NOTHING, primary_key=True)

    class Meta:
        #managed = False
        db_table = 'rater'
