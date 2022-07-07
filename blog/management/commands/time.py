from django.core.management.base import BaseCommand
from datetime import datetime

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = datetime.now().strftime('%X')
        self.stdout.write("Сейчас:  %s" % time)