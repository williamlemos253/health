# Generated by Django 2.2.5 on 2019-10-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_auto_20191003_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='declaracaodesaude',
            name='pontuacao',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
