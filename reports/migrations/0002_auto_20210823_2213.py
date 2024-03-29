# Generated by Django 3.2.6 on 2021-08-23 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postreport',
            name='air_pressure',
        ),
        migrations.RemoveField(
            model_name='postreport',
            name='battery',
        ),
        migrations.RemoveField(
            model_name='postreport',
            name='precipitation',
        ),
        migrations.RemoveField(
            model_name='postreport',
            name='precipitation_1h',
        ),
        migrations.RemoveField(
            model_name='postreport',
            name='precipitation_den',
        ),
        migrations.RemoveField(
            model_name='postreport',
            name='precipitation_doba',
        ),
        migrations.RemoveField(
            model_name='postreport',
            name='pruvodka',
        ),
        migrations.RemoveField(
            model_name='postreport',
            name='qml_Voltage',
        ),
        migrations.RemoveField(
            model_name='postreport',
            name='qml_temp',
        ),
        migrations.RemoveField(
            model_name='postreport',
            name='soil_temperature',
        ),
        migrations.RemoveField(
            model_name='postreport',
            name='station_name',
        ),
        migrations.RemoveField(
            model_name='postreport',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='postreport',
            name='water_level_BS',
        ),
        migrations.RemoveField(
            model_name='postreport',
            name='water_level_ymov',
        ),
    ]
