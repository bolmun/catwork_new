from django.core.management.base import BaseCommand
from cats.models import CoatColor


class Command(BaseCommand):

    help = "This command helps to create coat colors"

    def handle(self, *args, **options):
        coat_colours = [
            "Black",
            "Gray",
            "White",
            "Buff",
            "Brown",
            "Orange",
        ]
        for colour in coat_colours:
            CoatColor.objects.create(title=colour)
        self.stdout.write(
            self.style.SUCCESS(f"{len(coat_colours)} Coat colours created!")
        )