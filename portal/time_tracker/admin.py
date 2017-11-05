from django.contrib import admin

from . import models


@admin.register(models.Record)
class RecordForm(admin.ModelAdmin):

    search_fields = [
        'person'
    ]

    list_display = [
        'person'
    ]

    ordering = [
        'person'
    ]
    fields=("person", "date", "hours", "notes")
