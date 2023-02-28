# Generated by Django 4.1.6 on 2023-02-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coporate_sponsors",
            fields=[
                (
                    "coporate_sponsor_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("coporate_sponsor_name", models.CharField(max_length=50)),
                ("coporate_sponsor_description", models.TextField(max_length=200)),
                (
                    "coporate_sponsor_image",
                    models.ImageField(default="default.jpg", upload_to="campaign_pics"),
                ),
            ],
        ),
    ]