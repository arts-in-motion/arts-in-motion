# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Time_Tracker',
            new_name='TimeTracker',
        ),
    ]
