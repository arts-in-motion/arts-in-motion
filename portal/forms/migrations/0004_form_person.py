# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0014_auto_20171104_1800'),
        ('forms', '0003_remove_form_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='person',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='contacts.Individual'),
            preserve_default=False,
        ),
    ]
