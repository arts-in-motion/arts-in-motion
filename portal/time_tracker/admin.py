from django.contrib import admin

from . import models


@admin.register(models.Record)
class RecordForm(admin.ModelAdmin):

    fields = [
        'person',
        'hours',
        'notes',
        'date',
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

    raw_id_fields = [
        'person',
    ]
    fields = ("person", "date", "hours", "notes")
