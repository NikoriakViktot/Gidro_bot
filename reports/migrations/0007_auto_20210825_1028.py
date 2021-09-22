# Generated by Django 3.2.6 on 2021-08-25 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20210825_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postreport',
            old_name='name_post',
            new_name='post',
        ),
        migrations.AlterUniqueTogether(
            name='postreport',
            unique_together={('post', 'report_time', 'report_type')},
        ),
    ]
