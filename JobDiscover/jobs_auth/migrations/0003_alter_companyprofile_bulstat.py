# Generated by Django 3.2.5 on 2021-08-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_auth', '0002_auto_20210804_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='bulstat',
            field=models.IntegerField(max_length=15),
        ),
    ]
