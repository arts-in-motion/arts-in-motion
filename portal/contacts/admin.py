from django.contrib import admin

from . import models


class SingleInline(admin.StackedInline):
    max_num = 1
    extra = 0


class StudentInline(SingleInline):
    model = models.Student
    fk_name = 'individual'
    verbose_name = "Student Info"

    filter_horizontal = ['classes']


class VolunteerInline(SingleInline):
    model = models.Volunteer
    fk_name = 'individual'
    verbose_name = "Volunteer Info"

    filter_horizontal = ['events']


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
        'first_name',
        'last_name',
        'email_address',
    ]

    list_display = [
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
    ]

    list_filter = [
        'is_donor',
        'is_student',
        'is_volunteer',
        'is_artist',
    ]

    @staticmethod
    def _categories(individual):
        categories = []
        if individual.is_donor:
            categories.append('Donor')
        if individual.is_student:
            categories.append('Student')
        if individual.is_volunteer:
            categories.append('Volunteer')
        if individual.is_artist:
            categories.append('Artist')
        return ' / '.join(categories) if categories else None


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


@admin.register(models.Donor)
class DonorAdmin(admin.ModelAdmin):

    search_fields = [
        'individual__first_name',
        'individual__last_name',
        'organization__name',
    ]

    @staticmethod
    def get_model_perms(_request):
        """Hide this model, but make it available for search."""
        return {}


admin.site.register(models.Guardian)
