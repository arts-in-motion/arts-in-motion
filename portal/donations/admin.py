from django.contrib import admin

from . import models


@admin.register(models.Donation)
class DonationAdmin(admin.ModelAdmin):

    search_fields = [
        'donor, event',
    ]

    list_display = [
        'amount',
        'donor',
        'kind',
        'event',
    ]

    ordering = [
        'donor',
        'amount',
    ]

    raw_id_fields = [
        'donor',
        'event',
    ]
    related_lookup_fields = {
        'fk': ['donor', 'event'],
    }
