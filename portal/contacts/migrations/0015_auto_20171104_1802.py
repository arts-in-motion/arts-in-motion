# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 22:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0014_auto_20171104_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individual',
            old_name='mid',
            new_name='middle_name',
        ),
    ]