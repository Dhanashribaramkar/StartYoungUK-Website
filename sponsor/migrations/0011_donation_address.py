# Generated by Django 4.0.7 on 2023-05-06 08:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sponsor", "0010_donation_is_gift_aid"),
    ]

    operations = [
        migrations.AddField(
            model_name="donation",
            name="address",
            field=models.TextField(default="Newham, UK", max_length=100),
            preserve_default=False,
        ),
    ]
