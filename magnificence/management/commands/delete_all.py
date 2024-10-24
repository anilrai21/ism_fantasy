from django.core.management import BaseCommand

from magnificence.services import delete_populated_data


class Command(BaseCommand):
    help = "Delete Everything"

    def handle(self, *args, **options) -> None:
        delete_populated_data()
