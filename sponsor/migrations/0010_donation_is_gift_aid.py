# Generated by Django 4.0.7 on 2023-05-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sponsor", "0009_alter_donation_options_alter_donation_trxn_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="donation",
            name="is_gift_aid",
            field=models.BooleanField(default=False),
        ),
    ]
