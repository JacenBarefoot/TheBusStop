# Generated by Django 3.2.7 on 2021-11-15 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20211115_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='age',
            old_name='category',
            new_name='status',
        ),
    ]