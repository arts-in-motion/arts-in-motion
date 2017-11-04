from django.db import models
# from portal.contacts.models import Individual


class Class(models.Model):

    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    recurrence = models.DateTimeField()
    location = models.TextField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
