# Generated by Django 4.0.7 on 2023-04-04 20:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('date', models.DateTimeField(auto_created=True)),
                ('child_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=10)),
                ('class_std', models.CharField(max_length=10)),
                ('school', models.CharField(max_length=50)),
                ('hobbies', models.CharField(default='0000000000', max_length=10)),
                ('mentor', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StartYoungUKUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('address', models.TextField(max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('crn_no', models.CharField(default='00000000', max_length=8, validators=[django.core.validators.MinLengthValidator(limit_value=8)])),
                ('user_type', models.CharField(choices=[('I', 'Individual'), ('C', 'Corporate')], max_length=10)),
                ('is_verified', models.BooleanField(default=False)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('is_coordinator', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Buddy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hobbies', models.CharField(default='0000000000', max_length=10)),
                ('date_status_modified', models.DateTimeField(auto_now_add=True)),
                ('occupation', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')], default='pending', max_length=256)),
                ('approver', models.EmailField(max_length=256, null=True)),
                ('letter_received', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
