# Generated by Django 3.1.4 on 2022-10-13 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('platerak', '0002_auto_20221011_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erosketa',
            name='plateraIzena',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platerak.platera'),
        ),
    ]