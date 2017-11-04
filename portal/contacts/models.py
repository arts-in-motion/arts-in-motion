from django.db import models


class ContactType(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Contact Types"

    def __str__(self):
        return f"{self.name}"


class Contact(models.Model):

    kind = models.ForeignKey(ContactType, verbose_name="Type", null=True)

    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    PHONE = 'Phone'
    EMAIL = 'Email'
    CONTACT_METHOD_CHOICES = (
        (PHONE, 'Phone'),
        (EMAIL, 'Email'),
    )
    contact_method = models.CharField(
        max_length=20,
        choices=CONTACT_METHOD_CHOICES,
        default=PHONE
    )
    notes = models.TextField(blank=True, null=True)
    signed_up_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
