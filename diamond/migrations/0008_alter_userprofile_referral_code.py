# Generated by Django 4.1.6 on 2024-03-14 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diamond', '0007_alter_userprofile_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='referral_code',
            field=models.CharField(default='3OD4V', max_length=6),
        ),
    ]
