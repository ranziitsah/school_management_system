# Generated by Django 3.0 on 2020-09-26 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0013_auto_20200923_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='data',
            new_name='date',
        ),
    ]
