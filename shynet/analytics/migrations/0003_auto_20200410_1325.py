# Generated by Django 3.0.5 on 2020-04-10 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20200410_0258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hit',
            name='metadata_raw',
        ),
        migrations.RemoveField(
            model_name='session',
            name='metadata_raw',
        ),
    ]
