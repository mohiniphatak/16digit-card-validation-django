# Generated by Django 2.1.2 on 2018-10-30 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amazonapp', '0004_auto_20181030_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amzseries',
            old_name='cards_requirement',
            new_name='total_cards_requirement',
        ),
    ]