from django.contrib import admin
from portal.contacts.models import Volunteer
from . import models


class SingleInline(admin.StackedInline):
    max_num = 1
    extra = 0


class ListInline(admin.TabularInline):
    extra = 1


class VolunteerInline(ListInline):
    model = Volunteer.events.through
    verbose_name = "Volunteer"


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):

    search_fields = [
        'name',
    ]

    list_display = [
        'id',
        'name',
        'date',
    ]

    ordering = [
        '-date',
        'name',
    ]
    inlines = [
        VolunteerInline,
    ]
