# Generated by Django 4.2 on 2023-04-11 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_userprofile_user_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='order_history',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='payment_methods',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_last_login',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='wishlist',
        ),
    ]