# Generated by Django 4.1.3 on 2022-11-02 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_appealmodel_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appealmodel',
            old_name='services',
            new_name='servicesRelation',
        ),
    ]
