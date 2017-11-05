from django.contrib import admin

from . import models


@admin.register(models.Form)
class FormAdmin(admin.ModelAdmin):

    search_fields = [
        'name'
    ]

    list_display = [
        'id',
        'name',
    ]


@admin.register(models.FormSubmission)
class PersonFormAdmin(admin.ModelAdmin):

    search_fields = [
        'person',
    ]

    list_display = [
        'id',
        'person',
        'form_name',
        'is_filled',
    ]

    ordering = [
        'person',
    ]

    fields = [
        'person',
        'date',
        ('form_name', 'is_filled'),
        'notes',
    ]

    raw_id_fields = [
        'person',
    ]
    related_lookup_fields = {
        'fk': ['person'],
    }
