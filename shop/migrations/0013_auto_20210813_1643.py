# Generated by Django 3.2.4 on 2021-08-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_specproduct_microcontroller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specproduct',
            name='microcontroller',
            field=models.CharField(max_length=20, verbose_name='Microcontroller'),
        ),
        migrations.AlterField(
            model_name='specproduct',
            name='operating_voltage',
            field=models.CharField(max_length=10, verbose_name='Operating Voltage'),
        ),
    ]
