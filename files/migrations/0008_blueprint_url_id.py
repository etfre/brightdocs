# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_auto_20141021_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='blueprint',
            name='url_id',
            field=models.IntegerField(default=5),
            preserve_default=True,
        ),
    ]
