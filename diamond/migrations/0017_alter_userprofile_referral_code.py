# Generated by Django 4.1.6 on 2024-03-24 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diamond", "0016_alter_userprofile_referral_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="referral_code",
            field=models.CharField(default="71NNV", max_length=6),
        ),
    ]
