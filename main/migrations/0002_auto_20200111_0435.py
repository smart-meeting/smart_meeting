# Generated by Django 2.1 on 2020-01-11 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='join',
        ),
        migrations.DeleteModel(
            name='Calendar',
        ),
    ]
