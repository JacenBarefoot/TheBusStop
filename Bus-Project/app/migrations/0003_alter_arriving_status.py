# Generated by Django 3.2.7 on 2021-11-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211108_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriving',
            name='status',
            field=models.CharField(choices=[('On the way', 'On the way'), ('Made it off the bus', 'Made it off the bus')], max_length=200, null=True),
        ),
    ]
