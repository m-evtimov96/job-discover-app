# Generated by Django 3.2.5 on 2021-08-10 20:25

import JobDiscover.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_alter_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=25, validators=[JobDiscover.core.validators.validate_start_with_capital]),
        ),
    ]
