# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugs',
            name='person',
            field=models.CharField(default=datetime.datetime(2015, 11, 18, 6, 55, 19, 224000, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
