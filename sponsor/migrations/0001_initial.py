# Generated by Django 4.0.7 on 2022-09-29 07:35

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields

import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Donation",
            fields=[
                ("trxn_id", models.CharField(
                default=uuid.UUID("2e576392-4633-42ef-9afb-19817fabd898"),
                max_length=100,
                primary_key=True,
                serialize=False,
                unique=True,
                )),
                ("campaign_id", models.IntegerField(null=False, default=0)),
                ("user_id", models.IntegerField(null=False, default=0)),
                ("name", models.CharField(max_length=50, null=False)),
                ("email", models.EmailField(max_length=50, null=False)),
                ("mobile_number", phonenumber_field.modelfields.PhoneNumberField(
                                    max_length=128, region=None
                                )),
                ("address", models.TextField(max_length=100, null=False)),
                ("amount", models.PositiveIntegerField(null=False)),
                ("is_anonymous", models.BooleanField(null=False, default=False)),
                ("is_successful", models.BooleanField(null=False, default=False)),
                ("date_donation", models.DateTimeField(auto_now_add=True)),
                ("is_gift_aid", models.BooleanField(null=False, default=False)),
            ],
        ),
    ]
