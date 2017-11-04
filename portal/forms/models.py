from django.db import models


class Form(models.Model):
    BACKGROUND_CHECK = "background_check"
    ENROLLMENT_FORM = "enrollment_form"
    VOLUNTEER_FORM = "volunteer_form"

    FORM_TYPE_CHOICES = (
        (BACKGROUND_CHECK, 'Background Check'),
        (ENROLLMENT_FORM, 'Enrollment Form'),
        (VOLUNTEER_FORM, 'Volunteer Form')

    )
    name = models.CharField(max_length=100)
    person = models.name = models.ForeignKeyField(
        'contacts.person', on_delete=models.CASCADE)
    formType = models.CharField(
        choices=FORM_TYPE_CHOICES
    )
    isFilled = models.BooleanField()
    notes = models.CharField()

    date = models.DateField()
    lastEdited = models.DateField()
