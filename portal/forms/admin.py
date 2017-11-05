from django.contrib import admin

from . import models


@admin.register(models.FormSubmission)
class PersonForm(admin.ModelAdmin):

    search_fields = [
        'person',
    ]

    list_display = [
        'person',
    ]

    ordering = [
        'person',
    ]
    fields = ("person", "date", ("form_name", "is_filled"), "notes")


admin.site.register(models.Form)
