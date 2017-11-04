# pylint: disable=too-many-locals

import random
from contextlib import suppress

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from faker import Faker

from portal.contacts.models import ContactType, Contact


User = get_user_model()


class Command(BaseCommand):
    help = "Generate data for automated testing and manual review"

    fake = Faker()
    new_user_id = None

    def add_arguments(self, parser):
        parser.add_argument(
            'emails',
            nargs='?',
            type=lambda value: value.split(','),
            default=[],
        )

    def handle(self, *, emails, **_options):
        self.update_site()
        admin = self.get_or_create_superuser()
        self.new_user_id = self.get_or_create_user("newbie@example.com").id
        users = [self.get_or_create_user(email) for email in emails]
        self.generate_review_data(admin, *users)

    def update_site(self):
        site = Site.objects.get(id=1)
        site.name = f"portal {settings.BASE_NAME}"
        site.domain = settings.BASE_DOMAIN
        site.save()
        self.stdout.write(f"Updated site: {site}")

    def get_or_create_superuser(self, username="admin", password="password"):
        try:
            user = User.objects.create_superuser(
                username=username,
                email=f"{username}@{settings.BASE_DOMAIN}",
                password=password,
            )
            self.stdout.write(f"Created new superuser: {user}")
        except IntegrityError:
            user = User.objects.get(username=username)
            self.stdout.write(f"Found existing superuser: {user}")

        return user

    def get_or_create_user(self, base_email, password="password"):
        username, email_domain = base_email.split('@')

        user, created = User.objects.get_or_create(username=username)
        user.email = f"{username}+{settings.BASE_NAME}@{email_domain}"
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(f"Created new user: {user}")
        else:
            self.stdout.write(f"Update user: {user}")

        return user

    def generate_review_data(self, *_users):
        while User.objects.count() < 10:
            with suppress(IntegrityError):
                user = User.objects.create(
                    username=self.fake_username(),
                )
                self.stdout.write(f"Created user: {user}")

        donor, _ = ContactType.objects.get_or_create(name="Donor")
        staff, _ = ContactType.objects.get_or_create(name="Staff")
        student, _ = ContactType.objects.get_or_create(name="Student")
        volunter, _ = ContactType.objects.get_or_create(name="Volunteer")
        people_kinds = [donor, staff, student, volunter]

        business, _ = ContactType.objects.get_or_create(name="Business")
        parter, _ = ContactType.objects.get_or_create(name="Community Partner")
        company_kinds = [business, parter]

        while Contact.objects.count() < 200:
            if random.random() < .60:
                kind = random.choice(people_kinds)
                name = self.fake.name()
                date_of_birth = self.fake.date()
            else:
                kind = random.choice(company_kinds)
                name = self.fake.company()
                date_of_birth = None

            with suppress(IntegrityError):
                contact = Contact.objects.create(
                    kind=kind,
                    name=name,
                    street_address=self.fake.address(),
                    city=self.fake.city(),
                    state=self.fake.state(),
                    zip_code=self.fake.postalcode(),
                    phone_number=self.fake.phone_number(),
                    email_address=self.fake.email(),
                    date_of_birth=date_of_birth,
                    signed_up_date=self.fake.date(),
                )
                self.stdout.write(f"Created contact: {contact}")

    def random_user(self, skip=None):
        skip_ids = [self.new_user_id]
        if skip:
            skip_ids.append(skip.id)
        return random.choice(User.objects.exclude(id__in=skip_ids))

    def fake_username(self):
        return self.fake.name().replace(' ', '').lower()

    def fake_name(self):
        return self.fake.name()
