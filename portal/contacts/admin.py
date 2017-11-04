from django.contrib import admin

from . import models


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
        'name',
    ]

    list_display = [
        'name',
    ]

    ordering = [
        'name',
    ]


class StudentInline(admin.StackedInline):
    model = models.Student
    max_num = 1
    extra = 0
    verbose_name = "Student Info"


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):

    search_fields = [
        'name',
        'email_address',
    ]

    list_display = [
        'name',
        'phone_number',
        'email_address',
    ]

    ordering = [
        'name',
    ]

    inlines = [StudentInline]
