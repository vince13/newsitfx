# Generated by Django 4.1.6 on 2024-03-10 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='AccountNotification',
        ),
    ]
