# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0003_auto_20151118_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('person', models.CharField(max_length=30)),
                ('date', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='bug',
            old_name='date',
            new_name='create_date',
        ),
        migrations.AddField(
            model_name='stage',
            name='bug',
            field=models.ForeignKey(to='bugs.Bug'),
        ),
    ]
