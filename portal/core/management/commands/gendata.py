# pylint: disable=too-many-locals

import random
from contextlib import suppress

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from faker import Faker

from portal.contacts.models import (Individual, Organization,
                                    Student, Volunteer, Donor)
from portal.classes.models import Class

User = get_user_model()
fake = Faker()


def p(value):
    return value < random.random()


class Command(BaseCommand):
    help = "Generate data for automated testing and manual review"

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

        while Individual.objects.count() < 200:
            with suppress(IntegrityError):
                obj = Individual.objects.create(
                    prefix=fake.prefix() if p(.5) else None,
                    first_name=fake.first_name(),
                    middle_name=fake.first_name() if p(.1) else None,
                    last_name=fake.last_name(),
                    suffix=fake.suffix() if p(.1) else None,
                    street_address=fake.address(),
                    city=fake.city(),
                    state=fake.state(),
                    zip_code=fake.postalcode(),
                    phone_number=fake.phone_number(),
                    email_address=fake.email(),
                    date_of_birth=fake.date(),
                    signed_up_date=fake.date(),
                )
                self.stdout.write(f"Created individual: {obj}")

        while Organization.objects.count() < 200:
            with suppress(IntegrityError):
                obj = Organization.objects.create(
                    name=fake.company(),
                    street_address=fake.address(),
                    city=fake.city(),
                    state=fake.state(),
                    zip_code=fake.postalcode(),
                    phone_number=fake.phone_number(),
                    email_address=fake.email(),
                    signed_up_date=fake.date(),
                )
                self.stdout.write(f"Created individual: {obj}")

        while Student.objects.count() < 100:
            with suppress(IntegrityError):
                obj = Student.objects.create(
                    contact=self.random_individual(),
                )
                self.stdout.write(f"Created student: {obj}")

        while Volunteer.objects.count() < 100:
            with suppress(IntegrityError):
                obj = Volunteer.objects.create(
                    contact=self.random_individual(),
                )
                self.stdout.write(f"Created volunteer: {obj}")

        while Donor.objects.count() < 100:
            if p(.5):
                kwargs = {'individual': self.random_individual()}
            else:
                kwargs = {'organization': self.random_organization()}

            with suppress(IntegrityError):
                obj = Donor.objects.create(
                    **kwargs,
                )
                self.stdout.write(f"Created donor: {obj}")

        while Class.objects.count() < 10:
            with suppress(IntegrityError):
                obj = Class.objects.create(
                    description=fake.text(100),
                    instructor=self.random_individual(),
                    start_date=fake.date(),
                    end_date=fake.date() if p(0.3) else None,
                    location=fake.text(),
                )
                self.stdout.write(f"Created class: {obj}")

    def random_user(self, skip=None):
        skip_ids = [self.new_user_id]
        if skip:
            skip_ids.append(skip.id)
        return random.choice(User.objects.exclude(id__in=skip_ids))

    @staticmethod
    def random_individual():
        return random.choice(Individual.objects.filter())

    @staticmethod
    def random_organization():
        return random.choice(Organization.objects.filter())

    @staticmethod
    def fake_username():
        return fake.name().replace(' ', '').lower()
