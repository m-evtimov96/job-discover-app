# Generated by Django 3.2.5 on 2021-08-07 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_auth', '0008_alter_companyprofile_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
