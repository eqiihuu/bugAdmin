# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0008_auto_20151118_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bug',
            old_name='create_date',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='stage',
            old_name='date',
            new_name='time',
        ),
    ]
