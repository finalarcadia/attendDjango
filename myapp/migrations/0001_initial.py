# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 02:03
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendancePK', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
                ('mark', models.CharField(choices=[('attempt', 'attempt'), ('present', 'present'), ('late', 'late'), ('absent', 'absent')], default='attempt', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('classPK', models.AutoField(primary_key=True, serialize=False)),
                ('classId', models.CharField(max_length=30)),
                ('update', models.DateTimeField(auto_now=True)),
                ('start', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('lateThreshold', models.IntegerField(blank=True, null=True)),
                ('absentThreshold', models.IntegerField(blank=True, null=True)),
                ('codeExpiration', models.IntegerField(blank=True, null=True)),
                ('locationFlag', models.BooleanField(default=False)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('codeFlag', models.BooleanField(default=False)),
                ('code', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRequest',
            fields=[
                ('classRequestPK', models.AutoField(primary_key=True, serialize=False)),
                ('requestType', models.BooleanField(default=False)),
                ('classIdKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Class')),
                ('userIdKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoster',
            fields=[
                ('classRosterPK', models.AutoField(primary_key=True, serialize=False)),
                ('classIdKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Class')),
                ('userIdKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('universityPK', models.AutoField(primary_key=True, serialize=False)),
                ('universityName', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('userDetailPK', models.AutoField(primary_key=True, serialize=False)),
                ('userType', models.CharField(max_length=10)),
                ('schoolId', models.IntegerField()),
                ('universityKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.University')),
                ('userIdKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='universityKey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.University'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='classkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Class'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='userIdKey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='userdetail',
            unique_together=set([('universityKey', 'userIdKey')]),
        ),
        migrations.AlterUniqueTogether(
            name='classroster',
            unique_together=set([('classIdKey', 'userIdKey')]),
        ),
        migrations.AlterUniqueTogether(
            name='classrequest',
            unique_together=set([('classIdKey', 'userIdKey')]),
        ),
    ]
