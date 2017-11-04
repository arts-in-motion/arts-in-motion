from django.contrib import admin

from . import models


class SingleInline(admin.StackedInline):
    max_num = 1
    extra = 0


# @admin.register(models.Student)
# class StudentAdmin(admin.ModelAdmin):

#     search_fields = [
#         'contact__name',
#     ]

#     list_display = [
#         '_name',
#         'classes',
#     ]

#     ordering = [
#         'contact__name',
#     ]

#     @staticmethod
#     def _name(student):
#         return student.contact.n


class StudentInline(SingleInline):
    model = models.Student
    verbose_name = "Student Info"


# @admin.register(models.Volunteer)
# class VolunteerAdmin(admin.ModelAdmin):

#     search_fields = [
#         'contact__name',
#     ]

#     list_display = [
#         '_name',
#         'availability',
#     ]

#     ordering = [
#         'contact__name',
#     ]

#     @staticmethod
#     def _name(volunteer):
#         return volunteer.contact.name


class VolunteerInline(SingleInline):
    model = models.Volunteer
    verbose_name = "Volunteer Info"


# @admin.register(models.Donor)
# class DonorAdmin(admin.ModelAdmin):

#     search_fields = [
#         'contact__name',
#     ]

#     list_display = [
#         '_name',
#         'donor_type',
#     ]

#     ordering = [
#         'contact__name',
#     ]

#     @staticmethod
#     def _name(donor):
#         return donor.contact.name


class DonorInline(SingleInline):
    model = models.Donor
    verbose_name = "Donor Info"


class IndividualDonorInline(DonorInline):
    exclude = ['organization']


class OrganizationDonorInline(DonorInline):
    exclude = ['individual']


@admin.register(models.Individual)
class IndividualAdmin(admin.ModelAdmin):

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
        'first_name',
        'last_name',
    ]

    inlines = [
        StudentInline,
        VolunteerInline,
        IndividualDonorInline,
    ]


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):

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

    inlines = [
        OrganizationDonorInline,
    ]
