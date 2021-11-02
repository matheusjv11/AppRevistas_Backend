from django.core.management.base import BaseCommand
from .scriptsTest import *

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('id', nargs='+', type=int)

    def handle(self, **options):
        revista_id = options['id'][0]
        run(revista_id)
