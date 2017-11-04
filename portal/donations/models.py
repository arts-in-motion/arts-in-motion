from django.db import models

from portal.contacts.models import Donor
from portal.events.models import Event


class Donation(models.Model):

    donor = models.ForeignKey(Donor)
    amount = models.CharField(max_length=100)
    date = models.DateField()
    INKIND = 'In Kind'
    CASH = 'Cash'
    WEBSITE = 'Website'
    CHECK = 'Check'
    CREDIT_CARD = 'Credit Card'
    KIND_CHOICES = (
        (INKIND, 'In Kind'),
        (CASH, 'Cash'),
        (WEBSITE, 'Website'),
        (CHECK, 'Check'),
        (CREDIT_CARD, 'Credit Card'),
    )
    kind = models.CharField(choices=KIND_CHOICES, max_length=40)
    notes = models.TextField(blank=True, null=True)
    event = models.ForeignKey(Event, blank=True, null=True)

    def __str__(self):
        return f"{self.amount}"
