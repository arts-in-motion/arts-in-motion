from django.contrib import admin

from . import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):

    search_fields = [
        'name',
    ]

    list_display = [
        'id',
        'name',
        'date',
    ]

    ordering = [
        '-date',
        'name',
    ]
