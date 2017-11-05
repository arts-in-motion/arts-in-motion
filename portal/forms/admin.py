from django.contrib import admin

from . import models


@admin.register(models.Form)
class PersonForm(admin.ModelAdmin):

    search_fields = [
        'name',
    ]

    list_display = [
        'name',
    ]

    ordering = [
        'name',
    ]

    raw_id_fields = [
        'person',
    ]
