from django.core.management import BaseCommand

from hw_app.models import Product


class Command(BaseCommand):
    help = 'Get product by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.get(pk=pk)

        self.stdout.write(f'{product}')
