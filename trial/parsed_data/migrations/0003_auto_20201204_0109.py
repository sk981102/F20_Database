# Generated by Django 2.1.15 on 2020-12-03 16:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0002_auto_20201204_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parseddata',
            name='quality_score',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
