# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_auto_20141021_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('trigger', models.ForeignKey(to='files.Trigger')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
