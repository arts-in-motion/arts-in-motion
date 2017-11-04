from django.db import models


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
    person = models.name = models.ForeignKey(
        'contacts.person', on_delete=models.CASCADE)
    formType = models.CharField(
        choices=FORM_TYPE_CHOICES,
        max_length=30
    )
    isFilled = models.BooleanField()
    notes = models.TextField(blank=True, null=True)

    date = models.DateField()
    # TODO make this set auto based on edit
    lastEdited = models.DateField(auto_now=True)
