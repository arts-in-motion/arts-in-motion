from django.contrib import admin

from portal.contacts.models import Student

from . import models


class ListInline(admin.TabularInline):
    extra = 0


class StudentInline(ListInline):
    model = Student.classes.through


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
