# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 02:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0022_merge_20171104_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='guardian',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Guardian'),
        ),
    ]
