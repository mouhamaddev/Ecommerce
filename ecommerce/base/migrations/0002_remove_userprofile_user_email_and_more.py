# Generated by Django 4.2 on 2023-04-11 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_password',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
