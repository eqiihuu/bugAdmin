# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0025_auto_20151124_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='create_time',
            field=models.DateTimeField(verbose_name=b'Time created'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='update_time',
            field=models.DateTimeField(verbose_name=b'Time updeted'),
        ),
    ]
