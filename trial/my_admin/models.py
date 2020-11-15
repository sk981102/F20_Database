from django.db import models

# Create your models here.
class MyAdmin(models.Model):
    user_id = models.OneToOneField('accounts.UserProfile', models.DO_NOTHING,primary_key=True)

    class Meta:

        db_table = 'my_admin'