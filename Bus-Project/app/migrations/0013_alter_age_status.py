# Generated by Django 3.2.7 on 2021-11-15 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_age_age_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='age',
            name='status',
            field=models.CharField(choices=[('Kid', 'Kid'), ('Adult', 'Adult')], default='Kid', max_length=200, null=True),
        ),
    ]
