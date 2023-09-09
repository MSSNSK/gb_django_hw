from django.core.management import BaseCommand

from hw_app.models import Product


class Command(BaseCommand):
    help = 'Delete product by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        product.delete()

        self.stdout.write(f'Deleted product: {product}')
