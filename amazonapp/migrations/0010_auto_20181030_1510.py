# Generated by Django 2.1.2 on 2018-10-30 09:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazonapp', '0009_remove_amzorder_end_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='amzorder',
            name='end_series',
            field=models.CharField(default=0, max_length=16),
        ),
        migrations.AlterField(
            model_name='amzorder',
            name='start_series',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator('\\d{16,16}', 'Number must be 16 digits')]),
        ),
        migrations.AlterField(
            model_name='amzorder',
            name='total_cards_requirement',
            field=models.CharField(max_length=20),
        ),
    ]
