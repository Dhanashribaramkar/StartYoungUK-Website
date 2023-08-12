# Generated by Django 4.2.4 on 2023-08-11 15:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0013_alter_emailcontent_email_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailcontent",
            name="email_type",
            field=models.CharField(
                choices=[
                    ("approved", "Final Step: Setting up recurring donation plan"),
                    ("rejected", "Buddy Rejection Email"),
                    ("Letter", "Buddy Letter Reminder"),
                    ("final", "Welcome to SYUK"),
                ],
                max_length=50,
            ),
        ),
    ]