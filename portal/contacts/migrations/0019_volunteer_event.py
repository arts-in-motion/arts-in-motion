# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20171104_1737'),
        ('contacts', '0018_auto_20171104_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='event',
            field=models.ManyToManyField(to='events.Event'),
        ),
    ]