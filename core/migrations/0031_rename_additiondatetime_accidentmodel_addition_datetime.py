# Generated by Django 4.1.3 on 2022-11-03 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_accidentmodel_additiondatetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accidentmodel',
            old_name='additionDateTime',
            new_name='addition_datetime',
        ),
    ]