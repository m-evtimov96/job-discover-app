# Generated by Django 3.2.5 on 2021-08-01 07:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(help_text='Write the city name in english.', max_length=25),
        ),
    ]
