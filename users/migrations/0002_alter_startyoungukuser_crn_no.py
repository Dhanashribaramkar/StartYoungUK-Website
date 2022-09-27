# Generated by Django 4.0.7 on 2022-09-27 12:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startyoungukuser',
            name='crn_no',
            field=models.CharField(default='00000000', max_length=8, validators=[django.core.validators.MinLengthValidator(limit_value=8)]),
        ),
    ]
