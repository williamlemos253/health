# Generated by Django 2.2.6 on 2019-10-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_auto_20191015_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cpf',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
