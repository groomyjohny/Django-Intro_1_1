# Generated by Django 4.1.3 on 2022-11-02 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_emergencyservicemodel_phonenumber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appealmodel',
            options={'ordering': ['date', 'number'], 'verbose_name': 'Обращение', 'verbose_name_plural': 'Обращения'},
        ),
        migrations.AlterModelOptions(
            name='applicantmodel',
            options={'ordering': ['fullName'], 'verbose_name': 'Заявитель', 'verbose_name_plural': 'Заявители'},
        ),
        migrations.AlterModelOptions(
            name='emergencyservicemodel',
            options={'ordering': ['serviceCode'], 'verbose_name': 'Экстренная служба', 'verbose_name_plural': 'Экстренные службы'},
        ),
        migrations.AlterField(
            model_name='appealmodel',
            name='applicantId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appeals', to='core.applicantmodel'),
        ),
    ]