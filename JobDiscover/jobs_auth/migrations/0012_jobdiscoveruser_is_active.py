# Generated by Django 3.2.5 on 2022-02-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_auth', '0011_alter_companyprofile_bulstat'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdiscoveruser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]