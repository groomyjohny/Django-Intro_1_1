# Generated by Django 4.1.3 on 2022-11-02 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=128, verbose_name='ФИО')),
                ('phoneNumber', models.BigIntegerField(verbose_name='Номер телефона')),
                ('healthState', models.TextField(verbose_name='Состояние здоровья')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('serviceCode', models.IntegerField(verbose_name='Код службы')),
                ('phoneNumber', models.BigIntegerField(verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='AppealModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('applicantId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.applicantmodel')),
            ],
        ),
    ]
