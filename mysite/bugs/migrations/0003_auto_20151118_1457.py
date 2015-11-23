# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0002_bugs_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('person', models.CharField(max_length=30)),
                ('date', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bugs',
        ),
    ]
