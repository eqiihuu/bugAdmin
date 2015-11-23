# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0006_auto_20151118_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='date',
            field=models.DateTimeField(verbose_name=b'date changed'),
        ),
    ]
