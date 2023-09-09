import logging
from datetime import datetime

from django.views.generic import DetailView, TemplateView
from django.views.generic.dates import MonthArchiveView, WeekArchiveView, ArchiveIndexView, YearArchiveView

from hw_app import models

logger = logging.getLogger(__name__)


class HomeViews(TemplateView):
    template_name = 'hw_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница.'
        return context


class AboutViews(TemplateView):
    template_name = 'hw_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обо мне.'
        return context


class CustomerView(DetailView):
    model = models.Customer
    template_name = 'hw_app/customer_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = datetime.now()
        return context


class AllProducts(ArchiveIndexView):
    model = models.Order
    date_field = 'ordered_at'
    template_name = 'hw_app/all_products.html'
    allow_future = False
    week_format = '%U'
    year_format = '%Y'

    def get_context_data(self, **kwargs):
        customer = models.Customer.objects.get(pk=self.kwargs.get('pk'))
        orders = super().get_queryset().filter(customer=customer).prefetch_related('products')
        products = set(product for order in orders for product in order.products.values_list('title'))

        context = super().get_context_data(**kwargs)
        context['products'] = products
        context['customer'] = customer

        return context

    def get_queryset(self, **kwargs):
        orders = models.Order.objects.get_queryset().filter(customer=self.kwargs.get('pk'))

        return orders


class AllYearProducts(AllProducts, YearArchiveView):
    pass


class AllMonthProducts(AllProducts, MonthArchiveView):
    pass


class AllWeekProducts(AllProducts, WeekArchiveView):
    pass
