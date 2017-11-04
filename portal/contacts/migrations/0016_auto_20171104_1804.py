# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0015_auto_20171104_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='individual',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='individual',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
