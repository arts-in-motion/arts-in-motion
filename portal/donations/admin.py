from django.contrib import admin

from . import models


@admin.register(models.Donation)
class DonationAdmin(admin.ModelAdmin):

    search_fields = [
        'donor__individual__first_name',
        'donor__individual__last_name',
        'donor__individual__email_address',
        'donor__organization__name',
        'event__name',
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
