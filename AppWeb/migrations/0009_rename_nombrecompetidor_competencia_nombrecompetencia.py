# Generated by Django 4.1 on 2022-09-21 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0008_ejemplo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competencia',
            old_name='nombreCompetidor',
            new_name='nombreCompetencia',
        ),
    ]
