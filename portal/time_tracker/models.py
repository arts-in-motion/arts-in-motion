from django.db import models


class TimeTracker(models.Model):

    EVENT = "event"
    CLASS = "class"
    OTHER = "other"

    TIME_TYPE_CHOICES = (
        (EVENT, 'Event'),
        (CLASS, 'Class'),
        (OTHER, 'Other')
    )

    hours = models.IntegerField()
    notes = models.CharField(max_length=1000)
    person = models.name = models.ForeignKey(
        'contacts.person', on_delete=models.CASCADE)
    date = models.DateField()
