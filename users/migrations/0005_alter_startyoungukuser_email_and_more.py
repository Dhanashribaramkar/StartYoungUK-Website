# Generated by Django 4.1.5 on 2023-03-09 19:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_startyoungukuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startyoungukuser',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='startyoungukuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
