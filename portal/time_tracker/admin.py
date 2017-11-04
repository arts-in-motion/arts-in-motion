from django.contrib import admin

from . import models


@admin.register(models.TimeTracker)
class TimeTrackerForm(admin.ModelAdmin):

    search_fields = [
        'person'
    ]

    list_display = [
        'person'
    ]

    ordering = [
        'person'
    ]
