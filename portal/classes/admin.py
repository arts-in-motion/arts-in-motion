from django.contrib import admin

from portal.contacts.models import Student

from . import models


class ListInline(admin.TabularInline):
    extra = 0


class StudentInline(ListInline):
    model = Student.classes.through


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    def get_class_link(self, obj):
        return '<a href="/class-reports/{}">Class Report</a>'.format(obj.id)

    get_class_link.allow_tags = True
    search_fields = [
        'description',
    ]

    list_display = [
        'id',
        'description',
        'instructor',
        'start_date',
        'active',
        'get_class_link'
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
