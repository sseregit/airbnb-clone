import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from reservations import models as reservations_models
from users import models as users_models
from rooms import models as rooms_models

NAME = "reservations"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help=f"How many {NAME} do you want to created",
        )

    def handle(self, *args, **options):

        help = "This command creates many users"
        number = options.get("number")
        seeder = Seed.seeder()
        users = users_models.User.objects.all()
        rooms = rooms_models.Room.objects.all()
        seeder.add_entity(
            reservations_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(
                    [
                        "pending",
                        "confirmed",
                        "canceled",
                    ],
                ),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
