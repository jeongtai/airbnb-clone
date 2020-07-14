import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models

NAME = "lists"


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
            list_models.List, number, {"user": lambda x: random.choice(users),},
        )
        created = seeder.execute()
        # flatten을 통해 2차원 배열의 값에서 1차원으로 정리
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            # *을 붙이는 이유는 array안에 있는 요소를 가져오기 위함
            list_model.rooms.add(*to_add)
            print("********* : \n", *to_add)
            print("ㅡㅡㅡㅡㅡ : \n", to_add)

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
