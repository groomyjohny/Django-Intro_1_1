# Generated by Django 4.1.3 on 2022-11-02 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_appealmodel_status_alter_appealmodel_date'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='accidentmodel',
            name='core_accide_card_nu_ad4d6a_idx',
        ),
        migrations.RenameField(
            model_name='accidentmodel',
            old_name='card_number',
            new_name='number',
        ),
        migrations.AlterField(
            model_name='appealmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 2, 20, 9, 47, 58634), verbose_name='Дата'),
        ),
        migrations.AddIndex(
            model_name='accidentmodel',
            index=models.Index(fields=['number'], name='core_accide_number_5db3af_idx'),
        ),
    ]