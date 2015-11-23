# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0007_auto_20151118_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bug',
            old_name='name',
            new_name='problem',
        ),
    ]
