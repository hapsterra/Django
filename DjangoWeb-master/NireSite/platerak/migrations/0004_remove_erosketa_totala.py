# Generated by Django 3.1.4 on 2022-10-13 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platerak', '0003_auto_20221013_0806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='erosketa',
            name='totala',
        ),
    ]
