# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20171103_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.TextField(blank=True, null=True)),
                ('strengths', models.TextField(blank=True, null=True)),
                ('health_concerns', models.TextField(blank=True, null=True)),
                ('accessibility_needs', models.TextField(blank=True, null=True)),
                ('food_allergies', models.TextField(blank=True, null=True)),
                ('needs_tuition_assistance', models.BooleanField(default=False)),
                ('accepted_dance_liability', models.BooleanField(default=False)),
                ('photo_release', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, null=True)),
                ('name', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='contacts.Contact')),
            ],
        ),
    ]
