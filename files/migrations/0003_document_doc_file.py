# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_rule'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='doc_file',
            field=models.FileField(default=datetime.date(2014, 10, 18), upload_to='.'),
            preserve_default=False,
        ),
    ]
