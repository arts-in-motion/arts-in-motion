from django.db import models

from portal.contacts.models import Individual


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
    person = models.name = models.ForeignKey(Individual)
    date = models.DateField()
