from django.core.management import BaseCommand

from hw_app.models import Customer


class Command(BaseCommand):
    help = 'Delete customer by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = Customer.objects.get(pk=pk)
        customer.delete()

        self.stdout.write(f'Deleted customer: {customer}')
