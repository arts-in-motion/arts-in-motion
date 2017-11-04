from django.db import models

from portal.contacts.models import Individual


class Form(models.Model):
    BACKGROUND_CHECK = "background_check"
    ENROLLMENT_FORM = "enrollment_form"
    VOLUNTEER_FORM = "volunteer_form"
    OTHER = "other"

    FORM_TYPE_CHOICES = (
        (BACKGROUND_CHECK, 'Background Check'),
        (ENROLLMENT_FORM, 'Enrollment Form'),
        (VOLUNTEER_FORM, 'Volunteer Form'),
        (OTHER, 'Other')

    )
    name = models.CharField(max_length=100)
    person = models.name = models.ForeignKey(Individual)
    form_type = models.CharField(
        choices=FORM_TYPE_CHOICES,
        max_length=30
    )
    notes = models.TextField(blank=True, null=True)
    is_filled = models.BooleanField()

    date = models.DateField()
    last_edited = models.DateField(auto_now=True)
