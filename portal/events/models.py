from django.db import models


class Event(models.Model):

    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
