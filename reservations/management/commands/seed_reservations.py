import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from reservations import models as reservation_models
from users import models as user_models
from rooms import models as room_models

NAME = "reservations"


class Command(BaseCommand):

    help = "This command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many {NAME} you want to create"
        )

    def handle(self, *args, **options):

        number = options.get("number")
        seeder = Seed.seeder()
        # rooms과 users 전부를 가져옴
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: generate_dates_pair(False)[0],
                "check_out": lambda x: generate_dates_pair(True)[1],
            },
        )

        def generate_dates_pair(use_previous=False):
            if not use_previous:
                check_in = datetime.today() + timedelta(days=random.randint(-60, 30))
                check_out = check_in + timedelta(days=random.randint(1, 10))
                generate_dates_pair.previous = (check_in, check_out)
            return generate_dates_pair.previous

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
