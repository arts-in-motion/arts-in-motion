# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 13:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20171103_2252'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Contact',
        ),
    ]
