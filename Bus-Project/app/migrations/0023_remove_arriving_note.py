# Generated by Django 3.2.7 on 2021-11-18 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_arriving_passenger_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arriving',
            name='note',
        ),
    ]
