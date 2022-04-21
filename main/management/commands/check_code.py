from django.core.management.base import BaseCommand
from main import utils

class Command(BaseCommand):
    help = 'Check code'

    def add_arguments(self, parser):
        parser.add_argument('code', help='Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        code = kwargs['code']
        utils.check_for_exist_promocode(promocode=code)