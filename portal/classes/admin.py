from django.contrib import admin

from . import models


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):

    search_fields = [
        'name',
    ]

    list_display = [
        'name',
        'start_date',
    ]

    ordering = [
        '-start_date',
        'name',
    ]
