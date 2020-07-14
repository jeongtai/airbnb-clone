import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates amenities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        # 모든 유저를 데이터베이스에서 가져옴.
        # DB가 클 경우에는 절대 쓰면 안됨.
        all_users = user_models.User.objects.all()
        # 모든 룸 타입을 데이터베이스에서 가져옴.
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                # faker 라이브러리를 써서 그럴듯한 주소를 만들어줌.
                # 이외에 주소, 도시, 나라 등등 많음.
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        # flatten을 통해 2차원 배열의 값에서 1차원으로 정리
        created_clean = flatten(list(created_photos.values()))
        # 생성된 모든 룸을 루프
        for pk in created_clean:
            # pk로 각 room을 찾음 변수 room이 instance을 제공
            room = room_models.Room.objects.get(pk=pk)
            # 3부터 10-17까지 사진들을 만듦
            for i in range(3, random.randint(10, 17)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    # 파일을 제공하는 부분
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))

