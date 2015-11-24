# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0024_auto_20151124_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='create_time',
            field=models.DateTimeField(default=b'2015-11-24 01:28:51', verbose_name=b'Time created'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='update_time',
            field=models.DateTimeField(default=b'2015-11-24 01:28:51', verbose_name=b'Time updeted'),
        ),
    ]
