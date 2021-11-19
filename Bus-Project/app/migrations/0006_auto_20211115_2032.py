# Generated by Django 3.2.7 on 2021-11-15 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211115_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Kid', 'Kid'), ('Adult', 'Adult')], max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='parents_Number',
            new_name='parents_number',
        ),
        migrations.AddField(
            model_name='arriving',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.grade'),
        ),
    ]