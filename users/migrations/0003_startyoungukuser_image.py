# Generated by Django 4.0.7 on 2022-09-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_startyoungukuser_crn_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='startyoungukuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
