# Generated by Django 3.2.7 on 2021-11-15 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_age_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Kid', 'Kid'), ('Adult', 'Adult')], max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='arriving',
            name='age',
        ),
        migrations.DeleteModel(
            name='Age',
        ),
        migrations.AddField(
            model_name='arriving',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.grade'),
        ),
    ]