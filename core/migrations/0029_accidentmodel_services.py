# Generated by Django 4.1.3 on 2022-11-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_applicantmodel_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='accidentmodel',
            name='services',
            field=models.ManyToManyField(blank=True, to='core.emergencyservicemodel'),
        ),
    ]