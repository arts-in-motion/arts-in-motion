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
    ]

    ordering = [
        '-start_date',
        'description',
    ]

    raw_id_fields = [
        'instructor',
    ]
