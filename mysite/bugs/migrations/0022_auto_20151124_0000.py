# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0021_auto_20151123_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='create_time',
            field=models.DateTimeField(default=b'2015-11-24 00:00:41', verbose_name=b'Time created'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='update_time',
            field=models.DateTimeField(default=b'2015-11-24 00:00:41', verbose_name=b'Time updeted'),
        ),
    ]
