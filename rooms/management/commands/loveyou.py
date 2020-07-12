from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command love me"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want to me tell you that I love you?",
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("성공~_~"))
            self.stdout.write(self.style.ERROR("ㅜ실패ㅜ"))

