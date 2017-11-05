from django.db import models

from portal.contacts.models import Individual


class Form(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class FormSubmission(models.Model):

    person = models.ForeignKey(Individual)
    form_name = models.ForeignKey(Form)
    notes = models.TextField(blank=True, null=True)
    is_filled = models.BooleanField()

    date = models.DateField()
    last_edited = models.DateField(auto_now=True)
