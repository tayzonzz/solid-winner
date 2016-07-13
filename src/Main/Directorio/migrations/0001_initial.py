# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Codigo', models.CharField(max_length=20)),
                ('Nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Nombre', models.CharField(max_length=120)),
                ('Telefono', models.IntegerField(max_length=20)),
                ('Direccion', models.CharField(max_length=120)),
                ('Estado', models.BooleanField()),
                ('Descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Directorio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Cantidad', models.IntegerField(max_length=10000)),
                ('Categoria', models.ForeignKey(to='Directorio.Categoria')),
                ('Contactos', models.ForeignKey(to='Directorio.Contactos')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='Pertenecientes',
            field=models.ManyToManyField(through='Directorio.Directorio', to='Directorio.Contactos'),
        ),
    ]
