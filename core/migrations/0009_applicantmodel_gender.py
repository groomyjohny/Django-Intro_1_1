# Generated by Django 4.1.3 on 2022-11-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_applicantmodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantmodel',
            name='gender',
            field=models.CharField(choices=[('М', 'M'), ('Ж', 'F')], default='М', max_length=1, verbose_name='Пол'),
        ),
    ]
