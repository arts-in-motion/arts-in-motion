# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0002_auto_20171103_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time_Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField()),
                ('notes', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Person')),
            ],
        ),
    ]
