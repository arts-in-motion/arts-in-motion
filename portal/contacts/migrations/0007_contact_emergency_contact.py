# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='emergency_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Contact'),
        ),
    ]
