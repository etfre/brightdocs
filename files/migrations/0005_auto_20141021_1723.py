# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_auto_20141018_0548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Rule',
            new_name='Trigger',
        ),
        migrations.AddField(
            model_name='condition',
            name='trigger',
            field=models.ForeignKey(to='files.Trigger'),
            preserve_default=True,
        ),
    ]
