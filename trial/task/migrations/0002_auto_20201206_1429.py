# Generated by Django 2.1.15 on 2020-12-06 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdatatableschema',
            name='task_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='task.Task'),
        ),
    ]