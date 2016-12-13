# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('object_id', models.PositiveIntegerField(verbose_name='ID объекта приложения')),
                ('date', models.DateField(verbose_name='Дата', default=datetime.datetime.now)),
                ('hits', models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', verbose_name='Приложение')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='counter',
            unique_together=set([('content_type', 'object_id', 'date')]),
        ),
    ]
