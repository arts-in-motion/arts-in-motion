# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0034_auto_20171106_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='phone_number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone_number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]