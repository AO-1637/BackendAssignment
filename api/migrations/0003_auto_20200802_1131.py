# Generated by Django 3.0.2 on 2020-08-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200802_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userId',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]