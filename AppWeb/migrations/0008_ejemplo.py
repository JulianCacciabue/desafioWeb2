# Generated by Django 4.1 on 2022-09-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0007_lugar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ejemplo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEjemplo', models.CharField(max_length=60)),
            ],
        ),
    ]
