from django.db import models


class ContactInfo(models.Model):

    class Meta:
        abstract = True

    street_address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)

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


class Individual(ContactInfo):

    prefix = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    suffix = models.CharField(max_length=10, blank=True, null=True)

    date_of_birth = models.DateField(blank=True, null=True)

    @property
    def name(self):
        base = ' '.join([p for p in [self.prefix, self.first_name,
                                     self.middle_name, self.last_name] if p])
        if self.suffix:
            return f"{base}, {self.suffix}"
        else:
            return base


class Organization(ContactInfo):

    name = models.CharField(max_length=100)


class Student(models.Model):

    contact = models.OneToOneField(Individual)
    emergency_contact = models.ForeignKey(
        Individual, related_name="student_emergency_contact", blank=True, null=True)
    #  todo fk guardian
    guardian = models.TextField(blank=True, null=True)
    classes = models.ManyToManyField('classes.Class', blank=True, null=True)
    strengths = models.TextField(blank=True, null=True)
    health_concerns = models.TextField(blank=True, null=True)
    accessibility_needs = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    # todo link to forms
    needs_tuition_assistance = models.BooleanField(default=False)
    accepted_dance_liability = models.BooleanField(default=False)
    photo_release = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.contact}"


class Volunteer(models.Model):

    contact = models.OneToOneField(Individual)
    emergency_contact = models.ForeignKey(
        Individual, related_name="volunteer_emergency_contact", blank=True, null=True)
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
    ways_to_help = models.CharField(
        max_length=50,
        choices=WAYS_TO_HELP_CHOICES,
        blank=True,
        null=True
    )
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
    referral = models.CharField(
        max_length=40,
        choices=REFERRAL_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.contact}"


class CommunicationRecord(models.Model):

    internal_contact = models.ForeignKey(
        Individual,
        related_name="internal_contact"
    )

    # TODO: Make at least one required?
    external_contact = models.ForeignKey(Individual, blank=True, null=True)
    external_organization = models.ForeignKey(
        Organization, blank=True, null=True)

    date_of_communication = models.DateTimeField(auto_now=True)
    # follow_up = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)


class Donor(models.Model):

    # TODO: Make exactingly one required based on type?
    individual = models.ForeignKey(Individual, blank=True, null=True)
    organization = models.ForeignKey(Organization, blank=True, null=True)

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
        return f"{self.individual or self.organization}"
