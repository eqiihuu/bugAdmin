# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0012_auto_20151123_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stage',
            old_name='time',
            new_name='change_time',
        ),
        migrations.AddField(
            model_name='bug',
            name='note',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stage',
            name='note',
            field=models.CharField(default=' ', max_length=500),
            preserve_default=False,
        ),
    ]
