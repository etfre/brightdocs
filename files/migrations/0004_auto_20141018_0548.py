# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import files.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_document_doc_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc_file',
            field=models.FileField(upload_to=files.models.get_upload_file_name),
        ),
    ]
