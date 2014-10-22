# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0008_blueprint_url_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blueprint',
            name='url_id',
        ),
    ]
