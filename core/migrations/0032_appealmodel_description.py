# Generated by Django 4.1.3 on 2022-11-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_rename_additiondatetime_accidentmodel_addition_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='appealmodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]