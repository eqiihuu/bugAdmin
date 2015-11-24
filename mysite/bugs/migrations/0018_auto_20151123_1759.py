# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0017_auto_20151123_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='create_time',
            field=models.DateTimeField(default=b'2015-11-23 17:59:01', verbose_name=b'Time created'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='update_time',
            field=models.DateTimeField(default=b'2015-11-23 17:59:01', verbose_name=b'Time updeted'),
        ),
    ]
