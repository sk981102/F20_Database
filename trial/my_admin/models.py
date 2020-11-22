from django.db import models

# Create your models here.
class MyAdmin(models.Model):
    user_id = models.OneToOneField('accounts.UserProfile', models.DO_NOTHING,primary_key=True)

    class Meta:
        db_table = 'my_admin'

class TaskCreate(models.Model):
	#class Meta:
		Name=models.CharField(unique=True, max_length=100)
		Comment=models.CharField(max_length=100)
		TaskDataTableName=models.CharField(max_length=100)
		TaskDataTableScheme=models.CharField(max_length=100)


