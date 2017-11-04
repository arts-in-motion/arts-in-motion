from django.core.management.base import BaseCommand

import openpyxl

from portal.contacts.models import Individual


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

        self.parse_students(workbook, names)

        for name in names:
            self.stdout.write(f"Unused sheet: {name}")

    def parse_students(self, workbook, names):
        name = 'Students'
        names.remove(name)

        sheet = workbook[name]

        headers = None
        for row in sheet.rows:

            if headers is None:
                headers = [c.value for c in row if c.value]
                continue

            data = dict(zip(headers, [c.value for c in row]))

            obj, created = Individual.objects.get_or_create(
                name=f"{data['FIRST']} {data['LAST']}",
            )
            # TODO: Set additional fields
            # individual.foo = bar
            obj.save()
            if created:
                self.stdout.write(f"Created individual: {obj}")
            else:
                self.stdout.write(f"Updated individual: {obj}")
