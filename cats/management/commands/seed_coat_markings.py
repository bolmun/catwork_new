from django.core.management.base import BaseCommand
from cats.models import Marking


class Command(BaseCommand):

    help = "This command helps to create coat markings"

    def handle(self, *args, **options):
        coat_markings = [
            "Locket",
            "Tail Tip",
            "Socks",
            "Gloves",
            "Tights",
            "Hair Band",
            "Snot",
            "Nose Point",
            "Heart",
            "Eye Patch",
            "Tuxedo",
        ]
        for marking in coat_markings:
            Marking.objects.create(title=marking)
        self.stdout.write(
            self.style.SUCCESS(f"{len(coat_markings)} Coat markings created!")
        )