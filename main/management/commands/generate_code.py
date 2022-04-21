from django.core.management.base import BaseCommand
from main import utils

class Command(BaseCommand):
    help = 'Generate promocodes'

    def add_arguments(self, parser):
        parser.add_argument('-a', '--amount', type=int, help='Amount of promocodes', )
        parser.add_argument('-g', '--group', help='Name of group', )

    def handle(self, *args, **kwargs):
        amount = kwargs['amount']
        group = kwargs['group']
        utils.generate_promocodes(amount=amount, group=group)
