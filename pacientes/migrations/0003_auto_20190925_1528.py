# Generated by Django 2.2.5 on 2019-09-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_auto_20190925_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='empresa',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]