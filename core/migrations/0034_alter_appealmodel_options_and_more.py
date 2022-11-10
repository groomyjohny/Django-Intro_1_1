# Generated by Django 4.1.3 on 2022-11-10 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_applicantmodel_accidents_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appealmodel',
            options={'ordering': ('date', 'number'), 'verbose_name': 'Обращение', 'verbose_name_plural': 'Обращения'},
        ),
        migrations.AlterModelOptions(
            name='applicantmodel',
            options={'ordering': ('surname', 'first_name', 'patronymic_name'), 'verbose_name': 'Заявитель', 'verbose_name_plural': 'Заявители'},
        ),
        migrations.AlterModelOptions(
            name='emergencyservicemodel',
            options={'ordering': ('service_code',), 'verbose_name': 'Экстренная служба', 'verbose_name_plural': 'Экстренные службы'},
        ),
        migrations.AlterField(
            model_name='accidentmodel',
            name='dont_call',
            field=models.BooleanField(default=False, verbose_name='Не звонить'),
        ),
        migrations.AlterField(
            model_name='applicantmodel',
            name='first_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='applicantmodel',
            name='patronymic_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='applicantmodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='applicantmodel',
            name='surname',
            field=models.CharField(max_length=255, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='emergencyservicemodel',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='emergencyservicemodel',
            name='phone_number',
            field=models.CharField(max_length=255, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='emergencyservicemodel',
            name='service_code',
            field=models.CharField(max_length=255, verbose_name='Код службы'),
        ),
    ]
