from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class ParsedData(models.Model):
    parsed_id = models.AutoField(primary_key=True)
    task = models.ForeignKey('task.Task', models.DO_NOTHING,default=None)
    submitter = models.ForeignKey('submitter.Submitter', on_delete=models.CASCADE,default=None)
    rater = models.ForeignKey('rater.Rater', on_delete=models.CASCADE, default=None)
    raw_data_seq_file = models.ForeignKey('raw_data.RawDataSeqFile', models.DO_NOTHING, db_column='raw_data_seq_file',default=None)
    total_tuple_num = models.IntegerField(blank=True, null=True)
    duplicate_tuple_num = models.IntegerField(blank=True, null=True)
    column_null_ratio = models.FloatField(blank=True, null=True)
    quantity_score = models.IntegerField(blank=True, null=True)
    quality_score = models.PositiveIntegerField(blank=True, null=True, default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    evaluated = models.IntegerField()
    pass_or_not = models.IntegerField(db_column='pass')

    class Meta:
        #managed = False
        db_table = 'parsed_data'
