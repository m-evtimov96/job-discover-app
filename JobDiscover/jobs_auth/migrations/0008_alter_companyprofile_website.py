# Generated by Django 3.2.5 on 2021-08-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_auth', '0007_auto_20210807_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='website',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
