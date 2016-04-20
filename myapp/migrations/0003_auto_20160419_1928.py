# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 00:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160419_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='absentThreshold',
            field=models.TimeField(default=datetime.datetime(2016, 4, 20, 0, 28, 35, 262567, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class',
            name='lateThreshold',
            field=models.TimeField(default=datetime.datetime(2016, 4, 20, 0, 28, 44, 737835, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class',
            name='locationFlag',
            field=models.BooleanField(default=0),
        ),
    ]