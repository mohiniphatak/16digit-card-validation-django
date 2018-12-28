# Generated by Django 2.1.2 on 2018-10-29 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmzSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.CharField(max_length=16)),
                ('cardtype', models.CharField(max_length=120)),
                ('status', models.CharField(max_length=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]