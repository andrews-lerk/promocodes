from django.test import TestCase
from .utils import generate_promocodes, check_for_exist_promocode


class GeneratePromocodesCase(TestCase):
    def generate(self):
        generate_promocodes(amount=10, group='агенства')
        generate_promocodes(amount=1, group='агенства')
        generate_promocodes(amount=42, group='avtostop')
        generate_promocodes(amount=5, group=1)
