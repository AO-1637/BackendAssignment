# Generated by Django 3.0.2 on 2020-08-02 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200802_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='endTime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activityperiod',
            name='startTime',
            field=models.DateTimeField(),
        ),
    ]