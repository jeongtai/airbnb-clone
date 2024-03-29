from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command create amenities"

    # def add_arguments(self, parser):

    #     parser.add_argument(
    #         "--times",
    #         help="How many times do you want to me tell you that I love you?",
    #     )

    def handle(self, *args, **options):
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
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))

        # times = options.get("times")
        # for t in range(0, int(times)):
        #     self.stdout.write(self.style.SUCCESS("성공~_~"))
        #     self.stdout.write(self.style.ERROR("ㅜ실패ㅜ"))

