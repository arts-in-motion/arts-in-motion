from django.contrib import admin

from . import models


@admin.register(models.Record)
class RecordForm(admin.ModelAdmin):

    fields = [
        'person',
        'date',
        'class_event',
        'event',
        'hours',
        'notes',
    ]

    search_fields = [
        'person',
    ]

    list_display = [
        'person',
    ]

    ordering = [
        'person',
    ]

    fields = [
        'person',
        'date',
        'hours',
        'notes',
    ]

    raw_id_fields = [
        'person',
    ]

    related_lookup_fields = {
        'fk': ['person'],
    }
