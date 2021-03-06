# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 01:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('contacts', '0017_remove_donor_donor_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='food_allergies',
            new_name='allergies',
        ),
        migrations.RemoveField(
            model_name='individual',
            name='emergency_contact',
        ),
        migrations.AddField(
            model_name='student',
            name='emergency_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_emergency_contact', to='contacts.Individual'),
        ),
        migrations.AddField(
            model_name='student',
            name='guardian',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='emergency_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_emergency_contact', to='contacts.Individual'),
        ),
        migrations.RemoveField(
            model_name='student',
            name='classes',
        ),
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(blank=True, null=True, to='classes.Class'),
        ),
    ]
