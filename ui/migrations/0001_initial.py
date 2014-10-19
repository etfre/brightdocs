# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('doc_type', models.CharField(max_length=20)),
                ('upload_date', models.DateTimeField(verbose_name='date uploaded')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
