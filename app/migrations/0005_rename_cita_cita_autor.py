# Generated by Django 3.2.9 on 2022-01-14 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220114_1802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cita',
            old_name='cita',
            new_name='autor',
        ),
    ]
