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


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):

    search_fields = [
        'name__name',
    ]

    list_display = [
        '_name',
        'classes',
    ]

    ordering = [
        'name__name',
    ]

    @staticmethod
    def _name(student):
        return student.name.name


@admin.register(models.Volunteer)
class VolunteerAdmin(admin.ModelAdmin):

    search_fields = [
        'name__name',
    ]

    list_display = [
        '_name',
        'availability',
    ]

    ordering = [
        'name__name',
    ]

    @staticmethod
    def _name(volunteer):
        return volunteer.name.name
