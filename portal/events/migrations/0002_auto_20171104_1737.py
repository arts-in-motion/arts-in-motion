# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]