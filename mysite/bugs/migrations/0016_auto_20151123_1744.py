# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0015_auto_20151123_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='update_time',
            field=models.DateTimeField(default=b'2015-11-23 17:44:59', verbose_name=b'Time updeted'),
        ),
    ]
