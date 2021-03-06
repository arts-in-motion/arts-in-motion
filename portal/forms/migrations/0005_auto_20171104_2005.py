# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 00:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_form_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='form',
            name='form_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.FormType'),
        ),
    ]
