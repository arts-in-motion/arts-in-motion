# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0020_merge_20171104_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='is_donor',
            field=models.BooleanField(default=False, verbose_name='Donor?'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='is_student',
            field=models.BooleanField(default=False, verbose_name='Student?'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='is_volunteer',
            field=models.BooleanField(default=False, verbose_name='Volunteer?'),
        ),
    ]
