# Generated by Django 2.2.6 on 2019-10-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0005_auto_20191015_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cpf',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
