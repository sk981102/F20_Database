from django.db import models

# Create your models here.
class MyAdmin(models.Model):
    user_id = models.ForeignKey('accounts.UserProfile', models.DO_NOTHING,primary_key=True)

    class Meta:
        managed = False
        db_table = 'my_admin'