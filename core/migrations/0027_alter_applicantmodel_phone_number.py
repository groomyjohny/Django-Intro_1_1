# Generated by Django 4.1.3 on 2022-11-03 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_applicantmodel_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantmodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона'),
        ),
    ]