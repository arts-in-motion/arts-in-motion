from django.contrib import admin

from portal.donations.models import Donation
from portal.forms.models import FormSubmission

from . import models


class SingleInline(admin.StackedInline):
    max_num = 1
    extra = 0


class ListInline(admin.TabularInline):
    extra = 1


class StudentInline(SingleInline):
    model = models.Student
    fk_name = 'individual'
    verbose_name = "Student Info"

    filter_horizontal = ['classes']
    fields = (
        'individual',
        'emergency_contact',
        'guardian',
        'classes',
        'strengths',
        'health_concerns',
        'accessibility_needs',
        'allergies',
        (
            'needs_tuition_assistance',
            'accepted_dance_liability',
            'photo_release'
        ),
        'notes'
    )


@admin.register(models.WaysToHelp)
class WaysToHelpAdmin(admin.ModelAdmin):

    @staticmethod
    def get_model_perms(_request):
        """Hide this model, but make it available for search."""
        return {}


class VolunteerInline(SingleInline):
    model = models.Volunteer
    fk_name = 'individual'
    verbose_name = "Volunteer Info"

    filter_horizontal = ['events', 'ways_to_help']
    fields = (
        "ways_to_help",
        "events",
        "special_skills",
        "availability",
        "emergency_contact",
        "referral",
    )


class DonorInline(SingleInline):
    model = models.Donor
    verbose_name = "Donor Info"


class FormSubmissionInline(ListInline):
    model = FormSubmission


class IndividualDonorInline(DonorInline):
    exclude = ['organization']


class OrganizationDonorInline(DonorInline):
    exclude = ['individual']


@admin.register(models.Individual)
class IndividualAdmin(admin.ModelAdmin):

    search_fields = [
        'first_name',
        'last_name',
        'email_address',
    ]

    list_display = [
        'id',
        'name',
        'phone_number',
        'email_address',
        '_categories',
    ]

    ordering = [
        'first_name',
        'last_name',
    ]

    inlines = [
        StudentInline,
        VolunteerInline,
        IndividualDonorInline,
        FormSubmissionInline,
    ]

    list_filter = [
        'is_donor',
        'is_staff',
        'is_student',
        'is_volunteer',
        'is_artist',
        'is_board',
    ]

    fields = (
        'prefix',
        'first_name',
        'middle_name',
        'last_name',
        'suffix',
        'date_of_birth',
        ('is_donor', 'is_student', 'is_artist'),
        ('is_staff', 'is_volunteer', 'is_board'),
        'street_address',
        'city',
        'state',
        'zip_code',
        'phone_number',
        'email_address',
        'contact_method',
        'signed_up_date',
        'notes'
    )

    @staticmethod
    def _categories(individual):
        categories = []
        if individual.is_donor:
            categories.append('Donor')
        if individual.is_staff:
            categories.append('Staff')
        if individual.is_student:
            categories.append('Student')
        if individual.is_volunteer:
            categories.append('Volunteer')
        if individual.is_artist:
            categories.append('Artist')
        if individual.is_board:
            categories.append('Board Member')
        return ' / '.join(categories) if categories else None


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):

    search_fields = [
        'name',
        'email_address',
    ]

    list_display = [
        'id',
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
    fields = (
        ('name', 'is_donor'),
        'street_address',
        'city',
        'state',
        'zip_code',
        'phone_number',
        'email_address',
        'contact_method',
        'notes',
    )


class DonationInline(ListInline):
    model = Donation


@admin.register(models.Donor)
class DonorAdmin(admin.ModelAdmin):

    search_fields = [
        'individual__first_name',
        'individual__last_name',
        'organization__name',
    ]

    list_display = [
        'id',
        'individual',
        'organization',
    ]

    inlines = [
        DonationInline,
    ]


@admin.register(models.Guardian)
class GardianAdmin(admin.ModelAdmin):

    @staticmethod
    def get_model_perms(_request):
        """Hide this model, but make it available for search."""
        return {}
