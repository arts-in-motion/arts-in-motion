from django.contrib import admin

from . import models
from portal.contacts.models import Student


class ListInline(admin.TabularInline):
    extra = 1


class StudentInline(ListInline):
    model = Student
    fk_name = 'classes'


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):

    search_fields = [
        'description',
    ]

    list_display = [
        'id',
        'description',
        'instructor',
        'start_date',
        'active',
    ]
    list_filter = [
        'active',
    ]

    ordering = [
        '-start_date',
        'description',
    ]

    raw_id_fields = [
        'instructor',
    ]
    related_lookup_fields = {
        'fk': ['instructor'],
    }

    inlines = [
        StudentInline,
    ]
