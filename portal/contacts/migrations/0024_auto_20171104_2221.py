# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 02:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0023_auto_20171104_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardian',
            name='individual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Guardian', to='contacts.Individual'),
        ),
    ]