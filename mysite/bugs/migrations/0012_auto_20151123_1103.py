# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0011_auto_20151120_1753'),
    ]

    operations = [
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
