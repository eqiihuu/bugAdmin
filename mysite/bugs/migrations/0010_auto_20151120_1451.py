# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0009_auto_20151118_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='bug_id',
            field=models.CharField(default=datetime.datetime(2015, 11, 20, 6, 51, 24, 934000, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bug',
            name='create_time',
            field=models.DateTimeField(verbose_name=b'Time created'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='time',
            field=models.DateTimeField(verbose_name=b'Time changed'),
        ),
    ]
