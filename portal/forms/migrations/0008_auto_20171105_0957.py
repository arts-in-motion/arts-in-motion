# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_auto_20171105_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
