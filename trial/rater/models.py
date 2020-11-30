from django.db import models


class Rater(models.Model):
    user_id = models.OneToOneField('accounts.UserProfile', on_delete=models.CASCADE, primary_key=True)

    class Meta:
        # managed = False
        db_table = 'rater'


class AssignedTask(models.Model): # == Assigned file
    type_id = models.AutoField(primary_key=True)
    task = models.ForeignKey('task.Task', models.DO_NOTHING, default=None)
    raw_data = models.ForeignKey('raw_data.RawDataSeqFile', models.DO_NOTHING, db_column='raw_data_type', default=None)
    rater = models.ForeignKey(Rater, models.DO_NOTHING, db_column='rater', default=None)
    rated = models.IntegerField(default=0) #0 : not rated, 1 : rated

    class Meta:
        db_table = 'assigned_task'
