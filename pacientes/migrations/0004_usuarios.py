# Generated by Django 2.2.5 on 2019-09-26 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacientes', '0003_auto_20190925_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='pacientes.Profile')),
                ('user', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('profile', 'user')},
            },
        ),
    ]
