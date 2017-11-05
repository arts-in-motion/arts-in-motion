from django.db import models

from portal.contacts.models import Individual
from portal.events.models import Event
from portal.classes.models import Class


class Record(models.Model):

    EVENT = "event"
    CLASS = "class"
    OTHER = "other"

    TIME_TYPE_CHOICES = (
        (EVENT, 'Event'),
        (CLASS, 'Class'),
        (OTHER, 'Other')
    )
    event = models.ForeignKey(Event, blank=True, null=True)
    class_event = models.ForeignKey(Class, blank=True, null=True)
    hours = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    person = models.name = models.ForeignKey(Individual)
    date = models.DateField()
