# Generated by Django 2.2.6 on 2019-10-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0009_auto_20191016_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cpf',
            field=models.CharField(max_length=15),
        ),
    ]
