from django.contrib import admin

from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):

    search_fields = [
        'name',
    ]

    list_display = [
        'name',
    ]

    ordering = [
        'name',
    ]
