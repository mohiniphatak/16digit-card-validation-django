# Generated by Django 2.1.2 on 2018-10-29 12:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazonapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amzseries',
            name='cardtype',
        ),
        migrations.AlterField(
            model_name='amzseries',
            name='cardnumber',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator('\\d{16,16}', 'Number must be 16 digits')]),
        ),
    ]
