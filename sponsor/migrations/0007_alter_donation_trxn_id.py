# Generated by Django 4.1.5 on 2023-04-30 13:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0006_donation_date_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='trxn_id',
            field=models.CharField(default=uuid.UUID('2e576392-4633-42ef-9afb-19817fabd898'), max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
