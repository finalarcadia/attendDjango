# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20160419_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='codeFlag',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='class',
            name='locationFlag',
            field=models.NullBooleanField(default=False),
        ),
    ]