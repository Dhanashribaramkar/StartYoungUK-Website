# Generated by Django 4.0.7 on 2022-09-28 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigns',
            name='campaign_deadline',
            field=models.DateField(default=datetime.date.today),
            preserve_default=False,
        ),
    ]
