from django.db import models
from django.urls import reverse


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    registered_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_image',
                              default='default.png',
                              verbose_name='Изображение')

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('hw_app:product_page', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='order')
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f'Заказ номер {self.pk} клиента {self.customer}'
