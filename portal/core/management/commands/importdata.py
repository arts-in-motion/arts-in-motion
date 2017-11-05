# pylint: disable=too-many-arguments,too-many-locals

import logging

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

import openpyxl

from portal.contacts.models import Individual, Organization


class Command(BaseCommand):
    help = "Import existing spreadsheets into the database"

    @staticmethod
    def add_arguments(parser):
        parser.add_argument(
            'path',
            help="Full path to master contact list",
        )

    def handle(self, *, path, **_options):
        workbook = openpyxl.load_workbook(path)
        names = workbook.get_sheet_names()

        self.parse_sheet(
            'Artists', names, workbook, Individual,
            dict(
                first_name='First Name',
                last_name='Last Name',
            ),
            dict(
                street_address='Street',
                city='City',
                state='State',
                zip_code='Zip',
                email_address='Email',

            ),
            is_artist=True)

        self.parse_sheet(
            'Businesses', names, workbook, Organization,
            dict(
                name='Business Name',
            ),
            dict(
                street_address='Street',
                city='City',
                state='State',
                zip_code='Zip',
                phone_number='Phone',
                email_address='Email',
            ),
            notes="Business")

        self.parse_sheet(
            'Community Partners', names, workbook, Organization,
            dict(
                name='Name',
            ),
            dict(
                street_address='Address',
                city='City',
                state='State',
                zip_code='Zip',
                phone_number='Number',
                email_address='Email',
            ),
            notes="Community Parter")

        self.parse_sheet(
            'Individuals', names, workbook, Individual,
            dict(
                first_name='First Name',
                last_name='Last Name',
            ),
            dict(
                street_address='Street',
                city='City',
                state='State',
                zip_code='Zip',
                phone_number='Phone',
                email_address='Email',
            ))

        self.parse_sheet(
            'Students', names, workbook, Individual,
            dict(
                first_name='FIRST',
                last_name='LAST',
            ),
            dict(
                street_address='Address/Street',
                city='City',
                state='State',
                zip_code='ZIP',
            ),
            is_student=True)

        self.parse_sheet(
            'volunteers', names, workbook, Individual,
            dict(
                first_name='First Name',
                last_name='Last Name',
            ),
            dict(
                street_address='Street',
                city='City',
                state='State',
                zip_code='Zip',
                phone_number='Phone',
                email_address='Email',
            ),
            is_volunteer=True)

        if names:
            logging.warning(f"Unused sheets: {names}")

    def parse_sheet(self, name, names, workbook,
                    model, id_map, attr_map, **extra):
        names.remove(name)

        sheet = workbook[name]

        headers = None
        for row in sheet.rows:

            if headers is None:
                headers = [cell.value.strip() for cell in row if cell.value]
                continue

            data = dict(zip(headers, [cell.value for cell in row]))

            kwargs = {k: data.pop(v) for k, v in id_map.items()}
            try:
                obj, created = model.objects.get_or_create(**kwargs)
            except IntegrityError as exception:
                logging.error(f"{sheet.title}: {exception}")
                continue

            for key, value in attr_map.items():
                setattr(obj, key, data.pop(value))

            for key, value in extra.items():
                setattr(obj, key, value)

            if data:
                lines = [f"{key}: {value}" for key, value in data.items()]
                obj.notes = '\n'.join(lines)

            obj.save()

            if created:
                self.stdout.write(f"Created {model.__name__}: {obj}")
            else:
                logging.debug(f"Updated {model.__name__}: {obj}")
