# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0004_auto_20151118_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='create_date',
            field=models.DateTimeField(verbose_name=b'date created'),
        ),
    ]
