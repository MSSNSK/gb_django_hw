from django.core.management import BaseCommand

from hw_app.models import Order


class Command(BaseCommand):
    help = "Get all orders."

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()

        self.stdout.write(f'{orders}')
