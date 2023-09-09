from django.core.management import BaseCommand

from hw_app.models import Order


class Command(BaseCommand):
    help = 'Delete order by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.get(pk=pk)
        order.delete()

        self.stdout.write(f'Deleted order: {order}')
