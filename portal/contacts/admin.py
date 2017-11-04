from django.contrib import admin

from . import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):

    search_fields = [
        'name',
        'email_address',
    ]

    list_display = [
        'name',
        'kind',
        'phone_number',
        'email_address',
    ]
    list_filter = [
        'kind',
    ]

    ordering = [
        'name',
    ]


@admin.register(models.ContactType)
class ContactTypeAdmin(admin.ModelAdmin):

    search_fields = [
        'name',
    ]

    list_display = [
        'name',
    ]

    ordering = [
        'name',
    ]
