# Generated by Django 2.1.15 on 2020-12-05 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0002_assignedtask_rated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedtask',
            name='rater',
            field=models.ForeignKey(db_column='rater', default=None, on_delete=django.db.models.deletion.CASCADE, to='rater.Rater'),
        ),
    ]
