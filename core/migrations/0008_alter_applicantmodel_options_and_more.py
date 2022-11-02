# Generated by Django 4.1.3 on 2022-11-02 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_applicantmodel_birthdate_alter_appealmodel_services'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicantmodel',
            options={'ordering': ['full_name'], 'verbose_name': 'Заявитель', 'verbose_name_plural': 'Заявители'},
        ),
        migrations.AlterModelOptions(
            name='emergencyservicemodel',
            options={'ordering': ['service_code'], 'verbose_name': 'Экстренная служба', 'verbose_name_plural': 'Экстренные службы'},
        ),
        migrations.RenameField(
            model_name='appealmodel',
            old_name='applicantId',
            new_name='applicant',
        ),
        migrations.RenameField(
            model_name='applicantmodel',
            old_name='birthDate',
            new_name='birth_date',
        ),
        migrations.RenameField(
            model_name='applicantmodel',
            old_name='fullName',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='applicantmodel',
            old_name='healthState',
            new_name='health_state',
        ),
        migrations.RenameField(
            model_name='applicantmodel',
            old_name='phoneNumber',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='emergencyservicemodel',
            old_name='phoneNumber',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='emergencyservicemodel',
            old_name='serviceCode',
            new_name='service_code',
        ),
    ]
