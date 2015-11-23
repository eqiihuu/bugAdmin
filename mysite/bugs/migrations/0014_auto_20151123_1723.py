# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0013_auto_20151123_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bug',
            old_name='person',
            new_name='create_person',
        ),
        migrations.RenameField(
            model_name='stage',
            old_name='person',
            new_name='update_person',
        ),
        migrations.RenameField(
            model_name='stage',
            old_name='change_time',
            new_name='update_time',
        ),
    ]
