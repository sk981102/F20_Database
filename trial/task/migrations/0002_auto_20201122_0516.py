# Generated by Django 2.1.15 on 2020-11-22 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applytask',
            name='apply_task_id',
        ),
        migrations.AddField(
            model_name='applytask',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
