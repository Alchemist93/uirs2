# Generated by Django 2.1.4 on 2018-12-17 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ok', '0002_auto_20181217_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='citizenship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ok.Citizen', verbose_name='Гражданство'),
        ),
    ]
