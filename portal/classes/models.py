from django.db import models

from portal.contacts.models import Individual


class Class(models.Model):

    description = models.CharField(max_length=100)
    instructor = models.ForeignKey(Individual)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    recurrence = models.CharField(max_length=100, blank=True, null=True)
    location = models.TextField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.description}"
