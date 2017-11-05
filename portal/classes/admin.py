from django.contrib import admin

from . import models


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):

    search_fields = [
        'description',
    ]

    list_display = [
        'description',
        'instructor',
        'start_date',
        'active',
    ]
    list_filter = [
        'active',
    ]

    ordering = [
        '-start_date',
        'description',
    ]

    raw_id_fields = [
        'instructor',
    ]
    related_lookup_fields = {
        'fk': ['instructor'],
    }
