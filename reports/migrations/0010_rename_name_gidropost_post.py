# Generated by Django 3.2.6 on 2021-08-28 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_auto_20210825_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gidropost',
            old_name='name',
            new_name='post',
        ),
    ]
