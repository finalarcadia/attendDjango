# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20160419_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='absentThreshold',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='lateThreshold',
            field=models.TimeField(blank=True),
        ),
    ]