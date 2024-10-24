from django.core.management import BaseCommand

from magnificence.services import populate_data


class Command(BaseCommand):
    help = "Run Magnificence"

    def handle(self, *args, **options) -> None:
        populate_data()
