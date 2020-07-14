from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "This command create many users"

    def add_arguments(self, parser):

        parser.add_argument(
            "--number", default=2, type=int, help="How many users do you want to creat",
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!!"))

        # times = options.get("times")
        # for t in range(0, int(times)):
        #     self.stdout.write(self.style.SUCCESS("성공~_~"))
        #     self.stdout.write(self.style.ERROR("ㅜ실패ㅜ"))

