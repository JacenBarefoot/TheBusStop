# Generated by Django 3.2.7 on 2021-11-15 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_email_passenger_parents_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arriving',
            name='product',
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]
