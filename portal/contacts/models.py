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
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
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
    emergency_contact = models.ForeignKey("self", blank=True, null=True)

    def __str__(self):
        if self.kind:
            return f"{self.name} ({self.kind})"
        else:
            return f"{self.name}"


class Student(models.Model):

    contact = models.OneToOneField(Contact)

    # link to classes foreignkey
    classes = models.TextField(blank=True, null=True)
    strengths = models.TextField(blank=True, null=True)
    health_concerns = models.TextField(blank=True, null=True)
    accessibility_needs = models.TextField(blank=True, null=True)
    food_allergies = models.TextField(blank=True, null=True)
    # todo link to forms
    needs_tuition_assistance = models.BooleanField(default=False)
    accepted_dance_liability = models.BooleanField(default=False)
    photo_release = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.contact}"


class Volunteer(models.Model):

    contact = models.OneToOneField(Contact)

    special_skills = models.TextField(blank=True, null=True)
    FUNDRAISING = 'Fundraising'
    USHERING_STAFFING_EVENTS = 'Usering/Staffing Events'
    SERVING_ON_BOARD = 'Serving on the Board of Directors'
    COORDINATING_EVENTS = 'Coordinating Sepcial Events'
    ASSIST_DANCE = 'Assist in Dance Class'
    ASSIST_MUSIC = 'Assist in Music Class'
    ASSIST_ARTS = 'Assist in Arts Class'
    SERVE_COMMITTEE = 'Serve on Committee'
    OFFICE_ASSISTANCE = 'Office Assistance'
    TECHNICAL_SUPPORT = 'Technical Support'
    OTHER = 'Other'

    WAYS_TO_HELP_CHOICES = (
        (FUNDRAISING, 'Fundraising'),
        (USHERING_STAFFING_EVENTS, 'Usering/Staffing Events'),
        (SERVING_ON_BOARD, 'Serving on the Board of Directors'),
        (COORDINATING_EVENTS, 'Coordinating Sepcial Events'),
        (ASSIST_DANCE, 'Assist in Dance Class'),
        (ASSIST_MUSIC, 'Assist in Music Class'),
        (ASSIST_ARTS, 'Assist in Arts Class'),
        (SERVE_COMMITTEE, 'Serve on Committee'),
        (OFFICE_ASSISTANCE, 'Office Assistance'),
        (TECHNICAL_SUPPORT, 'Technical Support'),
        (OTHER, 'Other')
    )
    ways_to_help = models.CharField(max_length=50,choices=WAYS_TO_HELP_CHOICES, blank=True, null=True)
    availability = models.TextField(blank=True, null=True)
    FRIEND = 'From a Friend'
    POSTED_NOTICE = 'Posted Notice'
    NEWSLETTER = 'Newsletter'
    OTHER = 'Other'
    REFERRAL_CHOICES = (
        (FRIEND, 'From a Friend'),
        (POSTED_NOTICE, 'Posted Notice'),
        (NEWSLETTER, 'Newsletter'),
        (OTHER, 'Other')
    )
    referral = models.CharField(max_length=40, choices=REFERRAL_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.contact}"


class CommunicationRecord(models.Model):

    internal_contact = models.ForeignKey(
        Contact,
        related_name="internal_contact"
    )
    external_contact = models.ForeignKey(Contact)
    date_of_communication = models.DateTimeField(auto_now=True)
    # follow_up = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)


class Donor(models.Model):

    contact = models.ForeignKey(Contact)

    INDIVIDUAL = 'Individual'
    ORGANIZATION = 'Organization'
    DONOR_TYPE_CHOICES = (
        (INDIVIDUAL, 'Individual'),
        (ORGANIZATION, 'Organization')
    )
    donor_type = models.CharField(
        max_length=30,
        choices=DONOR_TYPE_CHOICES,
        default=INDIVIDUAL
    )
    organization = models.CharField(max_length=100, blank=True, null=True)
    billing_contact = models.CharField(max_length=100, blank=True, null=True)
    billing_street_address = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    billing_city = models.CharField(max_length=100, blank=True, null=True)
    billing_state = models.CharField(max_length=100, blank=True, null=True)
    billing_zip = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    WEEKLY = 'Weekly'
    MONTHLY = 'Monthly'
    YEARLY = 'Yearly'
    DONATION_FREQUENCY_CHOICES = (
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
        (YEARLY, 'Yearly')
    )
    frequency_of_giving = models.CharField(
        max_length=20,
        choices=DONATION_FREQUENCY_CHOICES,
        default=YEARLY
    )
    motivation = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.contact}"
