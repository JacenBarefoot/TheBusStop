# Generated by Django 3.2.7 on 2021-11-18 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_arriving_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriving',
            name='passenger_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.passenger'),
        ),
    ]
