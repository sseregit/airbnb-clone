from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    """def add_arguments(self, parser):
    parser.add_argument(
        "--times",
        help="How many times do you want me to tell you that I love you?",
    )"""

    def handle(self, *args, **options):

        help = "This command creates Facilities"

        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created!"))
