from django.contrib import admin

from . import models


@admin.register(models.Form)
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
    fields=("person", "date", "form_type", "is_filled", "notes")

@admin.register(models.FormType)
class FormType(admin.ModelAdmin):

	list_display = [
		'name',
	]