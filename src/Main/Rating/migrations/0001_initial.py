# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Titulo', models.CharField(max_length=100)),
                ('Calificacion', models.IntegerField(max_length=5)),
                ('Estado', models.BooleanField(default=True)),
                ('Comentario', models.TextField()),
            ],
        ),
    ]
