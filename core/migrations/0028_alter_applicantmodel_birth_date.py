# Generated by Django 4.1.3 on 2022-11-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_applicantmodel_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantmodel',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Дата рождения'),
        ),
    ]
