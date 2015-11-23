# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0010_auto_20151120_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Time created'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Time changed'),
        ),
    ]
