# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 03:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20160424_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroster',
            name='adminName',
        ),
        migrations.RemoveField(
            model_name='classroster',
            name='className',
        ),
        migrations.RemoveField(
            model_name='classroster',
            name='professorName',
        ),
        migrations.RemoveField(
            model_name='classroster',
            name='studentName',
        ),
    ]