# Generated by Django 3.2.5 on 2021-08-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_auth', '0006_alter_companyprofile_bulstat'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='website',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]