# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Integrantes',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Nombre', models.CharField(max_length=120)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('FechaRegistro', models.DateField(auto_now_add=True)),
                ('DescripcionInvitacion', models.CharField(max_length=100)),
                ('Equipos', models.ForeignKey(to='Equipos.Equipos')),
                ('Integrantes', models.ForeignKey(to='Equipos.Integrantes')),
            ],
        ),
        migrations.AddField(
            model_name='equipos',
            name='Integrador',
            field=models.ManyToManyField(through='Equipos.Membresia', to='Equipos.Integrantes'),
        ),
    ]
