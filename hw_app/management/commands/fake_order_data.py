import random

from django.core.management.base import BaseCommand
from hw_app.models import Customer, Product, Order


class Command(BaseCommand):
    help = "Generate fake orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count orders')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        customers = []
        products = []

        for i in range(1, count + 1):
            customer = Customer(
                first_name=f'Name{i}',
                last_name=f'Surname{i}',
                email=f'mail{i}@mail.ru',
                phone=f'+7{i:09}',
                address=f'Some address'
            )
            customer.save()
            customers.append(customer)

        for j in range(1, count + 1):
            product = Product(
                title=f'ProductTitle{j}',
                description=f'Product{j} Description',
                price=random.randint(1, 10),
                count=random.randint(1, 10),
            )
            product.save()
            products.append(product)

        for k in range(1, count + 1):
            order = Order(customer=random.choice(customers), total_price=0)
            order.save()
            selected_products = [random.choice(products) for i in range(5)]
            for product in selected_products:
                order.products.add(product)
            order.total_price = sum(product.price for product in selected_products)
            order.save()

        self.stdout.write('Fake orders added')