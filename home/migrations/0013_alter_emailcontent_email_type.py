# Generated by Django 4.0.7 on 2023-05-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0012_alter_emailcontent_email_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailcontent",
            name="email_type",
            field=models.CharField(
                choices=[
                    ("approved", "Final Step: Setting up SDP"),
                    ("rejected", "Buddy Rejection Email"),
                    ("Letter", "Buddy Letter Reminder"),
                    ("final", "Welcome to SYUK"),
                ],
                max_length=50,
            ),
        ),
    ]