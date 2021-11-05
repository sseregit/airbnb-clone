from django.core.management.base import BaseCommand
from rooms.models import Amenity, RoomType, HouseRule


class Command(BaseCommand):

    """def add_arguments(self, parser):
    parser.add_argument(
        "--times",
        help="How many times do you want me to tell you that I love you?",
    )"""

    def handle(self, *args, **options):

        help = "This command creates amentities"

        amentities = [
            "Kitchen",
            "Heating",
            "Air conditioning",
            "Washer",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor fireplace",
            "Iron",
            "Hair dryer",
            "Dedicated workspace",
            "TV",
            "Crib",
            "High chair",
            "Self check-in",
            "Smoke alarm",
            "Carbon monoxide alarm",
            "Private bathroom",
            "Ski-in/ski-out",
            "Beachfront",
            "Waterfront",
        ]

        for a in amentities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amentities created!"))

        roomtypes = ["Hotel room",
                    "Shared room",
                    "Private room",
                    "Entire place",]
        
        for r in roomtypes:
            RoomType.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS("RoomType created!"))    

        houserules = ["Don't smoke",]

        for h in houserules:
            HouseRule.objects.create(name=h)
        self.stdout.write(self.style.SUCCESS("HouseRules created!"))                

