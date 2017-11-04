from django.db import models

from portal.contacts.models import Contact


class Record(models.Model):

    EVENT = "event"
    CLASS = "class"
    OTHER = "other"

    TIME_TYPE_CHOICES = (
        (EVENT, 'Event'),
        (CLASS, 'Class'),
        (OTHER, 'Other')
    )

    hours = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    person = models.name = models.ForeignKey(
        Contact, on_delete=models.CASCADE)
    date = models.DateField()
