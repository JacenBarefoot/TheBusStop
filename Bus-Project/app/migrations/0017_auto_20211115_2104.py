# Generated by Django 3.2.7 on 2021-11-15 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20211115_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriving',
            name='age',
            field=models.CharField(choices=[('Kid', 'Kid'), ('Adult', 'Adult')], max_length=5, null=True),
        ),
        migrations.DeleteModel(
            name='Age',
        ),
    ]